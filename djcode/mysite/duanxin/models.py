# -*- coding: utf-8 -*-
from django.db import models
import datetime
#import pgcrypto


class DX_FaSongMX(models.Model):#短信发送明细
    #paizhaoyanse_CHOICES = (('','入库'),('OUT','出库'))
    #churukufangxiang = models.CharField(choices=churukufangxiang_CHOICES, max_length=10, verbose_name=u'出/入库')
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号')
    tijiao_datetime = models.DateTimeField(verbose_name=u'提交时间')
    tijiao_neirong = models.CharField(max_length=300, verbose_name=u'提交内容')
    fasong_datetime = models.DateTimeField(null= True,verbose_name=u'发送时间')
    is_delete = models.BooleanField(default=False,verbose_name=u'是否被删除')
    is_fasong = models.BooleanField(default=False,verbose_name=u'是否已发送')
    fasongjiekou = models.CharField(max_length=300, verbose_name=u'发送接口',null=True)
    dianhuahao = models.CharField(max_length=20, verbose_name=u'车户电话号码')
    yincheyuan_name = models.CharField(max_length=20, verbose_name=u'引车员姓名')
    yincheyuan_dianhua = models.CharField(max_length=20, verbose_name=u'引车员电话号码')
    fanhuizhi = models.CharField(max_length=20, verbose_name=u'接口返回值',null=True)
    fanhuixinxi = models.CharField(max_length=200,verbose_name=u'接口返回信息',null=True)


class DX_CarInfo(models.Model):
    chepai_qian_CHOICES = ((u'蒙','蒙'),(u'京','京'),(u'津','津'),(u'沪','沪'),(u'渝','渝'),(u'冀','冀'),(u'豫','豫'),
                           (u'云','云'),(u'辽','辽'),(u'黑','黑'),(u'湘','湘'),(u'皖','皖'),(u'鲁','鲁'),(u'新','新'),
                           (u'苏','苏'),(u'浙','浙'),(u'赣','赣'),(u'桂','桂'),(u'甘','甘'),(u'晋','晋'),(u'陕','陕'),
                           (u'吉','吉'),(u'闽','闽'),(u'贵','贵'),(u'青','青'),(u'藏','藏'),(u'琼','琼'),(u'粤','粤'))
    chepai_qian = models.CharField(choices=chepai_qian_CHOICES, max_length=10, verbose_name=u'请选择',default='蒙')
    chepai_hou_CHOICES = (('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('J','J'),
                          ('K','K'),('L','L'),('M','M'),('N','N'),('O','O'),('P','P'),('Q','Q'),('R','R'),('S','S'),
                          ('T','T'),('U','U'),('V','V'),('W','W'),('X','X'),('Y','Y'),('Z','Z'))
    chepai_hou = models.CharField(choices=chepai_hou_CHOICES, max_length=10, verbose_name=u'',default='A')
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号(不要再输入汉字部分！忽略大小写)')
    dianhua = models.CharField(max_length=11, verbose_name=u'电话号码',null=True)
    cheliangleibie_id = models.CharField(max_length=30,verbose_name=u'车辆类别ID', null=True)
    cheliangleibie_str = models.CharField(max_length=30, verbose_name=u'车辆类别字符串', null=True)

    paizhaoleibie_id = models.CharField(max_length=30, verbose_name=u'牌照类别ID', null=True)#对应'PZLBID'
    paizhaoleibie_str = models.CharField(max_length=30, verbose_name=u'牌照类别字符串', null=True)#对应'PZLBStr'
    yingyunleibie_id = models.CharField(max_length=10,verbose_name=u'营运类别ID', null=True)#对应‘SYXZID’
    yingyunleibie_str = models.CharField(max_length=20,verbose_name=u'营运类别字符串', null=True)#对应'SYXZStr'
    chezhu = models.CharField(max_length=50, verbose_name=u'车主姓名或单位名称', null=True)#对应'DW'
    dipanhao = models.CharField(max_length=50, verbose_name=u'底盘号', null=True)#对应'DPH'

    dengjiriqi = models.DateField(verbose_name=u'登记日期',null=True)
    next_riqi = models.CharField(max_length=11,verbose_name=u'下次检测日期',null=True)
    chuanjianriqi = models.DateTimeField(verbose_name=u'资料创建日期',auto_now_add=datetime.datetime.now())
    iswanzheng = models.BooleanField(verbose_name=u'资料是否完整',default=False)
    jiancecishu = models.IntegerField(verbose_name=u'检测次数',null=True,default=1)#记录车辆第几次来
    editriqi = models.DateTimeField(verbose_name=u'修改日期')#记录修改日期，完整数据时会修改，第二次录入会修改
    tongbulaiyuan = models.CharField(verbose_name=u'同步来源',null=True,max_length=10)#车辆信息来自于尾气还是年检



class DX_Tongbu(models.Model):
    auto_id = models.IntegerField(verbose_name=u'对应sqlserver autoid')
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号')#对应'CPH'
    cheliangleibie_id = models.CharField(max_length=30,verbose_name=u'车辆类别ID')#对应'CLLBXID'
    cheliangleibie_str = models.CharField(max_length=30, verbose_name=u'车辆类别字符串')#对应'CLLBXStr'
    paizhaoleibie_id = models.CharField(max_length=30, verbose_name=u'牌照类别ID')#对应'PZLBID'
    paizhaoleibie_str = models.CharField(max_length=30, verbose_name=u'牌照类别字符串')#对应'PZLBStr'
    yingyunleibie_id = models.CharField(max_length=10,verbose_name=u'营运类别ID')#对应‘SYXZID’
    yingyunleibie_str = models.CharField(max_length=20,verbose_name=u'营运类别字符串')#对应'SYXZStr'
    chezhu = models.CharField(max_length=50, verbose_name=u'车主姓名或单位名称')#对应'DW'
    dipanhao = models.CharField(max_length=50, verbose_name=u'底盘号')#对应'DPH'
    chuchangriqi = models.DateTimeField(verbose_name=u'出厂日期')#对应'MakeDate'
    dengjiriqi = models.DateTimeField(verbose_name=u'登记日期')#对应'DJDate'
    chuanjianriqi = models.DateTimeField(verbose_name=u'资料创建日期',auto_now_add=datetime.datetime.now())
    istongbu = models.BooleanField(default=False,verbose_name=u'是否已被读取')

class DX_Gezhongcanshu(models.Model):
    tongbu_auto_id = models.IntegerField(verbose_name=u'上次同步最后一个id')#记录最后一次同步的ID，为下次同步提供ID

class DX_Yincheyuan(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'引车员姓名')
    dianhua = models.CharField(max_length=30, verbose_name=u'引车员电话')
    isdelete = models.BooleanField(default=False,verbose_name=u'是否被删除')

class DX_Xingshizheng(models.Model):
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号(不要再输入汉字部分！忽略大小写)')
    cheliangleibie_id = models.CharField(max_length=30, verbose_name=u'车辆类别ID', null=True)
    is_fasong = models.BooleanField(verbose_name=u'是否发送信息', default=False)#是否发送

    chuanjianriqi = models.DateTimeField(verbose_name=u'资料创建日期', auto_now_add=datetime.datetime.now())
    fasong_time = models.DateTimeField(verbose_name=u'发送时间',null=True)




