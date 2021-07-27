from django.shortcuts import render
from django.http import HttpResponse
from .request_handler import process
from .forms import BatchForm
from .models import Batch


# heime/brygg
def index(request):
    batches = Batch.objects.all()
    return render(request, 'brew_app/index.html', {'batches': batches})

# full heime/brygg/leggtil
# django /brygg/leggtil
def add(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BatchForm()
    return render(request, 'brew_app/add.html', {'form': form})
