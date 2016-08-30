# coding=utf-8
from table import Table
from table.columns import Column
from table.columns import LinkColumn, Link,DatetimeColumn
from table.utils import A

class FaFangMXtable(Table):
    pinlei = Column(field='pinleiname',header=u'品类')
    jiaxiaoname = Column(field='jiaxiaoname',header=u'驾校名称')
    shuliang = Column(field='shuliang',header=u'数量',sortable=False,searchable=False)
    action = LinkColumn(header=u'操作',sortable=False, links=[
        Link(text=u'编辑', viewname='kucuntest.views.editjpfafangmx', args=(A('id'), )),
    ])
    #好像可以另外再加一个链接操作(需验证)
    #action1 = LinkColumn(header=u'操作',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.editjpfafangmx', args=(A('id'), )),
    #])
    class Meta:
      search=False

class BGnametable(Table):
    fenleiname = Column(field='fenleiname',header=u'分类')
    bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
    jianpin = Column(field='jianpin',header=u'简拼')
    bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
    isedit = Column(field='isedit',header=u'可否编辑')
    #action1 = LinkColumn(header=u'编辑',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.BG_edit_name', args=(A('id'), )),
    #])
    action = LinkColumn(header=u'入库',sortable=False, links=[
        Link(text=u'入库', viewname='kucuntest.views.BG_churuku', args=('ruku',A('id'), )),
    ])
    action2 = LinkColumn(header=u'出库',sortable=False, links=[
        Link(text=u'出库', viewname='kucuntest.views.BG_churuku', args=('chuku',A('id'), )),
    ])
    action3 = LinkColumn(header=u'查看明细',sortable=False, links=[
        Link(text=u'查看明细', viewname='kucuntest.views.BG_churuku_mx', args=(A('id'), )),
    ])

    #好像可以另外再加一个链接操作(需验证)
    #action1 = LinkColumn(header=u'操作',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.editjpfafangmx', args=(A('id'), )),
    #])

class BGkucuntable(Table):
    fenleiname = Column(field='fenleiname',header=u'分类')
    bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
    jianpin = Column(field='jianpin',header=u'简拼')
    bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
    bangongyongpinshuliang = Column(field='bangongyongpinshuliang',header=u'数量',sortable=False,searchable=False)
    bangongyongpinzongjia = Column(field='bangongyongpinzongjia',header=u'总价',sortable=False,searchable=False)
    action = LinkColumn(header=u'入库',sortable=False, links=[
        Link(text=u'入库', viewname='kucuntest.views.BG_churuku', args=('ruku',A('bangongyongpinname_id'), )),
    ])
    action2 = LinkColumn(header=u'出库',sortable=False, links=[
        Link(text=u'出库', viewname='kucuntest.views.BG_churuku', args=('chuku',A('bangongyongpinname_id'), )),
    ])
    action3 = LinkColumn(header=u'查询明细',sortable=False, links=[
        Link(text=u'查询明细', viewname='kucuntest.views.BG_churuku_mx', args=(A('bangongyongpinname_id'), )),
    ])

