# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from calendar import HTMLCalendar,monthrange
#from django.utils.translation import ugettext_lazy as _
from dateutil.relativedelta import relativedelta
from forms import *
from models import *
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404,HttpRequest, HttpResponse
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout
import datetime
import random
import imghdr
import os
from django.conf import settings
import shutil
from xpinyin import Pinyin
import string
from django.db.models import Count, Min, Sum, Avg
from tables import *
import simplejson as json
from xlrd import open_workbook
#from xlwt import Workbook
from xlutils.copy import copy
import pandas as pd
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
)
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import ImageFile as PILImageFile
import re
import operator
# from django.forms import *



# Create your views here.
idglobal = 0  #定义全局变量，以便在form中使用
hetongNOglobal = ''
caozuoglobal = ''
churukufangxiangglobal = ''
yiqianshujuglobal = 0
jiaxiaoidglobal = 0
end_time_global = ''


def logout_view(request):
	logout(request)

	return HttpResponseRedirect('/demo/')


def id():
	return idglobal  #返回全局变量


def hetongno():
	return hetongNOglobal


def caozuo():
	return caozuoglobal

def jiaxiaoid():
	return jiaxiaoidglobal


def churukufangxiang():
	return churukufangxiangglobal


def yiqianshuju():
	return yiqianshujuglobal

def end_time_global():
	return end_time_global


def demo(request):
	return render_to_response('demo.html', locals(), context_instance=RequestContext(request))


def jpdemo(request):
	return render_to_response('jpdemo.html', locals(), context_instance=RequestContext(request))


def liuchengtu(request):
	title = u'流程图'
	listleibie = 'liuchengtu'
	return render_to_response('liuchengtu.html', locals(), context_instance=RequestContext(request))


def creatID():  #生成随机ID
	chars = string.letters + string.digits
	creat_id = "".join(random.sample(chars, 15))
	return creat_id

def jiaxiaolist_test():#生成驾校列表供网页使用
	jiaxiaolist = JixiaoInfo.objects.filter(isuesful=True).order_by('name')
	list_dic = {}
	list_a = []
	list_b = []
	list_c = []
	list_d = []
	list_e = []
	list_f = []
	list_g = []
	list_h = []
	list_i = []
	list_j = []
	list_k = []
	list_l =[]
	list_m = []
	list_n = []
	list_o = []
	list_p = []
	list_q = []
	list_r = []
	list_s = []
	list_t = []
	list_u = []
	list_v = []
	list_w = []
	list_x = []
	list_y = []
	list_z = []
	for a in jiaxiaolist:
		if a.shouzimu == 'a':
			list_a.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'b':
			list_b.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'c':
						list_c.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'd':
						list_d.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'e':
						list_e.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'f':
						list_f.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'g':
						list_g.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'h':
						list_h.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'i':
						list_i.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'j':
						list_j.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'k':
						list_k.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'l':
						list_l.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'm':
						list_m.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'n':
						list_n.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'o':
						list_o.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'p':
						list_p.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'q':
						list_q.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'r':
						list_r.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 's':
						list_s.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 't':
						list_t.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'u':
						list_u.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'v':
						list_v.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'w':
						list_w.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'x':
						list_x.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'y':
						list_y.append({'name':a.name,'id':a.id})
		elif a.shouzimu == 'z':
						list_z.append({'name':a.name,'id':a.id})
	list_dic['a'] = list_a
	list_dic['b'] = list_b
	list_dic['c'] = list_c
	list_dic['d'] = list_d
	list_dic['e'] = list_e
	list_dic['f'] = list_f
	list_dic['g'] = list_g
	list_dic['h'] = list_h
	list_dic['i'] = list_i
	list_dic['j'] = list_j
	list_dic['k'] = list_k
	list_dic['l'] = list_l
	list_dic['m'] = list_m
	list_dic['n'] = list_n
	list_dic['o'] = list_o
	list_dic['p'] = list_p
	list_dic['q'] = list_q
	list_dic['r'] = list_r
	list_dic['s'] = list_s
	list_dic['t'] = list_t
	list_dic['u'] = list_u
	list_dic['v'] = list_v
	list_dic['w'] = list_w
	list_dic['x'] = list_x
	list_dic['y'] = list_y
	list_dic['z'] = list_z
	return list_dic



def index(request):
	title = u'首页'
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def zhongzhuanzhengpinmx_jinchisave(pinleitype, pinleiname, shuliang, tijiao_user, zhongzhuanid):
	pinleitype = pinleitype
	pinleiname = pinleiname
	shuliang = abs(shuliang)
	tijiao_user = tijiao_user
	tijiao_riqi = datetime.date.today()
	jieshou_riqi = None
	jieshou_user = None
	is_jieshou = False
	zhongzhuanid = zhongzhuanid
	p = ZhongzhuanZhengpinMX(pinleiname=pinleiname, shuliang=shuliang, tijiao_user=tijiao_user,
	                         tijiao_riqi=tijiao_riqi, jieshou_riqi=jieshou_riqi, jieshou_user=jieshou_user,
	                         is_jieshou=is_jieshou, zhongzhuanid=zhongzhuanid, pinleitype=pinleitype)
	p.save()
	return True


