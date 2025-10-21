from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookshelf
from .forms import BookshelfForm

#The render function generates HTTP response
#These functions handle HTTP requests and return HTTP response
def index(request): 
    return render(request, 'index_books.html') 

def about(request):
    return render(request, 'about_books.html')

def library_view(request):
    #list all book records
    book = Bookshelf.objects.all()

    if request.method == "POST":
        form = BookshelfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_view') #redirect to the same page
    else:
        form = BookshelfForm()
    return render(request, 'book_list.html', {'form': form, 'books': book})
    
def edit_book(request, book_id):
    #edit a specific book record
    book = get_object_or_404(Bookshelf, id=book_id)

    if request.method == "POST":
        form = BookshelfForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library_view')
    
    else:
        form = BookshelfForm(instance=book)

    return render(request, 'book_edit.html', {'form': form, 'books': book})

def delete_book(request, book_id):
    #delete a specific book record (and associated data in row)
    book = get_object_or_404(Bookshelf, id=book_id)

    #add confirmation before deletion
    if request.method == "POST":
        book.delete()
        return redirect('library_view')
    
    return render(request, 'book_confirm_delete.html', {'books': book})
