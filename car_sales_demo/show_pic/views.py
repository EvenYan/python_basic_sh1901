from django.shortcuts import render
from django.http import HttpResponse
import requests
import lxml
from lxml import etree
import json

# Create your views here.

def show_bar(request):
    return render(request, "show_bar.html")



def get_data(request):
    headers = {
        'authority': 'db.auto.sohu.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'dnt': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://www.google.com/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SUV=0433c356525009ec; _muid_=1555393236372419; gidinf=x099980109ee0f8c4d6280c51000bb869431f5ddcb1c; IPLOC=CN3100',
    }

    response = requests.get('https://db.auto.sohu.com/carsales/', headers=headers)
    mytree = lxml.etree.HTML(response.content)
    # print(response.content.decode("utf-8"))
    car_list = mytree.xpath("//*[@id='ucon_11']/ol[1]/li/a/text()")
    sale_list = mytree.xpath("//*[@id='ucon_11']/ol[1]/li/span/text()")
    print(car_list)
    resp = {"car_list": car_list, "sale_list": sale_list}
    return HttpResponse(json.dumps(resp), content_type="application/json")
