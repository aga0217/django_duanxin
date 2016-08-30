# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from django.core.files.storage import FileSystemStorage
#from django_pandas.managers import DataFrameManager
#from encrypted_fields import EncryptedCharField EncryptedIntegerField
#from pgcrypto import *
from encrypted_fields import EncryptedCharField,EncryptedIntegerField,EncryptedFloatField

# Create your models here.
class PinleiType(models.Model):
	type_name = models.CharField(max_length=30, verbose_name=u'品类分类')
	isedit = models.IntegerField(verbose_name=u'是否可更改')

	def __unicode__(self):
		return self.type_name

class PinleiGL(models.Model):
    pinleiname = models.CharField(max_length=30,verbose_name=u'品类名称')
    isedit = models.IntegerField(verbose_name=u'是否可更改')
    pinleitype = models.ForeignKey(PinleiType,verbose_name=u'商品分类')
    danjia = models.FloatField(blank=True,null=True, verbose_name=u'物品单价')
    zuhe = models.CharField(max_length=30,verbose_name=u'组合数值')#对应一次性录入组合产品时的值
    def __unicode__(self):
        return self.pinleiname

    class Meta:
        ordering = ['-id']

class GongyingshangGL (models.Model):
    name = models.CharField(max_length=30 , unique=True ,verbose_name=u'供应商名称')
    kaihuhang = models.CharField(max_length=30 , verbose_name=u'开户行')
    zhanghao = models.CharField(max_length=50 , verbose_name=u'帐号')
    hanghao = models.CharField(max_length=30 , verbose_name=u'行号')
    isedit = models.IntegerField(verbose_name=u'是否可更改')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HetongGL(models.Model):
    hetongNO = models.CharField(max_length=30,primary_key=True)
    name = models.ForeignKey(GongyingshangGL,verbose_name=u'供应商名称')
    pinleiname = models.ForeignKey(PinleiGL,verbose_name=u'品类名称')
    gongjia =  models.FloatField(verbose_name=u'供价')
    hetongshuliang = models.IntegerField(verbose_name=u'数量')
    hetongzongjia = models.FloatField(verbose_name=u'总价')
    kerukushuliang = models.IntegerField(verbose_name=u'可入库数量')
    hetongdate = models.DateField(verbose_name=u'签订日期')
    isedit = models.IntegerField(verbose_name=u'是否可更改')
    daifukuanjine = models.FloatField(blank=True,null=True,verbose_name=u'待付款金额')
    pinleitype = models.ForeignKey(PinleiType,verbose_name=u'商品类别',default='')


    def __unicode__(self):
        return unicode(self.hetongNO)


class FukuanMX(models.Model):
    fukuanmx_date = models.DateField(verbose_name=u'付款日期')
    fukuanmx_name = models.CharField(max_length=30 ,verbose_name=u'供应商名称')
    fukuanmx_pinlei = models.CharField(max_length=30,verbose_name=u'品类')
    hetongNO = models.ForeignKey(HetongGL,verbose_name=u'合同编号')
    fukuanmx_fukuanjine = models.FloatField(verbose_name=u'付款金额')

    def __unicode__(self):
        return unicode(self.hetongNO)
    class Meta:
        ordering = ['fukuanmx_date']

class FukuanGL(models.Model):
    fukuangl_name = models.ForeignKey(GongyingshangGL,verbose_name=u'供应商名称')
    fukuangl_hetongNO = models.CharField(max_length=30,verbose_name=u'合同编号')
    fukuangl_pinlei = models.ForeignKey(PinleiGL,verbose_name=u'品类' )
    fukuangl_hetongzongjia = models.FloatField(verbose_name=u'合同总价')
    fukuangl_yifukuanjine = models.FloatField(blank=True,null=True,verbose_name=u'已付款金额')
    fukuangl_daifukuanjine = models.FloatField(blank=True,null=True,verbose_name=u'待付款金额')
    pinleitype = models.ForeignKey(PinleiType,verbose_name=u'商品类别',default='')

    def __unicode__(self):
        return unicode(self.fukuangl_hetongNO)




