from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
