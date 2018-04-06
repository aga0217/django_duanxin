# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
import datetime
#import pgcryptof
import requests
import json
from .jiami_jiemi_test import AESCipher
from .tasks import fasong_yibutest,add,sendsms
from django.db.models import Max

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
    dianhuahao = models.CharField(max_length=256, verbose_name=u'车户电话号码')
    yincheyuan_name = models.CharField(max_length=20, verbose_name=u'引车员姓名')
    yincheyuan_dianhua = models.CharField(max_length=20, verbose_name=u'引车员电话号码')
    fanhuizhi = models.CharField(max_length=20, verbose_name=u'接口返回值',null=True)
    fanhuixinxi = models.CharField(max_length=200,verbose_name=u'接口返回信息',null=True)
    next_riqi = models.CharField(max_length=6,verbose_name=u'下次年检日期',null=True)
    gongyingshang = models.CharField(max_length=100,verbose_name=u'短信供应商',null=True)
    paizhaoleibie_id = models.CharField(max_length=30, verbose_name=u'牌照类别ID', null=True)#对应'PZLBID'
    tjrcount = models.IntegerField(verbose_name=u'推荐人本月推荐计数',null=True)


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
    dianhua = models.CharField(max_length=256, verbose_name=u'电话号码',null=True)
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
    chezhu_beizhu = models.CharField(verbose_name=u'车主备注信息',null=True,max_length=256)#对车辆的车主信息进行备注



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
    is_del = models.BooleanField(verbose_name=u'是否删除', default=False)#是否删除
    nexttime = models.CharField(max_length=11,verbose_name=u'下次检测日期',null=True)

