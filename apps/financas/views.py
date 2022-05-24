from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/usuarios/login')
def principal(request):
    template_name = 'financas/principal.html'
    context = {}
    return render(request, template_name, context)
