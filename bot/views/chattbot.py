import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime as dt


class ChatterBotAppView(TemplateView):
    template_name = 'bot/app.html'

    def get_context_data(self, **kwargs):

        if dt.now().hour > 0 and dt.now().hour <= 11:
            greeting = 'Morning'
        elif dt.now().hour >=12 and dt.now().hour < 18:
            greeting = 'Afternoon'
        else:
            greeting = 'Hello'

        data = super(ChatterBotAppView, self).get_context_data(**kwargs)
        if 'AnonymousUser' in self.request.user:
            data['greeting'] = '{},What can I help you? '.format()
        else:
            data['greeting'] = '{} {}, What can I help you? '.format(greeting,self.request.user)
        return data

@method_decorator(csrf_exempt, name='dispatch')
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    chatterbot = ChatBot(**settings.CHATTERBOT)


    def post(self, request, *args, **kwargs):
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()
        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):

        return JsonResponse({
            'name': self.chatterbot.name
        })