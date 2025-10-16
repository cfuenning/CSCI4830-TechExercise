from django.shortcuts import render, redirect, get_object_or_404
from .models import Score

#The render function generates HTTP response
#These functions handle HTTP requests and return HTTP response
def index(request): 
    return render(request, 'index_books.html') 

def about(request):
    return render(request, 'about_books.html')

def score_view(request):
    #list all scores
    scores = Score.objects.all()

    if request.method == "POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('score_view') #redirect to the same page?
    else:
        form = ScoreForm()
    return render(request, 'score_list.html', {'form': form, 'scores': scores})
    
def edit_score(request, score_id):
    #edit a specific score
    score = get_object_or_404(Score, id=score_id)

    if request.method == "POST":
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('score_view')
    
    else:
        form = ScoreForm(instance=score)

    return render(request, 'book_edit.html', {'form': form, 'scores': score})

def delete_score(request, score_id):
    #delete a specific score
    score = get_object_or_404(Score, id=score_id)

    #add confirmation before deletion
    if request.method == "POST":
        score.delete()
        return redirect('score_view')
    
    return render(request, 'book_confirm_delete.html', {'score': score})