class DX_ShouFei(models.Model):
    jczid = models.CharField(max_length=5, verbose_name=u'检测站id')
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号')
    cheliangleibie_id = models.CharField(max_length=30, verbose_name=u'车辆类别ID')
    cheliangleibie_str = models.CharField(max_length=256, verbose_name=u'车辆类别str')
    chezhudianhua = models.CharField(max_length=30, verbose_name=u'车主电话', null=True)
    jyxm =  models.CharField(max_length=30, verbose_name=u'检验项目')#对应安检、尾气、综检、其他项目
    jylb = models.CharField(max_length=30, verbose_name=u'检验类别')#对# 应在用车检验、不透光中型、等级评定、服务费
    jylb_pinyin = models.CharField(max_length=256,verbose_name=u'检验类别拼音',null=True)
    dyid = models.IntegerField(verbose_name=u'对应数据库ID，sql数据库返回值',null=True)
    skr = models.CharField(max_length=30, verbose_name=u'收款人姓名')
    skr_username = models.CharField(max_length=30,verbose_name=u'收款人用户名')
    skrq = models.DateTimeField(verbose_name=u'收款日期')
    skje = models.IntegerField(verbose_name=u'收款金额')
    is_jiezhang = models.BooleanField(verbose_name=u'是否结账',default=False)
    jiezhangriqi = models.DateTimeField(verbose_name=u'结账日期',null = True)
    zhifufangshi_zimu = models.CharField(max_length=30,verbose_name=u'支付方式')#'01','02'
    zhifufangshi_str = models.CharField(max_length=30,verbose_name=u'支付方式字符串')#微信，支付宝，现金
    pingzhenghao = models.CharField(max_length=256,verbose_name=u'凭证号',null=True)#非现金支付时的凭证号
    bjr = models.CharField(max_length=30,verbose_name=u'编辑人员姓名',null = True)
    bjr_username = models.CharField(max_length=30,verbose_name=u'编辑人用户名',null=True)
    is_kaifapiao = models.BooleanField(default=False,verbose_name=u'是否开具发票')
    fapiao_qiri = models.DateTimeField(verbose_name=u'开发票日期',null=True)
    is_kefu = models.BooleanField(verbose_name=u'是否是客服服务',default=False)
    is_zhuanru = models.BooleanField(verbose_name=u'是否是转入车',default=False)
    is_tuikuan = models.BooleanField(verbose_name=u'是否退款',default=False)
    tuikuan_riqi = models.DateTimeField(verbose_name=u'退款日期',null=True)
    tuikuan_shuoming = models.CharField(max_length=256,verbose_name=u'退款说明',null=True)
    is_weiqitongbu = models.BooleanField(default=False,verbose_name=u'是否被尾气同步程序读取过')
    zongjian_cheliangleixing = models.CharField(max_length=256,verbose_name=u'综检车辆类型',null=True)#综检对应车辆类型客车、货车、出租车

    def tuikuan(self,user,pws,id):
        yanzheng = DX_ShouFei_UserName().UserDengLu(user,pws)
        if yanzheng.get('denglu') ==True and yanzheng.get('is_tuikuan') == True:
            qs = DX_ShouFei.objects.filter(id=id)
            #print qs[0].id

            if not qs:#qs为空
                return {'chenggong': False, 'cuowu': u'没有找到指定ID'}
            if qs[0].is_tuikuan == True or qs[0].is_kaifapiao == True:#已经标记开票的不允许退款
                return {'chenggong':False,'cuowu':u'该车已经退款或者已经开具发票'}
            qs.update(is_tuikuan=True,bjr=yanzheng.get('user_str'),bjr_username=yanzheng.get('username'),
                          tuikuan_riqi=datetime.datetime.now())
            self.deleteCustomerFile(id)#同时删除客服档案（指定当天的同一车牌同一车辆类型的车辆）
            jczid = qs[0].jczid
            cph = qs[0].paizhaohao
            pzlb_int = qs[0].cheliangleibie_id
            pzlb_str = qs[0].cheliangleibie_str
            czry = qs[0].skr
            czry_user = qs[0].skr_username
            fkfs_id = qs[0].zhifufangshi_zimu
            fkfs = qs[0].zhifufangshi_str
            is_tuikuan = True
            jylb = qs[0].jylb
            jfje = -qs[0].skje
            zongjian_cheliangleixing = qs[0].zongjian_cheliangleixing
            chezhudh = ''
            bjr_username = yanzheng.get('username')
            bjr = yanzheng.get('user_str')
            data = {qs[0].jyxm:{'jylb':jylb,'jfje':jfje,'zongjian_cheliangleixing':zongjian_cheliangleixing}}
            return {'chenggong':True,'data':{'jczid':jczid,'cph':cph,'pzlb_int':pzlb_int,
                                                 'pzlb_str':pzlb_str,'chezhudh':chezhudh,
                                                 'czry':czry,'czry_user':czry_user,'fkfs_id':fkfs_id,
                                                 'fkfs':fkfs,'is_tuikuan':is_tuikuan,'bjr_username':bjr_username,
                                                 'bjr':bjr,'data':data}}




        else:
            return {'chenggong':False,'cuowu':u'没有通过验证或没有退款权限'}
    #删除收费信息同时删除客户档案
    def deleteCustomerFile(self,id):
        qs = DX_ShouFei.objects.get(id=id)
        day = qs.skrq.day
        month = qs.skrq.month
        year = qs.skrq.year
        paizhaohao = qs.paizhaohao
        cheliangleibie_id = qs.cheliangleibie_id
        qs_update = DX_CustomerFile.objects.filter(paizhaohao=paizhaohao,cheliangleibie_id=cheliangleibie_id,
                                                   banliriqi__day=day,banliriqi__month=month,
                                                   banliriqi__year=year)
        qs_update.update(isdel = True)
    def searchshoufei(self,cph,cheliangleibie_id):
        today = datetime.date.today()
        startday = today-datetime.timedelta(days=60)
        endday = today+datetime.timedelta(days=1)
        qs = DX_ShouFei.objects.filter(skrq__gte=startday,skrq__lte=endday).filter(paizhaohao=cph,cheliangleibie_id=cheliangleibie_id).order_by('-skrq')
        qs_anjian = qs.filter(jyxm='anjian')
        if len(qs_anjian) ==0:
            anjian_jine = 0
        else:
            anjian_jine = qs_anjian[0].skje
        qs_weiqi = qs.filter(jyxm='weiqi')
        if len(qs_weiqi) == 0:
            weiqi_jine = 0
        else:
            weiqi_jine = qs_weiqi[0].skje
        if anjian_jine >0 and weiqi_jine >0:
            return {'chenggong':True}
        if anjian_jine == 0 or anjian_jine <0:
            return {'chenggong':False,'neirong':u'没有找到车辆安检收费记录，是否继续？'}
        if weiqi_jine == 0 and weiqi_jine <0:
            return {'chenggong':False,'neirong':u'没有找到车辆尾气收费记录，是否继续？'}

    def getweiqitongbushoufei(self,startday,endday):
        qs = DX_ShouFei.objects.filter(skrq__gte=startday, skrq__lte=endday).filter(jyxm='weiqi',is_weiqitongbu=False) \
            .order_by('-skrq')
        if not qs:#if not qs表示在qs没有查询结果的情况
            return None
        else:
            return qs.values_list('paizhaohao', 'cheliangleibie_id', 'skje', 'is_tuikuan','skrq','cheliangleibie_str')
        #qs = DX_ShouFei.objects.filter(skrq__gte=startday, skrq__lte=endday).filter(jyxm='weiqi',is_weiqitongbu=False).values_list('paizhaohao', 'cheliangleibie_id', 'skje', 'is_tuikuan')
    def decrefund(self,startday,endday,cph,chepai_leibie):#判断是否退款
        qs = DX_ShouFei.objects.filter(skrq__gte=startday, skrq__lte=endday).filter(paizhaohao=cph,
                    cheliangleibie_id=chepai_leibie).filter(jyxm='weiqi', is_weiqitongbu=False).values_list('skje')
        sumlist = []
        for i in qs:
            sumlist.append(i[0])
        sumskje = sum(sumlist)
        if sumskje > 0:#近一个月的收款金额总和大于0
            return False #退款状态为未退款
        else:
            return True #退款状态为已退款


