#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from duanxin.models import *
import datetime
import pymssql
import re

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):#同步年检信息
        tongbu_next = DX_Gezhongcanshu.objects.get(id=2).tongbu_auto_id
        conn = pymssql.connect('172.18.130.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM ufee WHERE fphm>%d',tongbu_next)
        tongbu = None
        today = datetime.date.today()
        year,month,day = today.year , today.month,today.day
        if  cursor.fetchall()[0][0] == 0:
            tongbu = tongbu_next
        else:
            cursor = conn.cursor(as_dict=True)
            cursor.execute('SELECT * FROM ufee WHERE fphm>%d',tongbu_next)

            for i in cursor:
                chepaihao = i.get('CPH').replace(' ','')
                dianhua = i.get('JKDW')
                pzlbid = i.get('PZLBID')#牌照类别ID
                pzlb = i.get('PZLB')#类别ID对应中文
                if self.Isdianhua(dianhua):
                    chepai_qian_hou = self.Chepaihaofenkai(chepaihao)
                    chepai_qian = chepai_qian_hou.get('chepai_qian')
                    chepai_hou = chepai_qian_hou.get('chepai_hou')

                    if DX_CarInfo.objects.filter(paizhaohao=chepaihao,paizhaoleibie_id=pzlbid).exists():#如果车号和类别在车辆信息表存在
                        qs = DX_CarInfo.objects.filter(paizhaohao=chepaihao,paizhaoleibie_id=pzlbid)
                        if qs[0].iswanzheng == True and self.IsSameDay(qs[0].editriqi) != True:
                            qs.update(jiancecishu=qs[0].jiancecishu+1,editriqi=datetime.datetime.now(),dianhua=dianhua,
                                next_riqi=self.next_riqi_def(qs[0].dengjiriqi,qs[0].paizhaoleibie_id,qs[0].yingyunleibie_id))
                        else:
                            qs.update(editriqi=datetime.datetime.now(),dianhua=dianhua)
                    else:
                        p = DX_CarInfo(dianhua=dianhua,paizhaohao=chepaihao,chepai_hou=chepai_hou,chepai_qian=chepai_qian,
                                       paizhaoleibie_id=pzlbid,paizhaoleibie_str=pzlb,tongbulaiyuan='nianjian')
                        p.save()
                    if not DX_FaSongMX.objects.filter(paizhaohao=chepaihao).filter(tijiao_datetime__year=year,tijiao_datetime__month=month,
                                                                               tijiao_datetime__day=day).exists():#如果车号和类别在发送明细中不存在
                        q = DX_FaSongMX(paizhaohao=chepaihao,tijiao_datetime=datetime.datetime.now(),dianhuahao=dianhua,
                                        yincheyuan_name=u'空',yincheyuan_dianhua=u'空',fasongjiekou='yewu_kaishi')
                        q.save()


                tongbu = i.get('FPHM')
        p = DX_Gezhongcanshu.objects.filter(id=2)
        p.update(tongbu_auto_id=tongbu)
        conn.close()
        self.handle1()
        #TODO:完成尾气同步时同时判断车牌号和牌照类别

    def handle1(self, *args, **options):#t同步尾气信息
        tongbu_next = DX_Gezhongcanshu.objects.get(id=3).tongbu_auto_id
        conn = pymssql.connect('172.18.130.50', 'sa', 'svrcomputer', 'hbjcdb')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM ufee WHERE fphm>%d',tongbu_next)
        tongbu = None
        today = datetime.date.today()
        year,month,day = today.year , today.month,today.day

        if  cursor.fetchall()[0][0] == 0:
            tongbu = tongbu_next
        else:
            cursor = conn.cursor(as_dict=True)
            cursor.execute('SELECT * FROM ufee WHERE fphm>%d',tongbu_next)

            for i in cursor:
                chepaihao = i.get('CPH').replace(' ','')
                dianhua = i.get('JKDW')
                pzlbid = i.get('PZLBID')
                pzlbstr = i.get('PZLBStr')
                if self.Isdianhua(dianhua):
                    chepai_qian_hou = self.Chepaihaofenkai(chepaihao)
                    chepai_qian = chepai_qian_hou.get('chepai_qian')
                    chepai_hou = chepai_qian_hou.get('chepai_hou')

                    if DX_CarInfo.objects.filter(paizhaohao=chepaihao,paizhaoleibie_id=pzlbid).exists():
                        qs = DX_CarInfo.objects.filter(paizhaohao=chepaihao,paizhaoleibie_id=pzlbid)
                        if qs[0].iswanzheng == True and self.IsSameDay(qs[0].editriqi) != True:
                            qs.update(jiancecishu=qs[0].jiancecishu+1,editriqi=datetime.datetime.now(),dianhua=dianhua,
                                next_riqi=self.next_riqi_def(qs[0].dengjiriqi,qs[0].paizhaoleibie_id,qs[0].yingyunleibie_id))
                        else:
                            qs.update(editriqi=datetime.datetime.now(),dianhua=dianhua)
                    else:
                        p = DX_CarInfo(dianhua=dianhua,paizhaohao=chepaihao,chepai_hou=chepai_hou,chepai_qian=chepai_qian,
                                       paizhaoleibie_id=pzlbid,paizhaoleibie_str=pzlbstr,tongbulaiyuan='weiqi')
                        p.save()
                    if not DX_FaSongMX.objects.filter(paizhaohao=chepaihao).filter(tijiao_datetime__year=year,tijiao_datetime__month=month,
                                                                               tijiao_datetime__day=day).exists():
                        q = DX_FaSongMX(paizhaohao=chepaihao,tijiao_datetime=datetime.datetime.now(),dianhuahao=dianhua,
                                        yincheyuan_name=u'空',yincheyuan_dianhua=u'空',fasongjiekou='yewu_kaishi')
                        q.save()


                tongbu = i.get('FPHM')
        p = DX_Gezhongcanshu.objects.filter(id=3)
        p.update(tongbu_auto_id=tongbu)
        conn.close()



    def Isdianhua(self,dianhua):#简单判断是不是一个有效电话号码
        re_dianhua = ur"[0-9]"
        if re.match(re_dianhua,dianhua) and dianhua[0] == '1' and len(dianhua) == 11:
            return True
        else:
            return False

    def Chepaihaofenkai(self,chepaihao):
        chepai_qian = chepaihao[0]
        chepai_hou = chepaihao[1]
        return {'chepai_qian':chepai_qian,'chepai_hou':chepai_hou}


    def next_riqi_def(self,dengjiriqi,paizhaoleibie_id,yingyunleibie_id=None):
        korh = paizhaoleibie_id[0]
        dengjiriqi_year = dengjiriqi.year
        dengjiriqi_month = str(dengjiriqi)[5:7]
        today_year = datetime.date.today().year
        next_year = None
        if korh == "K" and yingyunleibie_id == "A": #出租车
            next_year = today_year+1
            return  str(next_year)+dengjiriqi_month
        if korh == 'K':
            if today_year-dengjiriqi_year >=6:
                next_year = today_year +1
            elif today_year-dengjiriqi_year < 6:
                next_year = today_year + 2
            return str(next_year)+dengjiriqi_month
        if korh == 'H':
            if today_year - dengjiriqi_year < 10:
                next_year = today_year +1
            else:
                bannian_next = datetime.datetime(today_year,int(dengjiriqi_month),1)+datetime.timedelta(days=185)
                next_year = bannian_next.year
                dengjiriqi_month = str(bannian_next.month)
            return str(next_year)+dengjiriqi_month
        if korh == 'M':

            if today_year - dengjiriqi_year < 4:
                next_year = today_year + 2
            else:
                next_year = today_year + 1
            return str(next_year)+dengjiriqi_month
        else:
            next_year = today_year+1
            next_riqi_str = str(next_year)+dengjiriqi_month
            return next_riqi_str

    def IsSameDay(self,datetime_1):
        year,month,day = datetime_1.year,datetime_1.month,datetime_1.day
        datetime_2 = datetime.date(year,month,day)
        today = datetime.date.today()
        if datetime_2 == today:
            return True
        else:
            return False



