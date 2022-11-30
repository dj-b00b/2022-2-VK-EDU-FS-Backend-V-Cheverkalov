from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET


@require_GET
def render_home_page(request):
    return render(request, 'index.html')
