from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items':items,
        'categories':categories
    }
    return render(request, 'core/index.html', context)


#view to the about page

def about(request):
    return render(request, 'core/about.html')


# view to the contact page

def contact(request):
    return render(request, 'core/contact.html')

#creating a signup form

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form':form})