class ChuRukuMX(models.Model):
    churukufangxiang_CHOICES = (('IN','入库'),('OUT','出库'))
    churukufangxiang = models.CharField(choices=churukufangxiang_CHOICES, max_length=10, verbose_name=u'出/入库')
    churukumx_date = models.DateField(verbose_name=u'出/入库日期')
    churukumx_name = models.CharField(max_length=30, verbose_name=u'供应商名称')
    hetongNO = models.ForeignKey(HetongGL,verbose_name=u'合同编号')
    churukumx_gongjia = models.FloatField(verbose_name=u'供价')
    churukumx_pinlei = models.CharField(max_length=30, verbose_name=u'品类')
    churukumx_shuliang = models.IntegerField(verbose_name=u'出/入库数量')
    churukumx_zongjia = models.FloatField(verbose_name=u'出/入库总价')
    zhongzhuanzhengpinkuid = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'对应中转正品库ID')
    isedit = models.BooleanField(default=None,verbose_name=u'是否可编辑')
    pinleitype = models.ForeignKey(PinleiType,verbose_name=u'商品类别',default='')


    def __unicode__(self):
        return unicode(self.hetongNO)
    class Meta:
        ordering = ['-churukumx_date']




class KucunGL(models.Model):
    kucungl_gongyingshangname = models.CharField(max_length=30,verbose_name=u'供应商名称')
    kucungl_hetongbianhao = models.CharField(max_length=30,verbose_name=u'合同号')
    kucungl_kucungongjia = models.FloatField(verbose_name=u'供价')
    kucungl_kucunshuliang = models.IntegerField(blank=True,null=True,verbose_name=u'库存数量')
    kucungl_kucunjine = models.FloatField(verbose_name=u'库存金额')
    kucungl_peileiname = models.CharField(max_length=30,verbose_name=u'品类')
    pinleitype = models.ForeignKey(PinleiType,verbose_name=u'商品类别',default='')

    def __unicode__(self):
        return self.kucungl_gongyingshangname

    class Meta:
        ordering = ['kucungl_gongyingshangname']


class TODO(models.Model):
	todo_is_complete = models.BooleanField(default=None,verbose_name=u'是否完成')
	todo_create_date = models.DateField(verbose_name=u'创建日期')
	todo_complete_date = models.DateField(blank=True,null=True,verbose_name=u'完成日期')
	todo_content=models.CharField(max_length=300,verbose_name=u'内容')



	class Meta:
		ordering = ['todo_create_date']

class yijian(models.Model):
	url = models.CharField(max_length=50,verbose_name=u'url') #前一页url
	yijian_riqi = models.DateField(verbose_name=u'填写日期')
	yijian_email = models.CharField(max_length=254, blank=True, null= True,verbose_name=u'E-mail,可以不填写。')
	yijian_neirong = models.CharField(max_length=400,verbose_name=u'请留下宝贵意见，谢谢！')

class Photo(models.Model):
	hetongNO = models.ForeignKey(HetongGL,verbose_name=u'合同号')
	name = models.CharField(max_length = 100,verbose_name="Name")
	image = models.ImageField(upload_to = "photo",blank=True,null=True)



class JixiaoInfo(models.Model):
	name = models.CharField(max_length = 30,verbose_name=u'驾校名称')
	pinyin = models.CharField(max_length = 100,verbose_name=u'拼音')
	shouzimu = models.CharField(max_length = 10,verbose_name=u'首字母')
	isuesful = models.BooleanField(default=None,verbose_name=u'是否使用')
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class ZhongzhuanZhengpinMX(models.Model):
	pinleiname = models.CharField(max_length=30, verbose_name=u'品类名称')
	shuliang = models.IntegerField(verbose_name=u'中转数量')
	tijiao_riqi = models.DateField(verbose_name=u'提交日期')
	jieshou_riqi = models.DateField(verbose_name=u'接收日期',blank=True, null= True)
	tijiao_user = models.CharField(max_length=30, verbose_name=u'提交用户')
	jieshou_user = models.CharField(max_length=30, verbose_name=u'接收用户',blank=True, null= True)
	is_jieshou = models.BooleanField(default=None, verbose_name=u'是否接收')
	zhongzhuanid = models.CharField(max_length=30, verbose_name=u'对应库存管理库存管理ID')
	pinleitype = models.ForeignKey(PinleiType, verbose_name=u'商品类别', default='')
	class Meta:
		ordering = ['-tijiao_riqi']
		permissions = (
						("can_update","Can update"),("can_delete","Can delete"),
						)