@login_required
def addpinlei(request):
	title = u'添加品类信息'
	listleibie = 'pl'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	if request.method == 'POST':
		form = AddPinlei(request.POST)
		if form.is_valid():
			pinleitype = form.cleaned_data['pinleitype']
			pinleiname = form.cleaned_data['pinleiname']
			danjia = form.cleaned_data['danjia']
			p = PinleiGL(pinleiname=pinleiname, isedit=1, pinleitype=pinleitype,danjia=danjia)
			q = PinleiType.objects.filter(type_name=pinleitype)
			q.update(isedit=0)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			p.save()
			return HttpResponseRedirect('/pinlei/pinleilist/')
	else:
		form = AddPinlei()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def addpinleitype(request):
	title = u'添加商品类别'
	listleibie = 'pltype'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	if request.method == 'POST':
		form = AddPinleitype(request.POST)
		if form.is_valid():
			type_name = form.cleaned_data['type_name']
			p = PinleiType(type_name=type_name, isedit=1)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			p.save()
			return HttpResponseRedirect('/pinlei/pinleitypelist/')
	else:
		form = AddPinleitype()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def addgongyingshang(request):
	title = u'添加供应商信息'
	listleibie = 'gys'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改供应商名称！'
	if request.method == 'POST':
		form = AddGongyingshang(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			kaihuhang = form.cleaned_data['kaihuhang']
			zhanghao = form.cleaned_data['zhanghao']
			hanghao = form.cleaned_data['hanghao']
			p = GongyingshangGL.objects.create(name=name, kaihuhang=kaihuhang, zhanghao=zhanghao, hanghao=hanghao, isedit=1)

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/gongyingshang/gongyingshanglist/')
	else:
		form = AddGongyingshang()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def addhetong(request):
	title = u'添加合同'
	listleibie = 'ht'
	erbuyanzheng = False
	erbuyanzhengneirong = u'添加合同信息后，在没有录入相关付款或库存记录的情况下可以进行修改，否则将无法修改。确定提交吗？'

	if request.method == 'POST':

		form = AddHetong(request.POST)

		if form.is_valid():
			hetongNO = form.cleaned_data['hetongNO']
			name = form.cleaned_data['name']
			#name = form_name.get('name')
			pinleiname = form.cleaned_data['pinleiname']
			#pinleiname = form_pinleiname.get('pinleiname')
			#name = form(initial = {'name': GongyingshangGL.name })
			#pinleiname = form(initial = {'pinleiname': PinleiGL.pinleiname })
			gongjia = form.cleaned_data['gongjia']
			hetongshuliang = form.cleaned_data['hetongshuliang']
			#kerukushuliang = form.cleaned_data['kerukushuliang']
			kerukushuliang = hetongshuliang
			pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype #取得分类信息
			hetongdate = form.cleaned_data['hetongdate']
			zongjia = gongjia * hetongshuliang
			isedit = 0

			p = HetongGL(name=name, hetongNO=hetongNO, pinleiname=pinleiname,
			             gongjia=gongjia, hetongshuliang=hetongshuliang, kerukushuliang=kerukushuliang,
			             hetongdate=hetongdate, hetongzongjia=zongjia, isedit=1, daifukuanjine=zongjia,pinleitype=pinleitype)
			p.save()
			#cd = {'hetongNO':hetongNO,'name':name,'pinleiname':pinleiname,'gongjia':gongjia,
			#'hetongshuliang':hetongshuliang,'kerukushuliang':kerukushuliang,'hetongdate':hetongdate,
			#'zongjia':zongjia}
			#return render_to_response('shuchujieguo.html',{'cd':cd})
			q = FukuanGL(fukuangl_name=name, fukuangl_hetongNO=hetongNO, fukuangl_pinlei=pinleiname,
			             fukuangl_hetongzongjia=zongjia, fukuangl_yifukuanjine=0, fukuangl_daifukuanjine=zongjia,pinleitype=pinleitype)
			q.save()

			j = PinleiGL.objects.filter(pinleiname=pinleiname)
			j.update(isedit=isedit)

			k = GongyingshangGL.objects.filter(name=name)
			k.update(isedit=isedit)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')


			#return render_to_response('caozuochenggong.html')
			return HttpResponseRedirect('/hetong/hetonglist/')

	else:
		form = AddHetong()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def addchurukumx(request, hetongno):
	title = u'添加出入库记录'
	listleibie = 'crk'
	caozuo_user = request.user.username
	if hetongno == 'null':
		hetongNO = 'null'
	else:
		hetongNO = hetongno
		if not HetongGL.objects.filter(hetongNO=hetongNO).exists():
			return HttpResponseNotFound

	erbuyanzheng = False
	erbuyanzhengneirong = u'录入信息后该合同将无法进行修改，请确认全部信息！提交吗？'
	if request.method == 'POST':
		form = AddChuRukumx(request.POST)

		if form.is_valid():
			churukufangxiang = form.cleaned_data['churukufangxiang']
			hetongNO = form.cleaned_data['hetongNO']
			churukumx_shuliang = form.cleaned_data['churukumx_shuliang']
			churukumx_date = form.cleaned_data['churukumx_date']
			hetong = HetongGL.objects.select_related('pinleiname__pinleitype').get(hetongNO=hetongNO)
			pinleiname = hetong.pinleiname
			pinleitype = hetong.pinleiname.pinleitype
			churukumx_name = hetong.name
			churukumx_gongjia = hetong.gongjia
			churukumx_pinlei = hetong.pinleiname
			kerukushuliang = hetong.kerukushuliang

			if churukufangxiang == 'IN':
				churukumx_zongjia = churukumx_shuliang * churukumx_gongjia
				#对出入库明细中入库且合同号为指定合同号的所有记录求和，如明细中没有该记录则和为0
				yirukushulinag = sum(ChuRukuMX.objects.filter(churukufangxiang='IN',
				                                              hetongNO=hetongNO).values_list('churukumx_shuliang',
				                                                                             flat=True))
				kerukushuliang = kerukushuliang - churukumx_shuliang  #需要更新的可入库数量为：合同管理中的合同数量-已经入库的数量-本次输入的数量
				j = HetongGL.objects.filter(hetongNO=hetongNO)
				j.update(kerukushuliang=kerukushuliang, isedit=0)

				if not KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO).exists():  #如果合同号在库存管理中不存在

					p = ChuRukuMX(churukufangxiang=churukufangxiang, hetongNO=hetongNO,
					              churukumx_shuliang=churukumx_shuliang,
					              churukumx_date=churukumx_date, churukumx_gongjia=churukumx_gongjia,
					              churukumx_name=churukumx_name, churukumx_pinlei=churukumx_pinlei,
					              churukumx_zongjia=churukumx_zongjia, zhongzhuanzhengpinkuid=None, isedit=True, pinleitype=pinleitype)

					q = KucunGL(kucungl_hetongbianhao=hetongNO, kucungl_gongyingshangname=churukumx_name,
					            kucungl_kucungongjia=churukumx_gongjia, kucungl_kucunshuliang=churukumx_shuliang,
					            kucungl_kucunjine=churukumx_zongjia, kucungl_peileiname=churukumx_pinlei, pinleitype=pinleitype)
					q.save()  #记录存入库存管理
					p.save()  #记录存入出入库明细
				else:  #如果合同编号在库存管理中存在
					kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
					kucunshuliang = kucungl.kucungl_kucunshuliang + churukumx_shuliang

					kucunjine = kucungl.kucungl_kucunjine + churukumx_zongjia
					p = ChuRukuMX(churukufangxiang=churukufangxiang, hetongNO=hetongNO,
					              churukumx_shuliang=churukumx_shuliang,
					              churukumx_date=churukumx_date, churukumx_gongjia=churukumx_gongjia,
					              churukumx_name=churukumx_name, churukumx_pinlei=churukumx_pinlei,
					              churukumx_zongjia=churukumx_zongjia, zhongzhuanzhengpinkuid=None, isedit=True, pinleitype=pinleitype)

					q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
					p.save()  #记录存入出入库明细
					q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)  #   更新库存管理中库存数量和金额

			elif churukufangxiang == 'OUT':
				churukumx_shuliang = -abs(churukumx_shuliang)  #出库数量为负数
				churukumx_zongjia = churukumx_shuliang * churukumx_gongjia
				kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
				kucunshuliang = kucungl.kucungl_kucunshuliang + churukumx_shuliang
				kucunjine = kucungl.kucungl_kucunjine + churukumx_zongjia
				zhongzhuanzhengpinkuid = creatID()

				p = ChuRukuMX(churukufangxiang=churukufangxiang, hetongNO=hetongNO,
				              churukumx_shuliang=churukumx_shuliang,
				              churukumx_date=churukumx_date, churukumx_gongjia=churukumx_gongjia,
				              churukumx_name=churukumx_name, churukumx_pinlei=churukumx_pinlei,
				              churukumx_zongjia=churukumx_zongjia, zhongzhuanzhengpinkuid=zhongzhuanzhengpinkuid,
				              isedit=True, pinleitype=pinleitype)
				p.save()
				q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
				q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)
				ret = zhongzhuanzhengpinmx_jinchisave(pinleitype, pinleiname, churukumx_shuliang, caozuo_user,
				                                      zhongzhuanzhengpinkuid)
				if not ret:
					messages.add_message(request, messages.SUCCESS, '245行错误')
					return HttpResponseRedirect('/kucun/kucunlist/')

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/kucun/kucunlist/')
		#return render_to_response('shuchujieguo.html',{'cd':cd})
	else:
		form = AddChuRukumx()
		if hetongNO != 'null':
			form.fields['hetongNO'].queryset = HetongGL.objects.filter(hetongNO=hetongNO)  #指定外键下拉框选择范围，可以使用查询条件
		#form.fields['churukufangxiang'] = forms.ChoiceField(choices=[('IN','入库')]) #指定一个列表
		#forms.ChoiceField(choices=[ (o.id, str(o)) for o in Waypoint.objects.all()])#可以生成一个动态的下拉列表

	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def editgongyingshang(request, id):
	id = int(id)
	listleibie = 'gys'
	editgongyingshang = get_object_or_404(GongyingshangGL, id=id)
	isedit = editgongyingshang.isedit
	nameorNO = editgongyingshang.name
	fangfatishi = u'如果该供应商存在相应合同信息，则无法修改名称。'
	fangfatishidis = False
	title = u'编辑供应商信息'
	erbuyanzheng = True
	erbuyanzhengneirong = u'确认提交吗？'
	if isedit == 1:
		isdel = True
	else:
		isdel = False
	if request.method == 'POST':
		form = EditGongyingshang(instance=editgongyingshang, data=request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, '数据更新成功！')
			#return HttpResponseRedirect('/caozuochenggong/1')
			#return HttpResponseRedirect(chongdingxiang)
			return HttpResponseRedirect('/gongyingshang/gongyingshanglist/')


	else:
		form = EditGongyingshang(instance=editgongyingshang)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def editgongyingshangname(request, id):
	id = int(id)
	editgongyingshang = get_object_or_404(GongyingshangGL, id=id)
	isedit = editgongyingshang.isedit
	nameorNO = editgongyingshang.name
	listleibie = 'gys'
	fangfatishi = u'如果需要更改供应商名称或者删除供应商，需要在“合同管理”中删除该供应商下所有合同内容。'
	fangfatishidis = False
	title = u'编辑供应商信息'
	erbuyanzheng = False
	erbuyanzhengneirong = u'确认提交吗？'
	chongdingxiang = "/gongyingshang/editgongyingshang/" + str(id)
	if isedit == 1:
		isdel = True
	else:
		return HttpResponseRedirect(chongdingxiang)
	if request.method == 'POST':
		form = EditGongyingshangname(instance=editgongyingshang, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				form.save()

				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/gongyingshang/gongyingshanglist/')
		if request.POST.has_key("del"):
			#if form.is_valid(): #删除时只是需要在表单中显示相关数据，但不需要进行数据验证。
			q = GongyingshangGL.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/gongyingshang/gongyingshanglist')

	else:
		form = EditGongyingshangname(instance=editgongyingshang)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def editpinlei(request, id):
	id = int(id)
	editpinlei = get_object_or_404(PinleiGL, id=id)
	isedit = editpinlei.isedit
	nameorNO = editpinlei.pinleiname
	listleibie = 'pl'
	fangfatishi = u'如果该品类用以生成合同，则该品类无法被修改或删除，即使删除合同信息后亦无法更改或删除该品类信息，请小心录入！'
	fangfatishidis = True
	title = u'编辑品类信息'
	erbuyanzheng = True
	erbuyanzhengneirong = u'确认提交吗？'
	chongdingxiang = "/pinlei/pinleilist/"
	if isedit == 1:
		isdel = True
	else:
		messages.add_message(request, messages.SUCCESS, '该数据不可编辑！')
		return HttpResponseRedirect(chongdingxiang)
	if request.method == 'POST':
		form = EditPinlei(instance=editpinlei, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/pinlei/pinleilist/')
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
			q = PinleiGL.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/pinlei/pinleilist/')
	else:
		form = EditPinlei(instance=editpinlei)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def editpinleitype(request, id):
	id = int(id)
	editpinleitype = get_object_or_404(PinleiType, id=id)
	isedit = editpinleitype.isedit
	nameorNO = editpinleitype.type_name
	listleibie = 'pltype'
	fangfatishi = u'如果该分类已经用于生成品类信息，则该分类无法被修改或删除，即使删除分类信息后亦无法更改或删除该分类信息，请小心录入！'
	fangfatishidis = True
	title = u'编辑商品分类信息'
	erbuyanzheng = True
	erbuyanzhengneirong = u'确认提交吗？'
	chongdingxiang = "/pinlei/pinleitypelist/"
	if isedit == 1:
		isdel = True
	else:
		messages.add_message(request, messages.SUCCESS, '该数据不可编辑！')
		return HttpResponseRedirect(chongdingxiang)
	if request.method == 'POST':
		form = EditPinleiType(instance=editpinleitype, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect(chongdingxiang)
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
			q = PinleiType.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect(chongdingxiang)
	else:
		form = EditPinleiType(instance=editpinleitype)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def editfukuanmx(request, id):
	global idglobal  #引入全局变量
	global hetongNOglobal
	id = int(id)
	idglobal = id  #更改全局变量
	editfukuanmx = get_object_or_404(FukuanMX, id=id)
	listleibie = 'fkmx'
	hetongNO = editfukuanmx.hetongNO
	hetongNOglobal = hetongNO
	yiqianshu = editfukuanmx.fukuanmx_fukuanjine
	fangfatishi = u'如果该品类用以生成合同，则该品类无法被修改或删除，即使删除合同信息后亦无法更改或删除该品类信息，请小心录入！'
	fukuangl = FukuanGL.objects.get(fukuangl_hetongNO=hetongNO)
	daifukuan = fukuangl.fukuangl_daifukuanjine
	yifukuan = fukuangl.fukuangl_yifukuanjine
	fangfatishidis = False
	title = u'编辑付款信息'
	erbuyanzheng = False  #是否在提交数据时弹出对话框
	erbuyanzhengneirong = u'确认提交吗？'
	isdel = True

	if request.method == 'POST':
		form = EditFukuanMX(instance=editfukuanmx, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				fukuanmx_fukuanjine = form.cleaned_data['fukuanmx_fukuanjine']  #本次输入的数据
				chae = yiqianshu - fukuanmx_fukuanjine
				daifukuan = daifukuan + chae
				yifukuan = yifukuan - chae
				j = HetongGL.objects.filter(hetongNO=hetongNO)
				j.update(daifukuanjine=daifukuan)
				q = FukuanGL.objects.filter(fukuangl_hetongNO=hetongNO)
				q.update(fukuangl_daifukuanjine=daifukuan, fukuangl_yifukuanjine=yifukuan)
				form.save()
				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/fukuan/fukuangllist/')
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
			chae = editfukuanmx.fukuanmx_fukuanjine
			daifukuan = daifukuan + chae
			yifukuan = yifukuan - chae
			k = HetongGL.objects.filter(hetongNO=hetongNO)
			k.update(daifukuanjine=daifukuan)
			j = FukuanGL.objects.filter(fukuangl_hetongNO=hetongNO)
			j.update(fukuangl_daifukuanjine=daifukuan, fukuangl_yifukuanjine=yifukuan)
			q = FukuanMX.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/fukuan/fukuangllist/')

	else:
		form = EditFukuanMX(instance=editfukuanmx)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


class pinleilist(LoginRequiredMixin, ListView):
	model = PinleiGL
	template_name = 'list.html'
	context_object_name = 'pinleilist'


	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(pinleilist, self).get_context_data(**kwargs)
		#context = self.dispatch(self,**kwargs)
		context['listleibie'] = 'pl'
		context['title'] = u'品类管理'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request  #附加request的信息，为模板提供变量值
		return context


class pinleitypelist(LoginRequiredMixin, ListView):
	model = PinleiType
	template_name = 'list.html'
	context_object_name = 'pinleitypelist'

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(pinleitypelist, self).get_context_data(**kwargs)
		#context = self.dispatch(self,**kwargs)
		context['listleibie'] = 'pltype'
		context['title'] = u'品类类别'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request  #附加request的信息，为模板提供变量值
		return context


class gongyingshanglist(LoginRequiredMixin, ListView):
	model = GongyingshangGL
	template_name = 'list.html'
	#效果好像是指定返回的值在模板中的变量名称
	context_object_name = 'gongyingshanglist'

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(gongyingshanglist, self).get_context_data(**kwargs)
		context['listleibie'] = 'gys'
		context['title'] = u'供应商管理'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


class hetonglist(LoginRequiredMixin, ListView):
	model = HetongGL
	template_name = 'list.html'
	context_object_name = 'hetonglist'

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(hetonglist, self).get_context_data(**kwargs)
		context['listleibie'] = 'ht'
		context['title'] = u'合同管理'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


class kucunlist(LoginRequiredMixin, ListView):
	model = KucunGL
	template_name = 'list.html'
	context_object_name = 'kucunlist'

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(kucunlist, self).get_context_data(**kwargs)
		context['listleibie'] = 'kc'
		context['title'] = u'库存管理'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


class churukulist(LoginRequiredMixin, ListView):
	model = ChuRukuMX
	template_name = 'list.html'

	def get_queryset(self):  #取得url中额外参数

		self.hetongNO = self.kwargs['hetongno']  #对应url配置中的关键字配置名称
		if self.hetongNO != 'null':

			self.churukulist = get_list_or_404(ChuRukuMX, hetongNO=self.hetongNO)  #获得一个列表显示多个结果，get_object_or_404获得单个结果
			return ChuRukuMX.objects.filter(hetongNO=self.churukulist)
		else:
			self.churukulist = get_list_or_404(ChuRukuMX)
			return ChuRukuMX.objects.all()

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(churukulist, self).get_context_data(**kwargs)
		context['churukulist'] = self.churukulist  #将变量名添加到输出结果中
		context['chukuzongshu'] = abs(sum(
			ChuRukuMX.objects.filter(hetongNO=self.hetongNO, churukufangxiang='OUT').values_list('churukumx_shuliang',
			                                                                                     flat=True)))
		context['rukuzongshu'] = sum(
			ChuRukuMX.objects.filter(hetongNO=self.hetongNO, churukufangxiang='IN').values_list('churukumx_shuliang',
			                                                                                    flat=True))
		context['listleibie'] = 'crk'
		context['title'] = u'出入库明细表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


class fukuangllist(LoginRequiredMixin, ListView):
	model = FukuanGL
	template_name = 'list.html'
	context_object_name = 'fukuangllist'

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(fukuangllist, self).get_context_data(**kwargs)
		context['listleibie'] = 'fkl'
		context['title'] = u'付款管理列表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


class fukuanmxlist(LoginRequiredMixin, ListView):  #不能添加额外参数
	model = FukuanMX
	template_name = 'list.html'

	#context_object_name = 'fukuanmxlist'
	def get_queryset(self):  #取得url中额外参数

		self.hetongNO = self.kwargs['hetongno']  #对应url配置中的关键字配置名称
		if self.hetongNO != 'null':

			self.fukuanmxlist = get_list_or_404(FukuanMX, hetongNO=self.hetongNO)  #获得一个列表显示多个结果，get_object_or_404获得单个结果
			return FukuanMX.objects.filter(hetongNO=self.fukuanmxlist)
		else:
			self.fukuanmxlist = get_list_or_404(FukuanMX)
			return FukuanMX.objects.all()
		#return FukuanMX.objects.filter(hetongNO =self.fukuanmxlist) #详细见https://docs.djangoproject.com/en/1.6/topics/class-based-views/generic-display/#dynamic-filtering

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(fukuanmxlist, self).get_context_data(**kwargs)
		context['fukuanmxlist'] = self.fukuanmxlist  #将变量名添加到输出结果中
		context['listleibie'] = 'fkmx'
		context['title'] = u'付款明细列表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


@login_required
def edithetong(request, hetongno):
	edithetong = get_object_or_404(HetongGL, hetongNO=hetongno)
	hetongNO = hetongno
	isedit = edithetong.isedit
	nameorNO = edithetong.hetongNO
	listleibie = 'ht'
	fangfatishi = u'如果该合同已经存在出/入库操作或付款操作，则无法再被编辑，请小心操作！'
	fangfatishidis = True
	title = u'编辑合同信息'
	erbuyanzheng = True
	erbuyanzhengneirong = u'确认提交吗？'
	chongdingxiang = "/hetong/hetonglist/"

	if isedit == 1:
		isdel = True
	else:
		return HttpResponseRedirect(chongdingxiang)

	if request.method == 'POST':

		form = EditHetong(instance=edithetong, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				name = form.cleaned_data['name']
				gongjia = form.cleaned_data['gongjia']
				pinleiname = form.cleaned_data['pinleiname']
				hetongdate = form.cleaned_data['hetongdate']
				pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
				hetongshuliang = form.cleaned_data['hetongshuliang']
				kerukushuliang = hetongshuliang
				zongjia = gongjia * hetongshuliang

				p = HetongGL.objects.filter(hetongNO=hetongNO)
				p.update(name=name, gongjia=gongjia, hetongshuliang=hetongshuliang,
				         hetongdate=hetongdate, hetongzongjia=zongjia,
				         kerukushuliang=kerukushuliang, pinleiname=pinleiname, daifukuanjine=zongjia,pinleitype=pinleitype)

				q = FukuanGL.objects.filter(fukuangl_hetongNO=hetongNO)

				q.update(fukuangl_name=name, fukuangl_pinlei=pinleiname, fukuangl_hetongzongjia=zongjia,
				         fukuangl_daifukuanjine=zongjia)
				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/hetong/hetonglist/')

		if request.POST.has_key("del"):
			#if form.is_valid(): #删除时只是需要在表单中显示相关数据，但不需要进行数据验证。
			j = FukuanGL.objects.filter(fukuangl_hetongNO=hetongNO)
			j.delete()
			q = HetongGL.objects.filter(hetongNO=hetongNO)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/hetong/hetonglist/')

	else:
		form = EditHetong(instance=edithetong)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def editchuruku(request, id):
	global idglobal
	global churukufangxiangglobal
	global hetongNOglobal
	global yiqianshujuglobal
	title = u'添加出入库记录'
	id = int(id)
	idglobal = id
	churukumx = get_object_or_404(ChuRukuMX, id=id)
	zhongzhuanid = churukumx.zhongzhuanzhengpinkuid  #取得对应中转库ID
	if churukumx.isedit:
		isdel = True
	else:
		messages.add_message(request, messages.WARNING, '该条记录不可编辑！')
		return HttpResponseRedirect('/kucun/kucunlist/')
	listleibie = 'crk'
	yiqianshuju = churukumx.churukumx_shuliang
	yiqianshujuglobal = yiqianshuju
	churukufangxiang = churukumx.churukufangxiang
	churukufangxiangglobal = churukufangxiang
	hetongNO = churukumx.hetongNO
	hetongNOglobal = hetongNO

	if request.method == 'POST':
		form = EditChurukuMX(instance=churukumx, data=request.POST)
		if request.POST.has_key("updata"):
			global caozuoglobal
			caozuoglobal = 'updata'
			if form.is_valid():
				if churukufangxiang == 'IN':
					shuliang = form.cleaned_data['churukumx_shuliang']
					date = form.cleaned_data['churukumx_date']
					kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
					kucunshuliang = kucungl.kucungl_kucunshuliang
					gongjia = kucungl.kucungl_kucungongjia
					chae = yiqianshuju - shuliang
					kucunshuliang = kucunshuliang - chae
					kucunjine = kucunshuliang * gongjia
					kerukushuliang = HetongGL.objects.get(hetongNO=hetongNO).kerukushuliang + chae
					q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
					q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)
					j = HetongGL.objects.filter(hetongNO=hetongNO)
					j.update(kerukushuliang=kerukushuliang)
					k = ChuRukuMX.objects.filter(id=id)
					k.update(churukumx_shuliang=shuliang, churukumx_date=date)
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
					return HttpResponseRedirect('/kucun/kucunlist/')
				if churukufangxiang == 'OUT':
					shuliang = form.cleaned_data['churukumx_shuliang']
					shuliang = -abs(shuliang)
					date = form.cleaned_data['churukumx_date']
					kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
					kucunshuliang = kucungl.kucungl_kucunshuliang
					gongjia = kucungl.kucungl_kucungongjia
					chae = yiqianshuju - shuliang
					kucunshuliang = kucunshuliang - chae
					kucunjine = kucunshuliang * gongjia
					q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
					q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)
					k = ChuRukuMX.objects.filter(id=id)
					k.update(churukumx_shuliang=shuliang, churukumx_date=date)
					j = ZhongzhuanZhengpinMX.objects.filter(zhongzhuanid=zhongzhuanid)  #更新中转库对应数据
					j.update(shuliang=abs(shuliang), tijiao_riqi=date)  #数量为本次输入数量，日期为修改后的日期。
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
					return HttpResponseRedirect('/kucun/kucunlist/')
		if request.POST.has_key("del"):
			caozuoglobal = 'del'
			if form.is_valid():
				if churukufangxiang == 'IN':
					shuliang = 0
					kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
					kucunshuliang = kucungl.kucungl_kucunshuliang
					gongjia = kucungl.kucungl_kucungongjia
					chae = yiqianshuju - shuliang
					kucunshuliang = kucunshuliang - chae
					kucunjine = kucunshuliang * gongjia
					kerukushuliang = HetongGL.objects.get(hetongNO=hetongNO).kerukushuliang + chae
					q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
					q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)
					j = HetongGL.objects.filter(hetongNO=hetongNO)
					j.update(kerukushuliang=kerukushuliang)
					k = ChuRukuMX.objects.filter(id=id)
					k.delete()
					messages.add_message(request, messages.SUCCESS, '数据删除成功！')
					return HttpResponseRedirect('/kucun/kucunlist/')
				if churukufangxiang == 'OUT':
					shuliang = 0
					shuliang = -shuliang
					kucungl = KucunGL.objects.get(kucungl_hetongbianhao=hetongNO)
					kucunshuliang = kucungl.kucungl_kucunshuliang
					gongjia = kucungl.kucungl_kucungongjia
					chae = yiqianshuju - shuliang
					kucunshuliang = kucunshuliang - chae
					kucunjine = kucunshuliang * gongjia
					q = KucunGL.objects.filter(kucungl_hetongbianhao=hetongNO)
					q.update(kucungl_kucunshuliang=kucunshuliang, kucungl_kucunjine=kucunjine)
					k = ChuRukuMX.objects.filter(id=id)
					k.delete()
					j = ZhongzhuanZhengpinMX.objects.filter(zhongzhuanid=zhongzhuanid)
					j.delete()

					messages.add_message(request, messages.SUCCESS, '数据删除成功！')
					return HttpResponseRedirect('/kucun/kucunlist/')
	else:
		form = EditChurukuMX(instance=churukumx)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


@login_required
def addfukuanmx(request, hetongno):
	title = u'添加付款记录'
	listleibie = 'fkmx'
	if hetongno == 'null':
		hetongNO = 'null'
	else:
		hetongNO = hetongno
		if not HetongGL.objects.filter(hetongNO=hetongNO).exists():
			return HttpResponseNotFound
	erbuyanzheng = False
	erbuyanzhengneirong = u'录入信息后该合同将无法进行修改，请确认全部信息！提交吗？'
	if request.method == 'POST':

		form = AddFukuanMX(request.POST)

		if form.is_valid():
			hetongNO = form.cleaned_data['hetongNO']
			fukuanmx = HetongGL.objects.get(hetongNO=hetongNO)
			name = fukuanmx.name
			pinlei = fukuanmx.pinleiname

			fukuanjine = form.cleaned_data['fukuanmx_fukuanjine']
			fukuandate = form.cleaned_data['fukuanmx_date']
			fukuangl = FukuanGL.objects.get(fukuangl_hetongNO=hetongNO)
			yifukuanjine = fukuangl.fukuangl_yifukuanjine + fukuanjine
			daifukuanjine = fukuangl.fukuangl_daifukuanjine - fukuanjine
			p = FukuanMX(fukuanmx_name=name, hetongNO=hetongNO, fukuanmx_date=fukuandate, fukuanmx_pinlei=pinlei,
			             fukuanmx_fukuanjine=fukuanjine)
			p.save()

			q = FukuanGL.objects.filter(fukuangl_hetongNO=hetongNO)
			q.update(fukuangl_yifukuanjine=yifukuanjine, fukuangl_daifukuanjine=daifukuanjine)
			j = HetongGL.objects.filter(hetongNO=hetongNO)
			j.update(isedit=0)
			k = HetongGL.objects.filter(hetongNO=hetongNO)
			k.update(daifukuanjine=daifukuanjine)

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			#return render_to_response('caozuochenggong.html')
			return HttpResponseRedirect('/fukuan/fukuangllist/')

	else:
		form = AddFukuanMX()
		if hetongNO != 'null':
			form.fields['hetongNO'].queryset = HetongGL.objects.filter(hetongNO=hetongNO)  #指定外键下拉框选择范围，可以使用查询条件
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def TodoCreate(request):  #不能添加额外参数
	title = u'添加TODO'
	if not request.user.username == 'admin':
		messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用,请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	if request.method == 'POST':

		form = Todo(request.POST)

		if form.is_valid():
			complete = form.cleaned_data['todo_is_complete']
			content = form.cleaned_data['todo_content']
			create_date = datetime.date.today()
			complete_date = datetime.date.today()

			p = TODO(todo_is_complete=complete, todo_content=content, todo_create_date=create_date,
			         todo_complete_date=complete_date)
			p.save()

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			#return render_to_response('caozuochenggong.html')
			return HttpResponseRedirect('/todo/todolist/')

	else:
		form = Todo()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


class TodoList(LoginRequiredMixin, ListView):  #不能添加额外参数
	model = TODO
	template_name = 'list.html'
	context_object_name = 'todolist'
	"""
	def get(self, request,**kwargs): #判断用户名，这里似乎只能使用get函数名称
		if self.request.user.username != 'admin':
			messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(TodoList, self).get_context_data(**kwargs)
	"""

	def dispatch(self, request, *args, **kwargs):  #判断用户名
		if not self.request.user.username == 'admin':
			messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(TodoList, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(TodoList, self).get_context_data(**kwargs)
		#context['todolist'] = self.todolist #将变量名添加到输出结果中
		context['listleibie'] = 'todo'
		context['title'] = u'ToduList'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


@login_required
def edittodo(request, id):
	id = int(id)
	edittodo = get_object_or_404(TODO, id=id)
	listleibie = 'todo'
	title = u'edittodo'
	isdel = True

	if not request.user.username == 'admin':
		messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用,请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	if request.method == 'POST':
		form = EditTodo(instance=edittodo, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				todo_is_complete = form.cleaned_data['todo_is_complete']
				if todo_is_complete == True:
					todo_complete_date = datetime.date.today()
					todo_content = form.cleaned_data['todo_content']
					q = TODO.objects.filter(id=id)
					q.update(todo_is_complete=todo_is_complete, todo_complete_date=todo_complete_date,
					         todo_content=todo_content)
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				else:
					form.save()
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/todo/todolist/')
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
			q = TODO.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/todo/todolist')
	else:
		form = EditTodo(instance=edittodo)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


def YijianCreate(request, url):
	url = url
	title = u'留言板'
	listleibie = 'yijian'
	if request.method == 'POST':

		form = Yijian(request.POST)

		if form.is_valid():
			yijian_email_raw = form.cleaned_data['yijian_email']
			if not yijian_email_raw != '':
				yijian_email = yijian_email_raw
			else:
				yijian_email = None
			yijian_neirong = form.cleaned_data['yijian_neirong']
			yijian_riqi = datetime.date.today()
			p = yijian(url=url, yijian_email=yijian_email, yijian_riqi=yijian_riqi, yijian_neirong=yijian_neirong)
			p.save()
			messages.add_message(request, messages.SUCCESS, '留言成功，谢谢！')
			return HttpResponseRedirect(url)

	else:
		form = Yijian()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@login_required
def edityijian(request, id):
	id = int(id)
	edityijian = get_object_or_404(yijian, id=id)
	listleibie = 'yijian'
	title = u'edityijian'
	isdel = True

	if not request.user.username == 'admin':
		messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用,请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	if request.method == 'POST':
		form = EditYijian(instance=edityijian, data=request.POST)
		if request.POST.has_key("updata"):
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, '数据更新成功！')
				return HttpResponseRedirect('/yijian/yijianlist/')
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
			q = yijian.objects.filter(id=id)
			q.delete()
			messages.add_message(request, messages.SUCCESS, '数据删除成功！')
			return HttpResponseRedirect('/yijian/yijianlist')
	else:
		form = EditYijian(instance=edityijian)
	return render_to_response('edit.html', locals(), context_instance=RequestContext(request))


class yijianlist(LoginRequiredMixin, ListView):  #不能添加额外参数
	model = yijian
	template_name = 'list.html'
	context_object_name = 'yijianlist'

	def dispatch(self, request, *args, **kwargs):  #判断用户名
		if not self.request.user.username == 'admin':
			messages.add_message(request, messages.WARNING, '这个模块只能由Admin使用，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(yijianlist, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(yijianlist, self).get_context_data(**kwargs)
		#context['todolist'] = self.todolist #将变量名添加到输出结果中
		context['listleibie'] = 'yijian'
		context['title'] = u'yijianlist'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		return context


def addphoto(request):
	path = settings.MEDIA_ROOT + 'photo/'
	if request.method == 'POST':

		form = Addphoto(request.POST, request.FILES)

		if form.is_valid():
			hetongNO = form.cleaned_data['hetongNO']
			name = form.cleaned_data['name']
			if request.FILES:  #判断是否存在上传信息，否则为空

				f = request.FILES['image']
				ret = handle_uploaded_file(f, path)
				if ret:
					p = Photo(hetongNO=hetongNO, name=name, image=ret)
					p.save()
					messages.add_message(request, messages.SUCCESS, '数据保存成功！')
				else:
					messages.add_message(request, messages.SUCCESS, '上传出现问题，请重新上传，请确保上传的文件类型正确。')

			else:
				p = Photo(hetongNO=hetongNO, name=name, image=None)
				p.save()
				messages.add_message(request, messages.SUCCESS, '数据保存成功！')
		return HttpResponseRedirect('/demo/')

	else:
		form = Addphoto()
	return render_to_response('fieldtest.html', locals(), context_instance=RequestContext(request))


def handle_uploaded_file(f, path):
	if f.size >= 5 * 1024 * 1024 or not handle_upload_types(f.name):
		return False
	file_type_name_path = handle_upload_types_finally(f)
	if not file_type_name_path:
		return False
	try:
		if not os.path.exists(path):
			os.mkdir(path)
		#image_path = settings.MEDIA_ROOT + 'photos/%s.%s' % (file_type_name_path[1],
		#file_type_name_path[0])
		shutil.move(file_type_name_path[2], path)
		image_path = 'photo/%s.%s' % (file_type_name_path[1], file_type_name_path[0])
		return image_path
	except IOError:
		return False


def handle_upload_types(file_name):
	file_name = unicode(file_name)  #将文件原始路径转为转换编码（应对原始路径中有中文字符的情况）
	not_allowed_tupes = ['.exe']  #排除exe

	for type in not_allowed_tupes:
		if file_name.endswith(type):
			return False
		else:
			return True


def handle_upload_types_finally(f):
	temp_name = str(
		datetime.date.today().strftime("%Y%m%d") + str(random.randint(1, 10000)))  #对文件进行改名，这里是按照日期加随机数生成一个文件名

	temp_path = settings.MEDIA_ROOT + "temp/%s" % temp_name  #临时文件路径（下面创建的是一个只有文件名没有扩展名的文件）
	#需要先创建一个空文件然后进行写操作
	try:
		if not os.path.exists(temp_path):
			os.mknod(temp_path)
	except IOError:
		return False
	temp_file = open(temp_path, 'wb+')  #打开临时文件
	for chunk in f.chunks():
		temp_file.write(chunk)
	temp_file.close()  #完成临时文件写入
	image_type = imghdr.what(temp_path)  #判断文件类型（只能判断图片）
	if not image_type:
		os.remove(temp_path)  #不是图片格式的删除临时文件
		return False  #如果不是图片则返回
	else:
		file_fullname = temp_path + '.%s' % image_type  #生成文件完全路径
		os.rename(temp_path, file_fullname)  #将临时文件转为正常文件
	return image_type, temp_name, file_fullname  #返回文件类型，文件名称，文件完整路径


def tupiantest(request):
	tupian = Photo.objects.get(hetongNO='kac20142')
	return render_to_response('tupiantest.html', locals(), context_instance=RequestContext(request))


def addjiaxiao(request):
	title = u'添加驾校名称'
	#listleibie = 'jx'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	#jiaxiaolist = jiaxiaolist_test()
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = Addjiaxiao(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			input_pinyin = Pinyin()
			pinyin = input_pinyin.get_pinyin(name, '')
			shouzimu = pinyin[0]


			p = JixiaoInfo(name=name, pinyin=pinyin, shouzimu=shouzimu, isuesful=True)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/jp/addjiaxiao/')
	else:
		form = Addjiaxiao()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))


def wupinjieshoulist(request):
	permission = request.user.has_perm('kucuntest.can_update')
	if not permission:
		messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	else:
		listleibie = 'wupinjieshou'
		title = u'中转商品接收'
		jiaxiaolist = jiaxiaolist_test()
		wupinjieshoulist = ZhongzhuanZhengpinMX.objects.all()
		return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_update')
def wupinjieshou(request, id):
	id = id
	jieshou_riqi = datetime.date.today()
	jieshou_user = request.user.username
	zhongzhuanwupin = get_object_or_404(ZhongzhuanZhengpinMX, id=id)
	zhongzhuanid = zhongzhuanwupin.zhongzhuanid  #得到中转id，在更新出入库明细时使用将isedit变更为Fales
	zhongzhuanpinlei = zhongzhuanwupin.pinleiname
	pinleiname = zhongzhuanpinlei
	pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=zhongzhuanpinlei).pinleitype
	zhongzhuanshuliang = zhongzhuanwupin.shuliang
	#写入正品库之前需判断是否存在
	if not Jpzhengpinku.objects.filter(pinleiname=zhongzhuanpinlei).exists():  #如果没有同品类
		zhengpinkuzhongzhuancaozuo = JPzhengpinkusave(pinleiname, zhongzhuanshuliang, pinleitype)
	else:  #如果有同品类
		zhengpinkuzhongzhuancaozuo = JPzhengpinkuupdate(pinleiname, zhongzhuanshuliang)
	gengxinchurukumx = GXchurukumx(zhongzhuanid)
	jj = ZhongzhuanZhengpinMX.objects.filter(id=id)  #更新中转库对应条目接收状态
	jj.update(is_jieshou=True,jieshou_riqi=jieshou_riqi, jieshou_user=jieshou_user)
	if zhengpinkuzhongzhuancaozuo and gengxinchurukumx:
		messages.add_message(request, messages.SUCCESS, '商品接收成功！')
		return HttpResponseRedirect('/jp/wupinjieshou/')


def JPzhengpinkusave(pinleiname, shuliang, pinleitype):  #驾培正品库新增
	pinleiname = pinleiname
	pinleiid = PinleiGL.objects.get(pinleiname=pinleiname).id
	pinleitype = pinleitype
	shuliang = shuliang
	p = Jpzhengpinku(pinleiname=pinleiname, shuliang=shuliang, pinleitype=pinleitype, pinleiid=pinleiid)
	p.save()
	return True


def JPzhengpinkuupdate(pinleiname, shuliang):  #驾培正品库更新
	pinleiname = pinleiname
	bencishuliang = shuliang
	yiqianshuliang = Jpzhengpinku.objects.get(pinleiname=pinleiname).shuliang
	gengxinshuliang = bencishuliang + yiqianshuliang
	q = Jpzhengpinku.objects.filter(pinleiname=pinleiname)
	q.update(shuliang=gengxinshuliang)
	return True


def GXchurukumx(zhongzhuan_id):  #更新出入库明细
	zhongzhuanzhengpinkuid = zhongzhuan_id
	q = ChuRukuMX.objects.filter(zhongzhuanzhengpinkuid=zhongzhuanzhengpinkuid)
	q.update(isedit=False)
	return True


class jpzhengpinkulist(LoginRequiredMixin, PermissionRequiredMixin, ListView):  #不能添加额外参数
	permission_required = 'kucuntest.can_update'  #使用APP.权限 进行判断
	model = Jpzhengpinku
	template_name = 'jplist.html'
	context_object_name = 'jpzhengpinlist'

	def dispatch(self, request, *args, **kwargs):  #判断用户名
		has_permission = self.check_permissions(request)
		if not has_permission:
			messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(jpzhengpinkulist, self).get_context_data(**kwargs)
		#context['todolist'] = self.todolist #将变量名添加到输出结果中
		context['listleibie'] = 'jpzhengpinkulist'
		context['title'] = u'驾培正品库列表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request
		context['jiaxiaolist'] = JixiaoInfo.objects.filter(isuesful=True)
		return context


def caozuoxuanze(request, jiaxiaoid):
	permission = request.user.has_perm('kucuntest.can_update')
	if not permission:
		messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	else:
		jiaxiaoid = int(jiaxiaoid)
		jiaxiao = get_object_or_404(JixiaoInfo, id=jiaxiaoid)
		title = jiaxiao.name
		jiaxiaolist = jiaxiaolist_test()
		return render_to_response('xuanze.html', locals(), context_instance=RequestContext(request))



def zhongzhuanmxlist(request, id):
	permission = request.user.has_perm('kucuntest.can_update')
	pinleiid = id
	pinleiname = PinleiGL.objects.get(id=pinleiid).pinleiname
	if not permission:
		messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	else:
		listleibie = 'zhongzhuanmxlist'
		title = u'商品中转记录'
		jiaxiaolist = jiaxiaolist_test()
		zhongzhuanmxlist = ZhongzhuanZhengpinMX.objects.filter(pinleiname=pinleiname)
		return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))

