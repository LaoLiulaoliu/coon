import time
import hashlib
from django.shortcuts import render

def regist(request):
    pass

def login(request):
    pass

def calculate_active_code(email):
    time = int(time.time())
    return hashlib.sha256(email + 'salt' + str(time)).hexdigest()