class Jpzhengpinku(models.Model):
	pinleiname = models.CharField(max_length=30, verbose_name=u'品类名称')
	shuliang = models.IntegerField(verbose_name=u'库存数量')
	pinleitype = models.ForeignKey(PinleiType, verbose_name=u'商品类别',default='')
	pinleiid = models.CharField(max_length=30, verbose_name=u'品类名称ID') #供查询明细时使用

class JpFafangMX(models.Model):
	#caozuo_CHOICES = (('IN','退回'),('OUT','发放'),('BORROW','借出'),('REPAY','还回'))
	caozuo_CHOICES = (('OUT','发放'),('IN','退回'),('CANCI','残次退还'))
	caozuo_fangxiang = models.CharField(choices=caozuo_CHOICES, max_length=10, verbose_name=u'发放/退回')
	jiaxiaoname = models.ForeignKey(JixiaoInfo, verbose_name=u'驾校名称', default='')
	pinleiname = models.ForeignKey(PinleiGL, verbose_name=u'品类名称')
	pinleitype = models.ForeignKey(PinleiType, verbose_name=u'商品类别',default='')
	riqi = models.DateField(verbose_name=u'发放日期',blank= True, null= True)
	shijian = models.DateTimeField(verbose_name=u'生成时间',blank= True, null= True)
	caozuo_user = models.CharField(max_length=30, verbose_name=u'操作用户')
	beizhu = models.CharField(max_length=300, null= True, verbose_name=u'备注（最多100个汉字和标点。）')
	shuliang = models.IntegerField(verbose_name=u'数量')

class JpjiaxiaoHZ(models.Model):
	jiaxiaoname = models.ForeignKey(JixiaoInfo, verbose_name=u'驾校名称', default='')
	pinleiname = models.ForeignKey(PinleiGL, verbose_name=u'品类名称')
	pinleitype = models.ForeignKey(PinleiType, verbose_name=u'商品类别',default='')
	shuliang = models.IntegerField(verbose_name=u'数量')
	def __unicode__(self):
		return self.jiaxiaoname
	class Meta:
		ordering = ['jiaxiaoname']

class BGYP_fenlei(models.Model):
    fenleiname = models.CharField(max_length=20, verbose_name=u'办公用品类别')
    isedit = models.BooleanField(default=None,verbose_name=u'可否变更')
    def __unicode__(self):
        return self.fenleiname


class BGYP_name(models.Model):
    fenleiname =  models.ForeignKey(BGYP_fenlei, verbose_name=u'办公用品类别')
    bangongyongpinname = models.CharField(max_length=30, verbose_name=u'办公用品名称')
    isedit = models.BooleanField(default=None, verbose_name=u'可否变更')
    jianpin = models.CharField(max_length=20,verbose_name=u'简拼')
    bangongyongpindanjia = models.FloatField( verbose_name=u'物品单价')
    def __unicode__(self):
        return self.bangongyongpinname


class BGYP_bumen(models.Model):
    bumenname = models.CharField(max_length=30, verbose_name=u'部门名称')
    isedit = models.BooleanField(default=None, verbose_name=u'可否变更')
    def __unicode__(self):
        return self.bumenname
    class Meta:
		ordering = ['bumenname']


class BGYP_kucun(models.Model):#TODO: 库存表展示时使用带搜索框的datatable
    fenleiname = models.ForeignKey(BGYP_fenlei, verbose_name=u'商品类别')
    jianpin = models.CharField(max_length=20,verbose_name=u'简拼')
    bangongyongpinname = models.ForeignKey(BGYP_name,verbose_name=u'办公用品名称_外键')
    bangongyongpindanjia = models.FloatField( verbose_name=u'物品单价')
    bangongyongpinshuliang = models.FloatField( verbose_name=u'物品数量')#允许小数
    bangongyongpinzongjia = models.FloatField(verbose_name=u'总价')

#将数量、单价数字类型更新为浮点数，对应数据库为双精度数，可以在使用pandas时直接汇总不必进行转换