def faka(request, jiaxiaoid):
	global jiaxiaoidglobal
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'物品发放'
	is_tishi = True
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = Addfafangmx(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_gx = pinleiname
			shuliang = form.cleaned_data['shuliang']
			shuliang_fachu = -abs(shuliang)
			shuliang_tuihui = abs(shuliang)
			beizhu = form.cleaned_data['beizhu']
			caozuo_fangxiang = form.cleaned_data['caozuo_fangxiang']
			riqi = form.cleaned_data['riqi']
			pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			if caozuo_fangxiang == 'OUT':
				p = JpFafangMX(jiaxiaoname=jiaxiaoname, shijian=shijian, caozuo_user=caozuo_user, pinleiname=pinleiname, beizhu=beizhu,
			              caozuo_fangxiang=caozuo_fangxiang, riqi=riqi, pinleitype=pinleitype, shuliang=shuliang)
				p.save()
				ret = JPzhengpinkuupdate(pinleiname_gx, shuliang_fachu)
				ret1 = jiaxiaohuizongcaozuo(jiaxiaoid, pinleiname, shuliang)
				if ret and ret1:
					messages.add_message(request, messages.SUCCESS, '数据添加成功！')
					html = "/jp/caozuo/%d/faka/" % (jiaxiaoid)
					return HttpResponseRedirect(html)
			elif caozuo_fangxiang == 'IN':
				p = JpFafangMX(jiaxiaoname=jiaxiaoname, shijian=shijian, caozuo_user=caozuo_user, pinleiname=pinleiname, beizhu=beizhu,
			              caozuo_fangxiang=caozuo_fangxiang, riqi=riqi, pinleitype=pinleitype, shuliang=-shuliang)
				p.save()
				ret = JPzhengpinkuupdate(pinleiname_gx, shuliang_tuihui)
				ret1 = jiaxiaohuizongcaozuo(jiaxiaoid, pinleiname, -shuliang)
				if ret and ret1:
					messages.add_message(request, messages.SUCCESS, '数据添加成功！')
					html = "/jp/caozuo/%d/faka/" % (jiaxiaoid)
					return HttpResponseRedirect(html)
	else:
		form = Addfafangmx()
	return render_to_response('jpadd.html', locals(), context_instance=RequestContext(request))

"""
def gouka(request, jiaxiaoid):
	global jiaxiaoidglobal
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'购卡'
	is_tishi = True
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_gouka_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_str = pinleiname
			gouka =abs( form.cleaned_data['gouka'])
			beizhu = form.cleaned_data['beizhu']
			jine = form.cleaned_data['jine']
			riqi = datetime.date.today()

			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,pinleiname=pinleiname,pinleiname_str=pinleiname_str,gouka=gouka,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,jine=jine)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_gouka_forms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request)
	"""


def jiaxiaohuizongcaozuo(jiaxiaoid,pinleiname,shuliang):
	jiaxiaoid = jiaxiaoid
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	pinleiname = pinleiname
	pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname)
	pinleitype = pinleitype.pinleitype #获得类型
	pinleinameid = pinleitype.id #获得对应品类ID
	shuliang = shuliang
	if not JpjiaxiaoHZ.objects.filter(jiaxiaoname=jiaxiaoid,pinleiname=pinleiname).exists():
		q = JpjiaxiaoHZ(jiaxiaoname=jiaxiaoname,pinleiname=pinleiname,pinleitype=pinleitype,shuliang=shuliang) #
		q.save()
		return True
	else:
		q = JpjiaxiaoHZ.objects.filter(jiaxiaoname=jiaxiaoid,pinleiname=pinleiname)
		yiqianshuliang = q[0].shuliang
		shuliang_gx = yiqianshuliang+shuliang
		q.update(shuliang=shuliang_gx)
		return True

def fafangmxlist(request, id):
	permission = request.user.has_perm('kucuntest.can_update')
	pinleiid = id
	pinleiname = PinleiGL.objects.get(id=pinleiid)
	if not permission:
		messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	else:
		listleibie = 'fafangmxlist'
		title = u'商品发放记录'
		jiaxiaolist = jiaxiaolist_test()
		fafangmxlist = JpFafangMX.objects.filter(pinleiname=pinleiname).order_by('-riqi')
		return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))

def chaxun(request):
	title = u'综合查询'
	#listleibie = 'zonghechaxun'
	listleibie = ''
	#listleibie = 'jiaxiaojuhe_pinlei'
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = jpchaxun(request.POST)
		if form.is_valid():
			today = datetime.date.today()
			jiaxiaonameid = form.cleaned_data['jiaxiaoname']
			mxorhuizong = form.cleaned_data['mxorhuizong']
			pinleinameid = form.cleaned_data['pinleiname']
			pinleitypeid = form.cleaned_data['pinleitype']
			caozuo_fangxiang = form.cleaned_data['caozuo_fangxiang']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			agve = {}
			kwargs = {}
			kwargs1 = {}
			agve1={}

			if mxorhuizong == 'MX':
				if caozuo_fangxiang != 'NONE':
					kwargs['caozuo_fangxiang'] = caozuo_fangxiang
				if pinleinameid is not None:
					kwargs['pinleiname'] = pinleinameid
				if pinleitypeid is not None:
					kwargs['pinleitype'] = pinleitypeid
				if start_time or end_time is not None:
					if start_time is not None and end_time is None:
						agve['riqi__gte']=start_time
					if end_time is not None:
						agve['riqi__lte']=end_time
				if start_time and end_time is not None:
					agve['riqi__range'] = (start_time,end_time)
				if jiaxiaonameid is not None:
					kwargs['jiaxiaoname'] = jiaxiaonameid
				listleibie = 'datatable'
				jieguo = FaFangMXtable(JpFafangMX.objects.filter(**kwargs).filter(**agve).order_by('-riqi'))
			#sum_shuliang = PinleiGL.objects.filter(jpfafangmx__jiaxiaoname=).annotate(pinleisum=Sum('jpfafangmx__shuliang')).values('pinleiname','pinleisum')
			#单品类各驾校时间范围聚合
			#sum_shuliang = JixiaoInfo.objects.filter(jpfafangmx__pinleiname=pinleinameid,**agve1).annotate(pinleisum=Sum('jpfafangmx__shuliang')).values('name','pinleisum')

				#sum_shuliang = jiaxiaojuhe(agve1,kwargs1)
			return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))
	else:
		form = jpchaxun()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))

def jiaxiaojuhe(agve,kwargs):#各驾校全品类时间范围聚合
	kwargs = kwargs
	agve = agve
	list1 = JixiaoInfo.objects.filter(isuesful=True).values_list('id',flat=True)
	list2 = []
	for j in list1:
		if JpFafangMX.objects.filter(jiaxiaoname=j).exists():
			list2.append(j)
	list3 = []
	for i in list2:
		jiaxiao_pinlei_sum = PinleiGL.objects.filter(jpfafangmx__jiaxiaoname=i,**agve).annotate(pinleisum=Sum('jpfafangmx__shuliang')).values('pinleiname','pinleisum')
		list_temp = list(jiaxiao_pinlei_sum)
		dic = {}
		jiaxiaoname = JixiaoInfo.objects.get(id=i).name
		dic['jiaxiaoname']=jiaxiaoname
		list_temp.insert(0,dic)
		list3.append(list_temp)
	return list3

def people(request):
	jiaxiaolist = jiaxiaolist_test()
	listleibie = 'datatable'
	jieguo = FaFangMXtable(JpFafangMX.objects.all())
	return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))

def editjpfafangmx(request,editid):
	id =editid
	listleibie = ''
	return render_to_response('jplist.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_add_fenlei(request):
	title = u'添加办公用品分类信息'
	listleibie = 'fenleilist'
	daohangleibie = 'fenleilist'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	if request.method == 'POST':
		form = BGaddfenlei(request.POST)
		if form.is_valid():
			fenleiname = form.cleaned_data['fenleiname']
			p = BGYP_fenlei(fenleiname=fenleiname,  isedit=True)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/bg/fenleilist/')
	else:
		form = BGaddfenlei()
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))


class BG_list_fenlei(LoginRequiredMixin, PermissionRequiredMixin,ListView):
	permission_required = 'kucuntest.bangongyongpin'  #使用APP.权限 进行判断
	model = BGYP_fenlei
	template_name = 'bglist.html'
	context_object_name = 'fenleilist'
	def dispatch(self, request, *args, **kwargs):  #判断用户名
		has_permission = self.check_permissions(request)
		if not has_permission:
			messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(BG_list_fenlei, self).get_context_data(**kwargs)
		#context = self.dispatch(self,**kwargs)
		context['listleibie'] = 'fenleilist'
		context['title'] = u'办公用品分类列表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request  #附加request的信息，为模板提供变量值
		context['daohangleibie'] = 'fenleilist'
		return context

@permission_required('kucuntest.bangongyongpin')
def BG_add_name(request):#TODO:价格、简拼、名称str同时保存到库存表,name列表展示使用数据表，增加“入库”“编辑”
	title = u'添加办公用品名称'
	listleibie = 'name'
	daohangleibie = 'name'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	if request.method == 'POST':
		form = BGaddname(request.POST)
		if form.is_valid():
			fenleiname = form.cleaned_data['fenleiname']
			bangongyongpinname = form.cleaned_data['bangongyongpinname']
			bangongyongpindanjia =  form.cleaned_data['bangongyongpindanjia']
			input_pinyin = Pinyin()
			pinyin = input_pinyin.get_initials(bangongyongpinname, u'').lower()
			q = BGYP_fenlei.objects.filter(fenleiname=fenleiname)
			q.update(isedit=False)
			p = BGYP_name(fenleiname=fenleiname,  bangongyongpinname=bangongyongpinname,isedit=True,jianpin=pinyin,bangongyongpindanjia=bangongyongpindanjia)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/bg/namesearch/')
	else:
		form = BGaddname()
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_add_bumen(request):
	title = u'添加部门信息'
	erbuyanzheng = False
	daohangleibie = 'bumenlist'
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
	if request.method == 'POST':
		form = BGaddbumen(request.POST)
		if form.is_valid():
			bumenname = form.cleaned_data['bumenname']
			p = BGYP_bumen(bumenname=bumenname,isedit=True)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/bg/bumenlist/')
	else:
		form = BGaddbumen()
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))


class BG_list_bumen(LoginRequiredMixin, PermissionRequiredMixin,ListView):
	permission_required = 'kucuntest.bangongyongpin'  #使用APP.权限 进行判断
	model = BGYP_bumen
	template_name = 'bglist.html'
	context_object_name = 'bumenlist'

	def dispatch(self, request, *args, **kwargs):  #判断用户名
		has_permission = self.check_permissions(request)
		if not has_permission:
			messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
			return HttpResponseRedirect('/accounts/login/')
		else:
			return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):  #向输出到模板的内容中添加其他模板变量，可用作在模板中临时添加另一列内容（使用queset）而无需更改数据库
		context = super(BG_list_bumen, self).get_context_data(**kwargs)
		#context = self.dispatch(self,**kwargs)
		context['listleibie'] = 'bumenlist'
		context['title'] = u'办公用品分类列表'  #不能同时添加多个模板变量，需要一行一行添加
		context['request'] = self.request  #附加request的信息，为模板提供变量值
		context['daohangleibie'] = 'bumenlist'
		return context

@permission_required('kucuntest.bangongyongpin')
def  BG_search_name(request):
	title = u'物品名称管理'
	listleibie = 'datatable'
	daohangleibie = 'name'
	is_tishi = True
	tishixinxi = u"本页面可以添加办公用品名称也可以根据办公用品分类进行查询并进行办公用品入库操作！"
	if request.method == 'POST':
		form = BG_namechaxun(request.POST)
		if form.is_valid():
			fenleiname = form.cleaned_data['fenleiname']
			kwargs = {}
			if fenleiname is not None:
				kwargs['fenleiname'] = fenleiname
			jieguo = BGnametable(BGYP_name.objects.filter(**kwargs).order_by('jianpin'))
			return render_to_response('bglist.html', locals(), context_instance=RequestContext(request))
	else:
		form = BG_namechaxun()
		listleibie = 'name'
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_churuku(request,caozuo,editid):
	addleibie = 'churuku'
	listleibie = 'kucungl'
	daohangleibie = 'kucungl'
	editid = editid
	caozuo = caozuo
	global caozuoglobal
	caozuoglobal = caozuo
	global idglobal
	id = int(editid)
	idglobal = id
	if not BGYP_name.objects.filter(id=id).exists():
		return HttpResponseNotFound
	if caozuo == 'ruku':
		fangxiang = u'入库'
		fangxiang_en = 'in'
	if caozuo == 'chuku':
		fangxiang = u'出库'
		fangxiang_en = 'out'
		if not BGYP_kucun.objects.filter(bangongyongpinname=id).exists() :
			messages.add_message(request, messages.WARNING, '这个商品没有入库记录，请重新选择！')
			return HttpResponseRedirect('/bg/namesearch/')
	bangongyongpinname = BGYP_name.objects.get(id=id)
	bangongyongpinname_str = bangongyongpinname.bangongyongpinname
	bangongyongpindanjia = bangongyongpinname.bangongyongpindanjia
	jianpin = bangongyongpinname.jianpin
	fenleiname = bangongyongpinname.fenleiname
	fenleiname_str = BGYP_fenlei.objects.get(id=fenleiname.id).fenleiname
	tijiaoriqi = datetime.date.today()

	is_tishi = True
	tishixinxi = u'正在进行%s操作，办公用品名称为：%s，单价为：%.2f，所属分类为：%s。请核对后小心录入！'%(fangxiang,
	                                                                     bangongyongpinname_str,bangongyongpindanjia, fenleiname_str)
	if request.method == 'POST':
		form = BG_add_churukumx(request.POST)
		if form.is_valid():
			bumenname = form.cleaned_data['bumenname']
			jingshouren = form.cleaned_data['jingshouren']
			bangongyongpinshuliang = form.cleaned_data['bangongyongpinshuliang']
			bangongyongpinshuliang = abs(bangongyongpinshuliang)
			churukuriqi = form.cleaned_data['churukuriqi']
			beizhu =  form.cleaned_data['beizhu']
			bangongyongpinzongjia = bangongyongpindanjia*bangongyongpinshuliang
			bumenname_str = bumenname
			if churukuriqi is None:
				churukuriqi = tijiaoriqi
			if caozuo == 'ruku':
				bangongyongpinshuliang_ruku = bangongyongpinshuliang
				q = BGYP_churukumx(bumenname=bumenname,bumenname_str=bumenname_str,fenleiname=fenleiname,fenleiname_str=fenleiname_str,
			                        bangongyongpinname=bangongyongpinname,bangongyongpinname_str=bangongyongpinname_str,jianpin=jianpin,
			                        bangongyongpindanjia=bangongyongpindanjia,bangongyongpinshuliang_ruku=bangongyongpinshuliang_ruku,
			                        bangongyongpinzongjia_ruku=bangongyongpinzongjia,beizhu=beizhu,churukuriqi=churukuriqi,tijiaoriqi=tijiaoriqi,
			                        fangxiang=fangxiang,jingshouren=jingshouren,fangxiang_en=fangxiang_en)
				q.save()
			if caozuo == 'chuku':
				bangongyongpinshuliang_chuku = bangongyongpinshuliang
				q = BGYP_churukumx(bumenname=bumenname,bumenname_str=bumenname_str,fenleiname=fenleiname,fenleiname_str=fenleiname_str,
			                        bangongyongpinname=bangongyongpinname,bangongyongpinname_str=bangongyongpinname_str,jianpin=jianpin,
			                        bangongyongpindanjia=bangongyongpindanjia,bangongyongpinshuliang_chuku=bangongyongpinshuliang_chuku,
			                        bangongyongpinzongjia_chuku=bangongyongpinzongjia,beizhu=beizhu,churukuriqi=churukuriqi,tijiaoriqi=tijiaoriqi,
			                        fangxiang=fangxiang,jingshouren=jingshouren,fangxiang_en=fangxiang_en)
				q.save()
			if  BGYP_kucun.objects.filter(bangongyongpinname=id).exists():
				kucun = BGYP_kucun.objects.filter(bangongyongpinname=id)
				yiqianshuliang = kucun[0].bangongyongpinshuliang
				if caozuo == 'ruku':
					gengxinhoushuliang = yiqianshuliang+bangongyongpinshuliang
				elif caozuo == 'chuku':
					gengxinhoushuliang = yiqianshuliang-bangongyongpinshuliang
				bangongyongpinzongjia = bangongyongpindanjia*gengxinhoushuliang
				if gengxinhoushuliang == 0:
					kucun.delete()
				else:
					kucun.update(bangongyongpinshuliang=gengxinhoushuliang,bangongyongpinzongjia=bangongyongpinzongjia)
			else:
				j = BGYP_kucun.objects.create(fenleiname=fenleiname,jianpin=jianpin,bangongyongpinname=bangongyongpinname,bangongyongpindanjia=bangongyongpindanjia,
				               bangongyongpinshuliang=bangongyongpinshuliang,bangongyongpinzongjia=bangongyongpinzongjia)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			if caozuo == 'ruku':
				return HttpResponseRedirect('/bg/namesearch/')
			if caozuo == 'chuku':
				return HttpResponseRedirect('/bg/kucunsearch/')
	else:
		form = BG_add_churukumx()
		if caozuo == 'ruku':
			#TODO:在选在出入库后更改表单显示选项，入库时只显示“采购入库”，出库时选择除采购入库以外的全部部门
			form.fields['bumenname'].queryset = BGYP_bumen.objects.filter(id=13)  #指定外键下拉框选择范围，可以使用查询条件
		elif caozuo == 'chuku':
			form.fields['bumenname'].queryset = BGYP_bumen.objects.exclude(id=13)
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

