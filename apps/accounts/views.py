import time
import hashlib

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from forms import registForm

@csrf_protect
def regist(request):
    if request.method == 'GET':
        form = registForm()
        return render('x.html', {})

@csrf_protect
def login(request):
    pass

def calculate_active_code(email):
    time = int(time.time())
    return hashlib.sha256(email + 'salt' + str(time)).hexdigest()
