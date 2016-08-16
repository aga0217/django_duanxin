#coding=utf-8
from django import forms
from models import *
from django.forms import ModelForm,Textarea,MultipleChoiceField
import datetime
import views
from bootstrap3_datetime.widgets import DateTimePicker
from django.db.models import Count, Min, Sum, Avg
import re

class DX_tijiao_form(ModelForm):
    class Meta:
        model = DX_CarInfo
        fields = ['chepai_qian','chepai_hou','paizhaohao','dianhua']

    def clean_paizhaohao(self):
        paizhaohao_num = self.cleaned_data['paizhaohao']
        re_paizhaohao_num = ur"[A-Za-z0-9]*$"
        if not re.match(re_paizhaohao_num , paizhaohao_num):
            raise forms.ValidationError(u'只能使用字母数字')
        if len(paizhaohao_num) !=5:
            raise forms.ValidationError(u'字母加数字必须是5位')
        return paizhaohao_num
    def clean_dianhua(self):
        dianhua = self.cleaned_data['dianhua']
        re_dainhua = ur"[0-9]*$"
        if not re.match(re_dainhua,dianhua):
            raise forms.ValidationError(u'只能使用字母数字')
        if len(dianhua) !=11 or dianhua[0] != '1':
            raise forms.ValidationError(u'请输入正确的手机号码')
        return dianhua

class DX_search_fasong_forms(forms.Form):
    start_time = forms.DateField(required=False,label=u'起始日期',widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    end_time = forms.DateField(required=False,label=u'截止日期',widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    #ishtml_CHOICES = (('datatable','数据表格'),('css','CSS样式'))
	#ishtml  = forms.ChoiceField(choices=ishtml_CHOICES,label=u'选择样式')
    shengchengwenjian_CHOICES = (('no','不生成'),('yes','生成'))
    shengchengwenjian  = forms.ChoiceField(choices=shengchengwenjian_CHOICES,label=u'是否生成文件')


CHELIANG_LIEXING_CHOICES = (
    ('H', u'货车'),
    ('K', u'客车'),
)

class DX_search_carinfo_forms(forms.Form):
    cheliang_leixing = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=CHELIANG_LIEXING_CHOICES,label=u'请选择查询车辆类型')


