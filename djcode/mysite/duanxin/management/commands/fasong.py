#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from duanxin.models import *
import datetime
import requests
import json
import time

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        qs = DX_FaSongMX.objects.filter(is_delete=False).filter(is_fasong=False)[:10]
        fasong_ID = []
        #fasong_neirong = u'【鑫运检测】尊敬的%s车主您好，欢迎来到我站，本次业务由%s电话%s为您服务，监督、投诉请拨打6491572。' % (i.paizhaohao,i.yincheyuan_name,i.yincheyuan_dianhua)

        if len(qs) == 0:
            exit()
        else:
            for i in qs:
                if i.fasongjiekou == 'yewu_kaishi':
                    resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                        data={
                            "uid": "ipScrzAANE33",
                            "pas": "jc5fv2nc",
                            "mob": i.dianhuahao,
                            "cid": "nEFFQCJiIImA",
                            "type": "json",
                            "p1": i.paizhaohao
                            },timeout=3 , verify=False)
                    result =  json.loads( resp.content )
                    fasongneirong = u'【鑫运检测】尊敬的%s车主您好，欢迎来到我站办理检测业务' % i.paizhaohao
                    fasong_ID.append({'id':i.id,'code':result.get('code'),'fanhuixinxi':result.get('msg'),
                                  'fasongneirong':fasongneirong})
                elif i.fasongjiekou == 'yewu_banjie':
                    resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                        data={
                            "uid": "ipScrzAANE33",
                            "pas": "jc5fv2nc",
                            "mob": i.dianhuahao,
                            "cid": "AW1EpStGp2cnull",
                            "type": "json",
                            "p1": i.paizhaohao
                            },timeout=3 , verify=False)
                    result =  json.loads( resp.content )
                    fasongneirong = u'【鑫运检测】尊敬的%s车主您好，您的检测业务已办结' % i.paizhaohao
                    fasong_ID.append({'id':i.id,'code':result.get('code'),'fanhuixinxi':result.get('msg'),
                                  'fasongneirong':fasongneirong})


                #result = {'code':0,'msg':u'发送成功'}


                time.sleep(2)
        for a in fasong_ID:
            q = DX_FaSongMX.objects.filter(id=a.get('id'))
            q.update(is_fasong=True,fasong_datetime=datetime.datetime.now(),fanhuizhi=a.get('code'),
                     tijiao_neirong=a.get('fasongneirong'),fanhuixinxi=a.get('fanhuixinxi'))


