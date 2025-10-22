from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Bookshelf
from .forms import BookshelfForm

#The render function generates HTTP response
#These functions handle HTTP requests and return HTTP response
def front_page(request): 
    return render(request, 'index_books.html') 

def about(request):
    return render(request, 'about_books.html')

def library_view(request):
    #list all book records
    book = Bookshelf.objects.all()
    paginator = Paginator(book, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_list.html', {'page_obj': page_obj})

def create_book(request):
    success = False
    added_book = None

    if request.method == "POST":
        form = BookshelfForm(request.POST)
        if form.is_valid():
            added_book = form.save()
            success = True
            return render(request, "add_book.html", {"form": form, "added_book":added_book, "success":success},)
    else:
        form = BookshelfForm()
    return render(request, "add_book.html", {"form": form, "added_book":added_book, "success":success,})


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

def search_list(request):
    form = BookshelfForm(request.POST or None) #to reuse the forms styling for input fields
    page_number = request.GET.get("page", 1)
    title = request.GET.get("title", "").strip()
    author = request.GET.get("author", "").strip()
    genre = request.GET.get("genre", "")

    if request.method== "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        genre = request.POST.get("genre", "")
        # Reset to first page on new search
        page_number = 1

    if title or author or genre:
        books = Bookshelf.objects.filter(
            title__icontains=title, author__icontains=author, genre__icontains=genre)
    else:
        books = Bookshelf.objects.all()

    paginator = Paginator(books, 10)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "search.html",
        {'form': form,
         "books": page_obj,
         "title_query": title,
         "author_query": author,
         "genre_query": genre},
    )
