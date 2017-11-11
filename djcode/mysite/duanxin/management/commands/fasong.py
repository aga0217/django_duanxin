#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from duanxin.models import *
import datetime
import requests
import json
import time
import urllib2
from keyczar import keyczar
from jiami_jiemi_test import AESCipher

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'
    aes_cipher = AESCipher()
    def handle(self, *args, **options):
        qs = DX_FaSongMX.objects.filter(is_delete=False).filter(is_fasong=False,fasongjiekou__in = ['yewu_kaishi','yewu_banjie','tixing_tjr'])
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
                            "mob": self.aes_cipher.decrypt(i.dianhuahao),
                            "cid": "nEFFQCJiIImA",
                            "type": "json",
                            "p1": i.paizhaohao
                            },timeout=3 , verify=False)
                    result =  json.loads( resp.content )
                    fasongneirong = u'【鑫运检测】尊敬的%s车主您好，欢迎来到我站办理检测业务' % i.paizhaohao
                    fasong_ID.append({'id':i.id,'code':result.get('code'),'fanhuixinxi':result.get('msg'),
                                  'fasongneirong':fasongneirong,'gongyingshang':u'微米'})
                elif i.fasongjiekou == 'yewu_banjie':
                    resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                        data={
                            "uid": "ipScrzAANE33",
                            "pas": "jc5fv2nc",
                            "mob": self.aes_cipher.decrypt(i.dianhuahao),
                            "cid": "AW1EpStGp2cnull",
                            "type": "json",
                            "p1": i.paizhaohao
                            },timeout=3 , verify=False)
                    result =  json.loads( resp.content )
                    fasongneirong = u'【鑫运检测】尊敬的%s车主您好，您的检测业务已办结' % i.paizhaohao
                    fasong_ID.append({'id':i.id,'code':result.get('code'),'fanhuixinxi':result.get('msg'),
                                  'fasongneirong':fasongneirong,'gongyingshang':u'微米'})
                elif i.fasongjiekou == 'tixing_tjr':
                    resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                                         data={
                                             "uid": "ipScrzAANE33",
                                             "pas": "jc5fv2nc",
                                             "mob": self.aes_cipher.decrypt(i.dianhuahao),
                                             "cid": "lcoDIQJHGdzQ",
                                             "type": "json",
                                             "p1": i.paizhaohao,
                                             "p2":str(i.tjrcount)
                                         }, timeout=3, verify=False)
                    result = json.loads(resp.content)
                    fasongneirong = u'【鑫运检测】%s已经登记，本月您已推荐%s台车辆。请核实。' % (i.paizhaohao,str(i.tjrcount))
                    fasong_ID.append({'id': i.id, 'code': result.get('code'), 'fanhuixinxi': result.get('msg'),
                                      'fasongneirong': fasongneirong, 'gongyingshang': u'微米'})




        for a in fasong_ID:
            q = DX_FaSongMX.objects.filter(id=a.get('id'))
            q.update(is_fasong=True,fasong_datetime=datetime.datetime.now(),fanhuizhi=a.get('code'),
                     tijiao_neirong=a.get('fasongneirong'),fanhuixinxi=a.get('fanhuixinxi'),
                     gongyingshang=a.get('gongyingshang'))
    """
    def def_jiami(self,yuanshi_str):
        #locfile = '/Users/houlipeng1/django/djcode/mysite/shoufei/fieldkeys' #上传后需修改
        locfile = '/home/www/djcode/mysite/fieldkeys'  # 上传后需修改

        crypter = keyczar.Crypter.Read(locfile)
        s_encrypted = crypter.Encrypt(yuanshi_str)
        return s_encrypted

    def def_jiemi(self,jiami_str):
        locfile = '/home/www/djcode/mysite/fieldkeys'
        #locfile = '/Users/houlipeng1/django/djcode/mysite/shoufei/fieldkeys'  # 上传后需修改
        crypter = keyczar.Crypter.Read(locfile)
        if jiami_str == None:
            return ''
        else:
            s_decrypted = crypter.Decrypt(jiami_str)
            return s_decrypted
    """


