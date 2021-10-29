from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import FileFieldForm, UserPicSelection
from .models import CloudPics, LocalPics
from .utils import VALID_PICS, random_username
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .api_for_xin import process_your_picture
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin 

def cloud_pic_select(request,pk):
    user =  request.user
    image = CloudPics.objects.filter(pk=pk).first().image
    lp = LocalPics.objects.filter(user=user).first()
    lp.imagecloud=image
    lp.save()
    return redirect('home')

def process_pic(request):
    user=request.user
    local_pic = user.localpics.imagelocal
    cloud_pic = user.localpics.imagecloud
    process_your_picture(user,local_pic,cloud_pic)
    return redirect('home')

def home(request):
    if request.user.is_anonymous:
        while True:
            username = random_username(15)
            if User.objects.filter(username=username).first() == None:
                break
        user = User.objects.create(username=username)
        login(request,user)
    else:
        user = request.user
    if request.method == 'POST':
        form = UserPicSelection(request.POST,request.FILES,instance=user.localpics)
        print(form.__dict__)
        if form.is_valid:
            form.save()
            messages.success(request,'Picture Uploaded')
            return redirect('home')
    else:
        form = UserPicSelection(instance=user.localpics)
    context = {
        'form':form,
        'localpic':user.localpics
    }
    return render(request,'deeppic/home.html',context)


class FileFieldFormView(UserPassesTestMixin,FormView):
    form_class = FileFieldForm
    template_name = 'deeppic/upload.html'  # Replace with your template.
    success_url = '/' # Replace with your URL or reverse().
    permission_denied_message = 'You are not admin'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                if f.name.upper().split('.')[-1] in VALID_PICS:
                    CloudPics.objects.create(image=f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def test_func(self):
        return (self.request.user.is_staff or self.request.user.is_superuser)

class CloudPicsView(ListView):
    model = CloudPics
    fields = ['pk','image']
    template_name = 'deeppic/cloud.html'
    context_object_name = 'cloud_pics'
    paginate_by = 6

    def get_queryset(self):
        return CloudPics.objects.all()

