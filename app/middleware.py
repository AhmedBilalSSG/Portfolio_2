from django.shortcuts import render
from django.http import Http404

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.status_code == 404:
                return render(request, '404.html', {})
            elif response.status_code == 500:
                return render(request, '500.html', {})
            return response
        except Http404:
            return render(request, 'admin/auth-404.html', {})
        except Exception:
            return render(request, 'admin/auth-500.html', {})