class DX_ShouFei_UserName(models.Model):
    username = models.CharField(max_length=30,verbose_name=u'用户名')
    userxingming = models.CharField(max_length=30,verbose_name=u'员工姓名')
    chuangjianshijian = models.DateTimeField(verbose_name=u'创建时间')
    password = models.CharField(max_length=256,verbose_name=u'密码')
    is_qiyong = models.BooleanField(verbose_name=u'是否启用',default=True)
    is_tuikuan = models.BooleanField(verbose_name=u'是否可以退款',default=False)
    is_shoukuan = models.BooleanField(verbose_name=u'是否可以收款',default=True)
    is_jiezhang = models.BooleanField(verbose_name=u'是否可以结账',default=True)

    #已完成models中验证数据
    #TODO:返回权限设置,返回用户名和中文名称
    def UserDengLu(self,user,pws):
        self.aes_cipher = AESCipher()
        if not DX_ShouFei_UserName.objects.filter(username=user).exists():
            return {'denglu':False,'cuowu':u'用户名不存在'}
        else:
            qs = DX_ShouFei_UserName.objects.get(username=user)
            if self.aes_cipher.decrypt(qs.password) == pws and qs.is_qiyong == True:
                #print self.aes_cipher.decrypt(qs.password),pws
                qs1 = DX_ShouFei_UserName.objects.get(username=user)
                return {'denglu':True,'username':user,'user_str':qs1.userxingming,'is_tuikuan':qs1.is_tuikuan}
            else:
                return {'denglu':False,'cuowu':u'用户密码不正确或用户被禁用'}

    def XiuGaiMiMa(self,user,yuanshi_pws,xin_pws):
        self.aes_cipher = AESCipher()
        if not DX_ShouFei_UserName.objects.filter(username=user).exists():
            return {'chenggong':False,'cuowu':u'用户名不存在'}
        else:
            qs = DX_ShouFei_UserName.objects.get(username=user)
            if self.aes_cipher.decrypt(qs.password) == yuanshi_pws and qs.is_qiyong == True:
                qs1 = DX_ShouFei_UserName.objects.filter(username=user)
                xinmima = self.aes_cipher.encrypt(xin_pws)
                qs1.update(password=xinmima)
                return {'chenggong':True}
            else:
                return {'chenggong':False,'cuowu':u'原始密码未通过验证或用户被禁用'}

