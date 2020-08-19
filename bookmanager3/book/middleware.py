from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('before request')
        # username = request.COOKIES.get('username')
        # if username:
        #     print('got')
        # else:
        #     print('new user')

    def process_responce(self, request, response):
        print('before response')

        return response


class Test2MiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('before request2')
        # username = request.COOKIES.get('username')
        # if username:
        #     print('got')
        # else:
        #     print('new user2')

    def process_responce(self, request, response):
        print('before response2')

        return response