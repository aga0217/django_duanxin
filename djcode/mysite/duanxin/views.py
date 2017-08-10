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
import time
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
import pyodbc
import requests
from xpinyin import Pinyin
from jiami_jiemi_test import AESCipher
ip_yunxu = ['192.168.0.179','192.168.0.1','15.29.32.56','15.29.32.55','15.29.32.49']
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
        conn1 = pymssql.connect('15.29.32.61', 'sa', 'svrcomputer', 'hbjcdb')
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT COUNT (*) FROM carinfo WHERE Car_CPH=%s',paizhaohao)
        qs_num1 = cursor1.fetchall()[0][0]
        if qs_num1 == 1:
            result = {'zhuangtai':'Error','fanhui_msg':u'该车信息已存在于环保数据库！'}
            return JsonResponse(result)
        conn1.close()


        conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
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
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            str1 = requset.body
            start_index = str1.find('{')
            end_index = str1.find('}') +1
            jieshou_json = json.loads(str1[start_index:end_index])
        #jieshou_json = json.loads(requset.body)
        paizhaohao = jieshou_json.get('paizhaohao').replace(' ','')
        paizhaoleibie_id = jieshou_json.get('paizhaoleibie_id').replace(' ','')
        zhuangtai = jieshou_json.get('zhuangtai')
        try:
            NetxTime = ''.join(jieshou_json.get('nexttime').replace(' ','').split('-'))[:6]#  将2016-10-31这样的格式转化为201610
        except:
            return HttpResponse(u'0%没有获取到车辆的下次检验日期，请重新运行。')

        if zhuangtai == 'del':#t处理状态变更时的数据删除
            qs = DX_Xingshizheng.objects.filter(is_del=False,paizhaohao=paizhaohao, cheliangleibie_id=paizhaoleibie_id).order_by(
                '-chuanjianriqi')[0].id

            qs_update = DX_Xingshizheng.objects.filter(id=qs)

            qs_update.update(is_del=True)
            return HttpResponse(u'1%成功')

        panduan = shijianchuli(paizhaohao,paizhaoleibie_id)
        if panduan.get('zhuangtai') == 'Success':
        #conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
        #cursor = conn.cursor()
        #cursor.execute('SELECT COUNT (*) FROM ufee WHERE CPH=%s AND PZLBID=%s',(paizhaohao,paizhaoleibie_id))
        #qs_num = cursor.fetchall()[0][0]
        #if not isinstance(qs_num,int):
            #result = {'zhuangtai':'Error','zhuangtai_str':u'查询出现错误，请检查'}
            #conn.close()
            #return JsonResponse(result)
        #elif  qs_num == 0:
            #result = {'zhuangtai':'Error','zhuangtai_str':u'没有查询到该车辆对应收费信息,请核对后重新录入!'}
            #conn.close()
            #return JsonResponse(result)
        #else:
            xingshizheng_baocun = DX_Xingshizheng(paizhaohao=paizhaohao,cheliangleibie_id=paizhaoleibie_id,
                                              chuanjianriqi=datetime.datetime.now(),nexttime=NetxTime)
            xingshizheng_baocun.save()
            car_info_chaxun = DX_CarInfo.objects.filter(paizhaohao__contains=paizhaohao,paizhaoleibie_id__contains=paizhaoleibie_id)
            if car_info_chaxun.exists():
                q = DX_FaSongMX(paizhaohao=paizhaohao, tijiao_datetime=datetime.datetime.now(), dianhuahao=car_info_chaxun[0].dianhua,
                            yincheyuan_name=u'空', yincheyuan_dianhua=u'空', fasongjiekou='yewu_banjie',is_delete=False)
                q.save()

                qs = DX_Xingshizheng.objects.filter(is_del=False,paizhaohao=paizhaohao,cheliangleibie_id=paizhaoleibie_id).order_by('-chuanjianriqi')[0].id

                qs_update = DX_Xingshizheng.objects.filter(id=qs)

                qs_update.update(fasong_time=datetime.datetime.now(),is_fasong=True)
                qs_update_carinfo = DX_CarInfo.objects.filter(id = car_info_chaxun[0].id)
                qs_update_carinfo.update(next_riqi=NetxTime,editriqi=datetime.datetime.now())
            #result = {'zhuangtai':'Success','zhuangtai_str':u'成功'}
            return HttpResponse(panduan.get('zhuangtai_str'))
        else:
            #return JsonResponse(panduan,safe=True)
            #return  HttpResponse(json.dumps(panduan), content_type='application/json')
            return HttpResponse(panduan.get('zhuangtai_str'))

    else:
        result = {'zhuangtai': 'Error', 'zhuangtai_str': u'出现错误500'}
        return JsonResponse(result)


def shijianchuli(paizhaohao,paizhaoleibie_id):
    now = datetime.datetime.now()
    #paizhaohao = u'蒙A18398'
    #paizhaoleibie_id = '13'
    jianyanleibie = u'在用机动车检验'
    jieguo = []
    jieguo_shuchu = []
    shijiancha_yueding = datetime.timedelta(days=91)
    #处理重复录入的车辆信息
    qs = DX_Xingshizheng.objects.filter(paizhaohao__contains=paizhaohao,cheliangleibie_id__contains=paizhaoleibie_id).order_by('-chuanjianriqi')
    if len(qs) != 0:
        chuangjianriqi = qs[0].chuanjianriqi
        shijiancha = now - chuangjianriqi
        if shijiancha < datetime.timedelta(days=15):
            return {'zhuangtai':'Error','zhuangtai_str':u'该车15天内已经录入请检查！'}
    conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM ufee WHERE CPH=%s AND PZLBID=%s AND JCLB=%s',
                   (paizhaohao, paizhaoleibie_id, jianyanleibie))

    for i in cursor:
        jieguo.append(i.get('SKRQ'))
    conn.close()
    if len(jieguo) == 0:
        return {'zhuangtai':'Error','zhuangtai_str':u'0%该车辆没有收费记录（年检）,请检查输入的车牌号和牌照类别'}
    else:
        for q in jieguo:
            shijiancha = now - q
            if shijiancha < shijiancha_yueding:
                jieguo_shuchu.append(shijiancha)
        if len(jieguo_shuchu) == 0:
            return {'zhuangtai':'Error','zhuangtai_str':u'0%该车辆收费日期（年检）与今天相差90天,请注意检查'}
        else:
            return {'zhuangtai':'Success','zhuangtai_str':u'1%成功'}