def BG_edit_name(request,editid):
	id = editid
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def  BG_search_kucun(request):
	title = u'库存管理'
	listleibie = 'datatable'
	daohangleibie = 'kucungl'
	is_tishi = True
	tishixinxi = u"本页面可以查看现有库存，可直接进行物品的出入库操作，“明细查询”链接可进行明细查询。"
	if request.method == 'POST':
		form = BG_namechaxun(request.POST)
		if form.is_valid():
			fenleiname = form.cleaned_data['fenleiname']
			kwargs = {}
			if fenleiname is not None:
				kwargs['fenleiname'] = fenleiname
				#TODO:这里是查询明细的时候需要使用的聚合
			#jieguo = BGkucuntable(BGYP_name.objects.filter(bgyp_churukumx__fangxiang_en='out',**kwargs).annotate(sum_shuliang=Sum('bgyp_churukumx__bangongyongpinshuliang'),
			                                                                                            #sum_jiage=Sum('bgyp_churukumx__bangongyongpinzongjia')))
			jieguo = BGkucuntable(BGYP_kucun.objects.filter(**kwargs).order_by('jianpin'))
			return render_to_response('bglist.html', locals(), context_instance=RequestContext(request))
	else:
		form = BG_namechaxun()
		listleibie = 'kucungl'
		addleibie = 'churuku'
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_churuku_mx(request,editid): #TODO:出入库明细表已经更改，需更改明细显示方式
	title = u'库存明细'
	listleibie = 'datatable'
	daohangleibie = 'kucungl'
	id = int(editid)
	bangongyongpinname = BGYP_name.objects.get(id=id).bangongyongpinname
	is_tishi = True
	tishixinxi = u'现在查看的是 %s的出入库明细，可以点击后面的“编辑”链接对明细条目进行修改或者删除。'  % bangongyongpinname
	if request.method == 'POST':
		form = BG_search_kucun_mx(request.POST)
		if form.is_valid():
			chukuorruku = form.cleaned_data['chukuorruku']
			bumenname = form.cleaned_data['bumenname']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			kwargs = {}
			agve = {}
			if chukuorruku is not None:
				if chukuorruku == 'any':
					pass
				else:
					kwargs['fangxiang_en'] = chukuorruku

			if bumenname is not None:
				if chukuorruku == 'in':
					kwargs['bumenname'] = 13
				if  chukuorruku == 'out':
					kwargs['bumenname'] = bumenname
			if start_time or end_time is not None:
					if start_time is not None and end_time is None:
						agve['churukuriqi__gte']=start_time
					if end_time is not None:
						agve['churukuriqi__lte']=end_time
			if start_time and end_time is not None:
				agve['churukuriqi__range'] = (start_time,end_time)
			kwargs['bangongyongpinname'] = id
			jieguo = BGchurukumxtable(BGYP_churukumx.objects.filter(**kwargs).filter(**agve).order_by('-churukuriqi'))
			return render_to_response('bglist.html', locals(), context_instance=RequestContext(request))
	else:
		form = BG_search_kucun_mx()
		form.fields['bumenname'].queryset = BGYP_bumen.objects.exclude(id=13)
		listleibie = 'kucungl'
		addleibie = 'churuku'
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_churuku_mx_edit(request,editid):#TODO：出入库明细表已经跟改，需要更改表单验证方式
	global idglobal
	global caozuoglobal
	global churukufangxiangglobal
	id = int(editid)
	idglobal = id
	title = u'编辑出入库明细'
	listleibie = 'datatable'
	daohangleibie = 'kucungl'
	editchurukumx = get_object_or_404(BGYP_churukumx, id=id)
	fangxiang = editchurukumx.fangxiang_en
	if fangxiang == 'in':
		churukufangxiangglobal = 'in'
		churuku_shuliang_orig = editchurukumx.bangongyongpinshuliang_ruku #原始明细数量
	if fangxiang == 'out':
		churukufangxiangglobal = 'out'
		churuku_shuliang_orig = editchurukumx.bangongyongpinshuliang_chuku
	bangongyongpinname = editchurukumx.bangongyongpinname
	bangongyongpindanjia = editchurukumx.bangongyongpindanjia
	kucun= BGYP_kucun.objects.filter(bangongyongpinname=bangongyongpinname)
	kucun_shuliang_orig = kucun[0].bangongyongpinshuliang

	isdel = True
	if request.method == 'POST':
		if fangxiang == 'in':
			form = BG_edit_churukumx_ruku(instance=editchurukumx, data=request.POST)
		else:
			form = BG_edit_churukumx_chuku(instance=editchurukumx, data=request.POST)
		if request.POST.has_key("updata"):
				caozuoglobal =  'updata'
				if form.is_valid():
					if fangxiang == 'in':
						shuliang_input = form.cleaned_data['bangongyongpinshuliang_ruku']  #本次输入的数据
						churukuriqi = form.cleaned_data['churukuriqi']
						beizhu = form.cleaned_data['beizhu']
						chae = churuku_shuliang_orig - abs(shuliang_input)
						churuku_zongjia_new = shuliang_input*bangongyongpindanjia
						kucun_shuliang_new = kucun_shuliang_orig-chae
						kucun_zongjia_new = bangongyongpindanjia*kucun_shuliang_new
						kucun.update(bangongyongpinshuliang=kucun_shuliang_new,bangongyongpinzongjia=kucun_zongjia_new)#更新库存数据
						q = BGYP_churukumx.objects.filter(id=id)#更新明细
						q.update(bangongyongpinshuliang_ruku=shuliang_input, bangongyongpinzongjia_ruku=churuku_zongjia_new,churukuriqi=churukuriqi,beizhu=beizhu)
					if fangxiang == 'out':
						shuliang_input = form.cleaned_data['bangongyongpinshuliang_chuku']  #本次输入的数据
						churukuriqi = form.cleaned_data['churukuriqi']
						beizhu = form.cleaned_data['beizhu']
						chae = churuku_shuliang_orig - abs(shuliang_input)
						churuku_zongjia_new = shuliang_input*bangongyongpindanjia
						kucun_shuliang_new = kucun_shuliang_orig+chae
						kucun_zongjia_new = kucun_shuliang_new*bangongyongpindanjia
						kucun.update(bangongyongpinshuliang=kucun_shuliang_new,bangongyongpinzongjia=kucun_zongjia_new)
						q = BGYP_churukumx.objects.filter(id=id)#更新明细
						q.update(bangongyongpinshuliang_chuku=shuliang_input, bangongyongpinzongjia_chuku=churuku_zongjia_new,churukuriqi=churukuriqi,beizhu=beizhu)
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
					return HttpResponseRedirect('/bg/kucunsearch/')
		if request.POST.has_key("del"):  #if form.is_valid(): #删除时只是需要在表单中显示相关数据，不需要进行数据验证。
				caozuoglobal = 'del'
				if form.is_valid():
					if fangxiang == 'in':
						kucun_shuliang_new = kucun_shuliang_orig - churuku_shuliang_orig
						kucun_zongjia_new = kucun_shuliang_new * bangongyongpindanjia
						kucun.update(bangongyongpinshuliang=kucun_shuliang_new,bangongyongpinzongjia=kucun_zongjia_new)
						q = BGYP_churukumx.objects.filter(id=id)
						q.delete()
					if fangxiang == 'out':
						kucun_shuliang_new = kucun_shuliang_orig + churuku_shuliang_orig
						kucun_zongjia_new = kucun_shuliang_new * bangongyongpindanjia
						kucun.update(bangongyongpinshuliang=kucun_shuliang_new,bangongyongpinzongjia=kucun_zongjia_new)
						q = BGYP_churukumx.objects.filter(id=id)
						q.delete()
					messages.add_message(request, messages.SUCCESS, '数据更新成功！')
					return HttpResponseRedirect('/bg/kucunsearch/')
	else:
		if fangxiang == 'in':
			form = BG_edit_churukumx_ruku(instance=editchurukumx)
		if fangxiang == 'out':
			form = BG_edit_churukumx_chuku(instance=editchurukumx)

	return render_to_response('bgedit.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.bangongyongpin')
def BG_search_zonghe(request):
	daohangleibie = 'zonghechaxun'
	title = u'pandas测试'
	download = False
	#listleibie = 'pandastest'
	listleibie = 'datatable'
	jieyu = ''
	fangshi = ''
	if request.method == 'POST':
		form = BG_search_zonghe_forms(request.POST)
		if form.is_valid():
			chukuorruku = form.cleaned_data['chukuorruku']
			mxorhuizong = form.cleaned_data['mxorhuizong']
			bumenname = form.cleaned_data['bumenname']
			fenleiname = form.cleaned_data['fenleiname']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			shengchengwenjian = form.cleaned_data['shengchengwenjian']
			ishtml = form.cleaned_data['ishtml']
			#bm =  ','.join(form.cleaned_data['bumenname'])
			kwargs = {}
			agve = {}
			if chukuorruku is not None:
				if chukuorruku == 'any':
					jieyu = 'yes'
					if len(bumenname) !=0:
						kwargs['bumenname__in'] = bumenname
					pass
				elif chukuorruku == 'in':
					kwargs['fangxiang_en'] = 'in'
				elif chukuorruku == 'out':
					if len(bumenname) !=0:
						kwargs['bumenname__in'] = bumenname #bumenname返回一个空列表，不为‘none’,所以需判断列表长度
					else:
						kwargs['fangxiang_en'] = 'out'
			if fenleiname is not None:
				kwargs['fenleiname'] = fenleiname
			if start_time or end_time is not None:
					if start_time is not None and end_time is None:
						jieyu = 'no'
						agve['churukuriqi__gte']=start_time
					if end_time is not None:
						agve['churukuriqi__lte']=end_time
			if start_time and end_time is not None:
				jieyu = 'no'
				agve['churukuriqi__range'] = (start_time,end_time)
			if shengchengwenjian == 'yes':
				download = True

			qs = BGYP_churukumx.objects.filter(**kwargs).filter(**agve).order_by('churukuriqi')
			if ishtml == 'datatable':
				if mxorhuizong == 'mx':
					jieguo = BGchurukumxtable(qs)
				if mxorhuizong == 'name':
					fangshi = 'name'
					gb = pandas_output_mx(qs,fangshi,jieyu)
					jieguo = BGchurukumxtable_name_or_fenleiname(gb)
				if mxorhuizong == 'bumen':
					fangshi = 'bumen'
					gb = pandas_output_mx(qs,fangshi,jieyu)
					jieguo = BGchurukumxtable_bumen(gb)
			if ishtml == 'css':
				if mxorhuizong == 'mx':
					jieguo = BGchurukumxtable(qs)
				if mxorhuizong == 'name':
					fangshi = 'name'
					listleibie = 'pandastest'
					data = BG_tohtml(qs,fangshi,jieyu)
				if mxorhuizong == 'bumen':
					fangshi = 'bumen'
					listleibie = 'pandastest'
					data = BG_tohtml(qs,fangshi,jieyu)

			if shengchengwenjian == 'yes':
				path = BGexcel(qs,fangshi,jieyu)

			return render_to_response('bglist.html', locals(), context_instance=RequestContext(request))
	else:
		form = BG_search_zonghe_forms()
		form.fields['bumenname'].queryset = BGYP_bumen.objects.exclude(id=13)
		addleibie = 'churuku'
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

def pandas_output_mx(qs,fangshi,jieyu=''):
	qs =qs
	jieyu = jieyu
	fangshi =fangshi
	gbtodic = {}
	df = qs.to_dataframe(['bumenname','fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia','bangongyongpinshuliang_ruku',
		                      'bangongyongpinzongjia_ruku','bangongyongpinshuliang_chuku','bangongyongpinzongjia_chuku']).fillna(0)
	if fangshi == 'name':
		if jieyu == 'yes':
			df['bangongyongpinshuliang_jieyu'] = df['bangongyongpinshuliang_ruku']-df['bangongyongpinshuliang_chuku']
			df['bangongyongpinzongjia_jieyu'] = df['bangongyongpinzongjia_ruku']-df['bangongyongpinzongjia_chuku']
			gbtodic= df.groupby(['fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia'],as_index=False).sum().to_dict('records')

		else:
			gbtodic= df.groupby(['fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia'],as_index=False).sum().to_dict('records')
	if fangshi == 'bumen':
		gbtodic= df.groupby(['bumenname','fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia'],as_index=False).sum().to_dict('records')

	return gbtodic

		#df.columns=['BM','FL','NAME','JP','DJ','RKS','RKJ','CKS','CKJ']

def BGexcel(qs,fangshi,jieyu=''):
	qs =qs
	jieyu = jieyu
	fangshi =fangshi
	temp_name = str(
		datetime.date.today().strftime("%Y%m%d") + str(random.randint(1, 10000)))
	path = "/home/python/djcode/mysite/kucuntest/static/file/%s.xlsx" % temp_name
	path_return = "/static/file/%s.xlsx" % temp_name
	df = qs.to_dataframe(['bumenname','fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia','bangongyongpinshuliang_ruku',
		                      'bangongyongpinzongjia_ruku','bangongyongpinshuliang_chuku','bangongyongpinzongjia_chuku']).fillna(0)
	if fangshi == 'name':
		if jieyu == 'yes':
			df['bangongyongpinshuliang_jieyu'] = df['bangongyongpinshuliang_ruku']-df['bangongyongpinshuliang_chuku']
			df['bangongyongpinzongjia_jieyu'] = df['bangongyongpinzongjia_ruku']-df['bangongyongpinzongjia_chuku']
			df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价','结余数量','结余总价']
			df.groupby(['分类','名称','简拼','单价']).sum().to_excel(path,sheet_name='sheet1')

		else:
			df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价']
			#df.groupby(['分类','名称','简拼','单价'],as_index=False).sum().to_excel(path,sheet_name='sheet1')
			df.pivot_table(['出库数量','出库总价'],rows=['分类','名称','单价'],cols=['部门'] ,aggfunc=sum,margins=True).to_excel(path,sheet_name='sheet1')
	if fangshi == 'bumen':
		df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价']
		df.groupby(['部门','分类','名称','简拼','单价'],as_index=False).sum().to_excel(path,sheet_name='sheet1')
	return path_return








def BG_tohtml(qs,fangshi,jieyu=''):
	qs =qs
	jieyu = jieyu
	fangshi =fangshi
	data = None
	df = qs.to_dataframe(['bumenname','fenleiname','bangongyongpinname','jianpin','bangongyongpindanjia','bangongyongpinshuliang_ruku',
		                      'bangongyongpinzongjia_ruku','bangongyongpinshuliang_chuku','bangongyongpinzongjia_chuku']).fillna(0)
	if fangshi == 'name':
		if jieyu == 'yes':
			df['bangongyongpinshuliang_jieyu'] = df['bangongyongpinshuliang_ruku']-df['bangongyongpinshuliang_chuku']
			df['bangongyongpinzongjia_jieyu'] = df['bangongyongpinzongjia_ruku']-df['bangongyongpinzongjia_chuku']
			df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价','结余数量','结余总价']
			#data = df.groupby(['分类','名称','简拼','单价']).sum().to_html( classes="table table-condensed")
			data = df.pivot_table(['入库数量','入库总价','出库数量','出库总价','结余数量','结余总价'],rows=['分类','名称','单价'],aggfunc=sum,margins=True).to_html( classes="table table-condensed")

		else:
			df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价']
			#data = df.groupby(['分类','名称','简拼','单价']).sum().to_html( classes="table table-condensed")
			#data = df.pivot_table(['入库数量','入库总价','出库数量','出库总价'],rows=['分类','名称','单价'],aggfunc=sum,margins=True).to_html( classes="table table-condensed")
			data = df.pivot_table(rows=['分类','名称','单价'],cols=['部门'] ,values = ['出库数量','出库总价'],aggfunc=sum,margins=True).to_html( classes="table table-condensed")

	if fangshi == 'bumen':
		df.columns=['部门', '分类','名称','简拼','单价','入库数量','入库总价','出库数量','出库总价']
		#data = df.groupby(['部门','分类','名称','简拼','单价']).sum().to_html( classes="table table-condensed")
		data = df.pivot_table(['入库数量','入库总价','出库数量','出库总价'],rows=['部门','分类','名称','单价'],aggfunc=sum,margins=True).to_html( classes="table table-condensed")

	return data

@permission_required('kucuntest.bangongyongpin')
def bg_index(request):
	daohangleibie = 'bgindex'
	title = u'办公用品管理系统'
	df_bgyp = None
	df_dianliao = None
	df_haocai= None
	fenleilist = [1,2,3]
	for fenlei in fenleilist:
		df= pd.DataFrame(list(BGYP_churukumx.objects.filter(fangxiang_en='out',fenleiname=fenlei).values('bumenname','bangongyongpinzongjia_chuku')))
		if fenlei == 1:
			df_bgyp = df
		elif fenlei == 2:
			df_dianliao = df
		else:
			df_haocai = df

	gb_dic_val_bgyp = chart_dic_get(df_bgyp)
	gb_dic_val_dianliao = chart_dic_get(df_dianliao)
	gb_dic_val_haocai = chart_dic_get(df_haocai)
	li_bgyp = chart_json(gb_dic_val_bgyp)
	li_dianliao = chart_json(gb_dic_val_dianliao)
	li_haocai = chart_json(gb_dic_val_haocai)
	return render_to_response('charttest1.html', locals(), context_instance=RequestContext(request))

def chart_dic_get(df):
	gb = df.groupby(['bumenname']).sum()
	gb_dic = gb.to_dict()
	gb_dic_val = gb_dic.get('bangongyongpinzongjia_chuku')
	return gb_dic_val


def chart_json(gb_dic_val):
	bumenlist = [1,2,3,4,5,6,7,8,9,10,11,12]
	li = []
	for i in bumenlist:
		a = gb_dic_val.get(i)
		li.append(a)
	li_json = json.dumps(li)
	return li_json

def LianJjie_ID():
	chars = string.letters + string.digits
	creat_id = "".join(random.sample(chars, 8))
	lianjie_id = str(
		datetime.date.today().strftime("%Y%m%d") + creat_id)  #生成日期+随机数字生成的字符串
	return lianjie_id

