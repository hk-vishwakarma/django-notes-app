from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    if request.user.is_authenticated :
        recent_notes = Notes.objects.order_by('-id')[0:2]
    else:
        recent_notes = []
   
    return render(
        request, 
        'home/index.html', 
        context={'recent_notes':recent_notes}
        )


@login_required(login_url='login')
def add_note_view(request):
    if request.method == 'POST':

        note_title = request.POST.get('title')
        note_content = request.POST.get('content')

        Notes.objects.create(user = request.user, title = note_title, content = note_content)
        messages.success(request, "Note saved successfully!")

        return render(request, 'home/message.html' )
    
    return render(request, 'home/addnote.html')

@login_required(login_url='login')
def all_note_view(request):
    all_note = Notes.objects.filter(user = request.user)
    if not all_note:
        messages.error(request, "No note is added!")
        return render(request, 'home/message.html')
    return render(request, 'home/allnote.html', context={'notes':all_note})

@login_required(login_url='login')
def view_note(request, note_id):
    note = Notes.objects.get(id=note_id)

    return render(request, 'home/view_note.html', context={'note':note})


# to update the note
@login_required(login_url='login')
def update_note(request, note_id):
    note = Notes.objects.get(id=note_id)

    if request.method == 'POST' :
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('view_note', note_id)
    
    return render(request, 'home/update_note.html', context={'note':note})


#  to delete the specific note
@login_required(login_url='login')
def delete_note(request, note_id):
    Notes.objects.get(id=note_id).delete()
    return redirect('allnote')


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if not user.exists():
            messages.error(request, "username not exist !")
            return redirect('login')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid password !")
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')


    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
    


def register_view(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "username already exist !")
            return redirect('register')

        User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
            
        )

        messages.success(request, "Register Successfully !")
        return redirect('login')
        

    return render(request, 'home/register.html')


 # this is a decorator function for login require with messages
# def login_required_with_msg(view_func):
#     def wrapper(request, *args, **kawgs):
#         if not request.user.is_authenticated :
#             messages.error(request,"You must be logged in to access this app.")
#             return redirect('login')
#         return view_func(request, *args, **kawgs)
#     return wrapper
    
