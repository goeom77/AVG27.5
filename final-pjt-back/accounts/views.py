from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html',context)