class BGchurukumxtable(Table):
	fenleiname = Column(field='fenleiname',header=u'分类')
	bumenname = Column(field='bumenname',header=u'部门')
	bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
	jianpin = Column(field='jianpin',header=u'简拼')
	bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
	bangongyongpinshuliang_ruku = Column(field='bangongyongpinshuliang_ruku',header=u'入库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_ruku = Column(field='bangongyongpinzongjia_ruku',header=u'入库总价',sortable=False,searchable=False)
	bangongyongpinshuliang_chuku = Column(field='bangongyongpinshuliang_chuku',header=u'出库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_chuku = Column(field='bangongyongpinzongjia_chuku',header=u'出库总价',sortable=False,searchable=False)
	churukuriqi = DatetimeColumn(field='churukuriqi',header=u'日期',sortable=False,format="%Y年%m月%d日")
	beizhu = Column(field='beizhu',header=u'备注',searchable=False)
	action = LinkColumn(header=u'编辑',sortable=False, links=[
        Link(text=u'编辑', viewname='kucuntest.views.BG_churuku_mx_edit', args=(A('id'), )),
    ])

class Pandastest(Table):
	fenleiname = Column(field='fenleiname',header=u'分类')
	bumenname = Column(field='bumenname',header=u'部门')
	churukufangxiang = Column(field='fangxiang',header=u'出入库')
	bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
	jianpin = Column(field='jianpin',header=u'简拼')
	bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
	bangongyongpinshuliang = Column(field='bangongyongpinshuliang',header=u'数量',sortable=False,searchable=False)
	bangongyongpinzongjia = Column(field='bangongyongpinzongjia',header=u'总价',sortable=False,searchable=False)
	churukuriqi = DatetimeColumn(field='churukuriqi',header=u'日期',sortable=False,format="%Y年%m月%d日")
	action = LinkColumn(header=u'编辑',sortable=False, links=[
        Link(text=u'编辑', viewname='kucuntest.views.BG_churuku_mx_edit', args=(A('id'), )),
    ])
	bangongyongpinzongjia1 = Column(field='bangongyongpinzongjia',header=u'总价',sortable=False,searchable=False)

class BGchurukumxtable_name_or_fenleiname(Table):
	fenleiname = Column(field='fenleiname',header=u'分类')
	bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
	jianpin = Column(field='jianpin',header=u'简拼')
	bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
	bangongyongpinshuliang_ruku = Column(field='bangongyongpinshuliang_ruku',header=u'入库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_ruku = Column(field='bangongyongpinzongjia_ruku',header=u'入库总价',sortable=False,searchable=False)
	bangongyongpinshuliang_chuku = Column(field='bangongyongpinshuliang_chuku',header=u'出库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_chuku = Column(field='bangongyongpinzongjia_chuku',header=u'出库总价',sortable=False,searchable=False)
	bangongyongpinshuliang_jieyu = Column(field='bangongyongpinshuliang_jieyu',header=u'结余数量',sortable=False,searchable=False)
	bangongyongpinzongjia_jieyu = Column(field='bangongyongpinzongjia_jieyu',header=u'结余金额',sortable=False,searchable=False)


class BGchurukumxtable_bumen(Table):
	bumenname = Column(field='bumenname',header=u'部门')
	fenleiname = Column(field='fenleiname',header=u'分类')
	bangongyongpinname = Column(field='bangongyongpinname',header=u'名称')
	jianpin = Column(field='jianpin',header=u'简拼')
	bangongyongpindanjia = Column(field='bangongyongpindanjia',header=u'单价',sortable=False,searchable=False)
	bangongyongpinshuliang_ruku = Column(field='bangongyongpinshuliang_ruku',header=u'入库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_ruku = Column(field='bangongyongpinzongjia_ruku',header=u'入库总价',sortable=False,searchable=False)
	bangongyongpinshuliang_chuku = Column(field='bangongyongpinshuliang_chuku',header=u'出库数量',sortable=False,searchable=False)
	bangongyongpinzongjia_chuku = Column(field='bangongyongpinzongjia_chuku',header=u'出库总价',sortable=False,searchable=False)


class JP_JiaXiaolisttable(Table):
	name = Column(field='name',header=u'驾校名称')
	pinyin = Column(field='pinyin',header=u'拼音')
	action = LinkColumn(header=u'操作',sortable=False, links=[
        Link(text=u'操作', viewname='kucuntest.views.caozuoxuanzenew', args=(A('id'), )),
    ])

class JP_ShouQuanmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	goukashu =  Column(field='gouka',header=u'购卡数')
	jine = Column(field='jine',header=u'金额')
	shouquan =  Column(field='shouquan',header=u'授权数')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	fukuanfangshi = Column(field='fukuanfangshi_str_cn',header=u'付款方式')
	beizhu =  Column(field='beizhu',header=u'备注')
	haoduanqizhi = Column(field='haoduanqizhi',header=u'号段')
	action1 = LinkColumn(header=u'删除',sortable=False, links=[
        Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    ])

	class Meta:
		search_placeholder = u'可进行搜索'
		pagination = False
		#sort = [(4, 'asc'), (1, 'desc')]
		sort = [(4, 'asc')]


class JP_YuLingmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yuling_in =  Column(field='yuling_in',header=u'登记数')
	yuling_out =  Column(field='yuling_out',header=u'交费数')
	jine = Column(field='jine',header=u'金额')
	fukuanfangshi = Column(field='fukuanfangshi_str_cn',header=u'付款方式')
	riqi_yewu =  DatetimeColumn(field='riqi_yewu',header=u'登记/交费日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')
	#action = LinkColumn(field='beizhu',header=u'编辑',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    #])
	#action1 = LinkColumn(header=u'删除',sortable=False, links=[
        #Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    #])

class JP_GenHuanmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	pinlei =  Column(field='pinleiname_str',header=u'品类')
	genghuan_in =  Column(field='genghuan_in',header=u'登记数')
	genghuan_out =  Column(field='genghuan_out',header=u'更换数')
	riqi =  DatetimeColumn(field='riqi',header=u'登记/更换日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')
	#action = LinkColumn(field='beizhu',header=u'编辑',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    #])
	#action1 = LinkColumn(header=u'删除',sortable=False, links=[
        #Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    #])

class JP_DanDougoumaimxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	pinlei =  Column(field='pinleiname_str',header=u'品类')
	dandugoumai_shuliang =  Column(field='dandugoumai_shuliang',header=u'单独购买数量')
	jine =  Column(field='jine',header=u'金额')
	fukuanfangshi_str_cn = Column(field='fukuanfangshi_str_cn',header=u'付款方式')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')
	#action = LinkColumn(field='beizhu',header=u'编辑',sortable=False, links=[
        #Link(text=u'编辑', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    #])
	#action1 = LinkColumn(header=u'删除',sortable=False, links=[
        #Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    #])

class JP_Jinchikucun_chukumx(Table):
	pinlei =  Column(field='pinleiname_str',header=u'品类')
	danjia =  Column(field='danjia',header=u'单价')
	chuku_shuliang =  Column(field='chuku_shuliang',header=u'出库数量')
	chuku_zongjia = Column(field='chuku_zongjia',header=u'出库总价')
	isjieshou = Column(field='isjieshou',header=u'是否接收')
	riqi =  DatetimeColumn(field='riqi',header=u'出库日期',format='%Y-%m-%d')
	edit_day_time =  DatetimeColumn(field='edit_day_time',header=u'接收日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')

class JP_Jinchikucun_rukumx(Table):
	pinlei =  Column(field='pinleiname_str',header=u'品类')
	danjia =  Column(field='danjia',header=u'单价')
	ruku_shuliang =  Column(field='ruku_shuliang',header=u'入库数量')
	ruku_zongjia = Column(field='ruku_zongjia',header=u'入库数量')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')

class JP_Jinchikucun_xiaoshoumx(Table):
	pinlei =  Column(field='pinleiname_str',header=u'品类')
	danjia =  Column(field='danjia',header=u'单价')
	xiaoshou_shuliang =  Column(field='xiaoshou_shuliang',header=u'销售数量')
	xiaoshou_danjia =  Column(field='xiaoshou_danjia',header=u'销售单价')
	xiaoshou_zongjia = Column(field='xiaoshou_zongjia',header=u'销售总价')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')


class JP_XuShoufeimxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yuling_in =  Column(field='yuling_in',header=u'登记数量')
	yuling_out =  Column(field='yuling_out',header=u'已缴费数量')
	xushoufei = Column(field='xujiaofei',header=u'需收费数量')

class JP_zonghechaxun_gouka_huizong_table(Table):
	jiaxiaoname_str =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	gouka =  Column(field='gouka',header=u'购买数量')
	dandugoumai_shuliang =  Column(field='dandugoumai_shuliang',header=u'单独购买数量')

class JP_zonghechaxun_shouquan_huizong_table(Table):
	jiaxiaoname_str =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	shouquan =  Column(field='shouquan',header=u'授权数量')

class JP_zonghechaxun_jiaocai_huizong_table(Table):
	jiaxiaoname_str =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yingling =  Column(field='tushu_yingling_shuliang',header=u'应领数量')
	shiling =  Column(field='tushu_shiling_shuliang',header=u'实领数量')
	qianshu =  Column(field='qianshu',header=u'欠书数量')

class JP_YingFukuanmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yingfukuan_dengji =  Column(field='yingfukuan_dengji',header=u'登记金额')
	yingfukuan_shoufei =  Column(field='yingfukuan_shoufei',header=u'收费金额')
	fukuanfangshi_str_cn = Column(field='fukuanfangshi_str_cn',header=u'付款方式')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')
	action = LinkColumn(field='beizhu',header=u'编辑',sortable=False, links=[
        Link(text=u'编辑', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    ])
	action1 = LinkColumn(header=u'删除',sortable=False, links=[
        Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    ])

class JP_XushoufeiYingFukuanmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yingfukuan_dengji =  Column(field='yingfukuan_dengji',header=u'应付款登记金额')
	yingfukuan_shoufei =  Column(field='yingfukuan_shoufei',header=u'应付款已收费金额')
	yingfukuan = Column(field='yingfukuan',header=u'应付款需收费金额')



class JP_TuShumxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yingling_shuliang =  Column(field='tushu_yingling_shuliang',header=u'应该领取数量')
	shiling_shuliang = Column(field='tushu_shiling_shuliang',header=u'实际领取数量')
	riqi =  DatetimeColumn(field='riqi',header=u'日期',format='%Y-%m-%d')
	beizhu =  Column(field='beizhu',header=u'备注')