class BGYP_churukumx(models.Model):
    bumenname = models.ForeignKey(BGYP_bumen, verbose_name=u'领用部门',blank=True, null= True)
    bumenname_str = models.CharField(max_length=50, verbose_name=u'办公用品名称字符串',blank=True, null= True)#外键对应字符串
    fenleiname = models.ForeignKey(BGYP_fenlei, verbose_name=u'商品类别')
    fenleiname_str = models.CharField(max_length=50, verbose_name=u'商品类别字符串')
    bangongyongpinname = models.ForeignKey(BGYP_name,verbose_name=u'办公用品名称_外键')
    bangongyongpinname_str = models.CharField(max_length=20, verbose_name=u'办公用品名称字符串')#外键对应字符串
    jianpin = models.CharField(max_length=20,verbose_name=u'简拼')
    bangongyongpindanjia = models.FloatField( verbose_name=u'物品单价')
    bangongyongpinshuliang_ruku = models.FloatField(verbose_name=u'入库数量',null=True)#允许小数
    bangongyongpinshuliang_chuku = models.FloatField(verbose_name=u'出库数量',null=True)
    bangongyongpinzongjia_ruku = models.FloatField(verbose_name=u'入库总价',null=True)
    bangongyongpinzongjia_chuku = models.FloatField(verbose_name=u'出库总价',null=True)
    beizhu =models.CharField(max_length=300,verbose_name=u'备注',blank=True,null=True)
    churukuriqi = models.DateField(verbose_name=u'出入库日期')
    tijiaoriqi = models.DateField(verbose_name=u'提交日期')
    fangxiang = models.CharField(max_length=10, verbose_name=u'出入库方向')#TODO:判断出入库方向后直接将中文写入数据库
    jingshouren = models.CharField(max_length=30, verbose_name=u'经手人',blank=True,null=True)
    fangxiang_en = models.CharField(max_length=10, verbose_name=u'出入库方向-英文')
    #objects =   DataFrameManager()
    class Meta:
        permissions = (
						("bangongyongpin","BangongYongpin"),
						)


class JpMX_new(models.Model):
    jiaxiaoname = models.ForeignKey(JixiaoInfo, verbose_name=u'驾校名称')
    jiaxiaoname_str =  models.CharField(max_length=50, verbose_name=u'驾校名称字符串',blank=True, null= True)#外键对应字符串
    pinleiname = models.ForeignKey(PinleiGL, verbose_name=u'品类名称',null=True)
    pinleiname_str = models.CharField(max_length=50, verbose_name=u'品类名称字符串',blank=True, null= True)
    gouka = models.IntegerField(verbose_name=u'购卡数量',null=True)#购卡数量
    shouquan = models.IntegerField(verbose_name=u'授权数量',null=True)#授权数量
    yuling_in = models.IntegerField(verbose_name=u'预领数量',null=True)#预领登记数量
    yingfukuan_dengji = models.IntegerField(verbose_name=u'应付款登记',null=True)#应付款登记
    yingfukuan_shoufei= models.IntegerField(verbose_name=u'应付款收费',null=True)#应付款收费
    yuling_out = models.IntegerField(verbose_name=u'预领收费数量',null=True)#预领收费数量
    genghuan_in = models.IntegerField(verbose_name=u'更换登记数量',null=True)#更换登记数量
    genghuan_out = models.IntegerField(verbose_name=u'更换处理数量',null=True)#更换处理数量
    user = models.CharField(max_length=50, verbose_name=u'操作员')#操作员
    riqi = models.DateTimeField(verbose_name=u'业务生成时间')
    beizhu = models.CharField(max_length=300, verbose_name=u'备注',blank=True,null=True)
    jine = models.FloatField(verbose_name=u'总价',null=True)
    riqi_yewu = models.DateTimeField(verbose_name=u'业务录入时间',null=True)
    edit_username = models.CharField(max_length=50, verbose_name=u'编辑操作员',null=True)
    edit_day_time = models.DateTimeField(verbose_name=u'编辑时间',auto_now=True,null=True)
    isdelete = models.BooleanField(default=False,verbose_name=u'是否被删除')
    fukuanfangshi_CHOICES = (('xianjin','现金'),('yinhang','银行存款'),('pos','POS刷卡'))
    fukuanfangshi = models.CharField(choices=fukuanfangshi_CHOICES, max_length=10, verbose_name=u'付款方式',null=True)
    fukuanfangshi_str_cn = models.CharField( max_length=10, verbose_name=u'付款方式中文字符串',null=True)
    lianjie_id = models.CharField(max_length=50, verbose_name=u'操作连接ID',null=True)
    dandugoumai_shuliang = models.IntegerField(verbose_name=u'单独购买数量',null=True)#单独购买数量
    tushu_yingling_shuliang = models.IntegerField(verbose_name=u'应该领取图书数量',null=True,blank=True)#应该领取图书数量
    tushu_shiling_shuliang = models.IntegerField(verbose_name=u'图书领取数量',null=True,blank=True)#实际领取图书数量
    is_tushu_qichushu = models.BooleanField(default=False,verbose_name=u'是否为图书的期初数')#是否为图书期初数，报表中不能将前期欠书数显示在本月查询结果中，只能增加属性来判断是否在本月查询中显示该数字（累计欠书数时需要计算该数）
    haoduanqizhi = models.CharField(max_length=3000,verbose_name=u'号段起止',null=True)



