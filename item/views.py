from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Item
from .forms import NewItemForm, EditItemForm

# Create your views here.
# creating a detail view for each ietm listed on the home page

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item':item,
        'related_items':related_items,
    }
    return render(request, 'item/detail.html', context)


# adding a new item using a form 
@login_required
def new_item(request):
    if request.method =='POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    context = {
            'form':form,
            'title':'New Item'
        }
    return render(request, 'item/new.html', context)
        
        
#editing an item in the dashboard

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, created_by=request.user, pk=pk)
    if request.method =='POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {
            'form':form,
            'title':'Edit Item'
        }
    return render(request, 'item/new.html', context)

#  deleting an item from a page use
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, created_by=request.user, pk=pk)
    item.delete()
    
    return redirect('dashboard:index')

