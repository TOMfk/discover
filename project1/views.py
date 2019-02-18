from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


import time
import datetime
from project1.sub import WorkDays
from project1.rili import get_num_of_days_in_month
from project1.la import lunar


def differ2(request):
    """
    给定一个起始时间,给定一个结束时间,计算出期间的工作时间,刨去节假日
    :param request:
    :return:
    """
    worktime = "{} 小时 {} 分钟"  # 区间运行时间
    if request.method == "POST":
        print("111111111111111111111111111111111111111111")
        lis = []
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        # print(starttime, type(endtime))
        # 起始时间和结束时间之间的差值,除去节假日的工作时间
        stime, stime1 = starttime.split("T")
        etime, etime1 = endtime.split("T")
        a, b, c = stime.split("-")
        e, f, g = etime.split("-")
        t1, t2 = stime1.split(":")
        q1, q2 = etime1.split(":")
        t = int(t1) * 60 + int(t2)
        q = int(q1) * 60 + int(q2)
        st = datetime.date(int(a), int(b), int(c))
        et = datetime.date(int(e), int(f), int(g))
        midtime = WorkDays(st, et)
        for i in midtime.workDays():
            lis.append(str(i))
        count = midtime.daysCount()
        vod = 0
        vod1 = 0
        if stime in lis:
            if 510 < t < 1035:  # 判断时间是在工作时间内,直接转化成秒数,判断是否在那个区间里面
                count -= 1
                vod = t - 510

        if etime in lis:
            if 510 < q < 1035:
                count -= 1
                vod1 = q - 510

        currtime = count * 525 + vod + vod1
        print(currtime, vod, vod1)
        sh, mi = divmod(currtime, 60)  # "内置函数,取商和余数"
        return render(request, "rili.html", {"worktime": worktime.format(sh, mi)})
    return render(request, "rili.html", {"worktime": 0})





class JieRi(APIView):

    def get(self, request):
        """

        :param request:
        :return: 1000    响应成功
                1001     响应失败
        """
        di  = {
                   "code": 0,
                    "msg": "",
                    "data": []
        }
        try:
            year = request.query_params.get["year"]
            st = {
                "data": {
                    "title": "任务1",
                    "location": "",
                    "description": "",
                    "color": "#ab3518",
                    "forecolor": "#ffffff",
                    "calendar": "",
                    "busy": True,
                    "icon": ""
                },
                "schedule": {
                    "duration": 28,
                    "dayOfMonth": [14],
                    "year": [2019],
                    "month": [1]
                }
            }
            feativals_CH = {
                '1-1': '元旦',
                '2-14': '情人节',
                '3-8': '妇女节',
                '3-12': '植树节',
                '4-1': '愚人节',
                '4-22': '地球日',
                '5-1': '劳动节',
                '5-4': '青年节',
                '6-1': '儿童节',
                '7-1': '建党节',
                '8-1': '建军节',
                '9-10': '教师节',
                '10-1': '国庆节',
                '12-25': '圣诞节',
                '2-4': '立春',
                '5-6': '立夏',
                '8-8': '立秋',
                '11-8': '立冬',
                '2-19': '雨水',
                '5-21': '小满',
                '8-23': '处暑',
                '11-22': '小雪',
                '3-6': '惊蛰',
                '6-6': '芒种',
                '9-8': '白露',
                '12-7': '大雪',
                '3-21': '春分',
                '6-21': '夏至',
                '9-23': '秋分',
                '12-22': '冬至',
                '4-5': '清明',
                '7-7': '小暑',
                '10-8': '寒露',
                '1-5': '小寒',
                '4-20': '谷雨',
                '7-23': '大暑',
                '10-24': '霜降',
                '1-20': '大寒',
            }
            lunarFeatival_CH = {
                '1-1': '春节',
                '2-2': '龙抬头',
                '1-15': '元宵节',
                '4-4': '寒食节',
                '4-5': '清明节',
                '5-5': '端午节',
                '8-15': '中秋节',
                '9-9': '重阳节',
                '12-30': '除夕',
            }
            dic = {}
            for i in lunarFeatival_CH:
                a, v = i.split("-")
                sun = lunar.getDayByLunar(2019, int(a), int(v))
                dic["{}-{}".format(sun.m, sun.d)] = lunarFeatival_CH[i]
            for i in dic:
                feativals_CH[i] = dic[i]
            for i, v in feativals_CH.items():
                t = {"data": {}, "schedule": {}}
                st["data"]["title"] = v
                st["data"]["description"] = ""
                st["data"]["location"] = ""
                st["data"]["color"] = "#ab3518"
                st["data"]["forecolor"] = "#ffffff"
                st["data"]["calendar"] = ""
                st["data"]["busy"] = True
                st["data"]["icon"] = ""
                s, e = i.split("-")
                st["schedule"]["dayOfMonth"] = [int(e)]
                st["schedule"]["month"] = [int(s) - 1]
                st["schedule"]["year"] = [int(2019)]
                st["schedule"]["duration"] = get_num_of_days_in_month(2019, s)
                di["data"].append(st)
                st = t
            di["code"] = 1000
        except Exception as e:
            di["code"] = 1001
            di["msg"] = str(e)
        return JsonResponse(di)









