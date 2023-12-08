class MenuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.current_url = request.path_info
        response = self.get_response(request)
        return response