class DX_CustomerFile(models.Model):
    jczid = models.CharField(max_length=5, verbose_name=u'检测站id')
    paizhaohao = models.CharField(max_length=30, verbose_name=u'牌照号')
    cheliangleibie_id = models.CharField(max_length=30, verbose_name=u'车辆类别ID')
    cheliangleibie_str = models.CharField(max_length=256, verbose_name=u'车辆类别str')
    chezhudianhua = models.CharField(max_length=30, verbose_name=u'车主电话', null=True)
    banliriqi = models.DateTimeField(verbose_name=u'办理日期')
    anjianshoufei = models.IntegerField(verbose_name=u'安检收费金额',null=True)
    weiqishoufei = models.IntegerField(verbose_name=u'尾气收费金额',null=True)
    heji = models.IntegerField(verbose_name=u'合计收费金额')#不包括其他收费项目，只有安检、尾气、服务费
    tuijianren = models.CharField(max_length=256,verbose_name=u'推荐人',null=True)
    jingbanren = models.CharField(max_length=256,verbose_name=u'经办人',null=True)
    isdel = models.BooleanField(default=False,verbose_name=u'是否被删除')
    czry_user = models.CharField(max_length=256,verbose_name=u'操作人用户名')
    czry = models.CharField(max_length=256,verbose_name=u'操作人员姓名')
    beizhu = models.CharField(max_length=512,verbose_name=u'备注',null=True)

    def savesms(self,paizhaohao,jczid,tuijianren):
        q = DX_FaSongMX(paizhaohao=paizhaohao, tijiao_datetime=datetime.datetime.now(),
                        dianhuahao=self.gettell(jczid,tuijianren),
                        tjrcount=self.tjrcount(jczid,tuijianren),
                        yincheyuan_name=u'空', yincheyuan_dianhua=u'空', fasongjiekou='tixing_tjr', is_delete=False)
        q.save()
        #异步运行，如果使用delay方法会同步执行
        sendsms.delay(q.id)








    def gettell(self,jczid,tuijianren):
        qs = Dx_Recommender.objects.filter(jczid=jczid,name=tuijianren)
        return qs[0].tellnumber
    def tjrcount(self,jczid,tuijianren):
        today = datetime.date.today()
        qs = DX_CustomerFile.objects.filter(jczid=jczid,tuijianren=tuijianren,isdel=False,banliriqi__year=today.year,banliriqi__month=today.month)
        return len(qs)
    def addcustomerfile(self,jczid,paizhaohao,cheliangleibie_id,cheliangleibie_str,chezhudianhua,
                        anjianshoufei,weiqishoufei,tuijianren,czry_user,czry):
        q = DX_CustomerFile(jczid=jczid,paizhaohao=paizhaohao,cheliangleibie_id=cheliangleibie_id,
                            cheliangleibie_str=cheliangleibie_str,chezhudianhua=chezhudianhua,
                            anjianshoufei=anjianshoufei,weiqishoufei=weiqishoufei,heji=anjianshoufei+weiqishoufei,
                            tuijianren=tuijianren,banliriqi=datetime.datetime.now(),czry_user=czry_user,czry=czry)
        q.save()
        self.savesms(paizhaohao,jczid,tuijianren)

    def jiaochaSearch(self,qsList):
        for i in qsList:
            carinfo = self.carinfoSearch(i['paizhaohao'],i['cheliangleibie_id'])
            i['dipanhao'] = carinfo.get('dipanhao')
            i['chezhu'] = carinfo.get('chezhu')
        return qsList

    def carinfoSearch(self,paizhaohao,cheliangleibie_id):
        dic = {}
        qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=cheliangleibie_id).order_by('-chuanjianriqi')
        if qs:
           dic['dipanhao'] = qs[0].dipanhao
           dic['chezhu'] = qs[0].chezhu
        else:
            dic['dipanhao'] = ''
            dic['chezhu'] = ''
        return dic

    def searchtelandtjr(self,paizhaohao,cheliangleibie_id):
        dic = {}
        qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=cheliangleibie_id).order_by('-chuanjianriqi')
        if qs:
            dic['dianhua'] = qs[0].dianhua
        else:
            dic['dianhua'] = None
        qs = DX_CustomerFile.objects.filter(paizhaohao=paizhaohao,cheliangleibie_id=cheliangleibie_id).order_by('-banliriqi')
        if qs:
            tuijianren = qs[0].tuijianren
            verifyname = Dx_Recommender().verifyrecommendername(tuijianren)
            if verifyname:
                dic['tjr'] = tuijianren
            else:
                dic['tjr'] = None#当查询出的推荐人不存在于推荐人列表中时返回空
        else:
            dic['tjr'] = None
        return dic

    def deldangan(self,id_list):
        qs = DX_CustomerFile.objects.filter(id__in=id_list)
        qs.update(isdel = True)
        return True

    def updatedangan(self,jczid,id,beizhu,tuijianren,dianhua):
        qs = DX_CustomerFile.objects.filter(jczid=jczid,id=id)
        if qs.exists():
            DXCustomerFileLog().addlog(id,qs[0].tuijianren,qs[0].beizhu,qs[0].chezhudianhua,
                                       tuijianren,beizhu,dianhua)
            qs.update(beizhu=beizhu, tuijianren=tuijianren,chezhudianhua=dianhua)
            paizhaohao = qs[0].paizhaohao
            paizhaoleibie_id = qs[0].cheliangleibie_id
            self.updatecarinfo_tell(paizhaohao,paizhaoleibie_id,dianhua)
            return {'chenggong':True}
        else:
            return {'chenggong':False,'cuowu':u'没有找到对应id'}

    def updatecarinfo_tell(self,paizhaohao,paizhaoleibie_id,dianhua):
        qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=paizhaoleibie_id)
        if dianhua != '':#删除电话后传入值为''
            self.aes_cipher = AESCipher()
            qs.update(dianhua=self.aes_cipher.encrypt(dianhua))
        else:
            qs.delete()