class JpMX_churuku(models.Model):
	pinleiname = models.ForeignKey(PinleiGL, verbose_name=u'品类名称',null=True)
	pinleiname_str = models.CharField(max_length=50, verbose_name=u'品类名称字符串',blank=True, null= True)
	danjia = models.FloatField(verbose_name=u'单价',null=True)
	caozuo_CHOICES = (('ruku','入库'),('chuku','出库'),('fafang','发放'),('zhanneixiaoshou','站内直接销售'),('jieshou','接收'))
	caozuo = models.CharField(choices=caozuo_CHOICES, max_length=20, verbose_name=u'操作')
	caozuo_str_cn = models.CharField( max_length=20, verbose_name=u'操作中文字符串',null=True)
	ruku_shuliang = models.IntegerField(verbose_name=u'入库数量',null=True)
	ruku_zongjia= models.FloatField(verbose_name=u'入库总价',null=True)
	xiaoshou_shuliang = models.IntegerField(verbose_name=u'销售数量',null=True)
	xiaoshou_danjia = models.FloatField(verbose_name=u'销售单价',null=True)
	xiaoshou_zongjia= models.FloatField(verbose_name=u'销售总价',null=True)
	chuku_shuliang = models.IntegerField(verbose_name=u'出库数量',null=True)
	chuku_zongjia= models.FloatField(verbose_name=u'出库总价',null=True)
	jieshou_shuliang = models.IntegerField(verbose_name=u'接收数量',null=True)
	fafang_shuliang = models.IntegerField(verbose_name=u'发放数量',null=True)
	user = models.CharField(max_length=50, verbose_name=u'操作员')#操作员
	isdelete = models.BooleanField(default=False,verbose_name=u'是否被删除')
	isjieshou = models.CharField(max_length=50, verbose_name=u'是否接收',null=True)
	riqi = models.DateTimeField(verbose_name=u'业务生成时间')
	edit_username = models.CharField(max_length=50, verbose_name=u'编辑操作员',null=True)
	edit_day_time = models.DateTimeField(verbose_name=u'编辑时间',null=True)
	lianjie_id= models.CharField(max_length=50, verbose_name=u'操作连接ID',null=True)
	beizhu = models.CharField(max_length=300, verbose_name=u'备注',blank=True,null=True)


