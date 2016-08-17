# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from calendar import HTMLCalendar,monthrange
#from django.utils.translation import ugettext_lazy as _
from dateutil.relativedelta import relativedelta
from forms import *
from models import *
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404,HttpRequest, HttpResponse,JsonResponse
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
from xlwt import Workbook
from xlutils.copy import copy
import xlsxwriter

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
import numpy as np
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import ImageFile as PILImageFile
import re
import pymssql

def tijiao(request):
	#global jiaxiaoidglobal
	#jiaxiaoid = int(jiaxiaoid)
	#jiaxiaoidglobal = jiaxiaoid
	title = u'短信提交'
	is_tishi = True
	erbuyanzheng = True
	#jiaxiaoname = JixiaoInfo.objects.get(id=jiaxiaoid)
	#jiaxiaoname_str = jiaxiaoname.name
	erbuyanzhengneirong = u'确认提交吗？'
	tishixinxi = u'现在操作的是：%s，请小心操作！' % (title)
	#caozuo_user = request.user.username
	#JpMX_new_id = JpMX_new.objects.filter(jiaxiaoname=jiaxiaoid) #TODO:使用函数提供各种数据
	if request.method == 'POST':
		form = DX_tijiao_form(request.POST)
		if form.is_valid():
			chepai_qian = form.cleaned_data['chepai_qian']
			chepai_hou = form.cleaned_data['chepai_hou']
			paizhaohao_num = form.cleaned_data['paizhaohao'].upper()
			dianhua = form.cleaned_data['dianhua']
			paizhaohao = chepai_qian+chepai_hou+paizhaohao_num
			if DX_CarInfo.objects.filter(paizhaohao=paizhaohao).exists():
				qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao)
				qs.update(jiancecishu=qs[0].jiancecishu+1,editriqi=datetime.datetime.now(),dianhua=dianhua)
			else:
			#pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
				p = DX_CarInfo(dianhua=dianhua,paizhaohao=paizhaohao,chepai_hou=chepai_hou,chepai_qian=chepai_qian)
				p.save()
			messages.add_message(request, messages.SUCCESS, '数据添加成功！')
			html = "/dx/dxtijiao/"
			return HttpResponseRedirect(html)
	else:
		form = DX_tijiao_form()
	return render_to_response('dxaddnew.html', locals(), context_instance=RequestContext(request))

def fasong_houtai(request):
    now = datetime.datetime.now()
    qs = DX_FaSongMX.objects.filter(is_delete=False)
    for i in qs:
        q = i.id
        DX_FaSongMX.objects.filter(id=q).update(fasong_datetime=now)
    html = "/dx/dxtijiao/"
    return HttpResponseRedirect(html)

def webservice_yincheyuan(requset):
    qs = DX_Yincheyuan.objects.filter(isdelete=False)
    yincheyuan_list = [a.name for a in qs]
    return JsonResponse({'name_list':yincheyuan_list})




def next_riqi_def(dengjiriqi,paizhaoleibie_id,yingyunleibie_id):
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
        else:
            next_year = today_year+1
            next_riqi_str = str(next_year)+dengjiriqi_month
            return next_riqi_str