class Dx_TellNumCount(models.Model):
    jczid = models.CharField(max_length=5, verbose_name=u'检测站id')
    tellnum = models.CharField(max_length=15,verbose_name=u'电话号码')
    tellnumcount = models.IntegerField(default=0,verbose_name=u'出现次数')

    def guishudi(self,tellnum):
        """
        #url = "https://way.jd.com/jisuapi/query4?shouji="+tellnum+"&appkey=f2a58b43cdc3bdfd31962fdf87b9dd88"
        url = 'https://way.jd.com/shujujia/mobile?mobile='+tellnum+'&appkey=f2a58b43cdc3bdfd31962fdf87b9dd88'
        try:
            resp = requests.get(url,timeout=2)
        except:
            guishudi = u'resp错误'
            return guishudi
        result_rep = resp.content
        try:
            result = json.loads(result_rep)
        except:
            guishudi = u'json cuowu'
            return guishudi
        if result.get('code') != '10000':
            guishudi = result.get('msg')
            return guishudi
        guishudi = result.get('result').get('province')
        """
        return u'内蒙古自治区'

    def count(self,jczid,tellnum):
        qs = Dx_TellNumCount.objects.filter(jczid=jczid,tellnum=tellnum)
        if qs.exists():#如果电话存在则加一
            cishu = qs[0].tellnumcount
            qs.update(tellnumcount=cishu+1)
            return cishu
        else:#不存在则 添加
            qs = Dx_TellNumCount(jczid=jczid,tellnum=tellnum,tellnumcount=1)
            qs.save()
            return 1

    def veriftell(self,jczid,tellnum):
        cishu = self.count(jczid,tellnum)
        guishudi = self.guishudi(tellnum)
        return {'guishudi':guishudi,'cishu':cishu}

