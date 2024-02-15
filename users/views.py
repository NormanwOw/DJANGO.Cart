from django.contrib import auth
from django.views.generic import FormView
from django.http import JsonResponse

from users.forms import LoginForm


class AuthLoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(self.request, user)

        return JsonResponse({'status': 'ok'}, status=200)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        return JsonResponse({'errors': errors}, status=400)