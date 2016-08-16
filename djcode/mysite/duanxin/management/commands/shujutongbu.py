#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from duanxin.models import *
import datetime
import pymssql

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        tongbu_next = DX_Gezhongcanshu.objects.get(id=1).tongbu_auto_id
        conn = pymssql.connect('172.18.130.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM carinfo WHERE autoid>%d',tongbu_next)
        tongbu = None
        if  cursor.fetchall()[0][0] == 0:
            tongbu = tongbu_next
        else:
            cursor = conn.cursor(as_dict=True)
            cursor.execute('SELECT * FROM carinfo WHERE autoid>%d',tongbu_next)

            for i in cursor:
                auto_id = i.get('AutoID')
                paizhaohao = i.get('CPH')
                cheliangleibie_id = i.get('CLLBXID')
                cheliangleibie_str = i.get('CLLBXStr')
                paizhaoleibie_id = i.get('PZLBID')
                paizhaoleibie_str = i.get('PZLBStr')
                chezhu = i.get('DW')
                dipanhao = i.get('DPH')
                chuchangriqi = i.get('MakeDate')
                dengjiriqi = i.get('DJDate')
                yingyunleibie_id = i.get('SYXZID')
                yingyunleibie_str = i.get('SYXZStr')
                if not DX_Tongbu.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=paizhaoleibie_id).exists():
                    q = DX_Tongbu(auto_id=auto_id,paizhaohao=paizhaohao,cheliangleibie_id=cheliangleibie_id,cheliangleibie_str=cheliangleibie_str,
                          paizhaoleibie_id=paizhaoleibie_id,paizhaoleibie_str=paizhaoleibie_str,chezhu=chezhu,dipanhao=dipanhao,
                          chuchangriqi=chuchangriqi,dengjiriqi=dengjiriqi,yingyunleibie_id=yingyunleibie_id,yingyunleibie_str=yingyunleibie_str)
                    q.save()
                    tongbu = i.get('AutoID')
        p = DX_Gezhongcanshu.objects.filter(id=1)
        p.update(tongbu_auto_id=tongbu)
        conn.close()


#s = "INSERT INTO UFee VALUES (74675,u'蒙AN5696','02','小型汽车',0,'在用机动车检验','','安检费','张晓林',datetime.datetime(),90)"

#s = "INSERT INFO UFee VALUES (74675,'蒙AN5696','02','小型汽车',0,'在用机动车检验','','安检费','张晓林','2016-5-5 10:43:44',90)"#