class SF_log(models.Model):
    json_jieshou = models.CharField(max_length=2048, verbose_name=u'接收内容')
    json_fanhui = models.CharField(max_length=2048, verbose_name=u'返回内容')
    jieshou_time = models.DateTimeField(verbose_name=u'接收时间', null=True)
    fanhui_time = models.DateTimeField(verbose_name=u'返回时间', null=True)

class DXCustomerFileLog(models.Model):
    original_id =  models.IntegerField(verbose_name=u'原始id')
    original_content = models.CharField(max_length=2048,verbose_name=u'原始内容')
    new_content = models.CharField(max_length=2048,verbose_name=u'新内容')
    upeate_time = models.DateTimeField(verbose_name=u'更新时间')
    update_host = models.CharField(max_length=32,verbose_name=u'更新机器IP地址',null=True)


    def addlog(self,id,otjr,obeizhu,odianhua,ntjr,nbeizhu,ndianhua):
        oconlist = []#原始内容列表
        nconlist = []#新内容列表
        otjr1 = u'推荐人：'+otjr
        if obeizhu == None:
            obeizhu1 = u'备注：空'
        else:
            obeizhu1 = u'备注：'+obeizhu
        if odianhua == None:
            odianhua1 = u'电话：空'
        else:
            odianhua1 = u'电话：'+odianhua
        oconlist.append(otjr1)
        oconlist.append(obeizhu1)
        oconlist.append(odianhua1)
        oconstr = ';'.join(oconlist)
        if ntjr == None:
            ntjr1 = u'推荐人：空'
        else:
            ntjr1 = u'推荐人'+ntjr
        if nbeizhu == None:
            nbeizhu1 = u'备注：空'
        else:
            nbeizhu1 = u'备注：'+nbeizhu
        if ndianhua == None:
            ndianhua1 = u'电话：空'
        else:
            ndianhua1 = u'电话：'+ndianhua
        nconlist.append(ntjr1)
        nconlist.append(nbeizhu1)
        nconlist.append(ndianhua1)
        nconstr = ';'.join(nconlist)
        q = DXCustomerFileLog(original_id=id,original_content=oconstr,new_content=nconstr,
                              upeate_time=datetime.datetime.now())
        q.save()

class Dx_Recommender(models.Model):#推荐人
    jczid = models.CharField(max_length=2,verbose_name=u'检测站id')
    name = models.CharField(max_length=30,verbose_name=u'推荐人姓名')
    tellnumber = models.CharField(max_length=256,verbose_name=u'推荐人电话')
    creattime = models.DateTimeField(verbose_name=u'创建时间')

    def getrecommenderlist(self,jczid):
        qs = Dx_Recommender.objects.filter(jczid=jczid).values_list('name')
        relist = []#返回类似[u'\u4faf\u5229\u9e4f', u'\u59da\u519b']的列表
        for i in qs:
            relist.append(i[0])
        return {'chenggong':True,'data':relist}

    def addrecommender(self,jczid,name,tellnumber):
        self.aes_cipher = AESCipher()
        qs = Dx_Recommender.objects.filter(jczid=jczid,name=name)
        if qs.exists():
            return {'chenggong':False,'cuowu':u'该人员已存在'}
        q = Dx_Recommender(jczid=jczid,name=name,tellnumber=self.aes_cipher.encrypt(tellnumber),
                           creattime=datetime.datetime.now())
        q.save()
        return {'chenggong':True}

    def verifyrecommendername(self,tuijianren):
        qs = Dx_Recommender.objects.filter(name=tuijianren)
        if qs.exists():
            return True
        else:
            return False

