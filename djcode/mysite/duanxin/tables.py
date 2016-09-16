# coding=utf-8
from table import Table
from table.columns import Column
from table.columns import LinkColumn, Link,DatetimeColumn
from table.utils import A



class JP_YingFukuanmxtable(Table):
	name =  Column(field='jiaxiaoname_str',header=u'驾校名称')
	yingfukuan_dengji =  Column(field='yingfukuan_dengji',header=u'应付款登记金额')
	yingfukuan_shoufei =  Column(field='yingfukuan_shoufei',header=u'应付款已收费金额')
	yingfukuan = Column(field='yingfukuan',header=u'应付款需收费金额')
	beizhu =  Column(field='beizhu',header=u'备注')
	action = LinkColumn(field='beizhu',header=u'编辑',sortable=False, links=[
        Link(text=u'编辑', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    ])
	action1 = LinkColumn(header=u'删除',sortable=False, links=[
        Link(text=u'删除', viewname='kucuntest.views.JP_JpMX_new_delete', args=(A('id'), )),
    ])

class DX_Fasongmxtable(Table):
	paizhaohao =  Column(field='paizhaohao',header=u'车牌号')
	dianhuahao =  Column(field='dianhuahao',header=u'电话号码')
	tijiao_neirong = Column(field='tijiao_neirong',header=u'发送内容')
	tijiao_datetime =  DatetimeColumn(field='tijiao_datetime',header=u'提交日期',format="%Y-%m-%d %H:%I:%S")
	yincheyuan_name = Column(field='yincheyuan_name',header=u'引车员姓名')
	is_fasong =  Column(field='is_fasong',header=u'已发送')

	action = LinkColumn(header=u'重新发送',sortable=False, links=[
        Link(text=u'重新发送', viewname='kucuntest.views.JP_JpMX_new_edit', args=(A('id'), )),
    ])

class DX_ZhiZheng_chaxun_table(Table):
	paizhaohao =  Column(field='paizhaohao',header=u'车牌号')
	cheliangleibie_id=  Column(field='cheliangleibie_id',header=u'车辆类型')
	zhizheng_datetime =  DatetimeColumn(field='chuanjianriqi',header=u'制证日期',format="%Y-%m-%d %H:%I:%S")

class DX_ShouFei_chaxun_table(Table):
	paizhaohao =  Column(field='CPH',header=u'车牌号')
	cheliangleibie_id=  Column(field='PZLBID',header=u'车辆类型')
	zhizheng_datetime =  DatetimeColumn(field='SKRQ',header=u'收费日期',format="%Y-%m-%d %H:%I:%S")


class DX_ShouFei_ZhiZheng_duibi_table(Table):
	paizhaohao =  Column(field='CPH',header=u'车牌号')
	cheliangleibie_id=  Column(field='PZLBID',header=u'车辆类型')
	zhizheng_datetime =  DatetimeColumn(field='ZZRQ',header=u'制证日期',format="%Y-%m-%d %H:%I:%S")
	shoufei_datetime = DatetimeColumn(field='SKRQ', header=u'收费日期', format="%Y-%m-%d %H:%I:%S")