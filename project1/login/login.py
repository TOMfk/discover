import hashlib
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from project1.models import User, UserToken, Desc


class Logins(APIView):

    def get_radon_str(self, user):
        ctime = str(time.time())
        md5 = hashlib.md5(bytes(user, encoding="utf-8"))
        md5.update(bytes(ctime, encoding="utf-8"))
        return md5.hexdigest()

    def post(self, request):
        """
        用户登录页面数据的校验
        :param request:
        :return:
        """
        #获取数据
        user = request.data.get("user")
        pwd = request.data.get("pwd")
        # 创建响应体
        respond = {
            "code": "",
            "msg": "",
            "data":{}
        }
        #用户校验
        user_obj = User.objects.filter(username=user, password=pwd).first()
        try:
            if user_obj:      #校验成功
                random_str = self.get_radon_str(user_obj.username)
                #数据库更新
                UserToken.objects.update_or_create(user=user_obj, defaults={"token": random_str})
                #对应用户的相关备注
                desc = Desc.objects.filter(user=user_obj)
                #构建响应体
                for i in desc:
                    respond["data"][i.time] = i.content
                respond["code"] = 1000
            else:
                respond["code"] = 1001
                respond["msg"] = "用户名或密码错误"
        except Exception as e:
            respond["code"] = 1004
            respond["err_msg"] = str(e)
        return Response(respond)











