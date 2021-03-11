from django.utils.deprecation import MiddlewareMixin


class AllowOrigin(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers'] = "Content-Type"
        return response
