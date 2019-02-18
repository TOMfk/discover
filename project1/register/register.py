from rest_framework.response import Response
from rest_framework.views import APIView
from project1.models import User


class Register(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        User.objects.create(name=username, password=password)
        return Response("注册成功")


