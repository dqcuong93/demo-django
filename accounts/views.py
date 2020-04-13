from django.shortcuts import render
from .forms import RegistrationForm
from django.views import View


# Create your views here.
class Registration(View):
    form = RegistrationForm()

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'accounts/registration.html', context=context)

    def post(self, request):
        form_data = RegistrationForm(request.POST)
        context = {
            'notification_title': 'Registration form',
            'notification_content': '',
        }
        if form_data.is_valid():
            form_data.save()
            context['notification_content'] = 'User created'
            return render(request, 'books/notification.html', context=context)
        context['notification_content'] = 'Data is not valid!'
        return render(request, 'books/notification.html', context=context)
