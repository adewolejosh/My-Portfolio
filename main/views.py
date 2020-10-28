from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View

from .models import Subscriber
from .forms import SubscriberForm, sending_mail

# Create your views here.)


class SubscribeView(View):
    model = Subscriber
    form_class = SubscriberForm
    template_name = 'main/subscribe.html'

    def get(self, request):
        form = self.form_class(request.GET)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                user = Subscriber.objects.get(email__iexact=email)
                if user:
                    user.delete()
            except Subscriber.DoesNotExist:
                pass
            form.save()
            sending_mail(
                email=str(form.cleaned_data['email'])
            )
            # message that returns success
            messages.success(request, "You Have Successfully subscribed to My Newsletter")
            return render(request, self.template_name, {'form': self.form_class})

        else:
            messages.error(request, 'An error occured')
            return render(request, self.template_name, {'form': self.form_class})
