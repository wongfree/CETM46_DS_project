import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class ChatterBotAppView(TemplateView):
    template_name = 'bot/app.html'

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