@permission_required('kucuntest.can_update')
def gouka(request, jiaxiaoid):
	#判断是否已生成今日报表，如生成，则不可继续操作
	if JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		return render_to_response('yishengchengribaobiao.html')
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'购卡'
	todayshuju = todayshuju_dic()
	qs_paichu= list(JpMX_yingfu_paichu.objects.filter().values('jiaxiao_id'))
	qs_paichu_list = []
	for i in qs_paichu:
		qs_paichu_list.append(i.get('jiaxiao_id'))
	if jiaxiaoid not in qs_paichu_list:
		if gezhongshuju_chugenghuan(jiaxiaoid)['yingfukuan'] != 0.0:
			messages.add_message(request, messages.ERROR, '有应付款未缴清的停止购卡!')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	is_tishi = True
	lianjie_id = LianJjie_ID()#生成随机ID
	if JpMX_new.objects.filter(lianjie_id=lianjie_id).exists():
		lianjie_id = LianJjie_ID()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_gouka_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_str = pinleiname
			danjia = PinleiGL.objects.get(pinleiname=pinleiname).danjia
			gouka =abs( form.cleaned_data['gouka'])
			beizhu = form.cleaned_data['beizhu']
			fukuanfangshi = form.cleaned_data['fukuanfangshi']
			tushu_shuliang = form.cleaned_data['tushu_shiling_shuliang']
			haoduanqizhi = form.cleaned_data['haoduanqizhi'].upper()
			if tushu_shuliang == None:
				tushu_shuliang = 0
			else:
				tushu_shuliang = abs(tushu_shuliang)
			jine = gouka*danjia
			riqi = datetime.date.today()
			pinleiname_zuhe = PinleiGL.objects.get(pinleiname=pinleiname).zuhe#获取组合值
			pinleiname_zuhe_str_list = pinleiname_zuhe.split(',')#组合值字符串（得到的结果为类似u'6,1'之类的字符串）,以','分割，得到类似[u'6',u'1']的结果
			pinleiname_zuhe_list = []
			fukuanfangshi_str_cn = None


			if fukuanfangshi == 'xianjin':
				fukuanfangshi_str_cn = '现金'
			if fukuanfangshi == 'pos':
				fukuanfangshi_str_cn = 'POS刷卡'
			if fukuanfangshi == 'yinhang':
				fukuanfangshi_str_cn = '银行存入'
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,pinleiname=pinleiname,pinleiname_str=pinleiname_str,gouka=gouka,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,jine=jine,fukuanfangshi=fukuanfangshi,fukuanfangshi_str_cn=fukuanfangshi_str_cn,lianjie_id=lianjie_id,
						 tushu_shiling_shuliang=tushu_shuliang,haoduanqizhi=haoduanqizhi)
			p.save()
			for i in pinleiname_zuhe_str_list:#得到组合值列表（将字符串转换为数字）
				pinleiname_zuhe_list.append(int(i))
			for a in pinleiname_zuhe_list:
				pinleiname_1 = PinleiGL.objects.get(id=a)
				pinleiname_str_1 = pinleiname_1.pinleiname
				if a == 11:#图书ID
					gouka = tushu_shuliang
				JpMX_churuku.objects.create(pinleiname=pinleiname_1,pinleiname_str=pinleiname_str_1,danjia=pinleiname_1.danjia,caozuo='fafang',caozuo_str_cn='发放',fafang_shuliang=gouka,
				                            user=caozuo_user,riqi=riqi,lianjie_id=lianjie_id)
			haoduanliebiao = fengehaoduan(haoduanqizhi)
			#
			qs_haoduan = JpMX_ICSN.objects.filter(sn__in=haoduanliebiao)
			qs_haoduan.update(zhuangtai=u'发放',zhuangtai_str='fafang',fafang_riqi=datetime.date.today(),fafang_user=caozuo_user,jiaxiaoname=jiaxiaoname_str,
							  lianjie_id=lianjie_id)

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_gouka_forms()
		form.fields['pinleiname'].queryset = PinleiGL.objects.filter(id=9)
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_update')
def jp_tianjianqianshu(request, jiaxiaoid):#添加驾校欠数数据
	caozuo_user = request.user.username
	if caozuo_user != 'aga0217':
		return HttpResponseNotFound
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'添加驾校欠书数据'
	todayshuju = todayshuju_dic()
	is_tishi = True
	lianjie_id = LianJjie_ID()#生成随机ID
	if JpMX_new.objects.filter(lianjie_id=lianjie_id).exists():
		lianjie_id = LianJjie_ID()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()

	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_tianjiaqianshu_forms(request.POST)
		if form.is_valid():
			yingling_shuliang = form.cleaned_data['tushu_yingling_shuliang']
			beizhu = form.cleaned_data['beizhu']


			riqi = datetime.date.today()

			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,lianjie_id=lianjie_id,tushu_shiling_shuliang=0,
						 tushu_yingling_shuliang=yingling_shuliang)
			p.save()
			pinleiname = PinleiGL.objects.get(id=11)
			pinleiname_str = pinleiname.pinleiname
			JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname_str,caozuo='fafang',caozuo_str_cn='发放',
										fafang_shuliang=0,user=caozuo_user,riqi=riqi,lianjie_id=lianjie_id)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_tianjiaqianshu_forms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def jp_lingshu(request, jiaxiaoid):#驾校单独领取教材
	caozuo_user = request.user.username
	global jiaxiaoidglobal
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'驾校领书'
	todayshuju = todayshuju_dic()
	is_tishi = True
	lianjie_id = LianJjie_ID()#生成随机ID
	if JpMX_new.objects.filter(lianjie_id=lianjie_id).exists():
		lianjie_id = LianJjie_ID()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！该驾校最大可领取教材数为%d！' % (jiaxiaoname,
														gezhongshuju_chugenghuan(jiaxiaoid).get('tushu_qian_shuliang'))
	shijian = datetime.datetime.now()

	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_lingshu_forms(request.POST)
		if form.is_valid():
			shiling_shuliang = form.cleaned_data['tushu_shiling_shuliang']
			beizhu = form.cleaned_data['beizhu']


			riqi = datetime.date.today()

			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,lianjie_id=lianjie_id,tushu_yingling_shuliang=0,
						 tushu_shiling_shuliang=shiling_shuliang)
			p.save()
			pinleiname = PinleiGL.objects.get(id=11)
			pinleiname_str = pinleiname.pinleiname
			JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname_str,caozuo='fafang',caozuo_str_cn='发放',
										fafang_shuliang=shiling_shuliang,user=caozuo_user,riqi=riqi,lianjie_id=lianjie_id)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_lingshu_forms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_update')
def shouquan(request, jiaxiaoid):
	global jiaxiaoidglobal
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'授权'
	todayshuju = todayshuju_dic()
	is_tishi = True
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_shouquan_froms(request.POST)
		if form.is_valid():

			shouquan =abs( form.cleaned_data['shouquan'])
			beizhu = form.cleaned_data['beizhu']
			riqi = datetime.date.today()
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,shouquan=shouquan,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_shouquan_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def yulingdengji(request, jiaxiaoid):
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'预领登记'
	is_tishi = True
	todayshuju = todayshuju_dic()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_yulingdengji_froms(request.POST)
		if form.is_valid():

			yuling_in =abs( form.cleaned_data['yuling_in'])
			beizhu = form.cleaned_data['beizhu']
			riqi_yewu = form.cleaned_data['riqi_yewu']
			riqi = datetime.date.today()
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,yuling_in=yuling_in,beizhu=beizhu,riqi=riqi,riqi_yewu=riqi_yewu,
			             user=caozuo_user)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_yulingdengji_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def yulingshoufei(request, jiaxiaoid):
	if JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		return Http404
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'预领收费'
	is_tishi = True
	todayshuju = todayshuju_dic()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_yulingshoufei_froms(request.POST)
		if form.is_valid():

			yuling_out =abs( form.cleaned_data['yuling_out'])
			fukuanfangshi =  form.cleaned_data['fukuanfangshi']
			beizhu = form.cleaned_data['beizhu']
			jine = yuling_out * 100
			riqi = datetime.date.today()
			if fukuanfangshi == 'xianjin':
				fukuanfangshi_str_cn = '现金'
			if fukuanfangshi == 'pos':
				fukuanfangshi_str_cn = 'POS刷卡'
			if fukuanfangshi == 'yinhang':
				fukuanfangshi_str_cn = '银行存入'
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,yuling_out=yuling_out,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,riqi_yewu = riqi,fukuanfangshi=fukuanfangshi,jine=jine,fukuanfangshi_str_cn=fukuanfangshi_str_cn)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_yulingshoufei_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def genghuandengji(request, jiaxiaoid):
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'更换商品登记'
	todayshuju = todayshuju_dic()
	is_tishi = True
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_genghuandengji_froms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_str = pinleiname
			genghuan_in =abs( form.cleaned_data['genghuan_in'])
			beizhu = form.cleaned_data['beizhu']
			sn = form.cleaned_data['sn'].upper()
			riqi = datetime.date.today()
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,genghuan_in=genghuan_in,pinleiname=pinleiname,pinleiname_str=pinleiname_str,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,haoduanqizhi=sn)
			p.save()

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			sn_list = sn.split(',')
			for i in sn_list:
				if JpMX_ICSN.objects.filter(sn=i).exists():
					JpMX_ICSN.objects.filter(sn=i).update(zhuangtai=u'更换登记',genghuan_in_riqi=riqi,genghuan_in_user=caozuo_user,jiaxiaoname=jiaxiaoname_str,
												   zhuangtai_str='genghuan_in',lianjie_id=None)
				else:
					JpMX_ICSN.objects.create(sn=i,dengji_riqi=riqi,zhuangtai=u'更换登记',genghuan_in_riqi=riqi,genghuan_in_user=caozuo_user,jiaxiaoname=jiaxiaoname_str,
												   zhuangtai_str='genghuan_in',lianjie_id=None,dengji_user=caozuo_user)
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_genghuandengji_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def genghuanchuli(request, jiaxiaoid):
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'更换商品处理'
	is_tishi = True
	todayshuju = todayshuju_dic()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_genghuanchuli_froms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_str = pinleiname
			pinleiname_id = PinleiGL.objects.get(pinleiname=pinleiname).id
			genghuan_out =abs( form.cleaned_data['genghuan_out'])
			beizhu = form.cleaned_data['beizhu']
			haoduanqizhi = form.cleaned_data['haoduanqizhi'].upper()
			riqi = datetime.date.today()
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,genghuan_out=genghuan_out,pinleiname=pinleiname,pinleiname_str=pinleiname_str,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,haoduanqizhi=haoduanqizhi)
			p.save()
			if pinleiname_id ==6:
				haoduanliebiao = fengehaoduan(haoduanqizhi)
				qs_haoduan = JpMX_ICSN.objects.filter(sn__in=haoduanliebiao)
				qs_haoduan.update(zhuangtai=u'更换处理',zhuangtai_str='genghuan_out',genghuan_out_riqi=datetime.date.today(),genghuan_out_user=caozuo_user,jiaxiaoname=jiaxiaoname_str)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_genghuanchuli_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def caozuoxuanzenew(request, jiaxiaoid):
	permission = request.user.has_perm('kucuntest.can_update')
	todayshuju = todayshuju_dic()
	user = request.user.username
	if not permission:
		messages.add_message(request, messages.WARNING, '你无权使用这个功能，请重新登录！')
		return HttpResponseRedirect('/accounts/login/')
	else:
		jiaxiaoid = int(jiaxiaoid)
		jiaxiao = get_object_or_404(JixiaoInfo, id=jiaxiaoid)
		title = jiaxiao.name
		jiaxiaolist = jiaxiaolist_test()
		yuling_shengyu_num = def_yuling_shengyu_num('yuling')
		yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
		genghuanshu = gezhongshuju_genghuan(jiaxiaoid)
		keshouquanshu_xujiaofeishu = gezhongshuju_chugenghuan(jiaxiaoid)
		yishengchengbaobiao = JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists()
	return render_to_response('xuanzenew.html', locals(), context_instance=RequestContext(request))

def gezhongshuju_genghuan(jiaxiaoid):#更换数据
	jiaxiaoid = jiaxiaoid

	df = pd.DataFrame(list(JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('pinleiname_id','genghuan_in','genghuan_out'))).fillna(0)
	if not df.empty:
		df['xugenghuanshu'] = df['genghuan_in']-df['genghuan_out']#生成需更换数
		group_dic=df.groupby(['pinleiname_id'],as_index=False).sum().to_dict('recodes')#对数据表按品类名称求和
		list_key = []
		list_val = []
		for i in group_dic:
			a = str(i.get('pinleiname_id')).split('.')[0]#将品类ID转换为字符串
			b = i.get('xugenghuanshu')#得到双精度数字
			list_key.append(a)
			list_val.append(b)
		dic = dict(zip(list_key,list_val))#合成为字典
		#del dic['0']
		dic1 = dic

		list_pinlei=['1','2','3','4','5','6']
		for pinlei in list_pinlei:#如果没有对应键则键值为零并加入字典
			if pinlei not in dic1:
				dic[pinlei] = 0.0
	else:
		dic1 = {'1':0.0,'2':0.0,'3':0.0,'4':0.0,'5':0.0,'6':0.0}
	return dic1

def gezhongshuju_chugenghuan(jiaxiaoid):#除更换以外的各种数据
	jiaxiaoid = jiaxiaoid
	df = pd.DataFrame(list(JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('gouka','shouquan',
			'yuling_in','yuling_out','yingfukuan_dengji','yingfukuan_shoufei','tushu_yingling_shuliang','tushu_shiling_shuliang'))).fillna(0)
	if not df.empty:
		df['keshouquanshu']=df['gouka']-df['shouquan']
		df['xujiaofei']=df['yuling_in']-df['yuling_out']
		df['yingfukuan']=df['yingfukuan_dengji']-df['yingfukuan_shoufei']
		df['tushu_qian_shuliang']=df['tushu_yingling_shuliang']-df['tushu_shiling_shuliang']
		df_sum=df.sum().to_dict()
	else:
		df_sum={'keshouquanshu':0.0,'xujiaofei':0.0,'yingfukuan':0.0,'tushu_qian_shuliang':0.0}
	return df_sum

@permission_required('kucuntest.can_update')
def  jiaxiaolist(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'驾校列表'
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()

	#daohangleibie = 'name'
	#is_tishi = True
	#tishixinxi = u"本页面可以添加办公用品名称也可以根据办公用品分类进行查询并进行办公用品入库操作！"
	qs = JixiaoInfo.objects.filter(isuesful=True)
	jieguo = JP_JiaXiaolisttable(qs)

	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def  shouquanmx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'购卡、授权明细'
	anniuzu = True
	jiaxiaoid =int(jiaxiaoid)
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	#daohangleibie = 'name'
	#is_tishi = True
	#tishixinxi = u"本页面可以添加办公用品名称也可以根据办公用品分类进行查询并进行办公用品入库操作！"
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','gouka','shouquan','riqi','beizhu','fukuanfangshi_str_cn','jine','haoduanqizhi')
	dic_list = mx_chulikonghang(qs,'gouka','shouquan')
	jieguo = JP_ShouQuanmxtable(dic_list)

	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def tushumx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'图书领取明细'
	anniuzu = True
	jiaxiaoid =int(jiaxiaoid)
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	#daohangleibie = 'name'
	#is_tishi = True
	#tishixinxi = u"本页面可以添加办公用品名称也可以根据办公用品分类进行查询并进行办公用品入库操作！"
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('jiaxiaoname_str','tushu_yingling_shuliang',
																			  'tushu_shiling_shuliang','riqi','beizhu')
	dic_list = mx_chulikonghang(qs,'tushu_yingling_shuliang','tushu_shiling_shuliang')
	jieguo = JP_TuShumxtable(dic_list)

	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))




@permission_required('kucuntest.can_update')
def  yulingmx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'预领登记、收费明细'
	anniuzu = True
	jiaxiaoid = int(jiaxiaoid)
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','yuling_in','yuling_out','riqi_yewu','beizhu','fukuanfangshi_str_cn','jine')
	dic_list = mx_chulikonghang(qs,'yuling_in','yuling_out')
	jieguo = JP_YuLingmxtable(dic_list)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def  genghuanmx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	anniuzu = True
	title = u'商品更换明细'
	jiaxiaoid =int(jiaxiaoid)
	listleibie = 'datatable'
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','pinleiname_str','genghuan_in','genghuan_out','riqi','beizhu')
	dic_list = mx_chulikonghang(qs,'genghuan_in','genghuan_out')
	jieguo = JP_GenHuanmxtable(dic_list)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

def mx_chulikonghang(qs,str_a,str_b=None,str_c=None):
	str_a = str_a
	str_b = str_b
	str_c = str_c
	dic_list = []
	for i in qs:
		if  i.get(str_a) or i.get(str_b) or i.get(str_c):
			dic_list.append(i)
	return dic_list

def todayshuju_dic():
	today = datetime.date.today()
	today_str = str(today.isoformat())
	qs = JpMX_new.objects.filter(riqi=today_str,isdelete=False)
	xianjin_list = []
	pos_list = []
	yinhang_list = []
	for a in qs:
		if a.fukuanfangshi == 'xianjin':
			xianjin_list.append(a.jine)
		elif a.fukuanfangshi == 'yinhang':
			yinhang_list.append(a.jine)
		elif a.fukuanfangshi == 'pos':
			pos_list.append(a.jine)
	sum_xianjin = sum(xianjin_list)
	sum_pos = sum(pos_list)
	sum_yinhang = sum(yinhang_list)
	sum_dic = qs.aggregate(sum_shouka=Sum('gouka'),sum_shouquan=Sum('shouquan'),sum_yulingshoufei=Sum('yuling_out'),
						   sum_dandugoumai=Sum('dandugoumai_shuliang'),sum_yingfukuan=Sum('yingfukuan_shoufei'))
	sum_dic['sum_xianjin'] = sum_xianjin
	sum_dic['sum_pos'] = sum_pos
	sum_dic['sum_yinhang'] = sum_yinhang
	return sum_dic

@permission_required('kucuntest.can_update')
def todayshuju_mx(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'日业务明细'
	today = datetime.date.today()
	today_str = str(today.isoformat())
	listleibie = 'todaymx'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	df = pd.DataFrame(list(JpMX_new.objects.filter(riqi=today_str,isdelete=False).values('jiaxiaoname_str','gouka','dandugoumai_shuliang','shouquan','yuling_out','yingfukuan_shoufei','jiaxiaoname_id'))).fillna(0)
	jieguo =  []
	if not df.empty:
		jieguo_df = df.groupby(['jiaxiaoname_str','jiaxiaoname_id'],as_index=False).sum().to_dict('recodes')
		for a in jieguo_df:
			if  a.get('dandugoumai_shuliang') != 0 or a.get('gouka') != 0 or a.get('shouquan') != 0 or a.get('yuling_out') != 0 or a.get('yingfukuan_shoufei') != 0:
				jieguo.append(a)
	else:
		jieguo = {'jiaxiaoname_str':0,'gouka':0,'shouquan':0,'yuling_out':0,'dandugoumai_shuliang':0,'yingfukuan_shoufei':0}
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))




@permission_required('kucuntest.can_update')
def JP_JpMX_new_edit(request,editid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	id = int(editid)
	title = u'编辑业务明细'
	jiaxiaolist = jiaxiaolist_test()
	erbuyanzheng = True
	todayshuju = todayshuju_dic()
	editmx = get_object_or_404(JpMX_new, id=id)
	jiaxiaoid = editmx.jiaxiaoname_id
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	nameorNO=jiaxiaoname
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	if request.method == 'POST':
		form = JP_edit_mx_beizhu(instance=editmx, data=request.POST)
		if form.is_valid():
			beizhu = form.cleaned_data['beizhu']
			q = JpMX_new.objects.filter(id = id)
			q.update(beizhu=beizhu)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/jp/caozuonew/%d/' %(jiaxiaoid))


	else:
		form = JP_edit_mx_beizhu(instance=editmx)

	return render_to_response('editnew.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_update')
def JP_JpMX_new_delete(request,editid):
	id = int(editid)
	edit_username = request.user.username
	deletemx = JpMX_new.objects.filter(id=id)
	edit_datetime =  datetime.datetime.now()
	if len(deletemx) == 0:
		return Http404
	jiaxiaoid = deletemx[0].jiaxiaoname_id
	if deletemx[0].gouka is None:
		messages.add_message(request, messages.ERROR, '只能删除购卡数据，其他数据删除请联系管理员！')
		return HttpResponseRedirect('/jp/caozuonew/%d/' %(jiaxiaoid))
	keshouquanshu = gezhongshuju_chugenghuan(jiaxiaoid).get('keshouquanshu')
	if deletemx[0].gouka>keshouquanshu:
		messages.add_message(request, messages.ERROR, '该条数据不可删除！因为如果删除将造成购卡数小于已授权数！')
		return HttpResponseRedirect('/jp/caozuonew/%d/' %(jiaxiaoid))
	lianjie_id = deletemx[0].lianjie_id#找到明细表中的对应lianjie_id
	if lianjie_id:#lianjie_id是否存在，除发放操作外，其他的操作不会生成lianjie_id
		JpMX_churuku.objects.filter(lianjie_id=lianjie_id).update(isdelete=True,edit_day_time=edit_datetime,edit_username=edit_username)
		JpMX_ICSN.objects.filter(lianjie_id=lianjie_id).update(zhuangtai=u'登记',zhuangtai_str='dengji',jiaxiaoname=None,
															   edit_username=edit_username,edit_day_time=edit_datetime,
															   lianjie_id=None)

	deletemx.update(isdelete=True,edit_username=edit_username,edit_day_time=edit_datetime)
	messages.add_message(request, messages.SUCCESS, '数据删除成功！')
	return HttpResponseRedirect('/jp/caozuonew/%d/' %(jiaxiaoid))

@permission_required('kucuntest.can_delete')
def Jp_new_jinchikucun(request):
	title = u'查看金赤库存'
	listleibie = 'jinchikucun'
	user = request.user.username
	df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False).exclude(caozuo='fafang').values('pinleiname_str',
	                                                    'danjia','ruku_shuliang','xiaoshou_shuliang','jieshou_shuliang'))).fillna(0)#生成数据表
	if not df.empty:
		df['jieyu_shuliang']=df['ruku_shuliang']-df['jieshou_shuliang']-df['xiaoshou_shuliang']#生成结余数列
		df_group = df.groupby(['pinleiname_str','danjia'],as_index=False).sum()#以品类名称和单价进行分组
		df_dic = df_group.to_dict('recodes')
	return render_to_response('list.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_new_ruku(request):
	title = u'添加出入库记录'
	listleibie = 'crk'
	user = request.user.username
	riqi = datetime.date.today()
	erbuyanzheng = True
	erbuyanzhengneirong = u'请确认全部信息！提交吗？'
	if request.method == 'POST':
		form = JP_new_ruku_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			danjia = form.cleaned_data['danjia']
			shuliang = form.cleaned_data['ruku_shuliang']
			beizhu = form.cleaned_data['beizhu']
			caozuo = 'ruku'
			ruku_zongjia = shuliang*danjia
			JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname,danjia=danjia,caozuo=caozuo,
			                            caozuo_str_cn='入库',ruku_shuliang=shuliang,
				                            ruku_zongjia=ruku_zongjia,user=user,riqi=riqi,beizhu=beizhu)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
		return HttpResponseRedirect('/jp/jinchikucun/')