class DX_CeleryLog(models.Model):
    comname = models.CharField(max_length=128,verbose_name=u'执行命令名称')
    starttime = models.DateTimeField(verbose_name=u'开始执行时间')
    endtime = models.DateTimeField(verbose_name=u'结束执行时间',null=True)
    result = models.CharField(max_length=1024, verbose_name=u'执行结果', null=True)
#TODO:增加记录付款方式的表
class DX_ShouFei_Config_FuKuanFangShi(models.Model):
    fukuanfangshi = models.CharField(max_length=100,verbose_name=u'付款方式列表')
    isuse = models.BooleanField(default=True)
    def getfukuanfangshi(self):
        fukuanfangshi = []
        qs = DX_ShouFei_Config_FuKuanFangShi.objects.filter(isuse = True).order_by('id').values_list('fukuanfangshi')
        for i in qs:
            fukuanfangshi.append(i[0])
        return fukuanfangshi

class DX_ShouFei_Config_CheLiangLeiXing(models.Model):
    cheliangleixing = models.CharField(max_length=100,verbose_name=u'车辆类型列表')
    isuse = models.BooleanField(default=True)
    def getcheliangleixing(self):
        cheliangleixing = []
        qs = DX_ShouFei_Config_CheLiangLeiXing.objects.filter(isuse = True).order_by('id').values_list('cheliangleixing')
        for i in qs:
            cheliangleixing.append(i[0])
        return cheliangleixing

class DX_ShouFei_Config_ChePaiQian(models.Model):
    chepaiqian = models.CharField(max_length=100,verbose_name=u'车牌省份简称')
    isuse = models.BooleanField(default=True)
    count = models.IntegerField(null=True,verbose_name=u'省份简称出现的次数')#为今后的动态排序提供基础
    def getchepaiqian(self):
        chepaiqian = []
        qs = DX_ShouFei_Config_ChePaiQian.objects.filter(isuse=True).order_by('-count').values_list('chepaiqian')
        for i in qs:
            chepaiqian.append(i[0])
        return chepaiqian

class DX_ShouFei_Config_ChePaiZiMu(models.Model):
    chepaizimu = models.CharField(max_length=10,verbose_name=u'车牌字母')
    isuse = models.BooleanField(default=True)
    def getchepaizimu(self):
        chepaizimu = []
        qs = DX_ShouFei_Config_ChePaiZiMu.objects.filter(isuse=True).order_by('id').values_list('chepaizimu')
        for i in qs:
            chepaizimu.append(i[0])
        return chepaizimu

class DX_ShouFei_Config_ChaXunShouFeiXiangMu(models.Model):
    chaxunshoufeixiangmu = models.CharField(max_length=50,verbose_name=u'查询收费项目')
    isuse = models.BooleanField(default=True)
    def getchaxunshoufeixiangmu(self):
        chaxunshoufeixiangmu = []
        qs = DX_ShouFei_Config_ChaXunShouFeiXiangMu.objects.filter(isuse=True).order_by('id').values_list('chaxunshoufeixiangmu')
        for i in qs:
            chaxunshoufeixiangmu.append(i[0])
        return chaxunshoufeixiangmu

class DX_ShouFei_Config_AnJianShouFeiXiangMuDic(models.Model):
    cheliangleixing_id = models.CharField(max_length=2,verbose_name=u'车辆类型id')
    shoufeixiangmu = models.CharField(max_length=200,verbose_name=u'收费项目')
    def getanjianshoufeixiangmudic(self):
        anjianshoufeixiangmudic = {}
        qs = DX_ShouFei_Config_AnJianShouFeiXiangMuDic.objects.all()
        for i in qs:
            shoufeixiangmulist = i.shoufeixiangmu.split(',')
            anjianshoufeixiangmudic[i.cheliangleixing_id] = shoufeixiangmulist
        return anjianshoufeixiangmudic