def Dx_zonghechaxun_fasong(request):
    title = u'综合查询测试'
    download = False
    listleibie = 'datatable'
    addleibie = 'churuku'


    if request.method == 'POST':
        form = DX_search_fasong_forms(request.POST)
        if form.is_valid():
            start_time_input = form.cleaned_data['start_time']
            if start_time_input is not None:
                start_time_year,start_time_month,start_time_day = start_time_input.year,start_time_input.month,start_time_input.day
                start_time = datetime.datetime(start_time_year,start_time_month,start_time_day,0,0,0)
            else:
                start_time = datetime.datetime(1900,1,1,0,0,0)

            end_time_input = form.cleaned_data['end_time']
            if  end_time_input is not None:
                end_time_year,end_time_month,end_time_day = end_time_input.year,end_time_input.month,end_time_input.day
                end_time = datetime.datetime(end_time_year,end_time_month,end_time_day,23,59,59)
            else:
                end_time = datetime.datetime(2030,12,31,23,59,59)

            shengchengwenjian = form.cleaned_data['shengchengwenjian']
            kwargs = {}
            agve = {}


            if start_time or end_time is not None:
                if start_time is not None and end_time is None:
                    agve['tijiao_datetime__gte']=start_time
                if end_time is not None:
                    agve['tijiao_datetime__lte']=end_time
            if start_time and end_time is not None:
                agve['tijiao_datetime__range'] = (start_time,end_time)


            #df =  pd.DataFrame(list(DX_FaSongMX.objects.filter(isdelete=False).filter(**agve).order_by('riqi').values(
				#'paizhaohao','tijiao_datetime','tijiao_neirong','fasong_datetime','dianhuahao','yincheyuan_name','is_fasong')))

            #df_copy = pd.DataFrame(list(DX_FaSongMX.objects.filter(isdelete=False).filter(**agve).order_by('riqi').values(
				#'paizhaohao','tijiao_datetime','tijiao_neirong','fasong_datetime','dianhuahao','yincheyuan_name','is_fasong')))
            #jieguo = JP_zonghechaxun_jiaocai_huizong_table(jieguo_dic.get('jieguo'))#输出datatable
            qs = DX_FaSongMX.objects.filter(is_delete=False).filter(**agve).values('id','tijiao_datetime','paizhaohao','dianhuahao',
                                        'tijiao_neirong','yincheyuan_name','is_fasong')
            df_copy = pd.DataFrame(list(DX_FaSongMX.objects.filter(is_delete=False).filter(**agve).order_by('tijiao_datetime').values(
				'tijiao_datetime','paizhaohao','dianhuahao','tijiao_neirong','yincheyuan_name','is_fasong','fasong_datetime',
                'fanhuizhi','fanhuixinxi')))
            dic_list=[]

            for i in qs:
                i['tijiao_neirong'] = i.get('tijiao_neirong')[:20]
                if i.get('is_fasong') == True:
                    i['is_fasong'] = u'是'
                else:
                    i['is_fasong'] = u'否'
                dic_list.append(i)

            jieguo = DX_Fasongmxtable(dic_list)
            #jieguo = DX_Fasongmxtable(qs)






            if shengchengwenjian == 'yes':
                path = JPexcel(df_copy)#输出文件路径

            return render_to_response('dxlistnew.html', locals(), context_instance=RequestContext(request))
    else:
            form = DX_search_fasong_forms()
    return render_to_response('dxaddnew.html', locals(), context_instance=RequestContext(request))




def JPexcel(df):
    temp_name = str(
    datetime.date.today().strftime("%Y%m%d") + str(random.randint(1, 10000)))
    path = settings.MEDIA_ROOT + "/file/%s.xls" % temp_name
    path_return = "/media/file/%s.xls" % temp_name
    #del df['shouquan']

    df.columns=['车户电话','接口返回信息','接口返回值','发送时间','发送状态','车牌号','提交日期','提交内容','引车员姓名']
    #df_shaixuan.columns=['单独购买','购卡','驾校名称','日期']
    #del df_shaixuan['shouquan']

    writer = pd.ExcelWriter(path, engine='openpyxl',date_format='mmm d yyyy')#使用openpyxl来输出中文
    df.to_excel(writer, sheet_name='Sheet1')
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    #worksheet.set_column('A:A', 20)
    writer.save()
    return path_return


def Dx_zonghechaxun_carinfo(request):
    title = u'车辆信息查询'
    download = False
    listleibie = 'datatable'
    addleibie = 'churuku'
    #查询首字母同时满足多个条件的情况
    filterList = ['H','K']
    query = Q()
    for i in filterList:
        query = query|Q(cheliangleibie_id__startswith=i)
    qs = DX_Tongbu.objects.filter(query)



    if request.method == 'POST':
        form = DX_search_carinfo_forms(request.POST)
        """
        if form.is_valid():


            cheliang_leixing = form.cleaned_data['cheliangleixing']
            if not cheliang_leixing == None:
        """

















        return render_to_response('test1.html', locals(), context_instance=RequestContext(request))
    else:
            form = DX_search_carinfo_forms()
    return render_to_response('dxaddnew.html', locals(), context_instance=RequestContext(request))