def Dx_shoufeizhizheng_chaxun(request):
    #jiaxiaolist = jiaxiaolist_test()
    #todayshuju = todayshuju_dic()
    title = u'收费制证对比查询'
    download = False
    listleibie = 'datatable'
    addleibie = 'churuku'
    #jieyu = ''
    fangshi = ''

    if request.method == 'POST':
        form = DX_chaxun_duibi_forms(request.POST)
        if form.is_valid():
            chaxun_or_duibi = form.cleaned_data['chaxun_or_duibi']
            #mxorhuizong = form.cleaned_data['mxorhuizong']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            shuchufangshi = form.cleaned_data['shuchufangshi']
            shengchengwenjian = form.cleaned_data['shengchengwenjian']
            kwargs = {}
            agve = {}
            path = None
            download = None

            is_sum = False

            if start_time or end_time is not None:
                if start_time is not None and end_time is None:
                    agve['chuanjianriqi__gte']=start_time
                    if end_time is not None:
                         agve['chuanjianriqi__lte']=end_time
            if start_time and end_time is not None:
                agve['chuanjianriqi__range'] = (start_time,end_time)
            if chaxun_or_duibi == 'shoufei':

                data = shoufei_chaxun_sql(start_time,end_time)
                #pd_dic = pd.DataFrame(data).to_dict('recode')
                for i in data:
                    i['PZLBID'] = cheliangleixingInt_cheliaangleixing_UTF8(i.get('PZLBID'))
                jieguo = DX_ShouFei_chaxun_table(data)

                #jieguo = DX_ShouFei_chaxun_table(data)
            elif chaxun_or_duibi == 'zhizheng':
                data =  pd.DataFrame(list(DX_Xingshizheng.objects.filter(is_del=False).filter(**agve).order_by('chuanjianriqi').values('paizhaohao',
                               'cheliangleibie_id','chuanjianriqi'))).to_dict('recode')
                for i in data:
                    i['cheliangleibie_id'] = cheliangleixingInt_cheliaangleixing_UTF8(i.get('cheliangleibie_id'))
                jieguo = DX_ZhiZheng_chaxun_table(data)
                #print data #输出的字典中时间为时间戳,需转换
            elif chaxun_or_duibi == 'shoufei_zhizheng_duibi':
                shoufei_list = shoufei_chaxun_sql(start_time,end_time)
                shoufei_df = pd.DataFrame(shoufei_list)
                zhizheng_list = list(DX_Xingshizheng.objects.filter(is_del=False).filter(**agve).order_by('chuanjianriqi').values('paizhaohao',
                                'cheliangleibie_id','chuanjianriqi'))
                zhizheng_list_pd = []
                for i in zhizheng_list:
                    list_dic = {}
                    list_dic['CPH'] = i.get('paizhaohao')
                    list_dic['PZLBID'] = i.get('cheliangleibie_id')
                    list_dic['ZZRQ'] = i.get('chuanjianriqi')
                    zhizheng_list_pd.append(list_dic)
                zhizheng_df = pd.DataFrame(zhizheng_list_pd)
                jieguo_df = pd.merge(shoufei_df, zhizheng_df, on=['CPH', 'PZLBID'], how='outer')
                if shuchufangshi == 'all':
                    listleibie = 'shoufei_zhizheng_duibi'
                    jieguo_fanhui = chuliduibijieguo_shuchu(jieguo_df,shuchufangshi)
                    jieguo = jieguo_fanhui[0]
                    yichang = jieguo_fanhui[1]
                    zongshu = jieguo_fanhui[2]
                    if shengchengwenjian == 'yes':
                        download = True
                        path = jieguo_to_excel(jieguo,chaxun_or_duibi)
                if shuchufangshi == 'chayi':
                    listleibie = 'shoufei_zhizheng_duibi'
                    jieguo_fanhui = chuliduibijieguo_shuchu(jieguo_df,shuchufangshi)
                    jieguo = jieguo_fanhui[0]
                    yichang = jieguo_fanhui[1]
                    zongshu = jieguo_fanhui[2]
                    if shengchengwenjian == 'yes':
                        download = True
                        path = jieguo_to_excel(jieguo,chaxun_or_duibi)








            """
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
            """

            #if shengchengwenjian == 'yes':
                #path = JPexcel(df_copy,fafangorshouquan,mxorhuizong,agve)

            return render_to_response('bglist.html', locals(), context_instance=RequestContext(request))
    else:
        form = DX_chaxun_duibi_forms()
    return render_to_response('bgadd.html', locals(), context_instance=RequestContext(request))

def shoufei_chaxun_sql(start_time,end_time):#查询区间收费信息
    conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
    cursor = conn.cursor(as_dict=True)
    if start_time is None:
        start_time = datetime.date(1900,1,1)
    if end_time is None:
        end_time = datetime.date.today() + datetime.timedelta(days = 1)
    else:
        end_time = end_time + datetime.timedelta(days = 1)
    #print start_time,end_time
    jianyanleibie = u'在用机动车检验'
    cursor.execute('SELECT * FROM ufee WHERE SKRQ>%s AND SKRQ<%s AND JCLB=%s', (start_time,end_time, jianyanleibie))
    shoufeiliebiao = []
    for i in cursor:
        dic = {}
        dic['CPH'] = i.get('CPH')
        dic['PZLBID'] = i.get('PZLBID')
        dic['SKRQ'] = i.get('SKRQ')
        shoufeiliebiao.append(dic)
    conn.close()
    return shoufeiliebiao
def shoufei_cheliang_chaxun_sql(CPH,PZLBID):#查询车辆收费信息
    conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
    cursor = conn.cursor(as_dict=True)
    jianyanleibie = u'在用机动车检验'
    cursor.execute('SELECT * FROM ufee WHERE CPH=%s AND PZLBID=%s AND JCLB=%s', (CPH, PZLBID, jianyanleibie))
    shoufeileibiao = []
    for i in cursor:
        shoufeileibiao.append(i.get('SKRQ'))
    conn.close()
    if len(shoufeileibiao) == 0:
        return u'车辆没有找到收费记录'
    else:
        return datetime.datetime.strftime(shoufeileibiao[-1], "%Y-%m-%d %H:%M:%S")


def chuliduibijieguo_yanse_xuhao(jieguo_pd):#为结果添加序号和颜色代码
    jieguo_return = []
    xuhao = 0
    yichang = 0
    for i in jieguo_pd:
        xuhao = xuhao+1
        dic = {}
        dic['CPH'] = i.get('CPH')
        dic['PZLBID'] = cheliangleixingInt_cheliaangleixing_UTF8(i.get('PZLBID'))
        if i.get('SKRQ') == datetime.datetime(1970,1,1 ,0,0,0,0):
            dic['SKRQ'] = shoufei_cheliang_chaxun_sql(i.get('CPH'),i.get('PZLBID'))
            yichang = yichang +1
        else:
            dic['SKRQ'] = datetime.datetime.strftime(i.get('SKRQ'),"%Y-%m-%d %H:%M:%S")
        if i.get('ZZRQ') == datetime.datetime(1970,1,1,0,0,0,0):
            dic['ZZRQ'] = ''
            yichang = yichang +1
        else:
            dic['ZZRQ'] = datetime.datetime.strftime(i.get('ZZRQ'),"%Y-%m-%d %H:%M:%S")
        dic['xuhao'] = xuhao
        if i.get('SKRQ') == datetime.datetime(1970,1,1 ,0,0,0,0):
            dic['yanse'] = 'red'
        if i.get('ZZRQ') == datetime.datetime(1970,1,1 ,0,0,0,0):
            dic['yanse'] = 'blue'
        jieguo_return.append(dic)
    zongshu = len(jieguo_return)
    return jieguo_return,yichang,zongshu


def chuliduibijieguo_shuchu(jieguo_pd,shuchufangshi):#控制结果输出方式
    if shuchufangshi == 'all':
        jieguo = chuliduibijieguo_yanse_xuhao(jieguo_pd.fillna(0).to_dict('recode'))
        return jieguo
    if shuchufangshi == 'chayi':
        jieguo_shaixuan = jieguo_pd[jieguo_pd.SKRQ.isnull()|jieguo_pd.ZZRQ.isnull()]
        jieguo = chuliduibijieguo_yanse_xuhao(jieguo_shaixuan.fillna(0).to_dict('recode'))
        return jieguo

def cheliangleixingInt_cheliaangleixing_UTF8(cheliangleixingInt):

    dic = {'02':u'小型汽车','01':u'大型汽车','03':u'使馆汽车','04':u'领馆汽车','05':u'境外汽车',
           '15':u'挂车','13':u'农用运输车','14':u'拖拉机','17':u'教练摩托车','23':u'警用汽车',
           '07':u'两、三轮摩托','06':u'外籍汽车','08':u'轻便摩托车','16':u'教练汽车','24':u'警用摩托车'}

    return dic[cheliangleixingInt]
