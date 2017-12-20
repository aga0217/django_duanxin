# -*- coding: utf-8 -*-
#from celerytest import app

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess
from .models import *
import datetime
from .jiami_jiemi_test import AESCipher
import psycopg2
import sys
import requests
LOGID = 0
@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
@shared_task
def fasong_yibutest():
    command = "python /home/www/djcode/mysite/manage.py fasong_yibutest"
    subprocess.call(command,shell=True)
    return 'sussess'

class SendSMSClass(object):
    help = u'使用异步方式发送短信以取代定时发送机制'
    aes_cipher = AESCipher()
    def __init__(self,id):
        self.id = id
        self.comname = 'SendSMSClass'
        try:
            self.conn = psycopg2.connect("dbname='kucuntest_duanxin' user='aga0217' host='192.168.0.127' password='1417123aga'")
        except:
            sys.exit()
        self.cur = self.conn.cursor()

    def starttime(self):#插入DX_CeleryLog starttime记录开始执行的时间并返回插入的id值，后续会在此条基础上更新结束时间和执行结果
        #注意语句中使用returning id来获取插入的id值
        sql = "INSERT INTO  duanxin_dx_celerylog(comname,starttime) VALUES(%s, now() ) RETURNING ID"
        try:
            self.cur.execute(sql,(self.comname,))
        except:
            self.close()
        # 必须先执行，否则不能插入
        try:
            self.conn.commit()
        except:
            self.close()
            return 'starttime shibai'
        # 返回id
        lastid = self.cur.fetchone()[0]
        global LOGID
        LOGID = lastid


    def query(self):#返回根据id查询发送明细中的结果
        sql = "SELECT * from duanxin_dx_fasongmx WHERE (id = %s)"
        try:
            self.cur.execute(sql,(self.id,))
        except Exception ,e:
            e = repr(e)
            self.updatecelerylog(e)
            self.close()
            return 'query shibai'
        result = self.cur.fetchall()[0]
        if not result:
            self.updatecelerylog('query is None')
        return result

    def send(self):
        self.starttime()
        qs = self.query()
        if qs[7] == 'yewu_kaishi':
            resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                                 data={
                                     "uid": "ipScrzAANE33",
                                     "pas": "jc5fv2nc",
                                     "mob": self.aes_cipher.decrypt(qs[8]),
                                     "cid": "nEFFQCJiIImA",
                                     "type": "json",
                                     "p1": qs[1]
                                 }, timeout=3, verify=False)
            result = json.loads(resp.content)
            fasongneirong = u'【鑫运检测】尊敬的%s车主您好，欢迎来到我站办理检测业务' % qs[1]
            dic = {'id': qs[0], 'fanhuizhi': result.get('code'), 'fanhuixinxi': result.get('msg'),
                              'tijiao_neirong': fasongneirong, 'gongyingshang': u'微米'}
            self.updatefasongmx(dic)
            self.updatecelerylog('yewu_kaishi sussessful')
            self.close()
        elif qs[7] == 'yewu_banjie':
            resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                                 data={
                                     "uid": "ipScrzAANE33",
                                     "pas": "jc5fv2nc",
                                     "mob": self.aes_cipher.decrypt(qs[8]),
                                     "cid": "AW1EpStGp2cnull",
                                     "type": "json",
                                     "p1": qs[1]
                                 }, timeout=3, verify=False)
            result = json.loads(resp.content)
            fasongneirong = u'【鑫运检测】尊敬的%s车主您好，您的检测业务已办结' % qs[1]
            dic = {'id': qs[0], 'fanhuizhi': result.get('code'), 'fanhuixinxi': result.get('msg'),
                              'tijiao_neirong': fasongneirong, 'gongyingshang': u'微米'}
            self.updatefasongmx(dic)
            self.updatecelerylog('yewu_banjie sussessful')
            self.close()
        elif qs[7] == 'tixing_tjr':
            resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),
                                 data={
                                     "uid": "ipScrzAANE33",
                                     "pas": "jc5fv2nc",
                                     "mob": self.aes_cipher.decrypt(qs[8]),
                                     "cid": "lcoDIQJHGdzQ",
                                     "type": "json",
                                     "p1": qs[1],
                                     "p2": str(qs[16])
                                 }, timeout=3, verify=False)
            result = json.loads(resp.content)
            fasongneirong = u'【鑫运检测】%s已经登记，本月您已推荐%s台车辆。请核实。' % (qs[1], str(qs[16]))
            dic = {'id': qs[0], 'fanhuizhi': result.get('code'), 'fanhuixinxi': result.get('msg'),
                              'tijiao_neirong': fasongneirong, 'gongyingshang': u'微米'}
            self.updatefasongmx(dic)
            self.updatecelerylog('tixing_tjr sussessful')
            self.close()

    def updatefasongmx(self,dic):
        sql = "UPDATE duanxin_dx_fasongmx set is_fasong=TRUE,fasong_datetime=now(),fanhuizhi=%s,tijiao_neirong=%s,fanhuixinxi=%s,gongyingshang=%s where ID=%s"
        try:
            self.cur.execute(sql, (dic.get('fanhuizhi'),dic.get('tijiao_neirong'),dic.get('fanhuixinxi'),dic.get('gongyingshang'),dic.get('id'),))
        except Exception,e:
            e = repr(e)  # 避免出现中文字符
            self.updatecelerylog(e)
            self.close()
        self.conn.commit()

    def updatecelerylog(self,st):
        sql = "UPDATE duanxin_dx_celerylog set result=%s,endtime=now() where ID=%s"
        self.cur.execute(sql, (st,LOGID,))
        self.conn.commit()
        self.close()

    def close(self):
        self.cur.close()
        self.conn.close()
@shared_task
def sendsms(id):
    SendSMSClass(id).send()


"""
class SendSMS(object):
    help = u'使用异步方式发送短信以取代定时发送机制'
    aes_cipher = AESCipher()
    def __init__(self,id):
        self.id = id
    def starttime(self):
        q = DX_CeleryLog(comname='class_sendsms',starttime=datetime.datetime.now())
        q.save()
        q_id = q.id
        return q_id
    def filter(self):
        self.qs = DX_FaSongMX.objects.filter(id=self.id)
        if len(self.qs) != 1:
            return False
        else:
            return self.qs
    def send(self):
        fasong_ID = []
        starttime_id = self.starttime()
        qs = self.filter()
        if qs:
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
                q.update(is_fasong=True, fasong_datetime=datetime.datetime.now(), fanhuizhi=a.get('code'),
                         tijiao_neirong=a.get('fasongneirong'), fanhuixinxi=a.get('fanhuixinxi'),
                         gongyingshang=a.get('gongyingshang'))
            a = DX_CeleryLog.objects.filter(id=starttime_id)
            a.update(result='success',endtime=datetime.datetime.now())
        else:
            a = DX_CeleryLog.objcets.filter(id=starttime_id)
            a.update(result='failure',endtime=datetime.datetime.now())
"""

"""
from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
"""
