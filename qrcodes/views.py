from rest_framework.views import APIView
from rest_framework.response import Response

class GenerateCodeView(APIView):
    def get(self, request):
        return Response({'code': '123'})