#
def jieguo_to_excel(jieguo_df,chaxun_or_duibi):
    temp_name = str(
    datetime.date.today().strftime("%Y%m%d") + str(random.randint(1, 10000)))
    path = settings.MEDIA_ROOT + "/file/%s.xls" % temp_name
    path_return = "/media/file/%s.xls" % temp_name
    print path_return
    if chaxun_or_duibi == 'shoufei_zhizheng_duibi':
        df = pd.DataFrame(jieguo_df)
        del df['xuhao']
        del df['yanse']
        df.columns = ['车牌号', '牌照类别', '收款日期','制证日期']
        writer = pd.ExcelWriter(path, engine='openpyxl', date_format='mmm d yyyy')
        df.to_excel(writer, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        # worksheet.set_column('A:A', 20)
        writer.save()
    return path_return

def webservice_weiqishofuei_chaxun(requset):
    if requset.method == 'POST':
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            str1 = requset.body
            start_index = str1.find('{')
            end_index = str1.find('}') +1
            jieshou_json = json.loads(str1[start_index:end_index])
        #jieshou_json = json.loads(requset.body)
        shijiancha_yueding = datetime.timedelta(days=91)
        now = datetime.datetime.now()
        paizhaohao = jieshou_json.get('paizhaohao')
        paizhaoleibie_id = jieshou_json.get('paizhaoleibie_id')
        paichuliebiao = ['01','02','03','04','05','06','16','23','13']#列表中为需要检测尾气的车型
        if paizhaoleibie_id not in paichuliebiao:#判断类型是否在排除列表中
            result = {'is_tixing':'no'}
            return JsonResponse(result)


        conn = pymssql.connect('15.29.32.3', 'sa', 'svrcomputer', 'NewGaJck_TB')
        cursor = conn.cursor(as_dict=True)
        cursor.execute('SELECT SYXZID,CLLBXID FROM carinfo WHERE AutoID = (SELECT MAX(AutoID) FROM carinfo WHERE CPH = %s AND PZLBID = %s)',
                        (paizhaohao, paizhaoleibie_id))
        cheliangxinxi = {}
        try:
            chaxunjieguo = cursor.fetchall()[0]
            cheliangxinxi['yingyunleibie_id'] = chaxunjieguo.get('SYXZID')
            cheliangxinxi['cheliangleibie_id'] = chaxunjieguo.get('CLLBXID')

        except:
            pass
        conn.close()
        if len(cheliangxinxi) == 0:
            return JsonResponse({'is_tixing':'yes','tixingxinxi':u'没有找到车辆的年检信息，是否继续？'})

        if cheliangxinxi.get('yingyunleibie_id') == 'D':
            result = {'is_tixing': 'no'}  # 界面是否需要提醒没有尾气收费
            return JsonResponse(result)
        if cheliangxinxi.get('cheliangleibie_id') == 'N11':
            result = {'is_tixing': 'no'}
            return JsonResponse(result)
        #查询尾气收费
        jieguo = {}
        conn1 = pymssql.connect('15.29.32.61', 'sa', 'svrcomputer', 'hbjcdb')
        cursor1 = conn1.cursor(as_dict=True)
        cursor1.execute('SELECT SKRQ,SKJE FROM ufee WHERE FPHM = (SELECT MAX(FPHM) FROM ufee WHERE CPH = %s )',
                        (paizhaohao))
        for i in cursor1.fetchall():
            try:
                jieguo['SKRQ'] = i.get('SKRQ')
                jieguo['SKJE'] = i.get('SKJE')
            except:
                pass
        conn1.close()
        if len(jieguo) == 0:
            return JsonResponse({'is_tixing': 'yes','tixingxinxi':u'没有找到该车的尾气收费信息，是否继续？'})
        if now - jieguo.get('SKRQ') < shijiancha_yueding and jieguo.get('SKJE') > 0 :
            return JsonResponse({'is_tixing':'no'})
        else:
            return JsonResponse({'is_tixing':'yes','tixingxinxi':u'该车90天内没有缴费记录或缴费金额小于0（尾气），是否继续？'})
    else:
        result = {'zhuangtai': 'Error', 'fanhui_msg': u'出现错误500'}
        return JsonResponse(result)


def webservice_shoufei(requset):#收费webserices
    if requset.method == 'POST':
        #验证IP地址
        try:
            ip =requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong':False,'cuowu':u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong':False,'cuowu':u'%s访问地址不匹配02' % ip})
        #处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong':False,'cuowu':u'数据格式不对'})
        jieshou_json_str = str(jieshou_json)
        jieshou_datetime = datetime.datetime.now()
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到检测站编号'})
        cph = jieshou_json.get('cph')
        if cph is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到牌照号'})
        else:
            cph = cph.replace(' ','')
        pzlb_str = jieshou_json.get('pzlb_str')
        if pzlb_str is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到牌照类别'})
        else:
            pzlb_str = pzlb_str.replace(' ','')

        pzlb_id = jieshou_json.get('pzlb')
        if pzlb_id is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到牌照类别ID'})
        czry_user = jieshou_json.get('czry')#操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ','')

        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong':False,'cuowo':u'没有找到操作人员密码'})
        czry = DX_ShouFei_UserName.objects.get(username=czry_user).userxingming
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        chezhudh = jieshou_json.get('chezhudh')
        if chezhudh is None:
            chezhudh = ''
        else:
            chezhudh = chezhudh.replace(' ','')
        fkfs = jieshou_json.get('fkfs')
        if fkfs is None:
            return JsonResponse({'chengong':False,'cuowu':u'没有找到付款方式'})
        fkfs_id = ''
        if fkfs == u'现金':
            fkfs_id='01'
        elif fkfs == u'微信支付':
            fkfs_id = '02'
        elif fkfs == u'支付宝支付':
            fkfs_id = '03'
        elif fkfs == u'预付费卡':
            fkfs_id = '04'
        elif fkfs == u'银行卡':
            fkfs_id = '05'
        data = jieshou_json.get('data')
        if data is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到操作数据'})
        t={}
        if jczid == '01':
            t = ShouFeiChuLi_1(jczid,cph,pzlb_id,pzlb_str,chezhudh,czry,czry_user,fkfs_id,fkfs,data)
        if t.get('chenggong') == True:
            return JsonResponse({'chenggong':True,'data':True})
        elif t.get('chenggong') != True:
            return JsonResponse({'chenggong': False,'cuowu':u'插入数据时出现错误'})

    else:
        result = {'chenggong': False, 'cuowu': u'出现错误500'}
        return JsonResponse(result)

def ShuaXin(requset):
    if requset.method == 'POST':
        #验证IP地址
        try:
            ip =requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong':False,'cuowu':u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong':False,'cuowu':u'%s访问地址不匹配02' % ip})
        #处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong':False,'cuowu':u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')#操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ','')
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong':False,'cuowo':u'没有找到操作人员密码'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        # 返回刷新结果及分收款方式统计结果
        qs = list(DX_ShouFei.objects.filter(skr_username=czry_user, jczid=jczid,
                                            is_jiezhang=False).order_by('-skrq').values('id', 'paizhaohao',
                                                                                        'cheliangleibie_str',
                                                                                        'jyxm', 'jylb', 'skje', 'skrq',
                                                                                        'skr', 'jiezhangriqi',
                                                                                        'fapiao_qiri',
                                                                                        'zhifufangshi_str',
                                                                                        'zhifufangshi_zimu',
                                                                                        'is_kefu'))
        # 分组计算总和并返回字典
        if not qs:
            return JsonResponse({'chenggong': True, 'data': {'qs': None, 'groupsum': None}})
        QsGroupSum = pd.DataFrame(qs).groupby(['zhifufangshi_zimu'], as_index=False).sum().to_dict('recodes')
        return JsonResponse({'chenggong':True,'data':{'qs': qs, 'groupsum': QsGroupSum}})
    else:
        result = {'chenggong': False, 'cuowu': u'出现错误500'}
        return JsonResponse(result)

def BiaoJiKaipiao(requset):
    if requset.method == 'POST':
        #验证IP地址
        try:
            ip =requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong':False,'cuowu':u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong':False,'cuowu':u'%s访问地址不匹配02' % ip})
        #处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong':False,'cuowu':u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')#操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ','')
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong':False,'cuowo':u'没有找到操作人员密码'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        user_str = yanzheng.get('user_str')
        id_list = jieshou_json.get('id_list')
        if id_list == None:
            return JsonResponse({'chenggong':False,'cuowu':u'没有找到ID列表'})
        chenggong_list = []
        shibai_list = []
        for i in id_list:
            qs = DX_ShouFei.objects.filter(id=i)
            if not qs.exists():
                shibai_list.append(u'不存在')
            else:
                if qs[0].is_kaifapiao == True:
                    shibai_list.append(qs[0].paizhaohao)
                else:
                    chenggong_list.append(qs[0].paizhaohao)
                    qs.update(is_kaifapiao=True,bjr=user_str,bjr_username=czry_user,fapiao_qiri=datetime.datetime.now())
        return JsonResponse({'chenggong':True,'data':{'chenggong_list':chenggong_list,
                                                     'shibai_list':shibai_list}})
    else:
        return JsonResponse({'chenggong':False,'cuowu':'500'})