def webservice_weiqi_chaxun(requset):
    if requset.method == 'POST':

        jieshou_json = json.loads(requset.body)
        #f = open('/home/www/djcode/mysite/duanxin/test.json','r+')
        #jieshou_json = json.load(f)
        chepaiqian = jieshou_json.get('chepaiqian')
        chepaihou = jieshou_json.get('chepaihou')
        chepaihao = jieshou_json.get('chepaihao')
        paizhaohao = chepaiqian+chepaihou+chepaihao

        #paizhaohao = u'\u8499AS7193'
        #result = {'zhuangtai':'Success','fanhui_msg':'chenggong'}
        #return JsonResponse(result)
        conn1 = pymssql.connect('172.18.130.50', 'sa', 'svrcomputer', 'hbjcdb')
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT COUNT (*) FROM carinfo WHERE Car_CPH=%s',paizhaohao)
        qs_num1 = cursor1.fetchall()[0][0]
        if qs_num1 == 1:
            result = {'zhuangtai':'Error','fanhui_msg':u'该车信息已存在于环保数据库！'}
            return JsonResponse(result)
        conn1.close()


        conn = pymssql.connect('172.18.130.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
        #conn = pymssql.connect('192.168.0.42', 'sa', 'svrcomputer', 'NewGaJck_TB')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM carinfo WHERE CPH=%s',paizhaohao)
        qs_num = cursor.fetchall()[0][0]
        if not isinstance(qs_num,int):
            result = {'zhuangtai':'Error','fanhui_msg':u'查询出现错误，请检查'}
            return JsonResponse(result)

        if qs_num >1:
            result = {'zhuangtai':'Error','fanhui_msg':u'查询到多于1台的车辆'}
            #result = {'zhuangtai':'Error','fanhui_msg':u'duoyu1tai'}
        elif  qs_num == 0:
            result = {'zhuangtai':'Error','fanhui_msg':u'没有查询到该车辆'}
            #result = {'zhuangtai':'Error','fanhui_msg':u'meiyougaiche'}


        elif qs_num == 1:
            result = {'zhuangtai':'Success','fanhui_msg':u'查询成功开始执行按键指令'}
            #result = {'zhuangtai':'Error','fanhui_msg':u'zhengque'}
            cursor = conn.cursor(as_dict=True)
            cursor.execute('SELECT * FROM carinfo WHERE CPH=%s',paizhaohao)
            for i in cursor:
                result['chepaihao'] = i.get('CPH')
                result['DW'] = i.get('DW')
                result['ChangPH'] = i.get('ChangPH')
                result['XingHao'] = i.get('XingHao')
                result['DPH'] = i.get('DPH')
                result['FDJH'] = i.get('FDJH')
                #将日期格式转换为'20150101'
                datetime_dic = i.get('DJDate')
                datetime_list = str(datetime_dic)[:10].split('-')
                datetime_str = ''.join(datetime_list)
                result['DJDate'] = datetime_str
                result['CLLBXID'] = i.get('CLLBXID')
                
        
        conn.close()
        return JsonResponse(result)
    else:
        result = {'zhuangtai':'Error','fanhui_msg':u'出现错误500'}
        return JsonResponse(result)


def webservice_tijiao(requset):
    if requset.method == 'POST':
        jieshou_json = json.loads(requset.body)
        chepaiqian = jieshou_json.get('chepaiqian')
        chepaihou = jieshou_json.get('chepaihou')
        chepaihao = jieshou_json.get('chepaihao')
        dianhuahao = jieshou_json.get('dianhuahao')
        yincheyuan_name = jieshou_json.get('yincheyuan')
        yincheyuan_dianhua = DX_Yincheyuan.objects.get(name=yincheyuan_name).dianhua
        paizhaohao = chepaiqian+chepaihou+chepaihao
        today_year,today_month,today_day = datetime.date.today().year,datetime.date.today().month,datetime.date.today().day
        qs_today_cheliang = DX_FaSongMX.objects.filter(tijiao_datetime__year=today_year,tijiao_datetime__month=today_month,
                                                       tijiao_datetime__day=today_day).filter(paizhaohao=paizhaohao)
        if len(qs_today_cheliang)>0 :
            cheliang_tijiaodatetime = qs_today_cheliang[0].tijiao_datetime
            shijiacha = (datetime.datetime.now() - cheliang_tijiaodatetime).seconds
            if shijiacha<600:
                fanhui_msg = u'车辆提交间隔不得小于10分钟!'
                result = {'zhuangtai':'Success','fanhui_msg':fanhui_msg}
                return JsonResponse(result)
        if DX_CarInfo.objects.filter(paizhaohao=paizhaohao).exists():
            qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao)
            if qs[0].iswanzheng == True:
                qs.update(jiancecishu=qs[0].jiancecishu+1,editriqi=datetime.datetime.now(),dianhua=dianhuahao,
                          next_riqi=next_riqi_def(qs[0].dengjiriqi,qs[0].paizhaoleibie_id,qs[0].yingyunleibie_id))
            else:
                qs.update(editriqi=datetime.datetime.now(),dianhua=dianhuahao)
        else:
     #pinleitype = PinleiGL.objects.select_related('pinleitype').get(pinleiname=pinleiname).pinleitype
            p = DX_CarInfo(dianhua=dianhuahao,paizhaohao=paizhaohao,chepai_hou=chepaihou,chepai_qian=chepaiqian)
            p.save()
        q = DX_FaSongMX(paizhaohao=paizhaohao,tijiao_datetime=datetime.datetime.now(),dianhuahao=dianhuahao,
                        yincheyuan_name=yincheyuan_name,yincheyuan_dianhua=yincheyuan_dianhua)
        q.save()
        fanhui_msg = u'%s提交成功，引车员为：%s' % (paizhaohao,yincheyuan_name)
        result = {'zhuangtai':'Success','fanhui_msg':fanhui_msg}
        return JsonResponse(result)
    else:
        result = {'zhuangtai': 'Error', 'fanhui_msg': u'出现错误500'}
        return JsonResponse(result)