#return render_to_response('shuchujieguo.html',{'cd':cd})
	else:
		form = JP_new_ruku_forms()
			#form.fields['hetongNO'].queryset = HetongGL.objects.filter(hetongNO=hetongNO)  #指定外键下拉框选择范围，可以使用查询条件
		#form.fields['churukufangxiang'] = forms.ChoiceField(choices=[('IN','入库')]) #指定一个列表
		#forms.ChoiceField(choices=[ (o.id, str(o)) for o in Waypoint.objects.all()])#可以生成一个动态的下拉列表

	return render_to_response('add.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_delete')


def Jp_new_addICSN(request):
	title = u'批量添加SN'
	listleibie = 'gys'
	erbuyanzheng = False
	erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改供应商名称！'
	today = datetime.date.today()
	user = request.user.username
	if request.method == 'POST':
		form = JP_tianjiaICSN_forms(request.POST)
		if form.is_valid():
			haoduanqizhi = form.cleaned_data['haoduanqizhi']
			liebiao = fengehaoduan(haoduanqizhi)
			for i in liebiao:
				JpMX_ICSN.objects.create(sn=i,zhuangtai=u'登记',zhuangtai_str='dengji',dengji_riqi=today,dengji_user=user)



			#p = GongyingshangGL.objects.create(name=name, kaihuhang=kaihuhang, zhanghao=zhanghao, hanghao=hanghao, isedit=1)

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/jp/jinchikucun/')
	else:
		form = JP_tianjiaICSN_forms()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))

def fengehaoduan(str_input):
    return_list = []
    str_input_split = str_input.split('|')
    for i in str_input_split:
        i_split = i.split('-')
        start,end = i_split[0],i_split[1]
        lst1 = shengchengliebiao(start,end)
        for a in lst1:
            return_list.append(a)
    return return_list

def shengchengliebiao(start,end):
    if start[0:5] != end[0:5]:
        return False

    sn_qian = start[:5]
    start_int,end_int = strtoint(start),strtoint(end)
    sn_hou_list = range(start_int,end_int+1)
    return_list = []
    for i in sn_hou_list:
        str_hou_int = inttostr(i)
        str_wanzheng = sn_qian+str_hou_int
        return_list.append(str_wanzheng)
    return return_list

def strtoint(str_input):
    re_int = int(str_input[5:11])
    return re_int

def inttostr(int_input):
    return_str=''
    inttostr_str_list = list(str(int_input))
    while len(inttostr_str_list)<6:
        inttostr_str_list[0:0] = '0'
    return return_str.join(inttostr_str_list)
@permission_required('kucuntest.can_delete')
def Jp_new_xiaoshou(request):
	title = u'添加销售记录'
	listleibie = 'crk'
	user = request.user.username
	riqi = datetime.date.today()
	erbuyanzheng = True
	erbuyanzhengneirong = u'请确认全部信息！提交吗？'
	if request.method == 'POST':
		form = JP_new_xiaoshou_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			danjia_org = form.cleaned_data['danjia']
			danjia = form.cleaned_data['xiaoshou_danjia']
			shuliang = form.cleaned_data['xiaoshou_shuliang']
			beizhu = form.cleaned_data['beizhu']
			caozuo = 'zhanneixiaoshou'
			xiaoshou_zongjia = shuliang*danjia
			JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname,danjia=danjia_org,
			                            xiaoshou_danjia=danjia,caozuo=caozuo,caozuo_str_cn='站内直接销售',xiaoshou_shuliang=shuliang,
				                            xiaoshou_zongjia=xiaoshou_zongjia,user=user,riqi=riqi,beizhu=beizhu)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
		return HttpResponseRedirect('/jp/jinchikucun/')
#return render_to_response('shuchujieguo.html',{'cd':cd})
	else:
		form = JP_new_xiaoshou_forms()
			#form.fields['hetongNO'].queryset = HetongGL.objects.filter(hetongNO=hetongNO)  #指定外键下拉框选择范围，可以使用查询条件
		#form.fields['churukufangxiang'] = forms.ChoiceField(choices=[('IN','入库')]) #指定一个列表
		#forms.ChoiceField(choices=[ (o.id, str(o)) for o in Waypoint.objects.all()])#可以生成一个动态的下拉列表

	return render_to_response('add.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_new_chuku(request):
	title = u'添加出库记录'
	listleibie = 'crk'
	user = request.user.username
	riqi = datetime.date.today()
	erbuyanzheng = True
	erbuyanzhengneirong = u'请确认全部信息！提交吗？'
	if request.method == 'POST':
		form = JP_new_chuku_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			danjia = form.cleaned_data['danjia']
			shuliang = form.cleaned_data['chuku_shuliang']
			beizhu = form.cleaned_data['beizhu']
			lianjie_id = LianJjie_ID()
			caozuo = 'chuku'
			chuku_zongjia = shuliang*danjia
			JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname,danjia=danjia,caozuo=caozuo,
			                            caozuo_str_cn='出库',chuku_shuliang=shuliang,
				                            chuku_zongjia=chuku_zongjia,user=user,riqi=riqi,beizhu=beizhu,
			                            isjieshou='no',lianjie_id=lianjie_id)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
		return HttpResponseRedirect('/jp/jinchikucun/')
	else:
		form = JP_new_chuku_forms()
	return render_to_response('add.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_new_shangpinjieshou(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'商品中转明细'
	listleibie = 'zhongzhuanmxlist'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	user = request.user.username
	zhongzhuan = JpMX_churuku.objects.filter(isdelete=False,caozuo='chuku').order_by('-riqi')
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_new_shangpinjieshou_jieshou(request,lianjieid):
	lianjie_id = lianjieid
	user = request.user.username
	zhongzhuanwupin =  get_object_or_404(JpMX_churuku, lianjie_id=lianjie_id)
	edit_id = zhongzhuanwupin.id
	pinleiname=zhongzhuanwupin.pinleiname
	pinleiname_str = zhongzhuanwupin.pinleiname_str
	danjia = zhongzhuanwupin.danjia
	jieshou_shuliang = zhongzhuanwupin.chuku_shuliang
	riqi = datetime.date.today()
	edit_riqi = datetime.datetime.now()
	JpMX_churuku.objects.create(pinleiname=pinleiname,pinleiname_str=pinleiname_str,danjia=danjia,caozuo='jieshou',
	                            user=user,riqi=riqi,
	                            lianjie_id=lianjie_id,caozuo_str_cn='接收',jieshou_shuliang=jieshou_shuliang)
	qs = JpMX_churuku.objects.filter(id=edit_id)
	qs.update(isjieshou='yes',edit_username=user,edit_day_time=edit_riqi)
	messages.add_message(request, messages.SUCCESS, '商品接收成功！')

	return HttpResponseRedirect('/jp/shangpinjieshou/')

@permission_required('kucuntest.can_delete')
def Jp_new_xiaoshoukucun(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'查看库存'
	listleibie = 'xiaoshoukucun'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	user = request.user.username
	df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False).values('pinleiname_str','fafang_shuliang',
	                                                                           'jieshou_shuliang'))).fillna(0)#生成数据表
	if not df.empty:
		df['jieyu_shuliang']=df['jieshou_shuliang']-df['fafang_shuliang']#生成结余数列
		df_group = df.groupby(['pinleiname_str'],as_index=False).sum()#以品类名称和单价进行分组
		df_dic = df_group.to_dict('recodes')
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def dandugoumai(request, jiaxiaoid):
	if JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		return Http404
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	global jiaxiaoidglobal
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'单独购买（不可授权）'
	todayshuju = todayshuju_dic()
	is_tishi = True
	lianjie_id = LianJjie_ID()#生成随机ID
	if JpMX_new.objects.filter(lianjie_id=lianjie_id).exists():
		lianjie_id = LianJjie_ID()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '本次输入的内容将不计算入可授权数，确认吗？'
	tishixinxi = '现在操作的是：%s驾校，且单独购买的数量不会计入可授权数！请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.now()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = JP_dandugoumai_forms(request.POST)
		if form.is_valid():
			pinleiname = form.cleaned_data['pinleiname']
			pinleiname_str = pinleiname
			danjia = PinleiGL.objects.get(pinleiname=pinleiname).danjia
			dandugoumai_shuliang = abs(form.cleaned_data['dandugoumai_shuliang'])
			beizhu = form.cleaned_data['beizhu']
			fukuanfangshi = form.cleaned_data['fukuanfangshi']
			haoduanqizhi = form.cleaned_data['haoduanqizhi']
			haoduanqizhi = haoduanqizhi.upper()
			jine = dandugoumai_shuliang*danjia
			riqi = datetime.date.today()
			pinleiname_zuhe = PinleiGL.objects.get(pinleiname=pinleiname).zuhe#获取组合值
			pinleiname_zuhe_str_list = pinleiname_zuhe.split(',')#组合值字符串（得到的结果为类似u'6,1'之类的字符串）,以','分割，得到类似[u'6',u'1']的结果
			pinleiname_zuhe_list = []
			for i in pinleiname_zuhe_str_list:#得到组合值列表（将字符串转换为数字）
				pinleiname_zuhe_list.append(int(i))
			for a in pinleiname_zuhe_list:
				pinleiname_1 = PinleiGL.objects.get(id=a)
				pinleiname_str_1 = pinleiname_1.pinleiname
				JpMX_churuku.objects.create(pinleiname=pinleiname_1,pinleiname_str=pinleiname_str_1,danjia=pinleiname_1.danjia,caozuo='fafang',caozuo_str_cn='发放',fafang_shuliang=dandugoumai_shuliang,
				                            user=caozuo_user,riqi=riqi,lianjie_id=lianjie_id)
			if fukuanfangshi == 'xianjin':
					fukuanfangshi_str_cn = '现金'
			if fukuanfangshi == 'pos':
					fukuanfangshi_str_cn = 'POS刷卡'
			if fukuanfangshi == 'yinhang':
					fukuanfangshi_str_cn = '银行存入'
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,pinleiname=pinleiname,pinleiname_str=pinleiname_str,
						 dandugoumai_shuliang=dandugoumai_shuliang,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user,jine=jine,fukuanfangshi=fukuanfangshi,fukuanfangshi_str_cn=fukuanfangshi_str_cn,
						 lianjie_id=lianjie_id,haoduanqizhi=haoduanqizhi)
			p.save()
			haoduanliebiao = fengehaoduan(haoduanqizhi)
			#
			qs_haoduan = JpMX_ICSN.objects.filter(sn__in=haoduanliebiao)
			qs_haoduan.update(zhuangtai=u'发放',zhuangtai_str='fafang',fafang_riqi=datetime.date.today(),fafang_user=caozuo_user,jiaxiaoname=jiaxiaoname_str,
							  lianjie_id=lianjie_id)
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_dandugoumai_forms()
		form.fields['pinleiname'].queryset = PinleiGL.objects.filter(id=9)
		#form.fields['pinleiname'].queryset = PinleiGL.objects.filter(id__in=[9,8])#多值
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def  dandugoumaimx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	anniuzu = True
	title = u'单独购买（不可授权）明细'
	jiaxiaoid =int(jiaxiaoid)
	listleibie = 'datatable'
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','pinleiname_str',
	                                            'fukuanfangshi_str_cn','jine','dandugoumai_shuliang','riqi','beizhu')
	
	dic_list = mx_chulikonghang(qs,'dandugoumai_shuliang')
	jieguo = JP_DanDougoumaimxtable(dic_list)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_new_jinchikucun_chukumx(request):
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	title = u'查看出库明细'
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	user = request.user.username
	df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False,caozuo='chuku').values('pinleiname_str','danjia',
	                                'chuku_shuliang','chuku_zongjia','isjieshou','riqi',
	                                'edit_day_time'))).fillna(datetime.datetime(1900, 1, 1, 1, 14, 29, 456451))
	if not df.empty:
		df_dic = df.to_dict('recodes')
	jieguo = JP_Jinchikucun_chukumx(df_dic)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_jinchikucun_rukumx(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'查看入库明细'
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	user = request.user.username
	df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False,caozuo='ruku').values('pinleiname_str','danjia','ruku_shuliang','ruku_zongjia','riqi','beizhu')))
	if not df.empty:
		df_dic = df.to_dict('recodes')
	jieguo = JP_Jinchikucun_rukumx(df_dic)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_delete')
def Jp_jinchikucun_xiaoshoumx(request):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'查看销售明细'
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	user = request.user.username
	df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False,caozuo='zhanneixiaoshou').values('pinleiname_str',
	                                'xiaoshou_danjia','danjia','xiaoshou_shuliang','xiaoshou_zongjia','riqi','beizhu')))
	if not df.empty:
		df_dic = df.to_dict('recodes')
	jieguo = JP_Jinchikucun_xiaoshoumx(df_dic)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))


@permission_required('kucuntest.can_update')
def Jp_new_xushoufeimx(request):
	title = u'预领需收费驾校列表'
	listleibie = 'datatable'
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	jieguo = JP_XuShoufeimxtable(def_df_dic('yuling'))
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

def def_df(fangshi):#创建df并进行筛选
	if fangshi == 'yuling':
		df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False).values('jiaxiaoname_str','yuling_in','yuling_out')))
	elif fangshi == 'yingfukuan':
		df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False).values('jiaxiaoname_str','yingfukuan_dengji','yingfukuan_shoufei')))
	df_fill = df.fillna(0)
	if fangshi == 'yuling':
		df_shaixuan = df_fill[(df.yuling_in >0)|(df.yuling_out >0)]
	elif fangshi == 'yingfukuan':
		df_shaixuan = df_fill[(df.yingfukuan_dengji >0)|(df.yingfukuan_shoufei >0)]
	df_sum = df_shaixuan.groupby(['jiaxiaoname_str'],as_index=False).sum()
	if fangshi == 'yuling':
		df_sum['xujiaofei'] = df_sum['yuling_in'] - df_sum['yuling_out']
		df_zaicishaixuan = df_sum[(df_sum.xujiaofei>0)]
	elif fangshi == 'yingfukuan':
		df_sum['yingfukuan'] = df_sum['yingfukuan_dengji'] - df_sum['yingfukuan_shoufei']
		df_zaicishaixuan = df_sum #不需要再次筛选,如果再次筛选会除去已付款驾校.
	return df_zaicishaixuan
def def_df_dic(fangshi):#将筛选结果转换为字典
		df_dic = def_df(fangshi).to_dict('recodes')
		return df_dic
def def_yuling_shengyu_num(fangshi):#得到汇总数字
		yuling_shengyu_num_df = def_df(fangshi)
		yuling_shengyu_num = yuling_shengyu_num_df['xujiaofei'].sum()
		return yuling_shengyu_num
def def_yingfukuan_shengyu_num(fangshi):#得到汇总数字
		yingfukuan_num_df = def_df(fangshi)
		yingfukuan_shengyu_num = yingfukuan_num_df['yingfukuan'].sum()
		return yingfukuan_shengyu_num

@permission_required('kucuntest.can_delete')
def Jp_new_zonghechaxun(request):
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	title = u'综合查询测试'
	download = False
	listleibie = 'pandastestnew'
	addleibie = 'churuku'
	jieyu = ''
	fangshi = ''

	if request.method == 'POST':
		form = JP_search_zonghe_forms(request.POST)
		if form.is_valid():
			fafangorshouquan = form.cleaned_data['fafangorshouquan']
			mxorhuizong = form.cleaned_data['mxorhuizong']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			shengchengwenjian = form.cleaned_data['shengchengwenjian']
			kwargs = {}
			agve = {}

			is_sum = False

			if start_time or end_time is not None:
					if start_time is not None and end_time is None:
						agve['riqi__gte']=start_time
					if end_time is not None:
						agve['riqi__lte']=end_time
			if start_time and end_time is not None:
				agve['riqi__range'] = (start_time,end_time)


			df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False).filter(**agve).order_by('riqi').values(
				'jiaxiaoname_str','riqi','gouka','shouquan','dandugoumai_shuliang','tushu_yingling_shuliang','tushu_shiling_shuliang','is_tushu_qichushu')))
			df_copy = pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False).filter(**agve).order_by('riqi').values(
				'jiaxiaoname_str','riqi','gouka','shouquan','dandugoumai_shuliang','tushu_yingling_shuliang','tushu_shiling_shuliang','is_tushu_qichushu')))
			if mxorhuizong == 'mx':
				data = JP_tohtml(df,fafangorshouquan,mxorhuizong)
			if mxorhuizong == 'jiaxiaoname':
				listleibie = 'datatable_pandas'
				jieguo_dic = JP_tohtml(df,fafangorshouquan,mxorhuizong)
				if fafangorshouquan =='fafang':
					jieguo = JP_zonghechaxun_gouka_huizong_table(jieguo_dic.get('jieguo'))
				if fafangorshouquan =='shouquan':
					jieguo = JP_zonghechaxun_shouquan_huizong_table(jieguo_dic.get('jieguo'))
				if fafangorshouquan == 'jiaocai':
					jieguo = JP_zonghechaxun_jiaocai_huizong_table(jieguo_dic.get('jieguo'))

			if shengchengwenjian == 'yes':
				path = JPexcel(df_copy,fafangorshouquan,mxorhuizong,agve)

			return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))
	else:
		form = JP_search_zonghe_forms()
	return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def Jp_new_shenfenbangdingchaxun(request):
	listleibie = 'shenfenbangding'
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'查询身份绑定信息'
	todayshuju = todayshuju_dic()
	is_tishi = True
	erbuyanzheng = False
	gengxinriqi = JpMX_SNgengxinriqi.objects.get(id=1).gengxinriqi.strftime('%Y-%m-%d')
	tishixinxi = '现在只能查询到%s以前制卡的信息,%s以后制卡信息只能等到下次更新后进行查询.' % (gengxinriqi,gengxinriqi)
	jiaxiaolist = jiaxiaolist_test()
	addleibie = 'churuku'
	jieguo_list = []

	if request.method == 'POST':
		form = JP_shenfenbangdingchaxun_forms(request.POST)
		if form.is_valid():
			SN = form.cleaned_data['SN']
			SN = SN.upper()
			sn_list = SN.split(',')
			sn_list_new = []
			for i in sn_list:
				if i[:3] == 'JAJ' or i[:2] == 'XY':
					sn_list_new.append(i)
				else:
					shiliutoshi_str = str(int(i,16))
					sn_list_new.append(shiliutoshi_str)


			#qs = JpICSN.objects.filter(sn__in=sn_list_new)
			#qs = JpICSN.objects.filter(sn__icontains=sn_list_new)
			#使用like语句获取列表中的所有值
			q = reduce(operator.and_, (Q(sn__contains=x) for x in sn_list_new))
			qs = JpICSN.objects.filter(q)




			for i in qs:
				jieguo={}
				jieguo['SN'] = i.sn
				jieguo['add_datetime'] = i.add_datetime
				if i.is_use == True:
					jieguo['is_use'] = u'已使用'
				else:jieguo['is_use'] = u'未被使用'
				jieguo['use_datetime'] = i.use_datetime
				jieguo['shenfenzhenghao'] = i.shenfenzhenghao[10:]
				jieguo_list.append(jieguo)




			return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))
	else:
		form = JP_shenfenbangdingchaxun_forms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))