class DX_ShouFei_Config_WeiQiShouFeiXiangMu(models.Model):
    weiqishoufeixiangmu = models.CharField(max_length=200,verbose_name=u'尾气收费项目')
    isuse = models.BooleanField(default=True)
    count = models.IntegerField(default=0,verbose_name=u'收费项目计数')
    def getweiqishoufeixiangmu(self):
        weiqishoufeixiangmu = []
        qs = DX_ShouFei_Config_WeiQiShouFeiXiangMu.objects.filter(isuse=True).order_by('id').values_list('weiqishoufeixiangmu')
        for i in qs:
            weiqishoufeixiangmu.append(i[0])
        return weiqishoufeixiangmu

class DX_ShouFei_Config_ZongJianXiangMu(models.Model):
    zongjianxiangmu = models.CharField(max_length=200,verbose_name=u'综检收费项目')
    isuse = models.BooleanField(default=True)
    count = models.IntegerField(default=0,verbose_name=u'收费项目计数')
    def getzongjianshoufeixiangmu(self):
        zongjianshoufeixiangmu = []
        qs = DX_ShouFei_Config_ZongJianXiangMu.objects.filter(isuse=True).order_by('id').values_list('zongjianxiangmu')
        for i in qs:
            zongjianshoufeixiangmu.append(i[0])
        return zongjianshoufeixiangmu

class DX_ShouFei_Config_ZongJianCheLiangLeiXing(models.Model):
    zongjiancheliangleixing = models.CharField(max_length=200,verbose_name=u'综检收费项目')
    isuse = models.BooleanField(default=True)
    count = models.IntegerField(default=0,verbose_name=u'收费项目计数')
    def getzongjiancheliangleixing(self):
        zongjiancheliangleixing = []
        qs = DX_ShouFei_Config_ZongJianCheLiangLeiXing.objects.filter(isuse=True).order_by('id').values_list('zongjiancheliangleixing')
        for i in qs:
            zongjiancheliangleixing.append(i[0])
        return zongjiancheliangleixing

class DX_ShouFei_Config_QiTaXiangMu(models.Model):
    qitaxiangmu = models.CharField(max_length=200,verbose_name=u'其他收费项目')
    isuse = models.BooleanField(default=True)
    count = models.IntegerField(default=0,verbose_name=u'收费项目计数')
    def getqitaxiangmu(self):
        qitaxiangmu = []
        qs = DX_ShouFei_Config_QiTaXiangMu.objects.filter(isuse=True).order_by('id').values_list('qitaxiangmu')
        for i in qs:
            qitaxiangmu.append(i[0])
        return qitaxiangmu

class DX_ShouFei_Config_CheLiangLeiXingToInt(models.Model):
    cheliangleixing = models.CharField(max_length=200,verbose_name=u'车辆类型')
    leixingint = models.CharField(max_length=2,verbose_name=u'车辆类型对应int')
    def getcheliangleixingtoint(self):
        dic1 = {}
        qs = DX_ShouFei_Config_CheLiangLeiXingToInt.objects.all()
        for i in qs:
            dic1[i.cheliangleixing] = i.leixingint
        return dic1
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
    def handle(self, *args, **options):
        q = DX_CeleryLog(comname='fasong_yibutest',starttime=datetime.datetime.now())
        q.save()
        q_id = q.id
        qs = DX_FaSongMX.objects.filter(is_delete=False).filter(is_fasong=False,fasongjiekou__in = ['yewu_kaishi','yewu_banjie','tixing_tjr'])
        fasong_ID = []
        #fasong_neirong = u'【鑫运检测】尊敬的%s车主您好，欢迎来到我站，本次业务由%s电话%s为您服务，监督、投诉请拨打6491572。' % (i.paizhaohao,i.yincheyuan_name,i.yincheyuan_dianhua)

        if len(qs) == 0:
            qs = DX_CeleryLog.objects.filter(id=q_id)
            qs.update(endtime=datetime.datetime.now())
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
        qs = DX_CeleryLog.objects.filter(id = q_id)
        qs.update(endtime=datetime.datetime.now())
    
"""




