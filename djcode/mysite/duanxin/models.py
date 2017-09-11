# -*- coding: utf-8 -*-
from django.db import models
import datetime
#import pgcryptof
from jiami_jiemi_test import AESCipher

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
    dyid = models.IntegerField(verbose_name=u'对应数据库ID，sql数据库返回值')
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

    def tuikuan(self,user,pws,id):
        yanzheng = DX_ShouFei_UserName().UserDengLu(user,pws)
        if yanzheng.get('denglu') ==True and yanzheng.get('is_tuikuan') == True:
            qs = DX_ShouFei.objects.filter(id=id)
            print qs[0].id

            if not qs:#qs为空
                return {'chenggong': False, 'cuowu': u'没有找到指定ID'}
            if qs[0].is_tuikuan == True or qs[0].is_kaifapiao == True:
                return {'chenggong':False,'cuowu':u'该车已经退款或者已经开具发票'}
            qs.update(is_tuikuan=True,bjr=yanzheng.get('user_str'),bjr_username=yanzheng.get('username'),
                          tuikuan_riqi=datetime.datetime.now())
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
            chezhudh = ''
            bjr_username = yanzheng.get('username')
            bjr = yanzheng.get('user_str')
            data = {qs[0].jyxm:{'jylb':jylb,'jfje':jfje}}
            return {'chenggong':True,'data':{'jczid':jczid,'cph':cph,'pzlb_int':pzlb_int,
                                                 'pzlb_str':pzlb_str,'chezhudh':chezhudh,
                                                 'czry':czry,'czry_user':czry_user,'fkfs_id':fkfs_id,
                                                 'fkfs':fkfs,'is_tuikuan':is_tuikuan,'bjr_username':bjr_username,
                                                 'bjr':bjr,'data':data}}



        else:
            return {'chenggong':False,'cuowu':u'没有通过验证或没有退款权限'}


    #TODO:标记开票的不允许退款

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


    def addcustomerfile(self,jczid,paizhaohao,cheliangleibie_id,cheliangleibie_str,chezhudianhua,
                        anjianshoufei,weiqishoufei,tuijianren,czry_user,czry):
        q = DX_CustomerFile(jczid=jczid,paizhaohao=paizhaohao,cheliangleibie_id=cheliangleibie_id,
                            cheliangleibie_str=cheliangleibie_str,chezhudianhua=chezhudianhua,
                            anjianshoufei=anjianshoufei,weiqishoufei=weiqishoufei,heji=anjianshoufei+weiqishoufei,
                            tuijianren=tuijianren,banliriqi=datetime.datetime.now(),czry_user=czry_user,czry=czry)
        q.save()
    def jiaochaSearch(self,qsList):
        for i in qsList:
            carinfo = self.carinfoSearch(i['paizhaohao'],i['cheliangleibie_id'])
            i['dipanhao'] = carinfo.get('dipanhao')
            i['chezhu'] = carinfo.get('chezhu')
        return qsList
    def carinfoSearch(self,paizhaohao,cheliangleibie_id):
        dic = {}
        print paizhaohao,cheliangleibie_id
        qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=cheliangleibie_id).order_by('-chuanjianriqi')
        if qs:
           dic['dipanhao'] = qs[0].dipanhao
           dic['chezhu'] = qs[0].chezhu
        else:
            dic['dipanhao'] = ''
            dic['chezhu'] = ''
        return dic








class SF_log(models.Model):
    json_jieshou = models.CharField(max_length=2048, verbose_name=u'接收内容')
    json_fanhui = models.CharField(max_length=2048, verbose_name=u'返回内容')
    jieshou_time = models.DateTimeField(verbose_name=u'接收时间', null=True)
    fanhui_time = models.DateTimeField(verbose_name=u'返回时间', null=True)