def VerifRePay(requset):
        if requset.method == 'POST':
            # 验证IP地址
            try:
                ip = requset.META['REMOTE_ADDR']
            except:
                return JsonResponse({'chenggong': False, 'cuowu': u'IP地址不匹配'})
            if ip not in ip_yunxu:
                return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
            # 处理json
            try:
                jieshou_json = json.loads(requset.body)
            except ValueError:
                return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
            jczid = jieshou_json.get('jczid')
            if jczid is None:
                return JsonResponse({'chenggong': False, 'cuowu': u'没有找到检测站编号'})
            czry_user = jieshou_json.get('czry')  # 操作人员用户名
            if czry_user is None:
                return JsonResponse({'chenggong': False, 'cuowu': u'没有找到操作人员用户名'})
            else:
                czry_user = czry_user.replace(' ', '')
            czry_pass = jieshou_json.get('czry_pass')
            if czry_pass is None:
                return JsonResponse({'chenggong': False, 'cuowo': u'没有找到操作人员密码'})
            jylb_str = jieshou_json.get('jylb_str')
            if jylb_str is None:
                return JsonResponse({'chenggong':False,'cuowu':u'没有找到检验类别字符串'})
            cph = jieshou_json.get('cph')
            if cph == None:
                return JsonResponse({'chenggong':False,'cuowu':u'没有找到车牌号'})
            cheliangleixingint = jieshou_json.get('cheliangleixingint')
            if cheliangleixingint == None:
                return JsonResponse({'chenggong':False,'cuowu':u'没有找到车辆类型'})
            yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user, czry_pass)
            if yanzheng.get('denglu') != True:
                return JsonResponse({'chenggong': False, 'cuowu': yanzheng.get('cuowu')})
            qs = DX_ShouFei.objects.filter(jczid=jczid,paizhaohao=cph,cheliangleibie_id=cheliangleixingint,jylb=jylb_str)
            if not qs.exists():
                return JsonResponse({'chenggong':True,'data':{}})
            skrq = qs.latest('id').skrq
            shijiancha = datetime.timedelta(days=60)
            now = datetime.datetime.now()
            if now - skrq < shijiancha:
                return JsonResponse({'chenggong':True,'data':{'skrq':skrq}})
            else:
                return JsonResponse({'chenggong':True,'data':{}})
        else:
            return JsonResponse({'denglu':False,'cuowu':500})

def Search(requset):
    if requset.method == 'POST':
        # 验证IP地址
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')  # 操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ', '')
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到操作人员密码'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        cph = jieshou_json.get('cph')
        shoufeixiangmu = jieshou_json.get('shoufeixiangmu')
        kwargs = {}
        if cph != None:

            kwargs['paizhaohao__contains'] = cph
        if shoufeixiangmu != None:
            kwargs['jyxm'] = shoufeixiangmu
        qs = list(DX_ShouFei.objects.filter(**kwargs).order_by('-skrq').values('id', 'paizhaohao',
                                                                                        'cheliangleibie_str',
                                                                                        'jyxm', 'jylb', 'skje', 'skrq',
                                                                                        'skr', 'jiezhangriqi',
                                                                                        'fapiao_qiri',
                                                                                        'zhifufangshi_str',
                                                                                        'zhifufangshi_zimu',
                                                                                        'is_kefu'))
        if len(qs) ==0:
            return JsonResponse({'chenggong': True, 'data': {'qs': None}})
        else:
            return JsonResponse({'chenggong': True, 'data': {'qs': qs}})
    else:
        return JsonResponse({'chenggong': False, 'cuowu':'500'})

def searchtell(requset):
    if requset.method == 'POST':
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')  # 操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到操作人员用户名'})
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到操作人员密码'})
        paizhaohao = jieshou_json.get('cph')
        if paizhaohao == None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到车牌号'})
        cheliangleibie_id = jieshou_json.get('cheliangleixingint')
        if cheliangleibie_id == None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到车辆类型'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        qs = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id=cheliangleibie_id)
        if not qs:
            return JsonResponse({'chenggong': True, 'data':{'dianhua':None}})
        else:
            dianhua = AESCipher().decrypt(qs[0].dianhua)
            return JsonResponse({'chenggong': True, 'data':{'dianhua':dianhua}})