class JpMX_ribaobiao(models.Model):
    riqi = models.DateField(verbose_name=u'营业日期')
    youpan_shuliang = models.IntegerField(verbose_name=u'优盘数量',null=True)#对应报表“优盘”
    youpan_jine = models.IntegerField(verbose_name=u'优盘金额',null=True)#对应报表“优盘”
    ICka_shuliang = models.IntegerField(verbose_name=u'IC卡数量',null=True)#对应报表‘IC卡’
    ICka_jine = models.FloatField(verbose_name=u'IC卡金额',null=True)#对应报表‘IC卡’
    jiaocai_shuliang = models.IntegerField(verbose_name=u'教材数量',null=True)#对应报表“教材”
    jiaocai_jine = models.IntegerField(verbose_name=u'教材金额',null=True)#对应报表“教材”
    ICkayoupan_shuliang = models.IntegerField(verbose_name=u'IC卡优盘数量',null=True)#对应报表“IC卡优盘数量”
    ICkayoupan_jine = models.IntegerField(verbose_name=u'IC卡优盘金额',null=True)#对应报表IC卡优盘
    beizhu = models.CharField(max_length=300, verbose_name=u'备注',blank=True,null=True)
    user = models.CharField(max_length=50, verbose_name=u'操作员')#操作员
    edit_day_time = models.DateTimeField(verbose_name=u'编辑时间',null=True)
    isdelete = models.BooleanField(default=False,verbose_name=u'是否被删除')
    jiaolianka_jine = models.FloatField(verbose_name=u'教练卡销售金额',default=0,null=True)
    ICka_leiji_xiuzheng = models.FloatField(verbose_name=u'IC卡累计收入修正',default=0,null=True)#针对2015年4月17日累计收入突然增加进行修正
    zhanneixiaoshou_shuliang = models.IntegerField(verbose_name=u'站内销售数量',default=0,null=True)#对应报表“侯利鹏卖出”
    zhanneixiaoshou_jine = models.FloatField(verbose_name=u'站内销售金额',default=0,null=True)

class JpMX_ICSN(models.Model):
    sn =  models.CharField(max_length=50,verbose_name=u'IC卡SN')
    ic4428id = models.CharField(max_length=50,verbose_name=u'4428ID',null=True)
    icm1id = models.CharField(max_length=50,verbose_name=u'M1ID',null=True)
    zhuangtai = models.CharField(max_length=20,verbose_name=u'卡片状态')#只有'登记','发放','更换登记(回收旧卡)','更换处理(换出新卡)'四种
    zhuangtai_str = models.CharField(max_length=20,verbose_name=u'卡片状态字符串')#'dengji','fafang','genghuan_in','genghuan_out'
    dengji_riqi = models.DateField(verbose_name=u'登记日期')
    fafang_riqi = models.DateField(verbose_name=u'发放日期',null=True)
    genghuan_in_riqi = models.DateField(verbose_name=u'更换登记日期',null=True)
    genghuan_out_riqi = models.DateField(verbose_name=u'更换处理日期',null = True)
    dengji_user = models.CharField(max_length=20,verbose_name=u'登记操作员')
    fafang_user = models.CharField(max_length=20,verbose_name=u'发放操作员',null=True)
    genghuan_in_user = models.CharField(max_length=20,verbose_name=u'更换登记操作员',null=True)
    genghuan_out_user = models.CharField(max_length=20,verbose_name=u'更换处理操作员',null=True)
    jiaxiaoname = models.CharField(max_length=20,verbose_name=u'驾校名称',null=True)
    edit_username= models.CharField(max_length=20,verbose_name=u"编辑信息用户名",null=True)
    edit_day_time = models.DateTimeField(verbose_name=u"编辑日期时间",null=True)
    lianjie_id = models.CharField(max_length=50,verbose_name=u"连接字符串",null=True)


class JpMX_yingfu_paichu(models.Model):
    jiaxiao_id = models.IntegerField(verbose_name=u'优盘数量',null=True)#对应驾校ID

class TEST_db(models.Model):
    test_char = EncryptedCharField(max_length=500, verbose_name=u'操作员')
    test_int = EncryptedIntegerField()
    test_float = EncryptedFloatField()

class JpICSN(models.Model):#导入驾培办ic卡序列号数据
    sn = models.CharField(max_length=40,verbose_name=u'IC卡SN')
    add_datetime = models.DateTimeField(verbose_name=u"sn加入时间",null=True)
    use_datetime = models.DateTimeField(verbose_name=u"使用时间",null=True)
    is_use = models.BooleanField(verbose_name=u'是否已使用')
    shenfenzhenghao = models.CharField(max_length=25,verbose_name=u'身份证号',null=True)

class JpMX_SNgengxinriqi(models.Model):
    gengxinriqi = models.DateField(verbose_name=u'更新日期')































