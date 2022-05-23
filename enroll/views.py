from django.shortcuts import render
from .forms import UserForm


# Create your views here.
def form(request):
    if request.method == 'POST':
        myForm = UserForm(request.POST)
    else:
        myForm = UserForm()

    return render(request, 'enroll/form.html', {'form': myForm})