def JieZhangYulan(requset):#结账预览
    if requset.method == 'POST':
        # 验证IP地址
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')  # 操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ', '')
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到操作人员密码'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user,czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong':False,'cuowu':yanzheng.get('cuowu')})
        skr_username_str = yanzheng.get('user_str')
        jiesuanxiangmu = jieshou_json.get('jiesuanxiangmu')
        if jiesuanxiangmu == None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到结算项目'})
        kwargs = {}
        if jiesuanxiangmu == 'anjian':
            kwargs['jyxm__in'] = ['anjian','qita']
            jiesuanxiangmu = u'安检'
        if jiesuanxiangmu == 'weiqi':
            kwargs['jyxm'] = 'weiqi'
            jiesuanxiangmu = u'尾气'
        jiezhangriqi = jieshou_json.get('jiezhangriqi')
        print jiezhangriqi
        shuju = []
        if jiezhangriqi == None:
            shuju = DX_ShouFei.objects.filter(is_jiezhang=False).filter(skr_username=czry_user,
                                                                 jczid=jczid).filter(**kwargs).order_by('skrq')
        else:
            date_list = jiezhangriqi.split('-')
            year, month, day = int(date_list[0]), int(date_list[1]), int(date_list[2])
            shuju = DX_ShouFei.objects.filter(jiezhangriqi__year=year,jiezhangriqi__month=month,jiezhangriqi__day=day).\
                filter(skr_username=czry_user,jczid=jczid).filter(**kwargs).order_by('skrq')
        if not shuju:
            return HttpResponse('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN""http://www.w3.org/TR/html4/loose.dtd"><html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style>
    @page {
        margin: 1cm 1cm 1cm 1cm;
        padding: 0;}
    @font-face {font-family: simsun;src: url(c:\windows\fonts\simsun.ttc);}body{font-family: simsun}

</style>
</head>
<body>
<div align="center">
	<span style="font-size:24px;">没有需要结账的了，再收点去吧</span>
</div></body></html>''')
        endtime_str = shuju.latest('id').skrq
        starttime_str = shuju.earliest('id').skrq
        zhibiaodatetime = datetime.datetime.now()
        sum_jine=sum(shuju.values_list('skje',flat=True))
        df1 = pd.DataFrame(list(shuju.values('cheliangleibie_str','jylb','zhifufangshi_str','skje','is_kefu')))
        df2 = pd.DataFrame(list(shuju.values('cheliangleibie_str','jylb','zhifufangshi_str','skje')))
        df1.columns = ['车辆类别','数量','检验类别','单价','支付方式']
        tabledata_count = df1.groupby(['支付方式','单价','车辆类别','检验类别'],as_index=True).count().to_html()
        sum_zhifufangshi = df2.groupby(['zhifufangshi_str'],as_index=False).sum().to_dict('recodes')
        print sum_zhifufangshi
        #for i in dictolist:
            #cont_zhifufangshi.append({'zhifufangshi_str':i,'count':dictolist.get(i)})



        #sum_zhifufangshi = df1.groupby(['支付方式'],as_index=False).sum().to_dict('recodes')
        #print sum_zhifufangshi
        #sum_jylb = df1.groupby(['jylb'],as_index=False).sum().to_dict('recodes')
        #sum_cheliangleibie_str = df1.groupby(['cheliangleibie_str'],as_index=False).sum().to_dict('recodes')
        #df2 = pd.DataFrame(list(shuju.values('cheliangleibie_id', 'jylb', 'zhifufangshi_zimu'))).to_dict('recode')
        #tabledata_jine = df1.groupby(['支付方式','车辆类别','检验类别'],as_index=True).sum().to_html(classes="table table-condensed")#as_index=TRUE可以在输出的html中合并单元格
        #df1 = df1.rename(columns={'金额': '数量'})
        #df2 = pd.DataFrame(list(shuju.values('cheliangleibie_id','jylb_pinyin','zhifufangshi_zimu','skje')))
        #tabledata_shuliang = df1.groupby(['支付方式','车辆类别','检验类别'],as_index=True).count().to_html(classes="table table-condensed")

        #df2 =
        #print df2
        """
        cont_zhifufangshi = []
        dictolist = df1['zhifufangshi_str'].value_counts().to_dict()
        for i in dictolist:
            cont_zhifufangshi.append({'zhifufangshi_str':i,'count':dictolist.get(i)})
        cont_jylb = []
        dictolist = df1['jylb'].value_counts().to_dict()
        for i in dictolist:
            cont_jylb.append({'jylb':i,'count':dictolist.get(i)})
        cont_cheliangleibie_str = []
        dictolist = df1['cheliangleibie_str'].value_counts().to_dict()
        for i in dictolist:
            cont_cheliangleibie_str.append({'cheliangleibie_str':i,'count':dictolist.get(i)})


        #cont_cheliangleibie_str = df2.groupby(['jylb'],as_index=False).count().to_dict('recodes')
        #print cont_cheliangleibie_str
        """



        return render_to_response('jiesuandan.html', locals(), context_instance=RequestContext(requset))
    else:
        return JsonResponse({'chenggong':False,'cuowu':500})

def JieZhang(requset):#结账
    if requset.method == 'POST':
        # 验证IP地址
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'IP地址不匹配'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        jczid = jieshou_json.get('jczid')
        if jczid is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到检测站编号'})
        czry_user = jieshou_json.get('czry')  # 操作人员用户名
        if czry_user is None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到操作人员用户名'})
        else:
            czry_user = czry_user.replace(' ', '')
        czry_pass = jieshou_json.get('czry_pass')
        if czry_pass is None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到操作人员密码'})
        yanzheng = DX_ShouFei_UserName().UserDengLu(czry_user, czry_pass)
        if yanzheng.get('denglu') != True:
            return JsonResponse({'chenggong': False, 'cuowu': yanzheng.get('cuowu')})
        skr_username_str = yanzheng.get('user_str')
        jiesuanxiangmu = jieshou_json.get('jiesuanxiangmu')
        if jiesuanxiangmu == None:
            return JsonResponse({'chenggong': False, 'cuowo': u'没有找到结算项目'})
        kwargs = {}
        if jiesuanxiangmu == 'anjian':
            kwargs['jyxm__in'] = ['anjian','qita']
        if jiesuanxiangmu == 'weiqi':
            kwargs['jyxm'] = 'weiqi'
        shuju = DX_ShouFei.objects.filter(is_jiezhang=False).filter(skr_username=czry_user,
                                                                 jczid=jczid).filter(**kwargs).order_by('skrq')
        shuju.update(is_jiezhang=True,jiezhangriqi=datetime.datetime.now())
        return JsonResponse({'chenggong':True,'data':{'jiezhang':True}})
    else:
        return JsonResponse({'chenggong':False,'cuowu':'500'})

def tuikuan(requset):
    if requset.method == 'POST':
            # 验证IP地址
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'访问地址不匹配01'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        user = jieshou_json.get('czry')
        if user == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有用户名'})
        pws = jieshou_json.get('czry_pass')
        if pws == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有密码'})
        id_list = jieshou_json['id_list']
        if id_list == None or len(id_list) != 1:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到列表'})
        tuikuan_chuli = DX_ShouFei().tuikuan(user,pws,int(id_list[0]))
        if tuikuan_chuli.get('chenggong') != True:
            return JsonResponse({'chenggong': False, 'cuowu': tuikuan_chuli.get('cuowu')})
            #jczid,cph,pzlb_int,pzlb_str,chezhudh,czry,czry_user,fkfs_id,fkfs,data,is_tuikuan = False,bjr = None,bjr_username=None
        data_fahui = tuikuan_chuli.get('data')
        if datetime == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'没有找到返回字典'})
        jczid = data_fahui.get('jczid')
        cph = data_fahui.get('cph')
        pzlb_int = data_fahui.get('pzlb_int')
        pzlb_str = data_fahui.get('pzlb_str')
        chezhudh = data_fahui.get('chezhudh')
        czry = data_fahui.get('czry')
        czry_user = data_fahui.get('czry_user')
        fkfs_id = data_fahui.get('fkfs_id')
        fkfs = data_fahui.get('fkfs')
        data = data_fahui.get('data')
        is_tuikuan = data_fahui.get('is_tuikuan')
        bjr = data_fahui.get('bjr')
        bjr_username = data_fahui.get('bjr_username')
        tuikuan_riqi = datetime.datetime.now()
        shujuchuli = ShouFeiChuLi_1(jczid,cph,pzlb_int,pzlb_str,chezhudh,czry,czry_user,fkfs_id,fkfs,data,
                                        is_tuikuan,bjr,bjr_username,tuikuan_riqi)
        if shujuchuli.get('chenggong') == True:
            return JsonResponse({'chenggong': True,'data':{'chenggong':True}})
        else:
            return JsonResponse({'chenggong': False,'cuowu':u'发生了一些错误'})
    else:
        return JsonResponse({'chenggong': False, 'cuowu': u'500'})







def PrintBill(requset,id):#单独打印票据
    try:
        qs = DX_ShouFei.objects.get(id = id)
    except:
        return Http404
    fphm = qs.dyid
    skrq = str(qs.skrq)[:23]
    cph = qs.paizhaohao
    jyxm = qs.jyxm
    if jyxm == 'anjian':
        jyxm = u'安检检测收费'
    elif jyxm == 'weiqi':
        jyxm = u'尾气检测收费'
    elif jyxm == 'qita':
        jyxm = u'其他检测项目'
    cheliangleibie_str = qs.cheliangleibie_str
    skje = qs.skje
    jylb = qs.jylb
    skr = qs.skr


    return render_to_response('dandudyin.html', locals(), context_instance=RequestContext(requset))


def ShouFeiDengLu(requset):
    if requset.method == 'POST':
        #验证IP地址
        try:
            ip =requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'dengliu':False,'cuowu':u'访问地址不匹配01'})

        if ip not in ip_yunxu:
            return JsonResponse({'denglu':False,'cuowu':u'%s访问地址不匹配02' % ip})
        #处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'denglu':False,'cuowu':u'数据格式不对'})
        skr_username = jieshou_json['skr_username']
        skr_password = jieshou_json['password']
        yanzheng = DX_ShouFei_UserName().UserDengLu(skr_username,skr_password)
        if yanzheng.get('denglu') == True:
            return JsonResponse({'denglu':True,'username':yanzheng.get('username'),
                                 'user_str':yanzheng.get('user_str'),'is_tuikuan':yanzheng.get('is_tuikuan')})
        else:
            return JsonResponse({'denglu':False,'cuowu':yanzheng.get('cuowu')})

def ShouFeiXiuGaiMiMa(requset):
    if requset.method == 'POST':
        # 验证IP地址
        try:
            ip = requset.META['REMOTE_ADDR']
        except:
            return JsonResponse({'chenggong': False, 'cuowu': u'访问地址不匹配01'})
        if ip not in ip_yunxu:
            return JsonResponse({'chenggong': False, 'cuowu': u'%s访问地址不匹配02' % ip})
        # 处理json
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return JsonResponse({'chenggong': False, 'cuowu': u'数据格式不对'})
        skr_username = jieshou_json.get('skr_username')
        if skr_username == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'收款人字段为空'})
        yuanshimima = jieshou_json.get('yuanshimima')
        if yuanshimima == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'原始密码字段为空'})
        mimayanzheng = MiMaYanZheng(yuanshimima)
        if mimayanzheng != True:
            return JsonResponse({'chenggong': False, 'cuowu': u'原始密码没有通过MiMaYanZheng'})
        xinmima = jieshou_json.get('xinmima')
        if xinmima == None:
            return JsonResponse({'chenggong': False, 'cuowu': u'新密码字段为空'})
        mimayanzheng = MiMaYanZheng(xinmima)
        if mimayanzheng != True:
            return JsonResponse({'chenggong': False, 'cuowu': u'新密码没有通过MiMaYanZheng'})
        yanzheng = DX_ShouFei_UserName().XiuGaiMiMa(skr_username,yuanshimima,xinmima)
        if yanzheng.get('chenggong') == True:
            return JsonResponse({'chenggong': True})
        else:
            return JsonResponse({'chenggong': False, 'cuowu': yanzheng.get('cuowu')})

def MiMaYanZheng(str1):
    re_mima = ur"[A-Za-z0-9]*$"
    if not re.match(re_mima,str1):
        return False
    else:
        return True

def ShouFeiChuLi_1(jczid,cph,pzlb_int,pzlb_str,chezhudh,czry,czry_user,fkfs_id,fkfs,data,is_tuikuan = False,bjr = None,
                   bjr_username=None,tuikuan_riqi = None):
    fanhui_dic = {}
    for i in data:
        if i == 'anjian':#处理年检
            is_kefu = data.get(i).get('is_kefu')
            if is_kefu == None:
                is_kefu = False
            jylb = data.get(i).get('jylb')
            jfje = data.get(i).get('jfje')
            anjian_fanhui =anjianshujucharu_1(cph,pzlb_int,pzlb_str,chezhudh,czry,jylb,jfje,is_kefu=False)

            q = DX_ShouFei(jczid=jczid,paizhaohao=cph,cheliangleibie_id=pzlb_int,
                           cheliangleibie_str=pzlb_str,chezhudianhua=chezhudh,
                           jyxm='anjian',jylb=jylb,dyid=anjian_fanhui,skr=czry,
                           skr_username=czry_user,skrq=datetime.datetime.now(),
                           skje=jfje,zhifufangshi_zimu=fkfs_id,zhifufangshi_str=fkfs,
                           is_kefu=is_kefu,is_tuikuan=is_tuikuan,bjr=bjr,bjr_username=bjr_username,tuikuan_riqi=tuikuan_riqi)

            q.save()#TODO:处理返回值
        if i == 'weiqi':#处理尾气
            jylb = data.get(i).get('jylb')
            jfje = data.get(i).get('jfje')
            is_zhuanru = data.get(i).get('is_zhuanru')
            if pzlb_int == '16':
                cph = cph + u'学'
            elif pzlb_int == '23':
                cph = cph + u'警'
            if is_zhuanru == True:
                cph = u'转' + cph
            weiqi_fanhui = weiqishujucharu_1(cph,pzlb_int,pzlb_str,czry,jylb,jfje,is_zhuanru=False)
            q = DX_ShouFei(jczid=jczid,paizhaohao=cph,cheliangleibie_id=pzlb_int,
                           cheliangleibie_str=pzlb_str,chezhudianhua=chezhudh,
                           jyxm='weiqi',jylb=jylb,dyid=weiqi_fanhui,skr=czry,
                           skr_username=czry_user,skrq=datetime.datetime.now(),
                           skje=jfje,zhifufangshi_zimu=fkfs_id,zhifufangshi_str=fkfs,is_tuikuan=is_tuikuan,
                           bjr=bjr, bjr_username=bjr_username,tuikuan_riqi=tuikuan_riqi)
            q.save()
        if i == 'qita':
            dic1 = data.get(i)
            for a in dic1:
                jylb = a
                jfje = dic1.get(a)
                qita_fanhui = anjianshujucharu_1_qita(cph,pzlb_int,pzlb_str,czry,jylb,jfje)

                q = DX_ShouFei(jczid=jczid,paizhaohao=cph,cheliangleibie_id=pzlb_int,
                           cheliangleibie_str=pzlb_str,chezhudianhua=chezhudh,
                           jyxm='qita',jylb=jylb,dyid=qita_fanhui,skr=czry,
                           skr_username=czry_user,skrq=datetime.datetime.now(),
                           skje=jfje,zhifufangshi_zimu=fkfs_id,zhifufangshi_str=fkfs,is_tuikuan=is_tuikuan,
                               bjr=bjr, bjr_username=bjr_username,tuikuan_riqi=tuikuan_riqi)
                q.save()
    #返回刷新结果及分收款方式统计结果
    '''
    qs = list(DX_ShouFei.objects.filter(skr_username=czry_user,jczid=jczid,
            is_jiezhang=False).order_by('-skrq').values('id','paizhaohao','cheliangleibie_str',
            'jyxm','jylb','skje','skrq','skr','jiezhangriqi',
            'fapiao_qiri','zhifufangshi_str','zhifufangshi_zimu'))
    #分组计算总和并返回字典
    QsGroupSum = pd.DataFrame(qs).groupby(['zhifufangshi_zimu'],as_index=False).sum().to_dict('recodes')
    '''
    #return {'qs':qs,'groupsum':QsGroupSum}
    return {'chenggong':True}

def anjianshujucharu_1(cph,pzlb_int,pzlb_str,chezhudh,czry,jylb,jfje,is_kefu):
    DBCONNECTSTR = 'DRIVER={SQL Server};SERVER=15.29.32.3;port=1433;DATABASE=NewGaJck_TB;UID=sa;PWD=svrcomputer;TDS_Version=7.1;'
    conn = pyodbc.connect(DBCONNECTSTR)
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(FPHM) FROM UFee')
    zuidashu = cursor.fetchall()[0][0]
    sql = ''
    parameters = ()
    if chezhudh != '' and is_kefu != False:
        sql = "insert into  UFee (FPHM,CPH,PZLBID,PZLB,JCSX,JCLB,JKDW,SKXM,SKR,SKRQ,SKJE,BZ) values (?,?,?,?,?,?,?,?,?,?,?,?)"
        parameters = (zuidashu+1, cph, pzlb_int, pzlb_str, 0, jylb, chezhudh, u'安检费', czry,datetime.datetime.now(), jfje,u'客服')
    elif chezhudh != '' and is_kefu == False:
        sql = "insert into  UFee (FPHM,CPH,PZLBID,PZLB,JCSX,JCLB,JKDW,SKXM,SKR,SKRQ,SKJE,BZ) values (?,?,?,?,?,?,?,?,?,?,?,?)"
        parameters = (zuidashu+1, cph, pzlb_int, pzlb_str, 0, jylb, chezhudh, u'安检费', czry,datetime.datetime.now(), jfje,'')
    elif chezhudh == '' and is_kefu != False:
        sql = "insert into  UFee (FPHM,CPH,PZLBID,PZLB,JKDW,JCSX,JCLB,SKXM,SKR,SKRQ,SKJE,BZ) values (?,?,?,?,?,?,?,?,?,?,?,?)"
        parameters = (zuidashu+1, cph, pzlb_int, pzlb_str, '',0, jylb, u'安检费', czry,datetime.datetime.now(), jfje,u'客服')

    elif chezhudh == '' and is_kefu == False:
        sql = "insert into  UFee (FPHM,CPH,PZLBID,PZLB,JKDW,JCSX,JCLB,SKXM,SKR,SKRQ,SKJE,BZ) values (?,?,?,?,?,?,?,?,?,?,?,?)"
        parameters = (zuidashu+1, cph, pzlb_int, pzlb_str, '',0, jylb, u'安检费', czry,datetime.datetime.now(), jfje,'')
    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()
    return zuidashu+1

def weiqishujucharu_1(cph,pzlb_int,pzlb_str,czry,jylb,jfje,is_zhuanru):
    skxm = ''
    if u'不透光' in jylb:
        skxm = u'不透光'
    elif u'稳态' in jylb:
        skxm = u'稳态收费'
    elif jylb == u'补打报告单':
        skxm = u'稳态收费'
    elif jylb == u'出租车':
        skxm = u'稳态收费'
    DBCONNECTSTR = 'DRIVER={SQL Server};SERVER=15.29.32.61;port=1433;DATABASE=hbjcdb;UID=sa;PWD=svrcomputer;TDS_Version=7.1;'
    conn = pyodbc.connect(DBCONNECTSTR)
    cursor = conn.cursor()
    sql = "insert into  UFee (CPH,PZLBID,PZLBStr,SFXMStr,JKDW,SKXM,JCCS,SKR,SKRQ,SKJE) values (?,?,?,?,?,?,?,?,?,?)"
    parameters = (cph, pzlb_int, pzlb_str,jylb, '',skxm, 1,czry, datetime.datetime.now(), jfje)
    cursor.execute(sql, parameters)
    conn.commit()
    cursor.execute("select @@IDENTITY")#这条不需要提交
    fanhui=cursor.fetchall()[0][0]
    conn.close()

    return fanhui
def anjianshujucharu_1_qita(cph,pzlb_int,pzlb_str,czry,jylb,jfje):
    DBCONNECTSTR = 'DRIVER={SQL Server};SERVER=15.29.32.3;port=1433;DATABASE=NewGaJck_TB;UID=sa;PWD=svrcomputer;TDS_Version=7.1;'
    conn = pyodbc.connect(DBCONNECTSTR)
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(FPHM) FROM UFee')
    zuidashu = cursor.fetchall()[0][0]
    sql = "insert into  UFee (FPHM,CPH,PZLBID,PZLB,JCSX,JCLB,JKDW,SKXM,SKR,SKRQ,SKJE,BZ) values (?,?,?,?,?,?,?,?,?,?,?,?)"
    parameters = (zuidashu+1, cph, pzlb_int, pzlb_str, 0, u'其他检验项目', '', u'安检费', czry,datetime.datetime.now(), jfje,jylb)
    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()
    return zuidashu+1



def cheliangleixingUTF8toInt(pzlb_str):
    dic1 = {u'小型汽车':'02',
           u'大型汽车':'01',
           u'使馆汽车':'03',
           u'领馆汽车':'04',
           u'境外汽车':'05',
           u'挂车':'15',
           u'农用运输车':'13',
           u'拖拉机':'14',
           u'教练摩托车':'17',
           u'警用汽车':'23',
           u'两、三轮摩托':'07',
           u'外籍汽车':'06',
           u'轻便摩托车':'08',
           u'教练汽车':'16',
           u'警用摩托车':'24'}
    return dic1[pzlb_str]


#以下为自助查询车辆检测状态部分
def zizhuchaxun_tijiao(request):#自助查询提交
    title = u'车辆检测状态自助查询'
    erbuyanzheng = False
    erbuyanzhengneirong = u'提交后如果增加相应合同则无法修改！'
    if request.method == 'POST':
        form = DX_zizhuchaxun_tijiao_forms(request.POST)
        if form.is_valid():
            chepai_qian = form.cleaned_data['chepai_qian']
            chepai_hou = form.cleaned_data['chepai_hou']
            chepai_leibie = cheliangleixingUTF8toInt(form.cleaned_data['chepai_leibie'])
            chepai_zimu = form.cleaned_data['chepai_zimu'].upper()
            chepai_wanzheng = chepai_qian+chepai_hou+chepai_zimu
            anjian_zhuangtai = anjian_zhuangtaichaxun(chepai_wanzheng,chepai_leibie).panduan()
            weiqi_zhuangtai = weiqi_zhuangtaichaxun(chepai_wanzheng,chepai_leibie).zhuangtaichaxun()
            #p = PinleiGL(pinleiname=pinleiname, isedit=1, pinleitype=pinleitype,danjia=danjia)
            #q = PinleiType.objects.filter(type_name=pinleitype)
            #q.update(isedit=0)
            #messages.add_message(request, messages.SUCCESS, '数据添加成功！')
            #p.save()
            #return HttpResponseRedirect('/pinlei/pinleilist/')
            return render_to_response('zizhu_dankehu_chaxunjiegu.html', locals(), context_instance=RequestContext(request))
    else:
        form = DX_zizhuchaxun_tijiao_forms()
    return render_to_response('add.html', locals(), context_instance=RequestContext(request))

class anjian_zhuangtaichaxun:
    """查询安检和尾气的车辆状态"""

    fanhui = {}
    def __init__(self,chepai_wanzheng,chepai_leibie):
        self.chepai_wanzheng = chepai_wanzheng
        self.chepai_leibie = chepai_leibie
        self.anjian_host = '15.29.32.3'
        #self.weiqi_host = '15.29.32.61'
        self.jianceleibie = u'在用机动车检验'
    def carreg(self):#查询carreg数据
        conn = pymssql.connect(self.anjian_host, 'sa', 'svrcomputer', 'NewGaJck_TB')
        jieguo = {}
        cursor = conn.cursor(as_dict=True)
        cursor.execute('SELECT JCZT,ReTest FROM carreg WHERE CPH=%s AND PZLBID=%s',
                       (self.chepai_wanzheng, self.chepai_leibie))
        # cursor.execute('SELECT * FROM ufee WHERE CPH=%s AND PZLBID=%s',(paizhaohao,paizhaoleibie_id))
        for i in cursor:
            jieguo['jczt'] = i.get('JCZT')
            jieguo['retest'] = i.get('ReTest')
        # print qs_num
        conn.close()
        if len(jieguo) == 0:
            return 'kong'
        chujianorfujian = jieguo.get('retest')#初检或者复检
        if chujianorfujian == 0:
            return u'初检'+' '+jieguo.get('jczt')
        elif chujianorfujian > 0:
            return u'复检'+ ' ' + jieguo.get('jczt')


    def CarDetInfo(self):#查询cardetinfo数据
        today = datetime.date.today()
        conn = pymssql.connect(self.anjian_host, 'sa', 'svrcomputer', 'NewGaJck_TB')
        jclsh_list = []
        cursor = conn.cursor(as_dict=True)
        cursor.execute('SELECT JCLSH FROM cardetinfo WHERE CPH=%s AND PZLBID=%s',
                       (self.chepai_wanzheng, self.chepai_leibie))
        # cursor.execute('SELECT * FROM ufee WHERE CPH=%s AND PZLBID=%s',(paizhaohao,paizhaoleibie_id))
        for i in cursor:
            jclsh_list.append(i.get('JCLSH'))
        conn.close()
        if len(jclsh_list) == 0:
            return 'kong'
        else:
            return_dic = self.getnewjclsh(jclsh_list)
            shijiancha = today - return_dic.get('date')
            if shijiancha > datetime.timedelta(days=30):
                return 'kong'
            else:
                return return_dic.get('jclsh')


    def JcBase(self,jclsh):
        jieguo_shuchu = []
        fanhui_list = []
        #jiancexiangmu_poingjia = {'Exa_SpeedEvl':u'速度','Exa_SlideEvl':u'侧滑','Exa_Brake1Evl':u'一轴制动',
                                  #'Exa_Brake2Evl':u'二轴制动','Exa_Brake3Evl':u'三轴制动','Exa_Brake4Evl':u'四轴制动',
                                  #'Exa_Brake5Evl':u'五轴制动','Exa_Brake6Evl':u'六轴制动','Exa_BrakeSEvl':u'驻车制动',
                                  #'Exa_BrakeZCEvl':u'整车制动','Exa_LightInLEvl':u'左副灯','Exa_LightInREvl':u'右副灯',
                                  #'Exa_LightOutLEvl':u'左主灯','Exa_LightOutREvl':u'右主灯','Exa_LightNearLEvl':u'左近光灯',
                                  #'Exa_LightNearREvl':u'右近光灯','Exa_OutCheckEvl':u'外检','Exa_DTCheckEvl':u'动态',
                                  #'Exa_DGCheckEvl':u'地沟','Exa_Evl':u'总检'}
        jiancexiangmu_pingjia = {'Evl':u'总检','Speed':u'速度','Slide':u'侧滑','Brake1':u'一轴制动','Brake2':u'二轴制动',
                                 'Brake3':u'三轴制动','Brake4':u'四轴制动','Brake5':u'五轴制动','Brake6':u'六轴制动',
                                 'BrakeS1':u'一轴驻车制动','BrakeS2':u'二轴驻车制动','BrakeS3':u'三轴驻车制动',
                                 'BrakeS4':u'四轴驻车制动','BrakeS5':u'五轴驻车制动','BrakeS6':u'六轴驻车制动',
                                 'BrakeS':u'整车驻车制动','BrakeZC':u'整车制动','LightInL':u'左副灯','LightInR':u'右副灯',
                                 'LightOutL':u'左主灯','LightOutR':u'右主灯','LightNearL':u'左近光灯','LightNearR':u'右近光灯',
                                 'OutCheckEvl':u'外检','DTCheckEvl':u'动态','DGCheckEvl':u'地沟',}
        conn = pymssql.connect(self.anjian_host, 'sa', 'svrcomputer', 'NewGaJck_TB')
        jieguo = {}
        cursor = conn.cursor()
        cursor.execute('SELECT MAX(JCMaxNum) FROM jcbase WHERE JCLSH = %s', (jclsh))#对多次检测的获取最后一次
        zuidashu = cursor.fetchall()[0][0]
        cursor = conn.cursor(as_dict=True)
        #cursor.execute('SELECT Exa_SpeedEvl,Exa_SlideEvl,Exa_Brake1Evl,Exa_Brake2Evl,Exa_Brake3Evl,Exa_Brake4Evl,Exa_Brake5Evl,Exa_Brake6Evl,Exa_BrakeSEvl,Exa_BrakeZCEvl,Exa_LightInLEvl,Exa_LightInREvl,Exa_LightOutLEvl,Exa_LightOutREvl,Exa_LightNearLEvl,Exa_LightNearREvl,Exa_OutCheckEvl,Exa_DTCheckEvl,Exa_DGCheckEvl,Exa_Evl FROM examine WHERE JCLSH = %s',(jclsh))
        cursor.execute('SELECT Evl,Speed,Slide,Brake1,Brake2,Brake3,Brake4,Brake5,Brake6,BrakeS1,BrakeS2,BrakeS3,BrakeS4,BrakeS5,BrakeS6,BrakeS,BrakeZC,LightInL,LightInR,LightOutL,LightOutR,LightNearL,LightNearR,OutCheckEvl,DTCheckEvl,DGCheckEvl FROM jcbase WHERE JCLSH = %s AND JCMaxNum = %s',(jclsh,zuidashu))

        # cursor.execute('SELECT * FROM ufee WHERE CPH=%s AND PZLBID=%s',(paizhaohao,paizhaoleibie_id))
        for i in cursor:#查询结果总检项为T则返回检测合格
            if i.get('Evl') == 'T':
                return 'jiancehege'
            else:#总检不合格的将不合格项加入列表
                for a in i:
                    if i.get(a).find('F') != -1:
                        jieguo_shuchu.append(a)
                jieguo_shuchu.remove('Evl')
        for i in jieguo_shuchu:
            fanhui_list.append(jiancexiangmu_pingjia.get(i))
        fanhui_str = ','.join(fanhui_list)
        conn.close()
        return fanhui_str
    def zhizheng(self):#查询制证日期
        zhizhengriqi = datetime.datetime.now()
        qs = DX_Xingshizheng.objects.filter(paizhaohao=self.chepai_wanzheng,
                                            cheliangleibie_id=self.chepai_leibie).order_by('-chuanjianriqi')
        if len(qs) == 0:#没有查询到结果
            return 'kong'
        elif len(qs) != 0:
            zhizhengriqi = qs[0].chuanjianriqi#创建日期
        today = datetime.datetime.now()
        shijiancha = today - zhizhengriqi
        if shijiancha > datetime.timedelta(days=30):
            return 'kong'
        else:
            return str(zhizhengriqi)[:19]#时间戳截断返回字符串

    def getnewjclsh(self,jclsh_list):
            # 获得车辆最近的流水号，注意：至少传入一个流水号
        return_list = []
        for i in jclsh_list:
            dic = {}
            year, mon, day, sn, jclsh = int(i[2:6]), int(i[6:8]), int(i[8:10]), int(i[10:]), i
            try:
                date = datetime.date(year, mon, day)
            except:
                print 'riqigeshibufu'
            dic['date'] = date
            dic['sn'] = sn
            dic['jclsh'] = jclsh
            return_list.append(dic)
        df = pd.DataFrame(return_list)
        df1 = df.sort(['date', 'sn'], ascending=[True, True])
        return_dic = {}
        df1_todic = df1[len(df1) - 1:].to_dict('records')[0]
        return_dic['date'] = date
        return_dic['jclsh'] = df1_todic.get('jclsh')
        return return_dic

    '''
    如果检测队列中有车辆信息则直接显示检测队列中的信息，如果检测队列中没有则通过查询cardetinfo得到jclsh 查询jcbase中的车辆信息并返回合格或不合格，
    如果合格则查询制证表中是否有记录，如果不合格则返回不合格提示并输出不合格项目提示复检，
    '''
    def panduan(self):
        carreg = self.carreg()
        if carreg != 'kong':
            return {'zhuangtai':'denglu','neirong':carreg}
        elif carreg == 'kong':
            cardetinfo = self.CarDetInfo()
            if cardetinfo == 'kong':
                return {'zhuangtai':'weibanli'}
            elif cardetinfo != 'kong':
                jcbase = self.JcBase(cardetinfo)
                if jcbase == 'jiancehege':
                    zhizheng = self.zhizheng()
                    if zhizheng == 'kong':
                        return {'zhuangtai':'dengdaizhizheng'}
                    elif zhizheng != 'kong':
                        return {'zhuangtai':'yibanjie','neirong':zhizheng}
                elif jcbase != 'jiancehege':
                    return {'zhuangtai':'anjian_buhege','neirong':jcbase}

class weiqi_zhuangtaichaxun:#尾气状态查询

    def __init__(self,chepai_wanzheng,chepai_leibie):
        self.chepai_wanzheng = chepai_wanzheng
        self.chepai_leibie = chepai_leibie
        self.weiqi_webservices_host = '15.29.32.61'
    def haopaichuli(self):#将号牌处理成为符合尾气习惯的号牌（比如：蒙A12345 大型车 处理为黄蒙A12345）
        paichu_list = ['15','14','17','07','08','24']
        if self.chepai_leibie in paichu_list:
            return 'buyongjian'
        if self.chepai_wanzheng.find(u'转') != -1:#确认车牌中没有转移登记车牌
            return 'zhuanyi'
        else:

            if self.chepai_leibie == '02':
                return u'蓝'+self.chepai_wanzheng
            elif self.chepai_leibie == '01':
                return u'黄'+self.chepai_wanzheng
            elif self.chepai_leibie == '13':
                return u'农黄'+self.chepai_wanzheng
            elif self.chepai_leibie == '16':
                return u'黄'+self.chepai_wanzheng+u'学'
            elif self.chepai_leibie == '24':
                return u'白'+self.chepai_wanzheng+u'警'

    def zhuangtaichaxun(self):
        paizhaohao_wanzheng = self.haopaichuli()
        fasong_data = {'paizhaohao_wanzheng': paizhaohao_wanzheng}
        # resp = requests.post('https://172.18.130.249:81/dx/webservices/ywbj/',verify=False,data=json.dumps(fasong_data))
        resp = requests.post('https://192.168.0.3:81/weiqiwebservices/zhuangtaichaxun/', verify=False,
                             data=json.dumps(fasong_data))
        resp_result = resp.content
        jieguo = json.loads(resp_result)['zhuangtai']
        return jieguo


"""
部署到0。3其他机器需注释掉

def webservices_weiqi_mysql(requset):
    if requset.method == 'POST':
        fanhui_dic = {}
        try:
            jieshou_json = json.loads(requset.body)
        except ValueError:
            return HttpResponse(u'数据格式不对')
        paizhaohao_wanzheng = jieshou_json.get('paizhaohao_wanzheng')
        if paizhaohao_wanzheng is None:
            return HttpResponse(u'数据内容不正确')
        today = datetime.datetime.now()
        chepaihao = paizhaohao_wanzheng
        db = MySQLdb.connect(host="15.29.32.61", user="root", passwd="", db="jfjl", charset="utf8")
        cursor = db.cursor()
        sql = "SELECT MAX(ID) FROM JIAOFEI WHERE CPH = '%s'" % (chepaihao)
        cursor.execute(sql)
        zuidashu = cursor.fetchall()[0][0]
        if zuidashu is None:
            fanhui_dic['zhuangtai'] = 'weibanli'
            return JsonResponse(fanhui_dic)
        sql1 = "SELECT STATUS,JCTIME FROM JIAOFEI WHERE  ID = '%s'" % (zuidashu)
        cursor.execute(sql1)
        jieguo = cursor.fetchall()[0]
        db.close()
        zhuangtai, jctime = jieguo[0], jieguo[1][:10]
        a = datetime.datetime.strptime(jctime, "%Y-%m-%d")
        shijiancha = today - a
        if shijiancha > datetime.timedelta(days=60):
            fanhui_dic['zhuangtai'] = 'weibanli'
            return JsonResponse(fanhui_dic)
        else:
            fanhui_dic['zhuangtai'] = zhuangtai
        return JsonResponse(fanhui_dic)
    else:
        result = {'zhuangtai': 'Error', 'fanhui_msg': u'出现错误500'}
        return JsonResponse(result)
"""
"""
qs = DX_ShouFei.objects.filter(skr_username='test')
for i in qs:
    id = i.id
    jylb = i.jylb
    input_pinyin = Pinyin()
    jylb_pinyin = input_pinyin.get_pinyin(jylb, '')
    DX_ShouFei.objects.filter(id=i.id).update(jylb_pinyin=jylb_pinyin)
    print i.id

qs = DX_ShouFei.objects.filter(skr_username='test').values('cheliangleibie_id','jyxm','zhifufangshi_zimu','jylb_pinyin')
df = pd.DataFrame(list(qs))
df.groupby(['zhifufangshi_zimu','jyxm','jylb_pinyin','cheliangleibie_id'],as_index=False).count().to_dict('recodes')
"""