from django.shortcuts import render
from .forms import RegistrationForm
from django.views import View


# Create your views here.
class Register(View):
    form = RegistrationForm()

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'books/../templates/index.html', context=context)
        pass

    def post(self, request):
        form_data = RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            context = {
                'notification_title': 'Registration form',
                'notification_content': 'User created',
            }
            return render(request, 'books/../templates/notification.html', context=context)
