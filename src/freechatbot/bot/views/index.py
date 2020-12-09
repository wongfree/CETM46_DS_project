from django.shortcuts import render

def index(request):
    template = 'bot/index.html'
    context = {}

    return render(request, template, context)
    # return HttpResponseRedirect('/tas/list/')