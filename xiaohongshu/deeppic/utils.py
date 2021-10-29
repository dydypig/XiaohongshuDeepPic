import random
import string

VALID_PICS = {
    'JPG',
    'JEPG',
    'PNG',
    'TIF'
}

def random_username(N):
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(N))
    return username