def JP_tohtml(df,fafangorshouquan,mxorhuizong):
	df1 = df
	if fafangorshouquan == 'fafang':
		del df1['is_tushu_qichushu']
		del df1['shouquan']
		del df1['tushu_yingling_shuliang']
		del df1['tushu_shiling_shuliang']
		df_fill = df1.fillna(0)
		df_shaixuan = df_fill[(df1.dandugoumai_shuliang >0)|(df1.gouka >0)]
		#df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
		data_dic = {}
		if mxorhuizong == 'mx':
			df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
			data = df_shaixuan.groupby(['日期','驾校名称']).sum().to_html(classes="table table-condensed")
			data_dic['data'] = data
			sum_dandu = df_shaixuan['单独购买'].sum()
			sum_gouka = df_shaixuan['购卡'].sum()
			data_dic['sum_dandu'] = sum_dandu
			data_dic['sum_gouka'] = sum_gouka
		if mxorhuizong == 'jiaxiaoname':
			del df_shaixuan['riqi']
			data = df_shaixuan.groupby(['jiaxiaoname_str'],as_index = False).sum().to_dict('recodes')
			sum_dandu = df_shaixuan['dandugoumai_shuliang'].sum()
			sum_gouka = df_shaixuan['gouka'].sum()
			data_dic['jieguo'] = data
			data_dic['sum_dandu'] = sum_dandu
			data_dic['sum_gouka'] = sum_gouka
	if fafangorshouquan == 'shouquan':
		del df1['dandugoumai_shuliang']
		del df1['is_tushu_qichushu']
		del df1['gouka']
		del df1['tushu_yingling_shuliang']
		del df1['tushu_shiling_shuliang']
		df_fill = df1.fillna(0)
		df_shaixuan = df_fill[(df1.shouquan>0)]
		data_dic = {}
		if mxorhuizong == 'mx':
				df_shaixuan.columns=['驾校名称','日期','授权数量']
				data = df_shaixuan.groupby(['日期','驾校名称']).sum().to_html(classes="table table-condensed")
				data_dic['data'] = data
				sum_shouquan = df_shaixuan['授权数量'].sum()
				#sum_gouka = df_shaixuan['购卡'].sum()
				data_dic['sum_shouquan'] = sum_shouquan
				#data_dic['sum_gouka'] = sum_gouka
		if mxorhuizong == 'jiaxiaoname':
				del df_shaixuan['riqi']
				data = df_shaixuan.groupby(['jiaxiaoname_str'],as_index = False).sum().to_dict('recodes')
				sum_shouquan = df_shaixuan['shouquan'].sum()
				#sum_gouka = df_shaixuan['gouka'].sum()
				data_dic['jieguo'] = data
				data_dic['sum_shouquan'] = sum_shouquan
				#data_dic['sum_gouka'] = sum_gouka
	if fafangorshouquan == 'jiaocai':
		del df1['is_tushu_qichushu']
		del df1['dandugoumai_shuliang']
		del df1['gouka']
		del df1['shouquan']
		df_fill = df1.fillna(0)
		#df_fill['qianshu'] = df_fill['tushu_yingling_shuliang']-df['tushu_shiling_shuliang']
		df_shaixuan = df_fill[(df1.tushu_yingling_shuliang>0)|(df1.tushu_shiling_shuliang>0)]

		data_dic = {}
		if mxorhuizong == 'mx':

			df_shaixuan.columns=['驾校名称','日期','实领数量','应领数量']
			data = df_shaixuan.groupby(['日期','驾校名称']).sum().to_html(classes="table table-condensed")
			data_dic['data'] = data
			sum_tushu_yingling = df_shaixuan['应领数量'].sum()
			sum_tushu_shiling = df_shaixuan['实领数量'].sum()
			#sum_tushu_qianshu = df_shaixuan['欠书数量'].sum()
			#sum_gouka = df_shaixuan['购卡'].sum()
			data_dic['sum_tushu_yingling'] = sum_tushu_yingling
			data_dic['sum_tushu_shiling'] = sum_tushu_shiling
			#data_dic['sum_tushu_qianshu'] = sum_tushu_qianshu
			data_dic['sum_tushu_qianshu'] = sum_tushu_yingling - sum_tushu_shiling
			#data_dic['sum_gouka'] = sum_gouka
		if mxorhuizong == 'jiaxiaoname':
				df_fill['qianshu'] = df_fill['tushu_yingling_shuliang']-df_fill['tushu_shiling_shuliang']
				df_shaixuan = df_fill[(df_fill.tushu_yingling_shuliang>0)|(df_fill.tushu_shiling_shuliang>0)|(df_fill.qianshu>0)]
				del df_shaixuan['riqi']
				data = df_shaixuan.groupby(['jiaxiaoname_str'],as_index = False).sum().to_dict('recodes')
				sum_tushu_yingling = df_shaixuan['tushu_yingling_shuliang'].sum()
				sum_tushu_shiling = df_shaixuan['tushu_shiling_shuliang'].sum()
				sum_qianshu = df_shaixuan['qianshu'].sum()
				#sum_gouka = df_shaixuan['gouka'].sum()
				data_dic['jieguo'] = data
				data_dic['sum_tushu_yingling'] = sum_tushu_yingling
				data_dic['sum_tushu_shiling'] = sum_tushu_shiling
				data_dic['sum_qianshu'] = sum_qianshu
				#data_dic['sum_gouka'] = sum_gouka



	return data_dic

def JPexcel(df,fafangorshouquan,mxorhuizong,agve=None):
	temp_name = str(
	datetime.date.today().strftime("%Y%m%d") + str(random.randint(1, 10000)))
	#path = "/home/python/djcode/mysite/kucuntest/static/file/%s.xlsx" % temp_name
	#path = "/home/python/djcode/mysite/kucuntest/static/file/%s.xlsx" % temp_name
	path = settings.MEDIA_ROOT + "/file/%s.xls" % temp_name
	path_return = "/media/file/%s.xls" % temp_name
	if fafangorshouquan == 'fafang':
		#del df['shouquan']
		df_fill = df.fillna(0)
		del df_fill['shouquan']
		del df_fill['is_tushu_qichushu']
		del df_fill['tushu_shiling_shuliang']
		del df_fill['tushu_yingling_shuliang']
		df_shaixuan = df_fill[(df_fill.dandugoumai_shuliang >0)|(df_fill.gouka >0)]
		df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
		if mxorhuizong == 'mx':
			#df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
			#del df_shaixuan['shouquan']
			df_test = df_shaixuan.groupby(['日期','驾校名称']).sum()
			writer = pd.ExcelWriter(path, engine='openpyxl',date_format='mmm d yyyy')#使用openpyxl来输出中文
			df_test.to_excel(writer, sheet_name='Sheet1')
			workbook  = writer.book
			worksheet = writer.sheets['Sheet1']
			#worksheet.set_column('A:A', 20)
			writer.save()
			#canshu_list = [{'row':0,'col':1,'values':''},{'row':0,'col':2,'values':''},{'row':0,'col':3,'values':''},
			               #{'row':1,'col':0,'values':u'日期'},{'row':1,'col':1,'values':u'驾校名称'},
			               #{'row':1,'col':2,'values':u'单独购买'},{'row':1,'col':3,'values':u'购卡'}]
			#edit_excel(path,canshu_list)df
		if mxorhuizong == 'jiaxiaoname':
			df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
			#del df_shaixuan['riqi']
			df_shaixuan.groupby(['驾校名称']).sum().to_excel(path,engine='openpyxl',sheet_name='sheet1')
			#canshu_list = [{'row':0,'col':1,'values':''},{'row':0,'col':2,'values':''},{'row':1,'col':0,'values':u'驾校名称'},
			               #{'row':1,'col':1,'values':u'单独购买'},{'row':1,'col':2,'values':u'购卡'}]
			#edit_excel(path,canshu_list)

	if fafangorshouquan == 'shouquan':
		#del df['gouka']
		df_fill = df.fillna(0)
		del df_fill['gouka']
		del df_fill['dandugoumai_shuliang']
		del df_fill['tushu_yingling_shuliang']
		del df_fill['tushu_shiling_shuliang']
		del df_fill['is_tushu_qichushu']
		df_shaixuan = df_fill[(df_fill.shouquan >0)]
		#df_shaixuan.columns=['','购卡','驾校名称','日期']
		if mxorhuizong == 'mx':
			df_shaixuan.columns=['驾校名称','日期','授权数量']
			#del df_shaixuan['shouquan']
			df_test = df_shaixuan.groupby(['日期','驾校名称']).sum()
			writer = pd.ExcelWriter(path, engine='openpyxl',date_format='mmm d yyyy')#使用openpyxl来输出中文
			df_test.to_excel(writer, sheet_name='Sheet1')
			workbook  = writer.book
			worksheet = writer.sheets['Sheet1']
			#worksheet.set_column('A:A', 20)
			writer.save()
			#canshu_list = [{'row':0,'col':1,'values':''},{'row':0,'col':2,'values':''},{'row':0,'col':3,'values':''},
			               #{'row':1,'col':0,'values':u'日期'},{'row':1,'col':1,'values':u'驾校名称'},
			               #{'row':1,'col':2,'values':u'单独购买'},{'row':1,'col':3,'values':u'购卡'}]
			#edit_excel(path,canshu_list)
		if mxorhuizong == 'jiaxiaoname':
			df_shaixuan.columns=['驾校名称','日期','授权数量']
			#del df_shaixuan['riqi']
			df_shaixuan.groupby(['驾校名称']).sum().to_excel(path,engine='openpyxl',sheet_name='sheet1')
			#canshu_list = [{'row':0,'col':1,'values':''},{'row':0,'col':2,'values':''},{'row':1,'col':0,'values':u'驾校名称'},
			               #{'row':1,'col':1,'values':u'单独购买'},{'row':1,'col':2,'values':u'购卡'}]
			#edit_excel(path,canshu_list)
	if fafangorshouquan == 'jiaocai':
		#del df1['dandugoumai_shuliang']
		#del df1['gouka']
		#del df1['shouquan']
		df_fill = df.fillna(0)
		#df_shaixuan = df_fill[(df_fill.tushu_yingling_shuliang>0)|(df_fill.tushu_shiling_shuliang>0)]
		if mxorhuizong == 'mx':
			del df_fill['gouka']
			del df_fill['shouquan']
			del df_fill['dandugoumai_shuliang']
			del df_fill['is_tushu_qichushu']
			df_shaixuan = df_fill[(df_fill.tushu_yingling_shuliang>0)|(df_fill.tushu_shiling_shuliang>0)]
			df_shaixuan.columns=['驾校名称','日期','实领数量','应领数量']
			df_test = df_shaixuan.groupby(['日期','驾校名称']).sum()
			writer = pd.ExcelWriter(path, engine='openpyxl',date_format='mmm d yyyy')#使用openpyxl来输出中文
			df_test.to_excel(writer, sheet_name='Sheet1')
			writer.save()
		if mxorhuizong == 'jiaxiaoname':
			del df_fill['riqi']
			del df_fill['gouka']
			del df_fill['shouquan']
			del df_fill['dandugoumai_shuliang']
			df_shaixuan = df_fill[(df_fill.tushu_shiling_shuliang>0)|(df_fill.tushu_yingling_shuliang>0)]
			df_shaixuan_budaiqichu = df_shaixuan[(df_shaixuan.is_tushu_qichushu != True)]
			del df_shaixuan['is_tushu_qichushu']
			del df_shaixuan['tushu_yingling_shuliang']
			del df_shaixuan_budaiqichu['is_tushu_qichushu']
			del df_shaixuan_budaiqichu['tushu_shiling_shuliang']
			df_shaixuan.columns=['驾校名称','查询区间实际领取数量']
			df_shaixuan_budaiqichu.columns=['驾校名称','查询区间购买数量']
			df_shaixuan_gp = df_shaixuan.groupby(['驾校名称']).sum()
			df_shaixuan_budaiqichu_gp = df_shaixuan_budaiqichu.groupby(['驾校名称']).sum()
			if agve.get('riqi__gte'):
				jiezhiriqi = datetime.date.today()
			if agve.get('riqi__lte'):
				jiezhiriqi = agve.get('riqi__lte')
			if agve.get('riqi__range'):
				jiezhiriqi = agve.get('riqi__range')[1]
			df_zongji = pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False).filter(riqi__lte=jiezhiriqi).order_by('riqi').values(
				'jiaxiaoname_str','tushu_yingling_shuliang','tushu_shiling_shuliang','is_tushu_qichushu')))
			df_zongji_shaixuan = df_zongji.fillna(0)[(df_zongji.tushu_yingling_shuliang>0)|(df_zongji.tushu_shiling_shuliang>0)]
			df_zongji_shaixuan_budaiqichu = df_zongji_shaixuan[(df_zongji_shaixuan.is_tushu_qichushu != True)]
			del df_zongji_shaixuan['is_tushu_qichushu']
			del df_zongji_shaixuan['tushu_yingling_shuliang']
			del df_zongji_shaixuan_budaiqichu['is_tushu_qichushu']
			del df_zongji_shaixuan_budaiqichu['tushu_shiling_shuliang']
			df_zongji_shaixuan.columns = ['驾校名称','截止实际领取累计']
			df_zongji_shaixuan_budaiqichu.columns=['驾校名称','截止购买累计']
			df_zongji_shaixuan_gp = df_zongji_shaixuan.groupby(['驾校名称']).sum()
			df_zongji_shaixuan_budaiqichu_gp = df_zongji_shaixuan_budaiqichu.groupby(['驾校名称']).sum()
			df_zongji_join = df_zongji_shaixuan_gp.join(df_zongji_shaixuan_budaiqichu_gp)

			df_test1 = df_shaixuan_gp.join(df_shaixuan_budaiqichu_gp)
			df_test = df_zongji_join.join(df_test1)


			#df_fill['qianshu'] = df_fill['tushu_yingling_shuliang']-df_fill['tushu_shiling_shuliang']
			#df_shaixuan = df_fill[(df_fill.tushu_yingling_shuliang>0)|(df_fill.tushu_shiling_shuliang>0)|(df_fill.qianshu>0)]
			#df_shaixuan.columns=['驾校名称','实领数量','应领数量','欠书数量']
			#df_test = df_shaixuan.groupby(['驾校名称']).sum()
			writer = pd.ExcelWriter(path, engine='openpyxl',date_format='mmm d yyyy')#使用openpyxl来输出中文
			df_test.to_excel(writer, sheet_name='Sheet1')
			writer.save()

	return path_return

def edit_excel(path,canshu_list):#使用这个函数后，按日期的明细汇总表将无法设置A列为date格式，按驾校名称汇总的表格不受影响
	rb = open_workbook(path)
	wb = copy(rb)
	s = wb.get_sheet(0)
	for i in canshu_list:
		row = i.get('row')
		col = i.get('col')
		values = i.get('values')
		s.write(row,col,values)
	wb.save(path)

@permission_required('kucuntest.can_update')
def yingfukuandengji(request, jiaxiaoid):
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'应付款登记'
	is_tishi = True
	todayshuju = todayshuju_dic()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '注意！这里填写的是金额而不是数量！确认吗？'
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = JP_yingfukuan_dengji_froms(request.POST)
		if form.is_valid():
			yingfukuan_dengji =abs( form.cleaned_data['yingfukuan_dengji'])
			beizhu = form.cleaned_data['beizhu']
			riqi = datetime.date.today()
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p = JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,yingfukuan_dengji=yingfukuan_dengji,beizhu=beizhu,riqi=riqi,
			             user=caozuo_user)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_yingfukuan_dengji_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def yingfukuanshoufei(request, jiaxiaoid):
	if JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		return Http404
	global jiaxiaoidglobal
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaoid = int(jiaxiaoid)
	jiaxiaoidglobal = jiaxiaoid
	title = u'应付款收费'
	is_tishi = True
	todayshuju = todayshuju_dic()
	erbuyanzheng = True
	jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = '现在操作的驾校是：%s,驾校，确认吗？' % (jiaxiaoname)
	tishixinxi = '现在操作的是：%s驾校，请小心操作！' % (jiaxiaoname)
	#shijian = datetime.datetime.today()
	caozuo_user = request.user.username
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = JP_yingfukuan_shoufei_froms(request.POST)
		if form.is_valid():

			yingfukuan_shoufei =abs( form.cleaned_data['yingfukuan_shoufei'])
			fukuanfangshi =  form.cleaned_data['fukuanfangshi']
			beizhu = form.cleaned_data['beizhu']
			riqi = datetime.date.today()
			if fukuanfangshi == 'xianjin':
				fukuanfangshi_str_cn = '现金'
			if fukuanfangshi == 'pos':
				fukuanfangshi_str_cn = 'POS刷卡'
			if fukuanfangshi == 'yinhang':
				fukuanfangshi_str_cn = '银行存入'
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
			p =  JpMX_new(jiaxiaoname=jiaxiaoname, jiaxiaoname_str=jiaxiaoname_str,yingfukuan_shoufei=yingfukuan_shoufei,beizhu=beizhu,riqi=riqi,
						  jine=yingfukuan_shoufei,user=caozuo_user,fukuanfangshi=fukuanfangshi,fukuanfangshi_str_cn=fukuanfangshi_str_cn)
			p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/jp/caozuonew/%d/" % (jiaxiaoid)
			return HttpResponseRedirect(html)
	else:
		form = JP_yingfukuan_shoufei_froms()
	return render_to_response('jpaddnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def yingfukuanmx(request,jiaxiaoid):
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	title = u'应付款登记、收费明细'
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	anniuzu = True
	jiaxiaoid = int(jiaxiaoid)
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','yingfukuan_dengji','yingfukuan_shoufei','riqi','beizhu','fukuanfangshi_str_cn')
	#df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False,caozuo='zhanneixiaoshou').values('pinleiname_str',
	                                #'xiaoshou_danjia','danjia','xiaoshou_shuliang','xiaoshou_zongjia','riqi','beizhu')))
	dic_list = mx_chulikonghang(qs,'yingfukuan_dengji','yingfukuan_shoufei')
	jieguo = JP_YingFukuanmxtable(dic_list)
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

@permission_required('kucuntest.can_update')
def Jp_new_xushouyingfukuanmx(request):
	title = u'应付款需收费驾校列表'
	listleibie = 'datatable'
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	jieguo = JP_XushoufeiYingFukuanmxtable(def_df_dic('yingfukuan'))
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	return render_to_response('jplistnew.html', locals(), context_instance=RequestContext(request))

"""
@permission_required('kucuntest.can_update')
def month_test(request, year,month,change=None):
	year,month = int(year),int(month)
	if change in ('next','prev'):
		now,mdelta = datetime.date(year,month,15),datetime.timedelta(days=31)
		if change == 'next': mod = mdelta
		elif change == 'prev': mod = -mdelta
		year,month = (now+mod).timetuple()[:2]

	cal = calendar.Calendar()
	month_days = cal.itermonthdates(year,month)
	nyear,nmonth,nday = time.localtime()[:3]
	lst = [[]]
	week = 0
	current = False
	for day in month_days:
		if day:
			entries = "test"
			if day == nday and year == nyear and month == nmonth:
				current = True
		lst[week].append((day,entries,current))
		if len(lst[week]) == 7:
			lst.append([])
			week += 1

	return render_to_response('month.html', dict(year=year,month=month,
												 user=request.user,month_days=lst), context_instance=RequestContext(request))

"""
class ContestCalendar(HTMLCalendar):

	def __init__(self,pContestEvents):
		super(ContestCalendar,self).__init__()
		self.contest_events = self.group_by_day(pContestEvents)

	def formatday(self, day, weekday):
		if day != 0:
			cssclass = self.cssclasses[weekday]
			if datetime.date.today() == datetime.date(self.theyear,self.themonth,day):
				cssclass += 'today'
			if day in self.contest_events:
				cssclass += 'filled'
				body = []
				for contest in self.contest_events[day]:
					year_test = contest.riqi.year
					month_test = contest.riqi.month
					day_test = contest.riqi.day
					test_num = contest.id
					chengtao_shuliang = contest.ICkayoupan_shuliang
					dandu_shuliang = contest.ICka_shuliang
					yingyeshouru = contest.ICkayoupan_jine + contest.jiaocai_jine + contest.ICka_jine + contest.youpan_jine + contest.zhanneixiaoshou_jine
					#body.append('<a href="/jp/ribaobiao/%d/%d/%d/">' %(year_test,month_test,day_test))#链接格式
					body.append('<button id="test%d" class="btn-default btn-block"><p>成套销售：%d</p><p>单独销售：%d</p><p><strong></span><span style="color:#E53333;">营业收入：%d</strong></span></p></button>' %
								(test_num,chengtao_shuliang,dandu_shuliang,yingyeshouru))

					#body.append(str(contest.riqi)[0:10])
					#body.append('<p>成套销售:%d</p><p>单独销售:%d</p><p>营业收入:%d</p>' % (chengtao_shuliang,dandu_shuliang,yingyeshouru)) #显示内容


					body.append('</a><br>')
					#body.append("""<script>$('#test%d').on('click', function(){layer.open({type:2,title:"monthtest",shadeClose: true,shade:0.8,area:['380px', '90%'],content: '/ribaobiao/'});});</script>""" % test_num)

				return  self.day_cell(cssclass,'<div class="dayNumber">%d</div> %s' % (day, ''.join(body)))
			return self.day_cell(cssclass, '<div class="dayNumber">%d</div>' % day)
		return self.day_cell('noday','&nbsp;')

	def formatmonth(self, theyear, themonth, withyear=True):
		self.theyear, self.themonth = theyear, themonth
		return super(ContestCalendar,self).formatmonth(theyear, themonth)

	def group_by_day(self,pContestEvents):
		field = lambda contest: contest.riqi.day
		return dict(
			[(day,list(items)) for day, items in groupby(pContestEvents,field)]
		)

	def day_cell(self,cssclass,body):
		return '<td class="%s">%s</td>' % (cssclass, body)

def named_month(pMonthNumber):
	"""
    Return the name of the month, given the month number
    """
	named_month = datetime.date(1900, pMonthNumber, 1).strftime('%B')
	named_month_dic = {'September':u'九月',
					   'January':u'一月',
					   'February':u'二月',
					   'March':u'三月',
					   'April':u'四月',
					   'May':u'五月',
					   'June':u'六月',
					   'July':u'七月',
					   'August':u'八月',
					   'October':u'十月',
					   'November':u'十一月',
					   'December':u'十二月'}
	named_month_return = named_month_dic.get(named_month)
	return named_month_return

def home(request):
	"""
    Show calendar of events this month
    """
	lToday = datetime.datetime.now()
	return calendar(request, lToday.year, lToday.month)

@permission_required('kucuntest.can_delete')
def calendar(request, pYear, pMonth):
	"""
    Show calendar of events for specified month and year
    """
	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	jiaxiaolist = jiaxiaolist_test()
	todayshuju = todayshuju_dic()
	#验证是否存在今日报表，如果存在，则“生成报表”按钮不可用，“添加侯利鹏销售数”与“添加驾培销售金额”按钮启用
	if JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		shengchengbaobiaoanniu = False
		#tianjiashujuanniuzu = True

	else:
		shengchengbaobiaoanniu = True
		#tianjiashujuanniuzu = False

	if  JpMX_new.objects.filter(isdelete=False,riqi=datetime.date.today()).exists():
		shengchengbaobiaoanniukeyong = True
	else:
		shengchengbaobiaoanniukeyong = False


	lYear = int(pYear)
	lMonth = int(pMonth)
	if dateisTrue(lYear,lMonth) is not True:
		return HttpResponseNotFound
	if lYear==2000 and lMonth==1:
		lYear,lMonth = datetime.date.today().year,datetime.date.today().month
	lCalendarFromMonth = datetime.datetime(lYear, lMonth, 1)
	lCalendarToMonth = datetime.datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])
	lContestEvents = JpMX_ribaobiao.objects.filter(isdelete=False,riqi__gte=lCalendarFromMonth, riqi__lte=lCalendarToMonth)
	#lContestEvents = 'test'
	riqi_shuju_duiying = []
	for i in lContestEvents:
		id_tmp = i.id
		datetime_org = i.riqi
		year_tmp,month_tmp,day_tmp = datetime_org.year,datetime_org.month,datetime_org.day
		dict_test = {'id':id_tmp,'year':year_tmp,'month':month_tmp,'day':day_tmp}
		riqi_shuju_duiying.append(dict_test)


	lCalendar_org = ContestCalendar(lContestEvents).formatmonth(lYear, lMonth)
	lPreviousYear = lYear
	lPreviousMonth = lMonth - 1
	if lPreviousMonth == 0:
		lPreviousMonth = 12
		lPreviousYear = lYear - 1
	lNextYear = lYear
	lNextMonth = lMonth + 1
	if lNextMonth == 13:
		lNextMonth = 1
		lNextYear = lYear + 1
	lYearAfterThis = lYear + 1
	lYearBeforeThis = lYear - 1

	return render_to_response('month.html', {'Calendar':mark_safe(lCalendar_org),
                                                       'Month':lMonth,
                                                       'MonthName':named_month(lMonth),
                                                       'Year':lYear,
                                                       'PreviousMonth':lPreviousMonth,
                                                       'PreviousMonthName':named_month(lPreviousMonth),
                                                       'PreviousYear':lPreviousYear,
                                                       'NextMonth':lNextMonth,
                                                       'NextMonthName':named_month(lNextMonth),
                                                       'NextYear':lNextYear,
                                                       'YearBeforeThis':lYearBeforeThis,
                                                       'YearAfterThis':lYearAfterThis,
											 		   'riqi_shuju_duiying':riqi_shuju_duiying,
											 		   'title':u'月销售情况一览',
											 		   'yuling_shengyu_num':yuling_shengyu_num,
	                                                   'jiaxiaolist':jiaxiaolist,
	                                                   'todayshuju':todayshuju,
											           'shengchengbaobiaoanniu':shengchengbaobiaoanniu,
											 		'shengchengbaobiaoanniukeyong':shengchengbaobiaoanniukeyong,
											        'erbuyanzheng':True,
											        'erbuyanzhengneirong':u'生成今日报表后今日收款业务将无法继续办理，确认吗？'
                                                   })