def webservice_yewubaijie(requset):#业务办结存入数据库
    if requset.method == 'POST':
        #try:
            #jieshou_json = json.loads(requset.body)
        #except ValueError:


        str1 = requset.body
        start_index = str1.find('{')
        end_index = str1.find('}') +1
        jieshou_json = json.loads(str1[start_index:end_index])

        #jieshou_json = json.loads(requset.body)
        paizhaohao = jieshou_json.get('paizhaohao')
        paizhaoleibie_id = jieshou_json.get('paizhaoleibie_id')
        xingshizheng_baocun = DX_Xingshizheng(paizhaohao=paizhaohao,cheliangleibie_id=paizhaoleibie_id,
                                              chuanjianriqi=datetime.datetime.now())
        xingshizheng_baocun.save()
        print 'cunchu'

        car_info_chaxun = DX_CarInfo.objects.filter(paizhaohao__contains=paizhaohao,paizhaoleibie_id__contains=paizhaoleibie_id)

        if car_info_chaxun.exists():
            q = DX_FaSongMX(paizhaohao=paizhaohao, tijiao_datetime=datetime.datetime.now(), dianhuahao=car_info_chaxun[0].dianhua,
                            yincheyuan_name=u'空', yincheyuan_dianhua=u'空', fasongjiekou='yewu_banjie',is_delete=False)
            q.save()

            qs = DX_Xingshizheng.objects.filter(paizhaohao=paizhaohao,cheliangleibie_id=paizhaoleibie_id).order_by('-chuanjianriqi')[0].id

            qs_update = DX_Xingshizheng.objects.filter(id=qs)

            qs_update.update(fasong_time=datetime.datetime.now())








        result = {'zhuangtai':'Success','zhuangtai_str':u'成功'}
        # return JsonResponse(result)



        print 'wancheng'
        return JsonResponse(result)
    else:
        result = {'zhuangtai': 'Error', 'fanhui_msg': u'出现错误500'}
        return JsonResponse(result)