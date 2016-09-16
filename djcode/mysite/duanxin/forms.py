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

class DX_chaxun_duibi_forms(forms.Form):
    chaxun_or_duibi_CHOICES = (('shoufei', '收费'), ('zhizheng', '制证'), ('shoufei_zhizheng_duibi', '收费与制证对比'))
    chaxun_or_duibi = forms.ChoiceField(choices=chaxun_or_duibi_CHOICES, label=u'查询方式')
    #mxorhuizong_CHOICES = (('mx', '明细'), ('jiaxiaoname', '按驾校名称汇总'))
    #mxorhuizong = forms.ChoiceField(choices=mxorhuizong_CHOICES, label=u'明细/汇总')
    # jiaxiaoname = forms.ModelMultipleChoiceField(queryset=BGYP_bumen.objects.all().order_by('bumenname'),required=False,label=u'选择部门（可多选）')
    # bumenname = forms.ModelChoiceField(queryset=BGYP_bumen.objects.all().order_by('bumenname'),required=False,label=u'领取部门（只有查看出库明细时此选项才生效）')
    # fenleiname = forms.ModelChoiceField(queryset=BGYP_fenlei.objects.all().order_by('fenleiname'),required=False,label=u'分类名称')
    start_time = forms.DateField(required=False, label=u'起始日期', widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                                                                               "pickTime": False}))
    end_time = forms.DateField(required=False, label=u'截止日期', widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                                                                         "pickTime": False}))
    shuchufangshi_CHOICES = (('all', '全部输出'), ('chayi', '只输出差异信息'))
    shuchufangshi = forms.ChoiceField(choices=shuchufangshi_CHOICES, label=u'输出方式')
    # ishtml_CHOICES = (('datatable','数据表格'),('css','CSS样式'))
    # ishtml  = forms.ChoiceField(choices=ishtml_CHOICES,label=u'选择样式')
    shengchengwenjian_CHOICES = (('no', '不生成'), ('yes', '生成'))
    shengchengwenjian = forms.ChoiceField(choices=shengchengwenjian_CHOICES, label=u'是否生成文件')


