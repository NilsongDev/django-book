# projectwo/middleware.py
from django.shortcuts import redirect

class CustomRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Aquí puedes implementar lógica para redirigir si es necesario
        response = self.get_response(request)
        return response