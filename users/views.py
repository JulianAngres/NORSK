from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import UserRegisterForm
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
#from .utils import token_generator

from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import SignUpForm
from django.contrib.auth.models import User

from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from django.utils.encoding import force_text





class SignUpView(View):
    form_class = SignUpForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site =get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('pleese_verify')

        return render(request, self.template_name, {'form':form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account has been confirmed.'))
            return redirect('success_verification')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('index')


#Class PleeseVerifyView(View):
#    template_name = 'register.html'
#    return render(request, 'users/pleese_verify.html')


#def register(request):
#    if request.method == 'POST':
#        form = UserRegisterForm(request.POST)
#        if form.is_valid():
#            form.is_active = False
#            form.save()

#            uidb64 = force_bytes(urlsafe_base64_encode(form.pk))
#            domain = get_current_site(request).domain
#            link = reverse('activate', kwargs={'uidb64' : uidb64, 'token' : token_generator.make_token(form)})

#            activate_url = 'http://'+domain+link
#            email = EmailMessage(
#                'Activate your account', 
#                'Please use this link to verify your account\n' + activate_url, 
#                'ja@julian-angres.no',
#                ['ja@julian-angres.de']
#            )

#            email.send(fail_silently=False)
#            username = form.cleaned_data.get('username')
#            #messages.success(request, f'Account created for {username}!')
#            return redirect('#')
#    else:
#        form = UserRegisterForm()
#    return render(request, 'users/register.html', {'form': form})


#class VerificationView(View):
#    def get(self, request, uidb64, token):
#        return redirect('login')