def word_replace(text,replace_dict):#对字符串内容根据字典进行替换
	rc = re.compile(r"[A-za-z_]\w*")
	def translate(match):
		word = match.group(0)
		return replace_dict.get(word,word)
	return rc.sub(translate,text)

def findStr(string, subStr, findCnt):#查找字符串总字符第N次出现位置
	listStr = string.split(subStr,findCnt)
	if len(listStr) <= findCnt:
		return -1
	return len(string)-len(listStr[-1])-len(subStr)

@permission_required('kucuntest.can_update')
def JP_ribaobiao(request,year,month,day):
    #开始判断日期
    year,month,day = int(year),int(month),int(day)
    if dateisTrue(year,month,day) is not True:
        return HttpResponseNotFound
    dangqianriqi = datetime.date(year,month,day)
    qianyitian_houyitian_date = qianyitian_houyitian(dangqianriqi)#获取前一天后一天日期
    if qianyitian_houyitian_date is False:
        return HttpResponseNotFound
    if qianyitian_houyitian_date.get('qianyitian') is None:
        qianyitianxianshi = False
    else:
        qianyitianxianshi = True
        qianyitian_year , qianyitian_month,qianyitian_day = qianyitian_houyitian_date.get('qianyitian').year,\
															qianyitian_houyitian_date.get('qianyitian').month,\
															qianyitian_houyitian_date.get('qianyitian').day
    if qianyitian_houyitian_date.get('houyitian') is None:
        houyitianxianshi = False
    else:
        houyitianxianshi = True
        houyitian_year,houyitian_month,houyitian_day = qianyitian_houyitian_date.get('houyitian').year,\
													   qianyitian_houyitian_date.get('houyitian').month,\
													   qianyitian_houyitian_date.get('houyitian').day
    #日期判断结束
    riqi = datetime.date(year,month,day)
    today = datetime.date.today()
    if riqi == today:
        tianjiashujuanniu = True
    qs = JpMX_ribaobiao.objects.filter(riqi__lte=riqi,isdelete=False)
    sum_leiji = baobiaoshuju(qs)
    sum_leiji['sum_ICka_jine'] += (sum_leiji.get('sum_ICka_leiji_xiuzheng') + sum_leiji.get('sum_jiaolianka_jine'))
    if riqi >= datetime.date(2015,4,1):
        sum_leiji['sum_youpan_shuliang'] = sum_leiji.get('sum_youpan_shuliang') + 2642
        sum_leiji['sum_youpan_jine'] = sum_leiji.get('sum_youpan_jine') + 2642*60
        sum_leiji['sum_ICkayoupan_shuliang'] = sum_leiji.get('sum_ICkayoupan_shuliang') - 2642
        sum_leiji['sum_ICkayoupan_jine'] = sum_leiji.get('sum_ICkayoupan_jine') - 2642*60

    sum_year_qs = qs.filter(riqi__year=year).order_by('riqi')
    sum_year = baobiaoshuju(sum_year_qs)
    #判断日期,如果在2015年,年累计数据从累计数据中取数,如果大于20160101则从sum_year中进行计算
    if riqi >= datetime.date(2015,4,1) and riqi <= datetime.date(2015,12,31):
        sum_year['sum_youpan_shuliang'] = sum_leiji.get('sum_youpan_shuliang')
        sum_year['sum_youpan_jine'] = sum_leiji.get('sum_youpan_jine')
        sum_year['sum_ICkayoupan_shuliang'] = sum_leiji.get('sum_ICkayoupan_shuliang')
        sum_year['sum_ICkayoupan_jine'] = sum_leiji.get('sum_ICkayoupan_jine')
        sum_year['sum_ICka_shuliang_year'] = sum_leiji.get('sum_ICka_shuliang')
        sum_year['nianshouru_jiaolianka_jine'] = sum_leiji.get('sum_ICka_jine')
        sum_year['sum_jiaocai_shuliang'] = sum_leiji.get('sum_jiaocai_shuliang')
        sum_year['sum_jiaocai_jine'] = sum_leiji.get('sum_jiaocai_jine')
        sum_year['sum_zhanneixiaoshou_shuliang'] = sum_leiji.get('sum_zhanneixiaoshou_shuliang')
        sum_year['sum_zhanneixiaoshou_jine'] = sum_leiji.get('sum_zhanneixiaoshou_jine')
    if riqi >= datetime.date(2016,1,1):
        sum_year['nianshouru_jiaolianka_jine'] = sum_year.get('sum_ICka_jine') + sum_year.get('sum_jiaolianka_jine')
    sum_month_qs = qs.filter(riqi__month=month).filter(riqi__year=year).order_by('riqi')
    sum_month = baobiaoshuju(sum_month_qs)
    sum_month['yueshouru_jiaolianka_jine'] = sum_month.get('sum_ICka_jine') + sum_month.get('sum_jiaolianka_jine')
    #得到当月最后一个营业报表的日期
    month_last_day = list(sum_month_qs.values_list('riqi',flat=True))[-1]
    #对应报表中“杜丽霞销售”的金额（前两个月没有这个数据））
    jiaoliankaxiaoshou_jine = JpMX_ribaobiao.objects.get(isdelete=False,riqi=month_last_day).jiaolianka_jine
    #如果最后一天的报表中教练卡销售金额有数字，则显示出来，否则不显示
    if  jiaoliankaxiaoshou_jine != 0:
        jiaoliankaxiaoshouxianshi = True

    sum_day_qs = qs.filter(riqi=riqi)
    if sum_day_qs[0].zhanneixiaoshou_jine != 0 or sum_day_qs[0].zhanneixiaoshou_shuliang !=0:
        zhanneixiaoshouanniu = False
    else:
        zhanneixiaoshouanniu = True
    if sum_day_qs[0].jiaolianka_jine != 0:
        jiaoliankaanniu = False
    else:
        jiaoliankaanniu = True
    sum_day = baobiaoshuju(sum_day_qs)
    #当日营业金额总计
    sum_day_jine = sum_day.get('sum_ICka_jine')+sum_day.get('sum_jiaocai_jine')+sum_day.get('sum_ICkayoupan_jine')+\
				   sum_day.get('sum_youpan_jine')+sum_day.get('sum_zhanneixiaoshou_jine')
    #当月营业金额总计
    sum_month_jine = sum_month.get('yueshouru_jiaolianka_jine')+sum_month.get('sum_jiaocai_jine')+sum_month.get('sum_ICkayoupan_jine')+\
					 sum_month.get('sum_youpan_jine')+sum_month.get('sum_zhanneixiaoshou_jine')
    #累计营业金额总计
    sum_leiji_jine = sum_leiji.get('sum_ICka_jine')+sum_leiji.get('sum_jiaocai_jine')+sum_leiji.get('sum_ICkayoupan_jine')+\
					 sum_leiji.get('sum_youpan_jine')+sum_leiji.get('sum_zhanneixiaoshou_jine')
    sum_year_jine = sum_year.get('nianshouru_jiaolianka_jine')+sum_year.get('sum_jiaocai_jine')+sum_year.get('sum_ICkayoupan_jine')+\
					 sum_year.get('sum_youpan_jine')+sum_year.get('sum_zhanneixiaoshou_jine')
    #sum_dandu = df_shaixuan['单独购买'].sum()
    #df =  pd.DataFrame(list(JpMX_churuku.objects.filter(isdelete=False,caozuo='zhanneixiaoshou').values('pinleiname_str',
	                                #'xiaoshou_danjia','danjia','xiaoshou_shuliang','xiaoshou_zongjia','riqi','beizhu')))

    return render_to_response('jpribaobiao.html', locals(), context_instance=RequestContext(request))

def baobiaoshuju(qs):
	sum_dic = qs.aggregate(sum_youpan_shuliang=Sum('youpan_shuliang'),sum_youpan_jine=Sum('youpan_jine'),
								 sum_ICka_shuliang=Sum('ICka_shuliang'),sum_ICka_jine=Sum('ICka_jine'),
								 sum_jiaocai_shuliang=Sum('jiaocai_shuliang'),sum_jiaocai_jine=Sum('jiaocai_jine'),
								 sum_ICkayoupan_shuliang=Sum('ICkayoupan_shuliang'),sum_ICkayoupan_jine=Sum('ICkayoupan_jine'),
						   sum_jiaolianka_jine = Sum('jiaolianka_jine'),sum_ICka_leiji_xiuzheng=Sum('ICka_leiji_xiuzheng'),
						   sum_zhanneixiaoshou_shuliang=Sum('zhanneixiaoshou_shuliang'),sum_zhanneixiaoshou_jine=Sum('zhanneixiaoshou_jine'))
	return sum_dic

@permission_required('kucuntest.bangongyongpin')
def JP_shengchengribaobiao_all(request,year,month,day):
	user = request.user.username
	year,month,day=int(year),int(month),int(day)
	riqi = datetime.date(year,month,day)
	#df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False,riqi__gte=riqi).order_by('riqi').values('riqi','gouka','dandugoumai_shuliang','yuling_out'))).fillna(0)
	df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False,riqi=riqi).order_by('riqi').values('riqi','gouka','dandugoumai_shuliang','yuling_out','tushu_yingling_shuliang'))).fillna(0)
	df_shaixuan = df[(df.gouka>0)|(df.dandugoumai_shuliang>0)|(df.yuling_out>0)]
	df_dic = df_shaixuan.groupby(['riqi'],as_index=False).sum().to_dict('recodes')
	for i in df_dic:
		edit_day_time = datetime.datetime.now()
		riqi = i.get('riqi')
		ICkayoupan_shuliang = i.get('gouka')
		ICkayoupan_jine = ICkayoupan_shuliang*60
		youpan_shuliang = i.get('yuling_out')
		youpan_jine = youpan_shuliang*60
		ICka_shuliang = i.get('dandugoumai_shuliang')
		ICka_jine = ICka_shuliang*60
		jiaocai_shuliang = i.get('tushu_yingling_shuliang')
		jiaocai_jine = jiaocai_shuliang*40
		p = JpMX_ribaobiao(user=user,edit_day_time=edit_day_time,riqi=riqi,ICkayoupan_shuliang=ICkayoupan_shuliang,
						   ICkayoupan_jine=ICkayoupan_jine,youpan_shuliang=youpan_shuliang,youpan_jine=youpan_jine,
						   ICka_shuliang=ICka_shuliang,ICka_jine=ICka_jine,jiaocai_shuliang=jiaocai_shuliang,
						   jiaocai_jine=jiaocai_jine)
		p.save()
	return HttpResponseRedirect('/jp/yingyeyilan/2000/1/')

@permission_required('kucuntest.can_update')
def JP_shengchengribaobiao_today(request):
	datetime_today = datetime.date.today()
	qs_yingye = JpMX_new.objects.filter(isdelete=False,riqi=datetime_today)
	if len(qs_yingye) == 0:
		messages.add_message(request, messages.WARNING, '当日没有营业数据，无法生成营业报表')
		return HttpResponseRedirect('/jp/yingyeyilan/%d/%d/' % (datetime_today.year,datetime_today.month))
	year,month = datetime_today.year , datetime_today.month
	user = request.user.username
	riqi = datetime.date.today()
	qs_baobiao = JpMX_ribaobiao.objects.filter(riqi=riqi)
	if len(qs_baobiao) !=0:
		messages.add_message(request, messages.WARNING, '当日已经生成报表,不能重新生成!')
		return HttpResponseRedirect('/jp/yingyeyilan/%d/%d/' % (datetime_today.year, datetime_today.month))
	df =  pd.DataFrame(list(JpMX_new.objects.filter(isdelete=False,riqi=riqi).order_by('riqi').values('riqi','gouka','dandugoumai_shuliang','yuling_out','tushu_yingling_shuliang'))).fillna(0)
	df_shaixuan = df[(df.gouka>0)|(df.dandugoumai_shuliang>0)|(df.yuling_out>0)]
	df_dic = df_shaixuan.groupby(['riqi'],as_index=False).sum().to_dict('recodes')
	for i in df_dic:
		edit_day_time = datetime.datetime.now()
		riqi = i.get('riqi')
		ICkayoupan_shuliang = i.get('gouka')
		ICkayoupan_jine = ICkayoupan_shuliang*60
		youpan_shuliang = i.get('yuling_out')
		youpan_jine = youpan_shuliang*60
		ICka_shuliang = i.get('dandugoumai_shuliang')
		ICka_jine = ICka_shuliang*60
		jiaocai_shuliang = i.get('tushu_yingling_shuliang')
		jiaocai_jine = jiaocai_shuliang*40
		p = JpMX_ribaobiao(user=user,edit_day_time=edit_day_time,riqi=riqi,ICkayoupan_shuliang=ICkayoupan_shuliang,
						   ICkayoupan_jine=ICkayoupan_jine,youpan_shuliang=youpan_shuliang,youpan_jine=youpan_jine,
						   ICka_shuliang=ICka_shuliang,ICka_jine=ICka_jine,jiaocai_shuliang=jiaocai_shuliang,
						   jiaocai_jine=jiaocai_jine)
		p.save()
	return HttpResponseRedirect('/jp/yingyeyilan/%d/%d/' % (year,month))

def dateisTrue(year,month,day=None):
	if year in range(1900,2100):
		yearisTrue = True
	else:yearisTrue = False
	if month in range(1,13):
		monthisTrue = True
	else:monthisTrue = False
	if day is not None:
		if day in range(1,monthrange(year,month)[1]+1):
			dayisTrue = True
		else:dayisTrue = False
	else:dayisTrue = True
	if yearisTrue and monthisTrue and dayisTrue is True:
		return True
	else:
		return False



#测试图表输出
def test(request):
	#p = TEST_db(_youpan_shuliang=100)
	#p.save()
	name_list = ['Tokyo','New York','Berlin','London']
	val_list = [[7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, None],[-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5],
				[-0.9, 0.6, 3.5, 8.4, 16, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0],[3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]]
	jieguo_dict = []
	for i,j in enumerate(name_list):
		jieguo_dict.append({'name':name_list[i],'data':val_list[i]})
	jieguo_json = json.dumps(jieguo_dict)


	return render_to_response('Echartstest.html', locals(), context_instance=RequestContext(request))

def test1(request):

	yuling_shengyu_num = def_yuling_shengyu_num('yuling')
	yingfukuan_shengyu_num = def_yingfukuan_shengyu_num('yingfukuan')
	title = u'购卡、授权明细'
	#anniuzu = True
	jiaxiaoid =76
	listleibie = 'datatable'
	todayshuju = todayshuju_dic()
	jiaxiaolist = jiaxiaolist_test()
	if request.method == 'POST':
		form = JP_test_fuben_add(request.POST)
		if form.is_valid():
			haoduanqizhi = form.cleaned_data['haoduanqizhi']
			liebiao = fengehaoduan(haoduanqizhi)
			#for i in liebiao:
				#JpMX_ICSN.objects.create(sn=i,zhuangtai=u'登记',zhuangtai_str='dengji',dengji_riqi=today,dengji_user=user)



			#p = GongyingshangGL.objects.create(name=name, kaihuhang=kaihuhang, zhanghao=zhanghao, hanghao=hanghao, isedit=1)

			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			return HttpResponseRedirect('/jp/jinchikucun/')
	else:
		form = JP_test_fuben_add()
	#daohangleibie = 'name'
	#is_tishi = True
	#tishixinxi = u"本页面可以添加办公用品名称也可以根据办公用品分类进行查询并进行办公用品入库操作！"
	qs = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid,isdelete=False).values('id','jiaxiaoname_str','gouka','shouquan','riqi','beizhu','fukuanfangshi_str_cn','jine','haoduanqizhi')
	dic_list = mx_chulikonghang(qs,'gouka','shouquan')
	jieguo = JP_ShouQuanmxtable(dic_list)

	return render_to_response('test_fuben_add.html', locals(), context_instance=RequestContext(request))


"""
def test(request):
	return render_to_response('test1.html')
"""
def qianyitian_houyitian(datetime_def):
	riqishaixuan = {}
	riqi_list = list(JpMX_ribaobiao.objects.filter(isdelete=False,).order_by('riqi').values_list('riqi',flat=True))
	if datetime_def not in riqi_list:
		return False
	riqi_index = riqi_list.index(datetime_def)
	if  riqi_index==0:
		riqishaixuan['qianyitian'] = None
	else:
		riqishaixuan['qianyitian'] = riqi_list[riqi_index-1]
	if riqi_index==len(riqi_list)-1:
		riqishaixuan['houyitian'] = None
	else:
		riqishaixuan['houyitian'] = riqi_list[riqi_index+1]
	return riqishaixuan

def JP_tianjiazhanneixiaoshou(request):
	datetime_today = datetime.date.today()
	qs = JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime_today)
	if not qs.exists():
		return Http404
	if request.method == 'POST':
		form = JP_tianjiazhanneixiaoshou_forms(request.POST)
		if form.is_valid():

			zhanneixiaoshou_shuliang =abs( form.cleaned_data['zhanneixiaoshou_shuliang'])
			zhanneixiaoshou_jine =  abs(form.cleaned_data['zhanneixiaoshou_jine'])
			qs.update(zhanneixiaoshou_jine=zhanneixiaoshou_jine,zhanneixiaoshou_shuliang=zhanneixiaoshou_shuliang)
			#p.save()
			html = "/jp/ribaobiao/%d/%d/%d/" % (datetime_today.year,datetime_today.month,datetime_today.day)
			return HttpResponseRedirect(html)
	else:
		form = JP_tianjiazhanneixiaoshou_forms()
	return render_to_response('jpaddnew_motaikuang.html', locals(), context_instance=RequestContext(request))


def JP_tianjiajiaoliankashuju(request):
	datetime_today = datetime.date.today()
	qs = JpMX_ribaobiao.objects.filter(isdelete=False,riqi=datetime_today)
	if not qs.exists():
		return Http404
	if request.method == 'POST':
		form = JP_tianjiajiaoliankaxiaoshou_forms(request.POST)
		if form.is_valid():

			jiaoliankaxiaoshou_jine =abs( form.cleaned_data['jiaolianka_jine'])
			qs.update(jiaolianka_jine=jiaoliankaxiaoshou_jine)
			#p.save()
			html = "/jp/ribaobiao/%d/%d/%d/" % (datetime_today.year,datetime_today.month,datetime_today.day)
			return HttpResponseRedirect(html)
	else:
		form = JP_tianjiajiaoliankaxiaoshou_forms()
	return render_to_response('jpaddnew_motaikuang.html', locals(), context_instance=RequestContext(request))

#完成对加密信息的解密类
"""
class JieMi(object):
    #将传如的qs_val（字典）中的加密字符串转换为对应原始字符串或者数字或者浮点数返回
    #传入的qs_dic必须使用list()进行转换
    def __init__(self,qs_dic):#只接list受已经转换为字典的qs

        self.qs_dic = qs_dic
    def __str__(self):
        return self.qs_dic

    def jiegouyanzheng(self):
        if  not isinstance(self.qs,list):
            print 'qs_dic is not list'
        else:
            if not isinstance(self.qs[0],dict):
                print 'qs_dic is not dict'
            print 'tongguoyanzheng'
"""







