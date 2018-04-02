# -*- coding: utf-8 -*-
import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtCore
from PySide.QtWebKit import *
from denglu_ui import Ui_denglu_Dialog
from shoufei_ui import Ui_MainWindow
from xiugaimima_ui import Ui_xiugaimima_Dialog
from shoufeidan_ui import Ui_Ui_shoufeidanyulan_Dialog
from jiezhang_chuangkou import Ui_Ui_jiezhang_Dialog
from tuikuanyuanyin_ui import Ui_Ui_tuikuan_Dialog
from tuijianren_ui import Ui_TuiJianRen_UI_Dialog
import datetime
import re
import json
import requests
from xhtml2pdf import pisa
import testprint
requests.packages.urllib3.disable_warnings()#关闭证书的安全提示
dizhi = ''
skr_username = ''
skr_username_str = u''
jcz_id = ''
user_pass = ''
CAN_TUIKUAN = ''
ID_LIST = []
TJRNAME = ''
SHOUFEICONFIG = {}

class xinhao_class(QtCore.QObject):
    speak = QtCore.Signal(str)
class denglu_chuangkou(QDialog,Ui_denglu_Dialog):
    def __init__(self, parent=None):
        super(denglu_chuangkou, self).__init__(parent)
        self.setupUi(self)
        self.tishikuang = QMessageBox()
        try:
            f = open('settings_shoufei.json','r+')
            data = json.load(f)

            self.dizhi = data.get('dizhi')
            self.jcz_id = data.get('jcz_id')
            global dizhi
            global jcz_id
            dizhi = self.dizhi
            jcz_id = self.jcz_id
            if self.dizhi == None or self.jcz_id==None:
                self.tishikuang.setText(u'配置文件没有地址信息或检测站ID')
                self.tishikuang.exec_()
                sys.exit(app.exit())
        except IOError:
            self.tishikuang.setText(u'没有配置文件')
            self.tishikuang.exec_()
            sys.exit(app.exit())
        self.username.editingFinished.connect(lambda :self.FinishUserName())
        self.denglu_Button.clicked.connect(lambda: self.handleLogin())
    def getconfig(self):#获取配置文件
        fasong_data = {'skr_username':skr_username , 'password':user_pass}
        url = dizhi + 'getconfig/'
        try:#处理连接时候的异常
            resp = requests.post(url, verify=False, data=json.dumps(fasong_data))
        except Exception,e:
            e = repr(e)#避免出现中文字符
            f = open('error.log','a')#文件追加模式
            s1 = str(datetime.datetime.now())+e+'\n'
            f.write(s1)
            f.close()
            self.tishikuang.setText(u'getconfig连接出现错误，查看日志文件')
            self.tishikuang.exec_()
            sys.exit(app.exit())
        result_rep = resp.content
        global SHOUFEICONFIG
        try:  # 处理接受json的异常
            SHOUFEICONFIG = json.loads(result_rep)
        except:
            f = open('error.log', 'a')
            f.write(result_rep)
            f.close()
            self.tishikuang.setText(u'getconfig返回结果格式不正确')
            self.tishikuang.exec_()
            sys.exit(app.exit())

    def handleLogin(self):
        password =  self.password.text()
        username = self.username.text()
        if len(username) == 0 or len(password) == 0:
            self.tishikuang.setText(u'没有输入用户名或密码')
            self.tishikuang.exec_()
            self.username.clear()
            self.password.clear()
            return
        fasong_data = {'skr_username': username, 'password': password}
        url = dizhi+'denglu/'
        try:#处理连接时候的异常
            resp = requests.post(url, verify=False, data=json.dumps(fasong_data))
        except Exception,e:
            e = repr(e)#避免出现中文字符
            f = open('error.log','a')#文件追加模式
            s1 = str(datetime.datetime.now())+e+'\n'
            f.write(s1)
            f.close()
            self.tishikuang.setText(u'连接出现错误，查看日志文件')
            self.tishikuang.exec_()
            sys.exit(app.exit())


        result_rep = resp.content
        try:#处理接受json的异常
            result = json.loads(result_rep)
        except:
            f=open('error.log','a')
            f.write(result_rep)
            f.close()
            self.tishikuang.setText(u'返回结果格式不正确')
            self.tishikuang.exec_()
            sys.exit(app.exit())
        if result.get('denglu') != True:
            #print result
            self.tishikuang.setText(u'登录错误'+result.get('cuowu'))
            self.tishikuang.exec_()
            self.username.clear()
            self.password.clear()
        elif result.get('denglu') == True:
            global skr_username
            global skr_username_str
            global CAN_TUIKUAN
            skr_username = result.get('username')
            skr_username_str = result.get('user_str')
            CAN_TUIKUAN = result.get('is_tuikuan')
            global user_pass
            user_pass = self.password.text()
            self.getconfig()

            self.accept()  # 关键

        #if (self.textName.text() == 'foo' and
            #self.textPass.text() == 'bar'):
        #print
        #self.accept() #关键
        #else:
            #QtGui.QMessageBox.warning(
                #self, 'Error', 'Bad user or password')
    def FinishUserName(self):#验证用户名输入是否正确只能输入小写字母和数字
        username = self.username.text()
        re_username = ur"[a-z0-9]*$"
        if not re.match(re_username, username):
            self.tishikuang.setText(u'只能输入小写字母和数字')
            self.tishikuang.exec_()
            self.username.clear()

class xiugaimima_chuangkou(QDialog,Ui_xiugaimima_Dialog):
    def __init__(self, parent=None):
        super(xiugaimima_chuangkou, self).__init__(parent)
        self.setupUi(self)
        self.tishikuang = QMessageBox()
        self.yuanshimima.editingFinished.connect(lambda :self.FinishYuanShiMima())
        self.xinmima1.editingFinished.connect(lambda : self.XinMima1())
        self.xinmima2.editingFinished.connect(lambda : self.XinMima2())
        self.Button_gengtaimima.clicked.connect(lambda : self.GengGaiMiMa())

    def FinishYuanShiMima(self):
        yuanshimima = self.yuanshimima.text()
        if self.MiMaYanZheng(yuanshimima) != True:
            self.tishikuang.setText(u'只能输入字母和数字')
            self.tishikuang.exec_()
            self.yuanshimima.clear()

    def XinMima1(self):
        xinmima1 = self.xinmima1.text()
        if self.MiMaYanZheng(xinmima1) != True:
            self.tishikuang.setText(u'只能输入字母和数字')
            self.tishikuang.exec_()
            self.xinmima1.clear()

    def XinMima2(self):
        xinmima2 = self.xinmima1.text()
        if self.MiMaYanZheng(xinmima2) != True:
            self.tishikuang.setText(u'只能输入字母和数字')
            self.tishikuang.exec_()
            self.xinmima2.clear()

    def MiMaYanZheng(self,str1):
        re_mima = ur"[A-Za-z0-9]*$"
        if not re.match(re_mima,str1):
            return False
        else:
            return True

    def GengGaiMiMa(self):
        if self.xinmima1.text() != self.xinmima2.text():
            self.tishikuang.setText((u'两次输入的密码不一致，请检查！'))
            self.tishikuang.exec_()
            self.xinmima2.clear()
            self.xinmima1.clear()
        else:
            global skr_username

            fasong_data = {'skr_username':skr_username,'yuanshimima': self.yuanshimima.text(),
                           'xinmima':self.xinmima1.text()}
            url = dizhi+'xiugaimima/'
            try:  # 处理连接时候的异常
                resp = requests.post(url, verify=False, data=json.dumps(fasong_data))
            except Exception, e:
                e = repr(e)  # 避免出现中文字符
                f = open('error.log', 'a')  # 文件追加模式
                s1 = str(datetime.datetime.now()) +'--'+ e + '\n'
                f.write(s1)
                f.close()
                self.tishikuang.setText(u'连接出现错误，查看日志文件')
                self.tishikuang.exec_()
                sys.exit(app.exit())
            result_rep = resp.content
            try:  # 处理接受json的异常
                result = json.loads(result_rep)
            except:
                f = open('error.log', 'a')
                f.write(result_rep)
                f.close()
                self.tishikuang.setText(u'返回结果格式不正确')
                self.tishikuang.exec_()
                sys.exit(app.exit())
            if result.get('chenggong') == None:
                self.tishikuang.setText(u'字段为空')
                self.tishikuang.exec_()
                self.yuanshimima.clear()
                self.xinmima1.clear()
                self.xinmima2.clear()
            elif result.get('chenggong') != True:
                self.tishikuang.setText(result.get('cuowu'))
                self.tishikuang.exec_()
                self.yuanshimima.clear()
                self.xinmima2.clear()
                self.xinmima1.clear()
            elif result.get('chenggong') == True:
                self.tishikuang.setText(u'密码修改成功，请使用新密码重新登录')
                self.tishikuang.exec_()
                sys.exit(app.exit())

class shoufeidanyulan_chuangkou(QDialog,Ui_Ui_shoufeidanyulan_Dialog):
    def __init__(self, parent=None):
        super(shoufeidanyulan_chuangkou, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda :self.PrintBill())



        self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))


        #view_html.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))
        self.webView.show()

    def PrintBill(self):
        filename = 'shoufeidan.html'
        Window().HtmlToPDF(filename)
        testprint.printPDF(filename)

class tuikuanyuanyin_chuangkou(QDialog,Ui_Ui_tuikuan_Dialog):
    def __init__(self, parent=None):
        super(tuikuanyuanyin_chuangkou, self).__init__(parent)
        self.setupUi(self)
        self.xinhao = xinhao_class()
        self.button_tuikuan.clicked.connect(lambda :self.tuikuan())

        #view_html.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))


    def getvlue(self):
        yuanyinlist = []
        if self.yuanyin_1.isChecked():
            yuanyinlist.append('1')
        if self.yuanyin_2.isChecked():
            yuanyinlist.append('2')
        if self.yuanyin_3.isChecked():
            yuanyinlist.append('3')
        if self.yuanyin_4.isChecked():
            yuanyinlist.append('4')
        if self.yuanyin_5.isChecked():
            yuanyinlist.append('5')
        if self.yuanyin_6.isChecked():
            yuanyinlist.append('6')
        if len(self.yuanyin_input.text())!=0:
            yuanyinlist.append(self.yuanyin_input.text())
        if len(yuanyinlist) == 0:
            self.tixingkuang = QMessageBox()
            self.tixingkuang.setText(u'至少选择一种原因')
            self.tixingkuang.exec_()
            return None
        return ','.join(yuanyinlist)

    def tuikuan(self):
        self.tixingkuang = QMessageBox()
        tuikuanyuanyin = self.getvlue()
        if tuikuanyuanyin == None:
            return
        data = {'jczid': jcz_id, 'czry': skr_username, 'czry_pass': user_pass,'id_list':ID_LIST,
                'tuikuanyuanyin':tuikuanyuanyin}
        lianjie = Window().LianJie('tuikuan/', data)
        fanhui = lianjie.get('chenggong')
        if fanhui == True:
            self.tixingkuang.setText(u'处理成功')
            self.tixingkuang.exec_()
            #self.fasongxinhao()
            self.close()#关闭窗口

        else:
            self.tixingkuang.setText(u'发生错误')
            self.tixingkuang.exec_()
    '''
    def fasongxinhao(self):
        self.xinhao.speak.connect(Window().receivslot)
        self.xinhao.speak.emit('shuaxinliebiao')
    '''

class jiezhang_chuangkou(QDialog,Ui_Ui_jiezhang_Dialog):
    def __init__(self, parent=None):
        super(jiezhang_chuangkou, self).__init__(parent)
        self.setupUi(self)
        today = datetime.date.today()
        xianshiqiri = today+ datetime.timedelta(-1)
        self.jiezhang_dateEdit.setDate(xianshiqiri)
        self.anjian_radioButton.toggled.connect(lambda :self.Clickradiobutton())
        self.weiqi_radioButton.toggled.connect(lambda: self.Clickradiobutton())
        self.zongjian_radioButton.toggled.connect(lambda: self.Clickradiobutton())
        self.Button_dayin.setDisabled(True)
        self.Button_chazhaojiehangdan.setDisabled(True)
        self.Button_chazhaojiehangdan.clicked.connect(lambda :self.chazhaojiezhangdan())
        self.Button_dayin.clicked.connect(lambda :self.PrintBill())#当日结账并打印
        self.Button_chongxindayin.clicked.connect(lambda :self.reprint())#单独打印

    def Clickradiobutton(self):
        if self.anjian_radioButton.isChecked():
            self.Button_chazhaojiehangdan.setEnabled(True)
            self.Button_dayin.setEnabled(True)
            self.jiesuangxiangmu = 'anjian'
            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'jiesuanxiangmu':self.jiesuangxiangmu}
            url = dizhi + 'jiezhangyulan/'
            resp = requests.post(url, verify=False, data=json.dumps(data))
            result_rep = resp.content
            with open('shoufeidan.html', 'wb') as f:
                f.write(result_rep)
                f.close()
            self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))
        if self.weiqi_radioButton.isChecked():
            self.Button_chazhaojiehangdan.setEnabled(True)
            self.Button_dayin.setEnabled(True)
            self.jiesuangxiangmu = 'weiqi'
            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'jiesuanxiangmu':self.jiesuangxiangmu}
            url = dizhi + 'jiezhangyulan/'
            resp = requests.post(url, verify=False, data=json.dumps(data))
            result_rep = resp.content
            with open('shoufeidan.html', 'wb') as f:
                f.write(result_rep)
                f.close()
            self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))
        if self.zongjian_radioButton.isChecked():
            self.Button_chazhaojiehangdan.setEnabled(True)
            self.Button_dayin.setEnabled(True)
            self.jiesuangxiangmu = 'zongjian'
            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'jiesuanxiangmu':self.jiesuangxiangmu}
            url = dizhi + 'jiezhangyulan/'
            resp = requests.post(url, verify=False, data=json.dumps(data))
            result_rep = resp.content
            with open('shoufeidan.html', 'wb') as f:
                f.write(result_rep)
                f.close()
            self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))

    def chazhaojiezhangdan(self):#查找结账单
        date_str = self.jiezhang_dateEdit.date().toString("yyyy-MM-dd")
        #datetime格式不能打包到json，这里传输字符串
        data = {'jczid': jcz_id, 'czry': skr_username, 'czry_pass': user_pass,
                'jiesuanxiangmu': self.jiesuangxiangmu,'jiezhangriqi':date_str}
        url = dizhi + 'jiezhangyulan/'

        resp = requests.post(url, verify=False, data=json.dumps(data))
        result_rep = resp.content
        with open('shoufeidan.html', 'wb') as f:
            f.write(result_rep)
            f.close()
        self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))#结账单与收费单使用同一文件

    def PrintBill(self):#当日结账并打印
        jiesuanxiangmu = self.jiesuangxiangmu
        data = {'jczid': jcz_id, 'czry': skr_username, 'czry_pass': user_pass, 'jiesuanxiangmu': jiesuanxiangmu}
        lianjie = Window().LianJie('jiezhang/',data)
        if lianjie.get('jiezhang') == True:
            filename = 'shoufeidan.html'
            Window().HtmlToPDF(filename)
            testprint.printPDF(filename)
            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'jiesuanxiangmu':self.jiesuangxiangmu}
            url = dizhi + 'jiezhangyulan/'
            resp = requests.post(url, verify=False, data=json.dumps(data))
            result_rep = resp.content
            with open('shoufeidan.html', 'wb') as f:
                f.write(result_rep)
                f.close()
            self.webView.load(QUrl.fromLocalFile(os.path.abspath("shoufeidan.html")))
            self.Button_dayin.setDisabled(True)

    def reprint(self):#单独打印
        filename = 'shoufeidan.html'
        Window().HtmlToPDF(filename)
        testprint.printPDF(filename)

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.tixingkuang = QMessageBox()
        global skr_username_str
        self.WindowTitle = u'鑫运统一收费系统，当前登录：'+skr_username_str
        self.setWindowTitle(self.WindowTitle)
        #self.xiugaimima_chuangkou = xiugaimima_chuangkou()
        self.anjian_jine = 0
        self.weiqi_jine = 0
        self.zongjian_jine = 0
        self.zongjian_jine_2 = 0
        self.qita_jine1 = 0
        self.qita_jine2 = 0
        self.qita_jine3 = 0
        self.qita_jine4 = 0
        self.tuijianren.setReadOnly(True)
        #self.tuijianren.setText('123456')
        #self.tuijianren.setText('12')
        self.button_shoukuan.setDisabled(True)
        self.button_chexiao.setDisabled(True)
        #self.tuijianren.setReadOnly(True)
        if not CAN_TUIKUAN:
            self.button_tuikuan.setDisabled(True)
        #self.button_dayin.setDisabled((True))
        #self.button_jiezhang.setDisabled(True)
        #self.button_biaojikaipiao.setDisabled(True)
        #将fukuangfangshi_list更改为由SHOUFEICONFIG获得
        self.fukuangfangshi_list = SHOUFEICONFIG['fukuanfangshi']
        #将cheliang_leixing_list更改为由SHOUFEICONFIG获得
        self.cheliang_leixing_list = SHOUFEICONFIG['cheliangleixing']
        #将chepai_qian更改为由SHOUFEICONFIG获得
        self.chepai_qian.addItems(SHOUFEICONFIG['chepaiqian'])
        #将chepai_zimu更改为由SHOUFEICONFIG获得
        self.chepai_zimu.addItems(SHOUFEICONFIG['chepaizimu'])
        #将chaxun_shoufeixiangmu更改为由SHOUFEICONFIG获得
        self.chaxun_shoufeixiangmu.addItems(SHOUFEICONFIG['chaxunshoufeixiangmu'])
        #将anjianshoufei_xiangmu_dic更改为由SHOUFEICONFIG获得
        self.anjianshoufei_xiangmu_dic = SHOUFEICONFIG['anjianshoufeixiangmudic']
        #将weiqishoufei_xiangmu_list更改为由SHOUFEICONFIG获得
        self.weiqishoufei_xiangmu_list = SHOUFEICONFIG['weiqishoufeixiangmu']
        #将zongjian_xiangmu_list更改为由SHOUFEICONFIG获得
        self.zongjian_xiangmu_list = SHOUFEICONFIG['zongjianshoufeixiangmu']
        #将zongjian_cheliangleixing_list更改为由SHOUFEICONFIG获得
        self.zongjian_cheliangleixing_list = SHOUFEICONFIG['zongjiancheliangleixing']
        #将qita_xiangmu_list更改为由SHOUFEICONFIG获得
        self.qita_xiangmu_list = SHOUFEICONFIG['qitaxiangmu']
        self.cheliang_leixing.addItems(self.cheliang_leixing_list)
        self.chaxun_chepai_qian.addItems(SHOUFEICONFIG['chepaiqian'])
        self.chaxun_chepai_zimu.addItems(SHOUFEICONFIG['chepaizimu'])
        self.start_dateTimeEdit.setDate(datetime.date.today())#设置时间框为今天，setDateTime为设定时间
        self.FreTableOnRun()
        self.chepai_hou.editingFinished.connect(lambda :self.FinishiChePaiHou())
        self.dianhua.editingFinished.connect(lambda :self.FinishDianHua())
        self.cheliang_leixing.activated.connect(lambda : self.Click_cheliangleixing())#绑定下拉列表点击后的动作
        self.anjianshoufei_xiangmu.activated.connect(lambda: self.Click_anjianshoufeixiangmu())  # 绑定下拉列表点击后的动作
        self.weiqishoufei_xiangmu.activated.connect(lambda: self.Click_weiqishoufeixiangmu())
        self.zongjian_xiangmu.activated.connect(lambda :self.Click_zongjianshoufeixiangmu())
        self.zongjian_xiangmu_2.activated.connect(lambda :self.Click_zongjianshoufeixiangmu_2())
        self.qitajine_1.editingFinished.connect(lambda :self.FinishQitajine1())
        self.qitajine_2.editingFinished.connect(lambda: self.FinishQitajine2())
        self.qitajine_3.editingFinished.connect(lambda: self.FinishQitajine3())
        self.qitajine_4.editingFinished.connect(lambda: self.FinishQitajine4())
        self.qita_xiangmu1.activated.connect(lambda :self.Click_qitashoufeixiangmu1())
        self.qita_xiangmu2.activated.connect(lambda: self.Click_qitashoufeixiangmu2())
        self.qita_xiangmu3.activated.connect(lambda: self.Click_qitashoufeixiangmu3())
        self.qita_xiangmu4.activated.connect(lambda: self.Click_qitashoufeixiangmu4())
        self.fukuanfangshi.activated.connect(lambda: self.Click_fukuanfangshi())
        self.button_shoukuan.clicked.connect(lambda: self.ZuHeValue())
        self.button_xiugaimima.clicked.connect(lambda :self.XiuGaiMiMa())
        self.button_chexiao.clicked.connect(lambda :self.CheXiao())
        self.button_biaojikaipiao.clicked.connect(lambda :self.MarkTheInvoice())
        self.button_chaxun.clicked.connect(lambda :self.Search())
        self.button_dayin.clicked.connect(lambda :self.PrintBill())
        self.button_jiezhang.clicked.connect(lambda :self.JieZhang())
        self.liebiao_table.doubleClicked.connect(lambda :self.test())#TODO:测试表格双击动作
        self.button_tuikuan.clicked.connect(lambda :self.tuikuan())
        self.button_fretable.clicked.connect(lambda :self.fretable())
        self.tjrxuanze_Button.clicked.connect(lambda :self.tjrshow())
        self.tjrdel_Button.clicked.connect(lambda :self.tjrdel())
        #self.xinhao = tuijianren_chuangkou().xinhao
        #self.xinhao.speak.connect(self.genggaituijianren)
    '''
    @Slot(str)
    def receivslot(self,str):
        self.str1 = str
        if self.str1 == 'shuaxinliebiao':
            
            self.ReMoveRow()
            self.FreTableOnRun()
    '''

    #@QtCore.Slot(str)
    def tjrdel(self):
        global TJRNAME
        TJRNAME = ''
        self.tuijianren.setText(TJRNAME)
    def genggaituijianren(self,tjrname):
        self.tuijianren.setText(TJRNAME)
    def tjrshow(self):

        self.tuijianren_chuangkou = tuijianren_chuangkou()
        self.xinhao = self.tuijianren_chuangkou.xinhao
        self.xinhao.speak.connect(self.genggaituijianren)
        self.tuijianren_chuangkou.show()
    def XiuGaiMiMa(self):
        self.xiugaimima_chuankou = xiugaimima_chuangkou()
        self.xiugaimima_chuankou.exec_()
    def JieZhang(self):
        self.jiezhang_chuangkou = jiezhang_chuangkou()
        self.jiezhang_chuangkou.exec_()
    def ChangeLcdToZero(self):#将所有金额重置为0并使LCD显示为0
        self.anjian_jine = 0
        self.weiqi_jine = 0
        self.zongjian_jine = 0
        self.zongjian_jine_2 = 0
        self.qita_jine1 = 0
        self.qita_jine2 = 0
        self.qita_jine3 = 0
        self.qita_jine4 = 0
        self.ChangeLcd()
    def ChangeLcd(self):
        self.lcdNumber.display(self.anjian_jine + self.weiqi_jine + self.zongjian_jine+self.qita_jine1
                               +self.qita_jine2+self.qita_jine3+self.qita_jine4+self.zongjian_jine_2)  # 控制LCD显示数字
    def test(self):
        #print self.start_dateTimeEdit.dateTime().toPython()#转换为python datetime格式
        #self.label_xianjin.setText('50')#设置文本内容，只接受str
        #print self.qitajine_1_value
        id_list = []
        rows = self.SelectRow()
        model = self.liebiao_table.model()
        for row in rows:
            index = model.index(row,0)
            id_list.append(int((model.data(index))))



    def CheliangleixingToInt(self,cheliangleixing_str):#将车辆类型文本转化为'01'数字
        dic1 = SHOUFEICONFIG['cheliangleixingtoint']
        return dic1[cheliangleixing_str]

    def Click_cheliangleixing(self):#点击车辆类型
        cheliang_leixing_val = unicode(self.cheliang_leixing.currentText())
        if cheliang_leixing_val != '--':
            if len(self.chepai_hou.text()) == 0:
                self.tixingkuang.setText(u'先输入车牌号码')
                self.tixingkuang.show()
                return
            self.ChangeLcdToZero()
            self.SetAnjianShoufeixiangmu(self.CheliangleixingToInt(cheliang_leixing_val))
            self.SetWeiqiShoufeixiangmu()
            self.SetQitaShoufeixiangmu()
            self.SetFukuangFangshi()
            self.SetZongjianShoufeixiangmu()
            self.SetZongjianShoufeixiangmu_2()
            self.SetZongjianCheliangleixing()
            self.button_chexiao.setEnabled(True)
        self.filltell()
    def SetQitaShoufeixiangmu(self):
        self.qita_xiangmu1.clear()
        self.qita_xiangmu2.clear()
        self.qita_xiangmu3.clear()
        self.qita_xiangmu4.clear()
        self.qita_xiangmu1.addItems(self.qita_xiangmu_list)
        self.qita_xiangmu2.addItems(self.qita_xiangmu_list)
        self.qita_xiangmu3.addItems(self.qita_xiangmu_list)
        self.qita_xiangmu4.addItems(self.qita_xiangmu_list)
        self.qitajine_1.setDisabled(True)
        self.qitajine_2.setDisabled(True)
        self.qitajine_3.setDisabled(True)
        self.qitajine_4.setDisabled(True)

    def SetFukuangFangshi(self):
        self.fukuanfangshi.clear()
        self.fukuanfangshi.addItem('--')
        self.fukuanfangshi.addItems(self.fukuangfangshi_list)

    def SetAnjianShoufeixiangmu(self,cheliangleixingint):
        self.anjianshoufei_xiangmu.clear()
        self.anjianshoufei_xiangmu.addItem('--')
        self.anjianshoufei_xiangmu.addItems(self.anjianshoufei_xiangmu_dic[cheliangleixingint])


    def SetWeiqiShoufeixiangmu(self):
        self.weiqishoufei_xiangmu.clear()
        self.weiqishoufei_xiangmu.addItem('--')
        self.weiqishoufei_xiangmu.addItems(self.weiqishoufei_xiangmu_list)

    def SetZongjianShoufeixiangmu(self):
        self.zongjian_xiangmu.clear()
        self.zongjian_xiangmu.addItem('--')
        self.zongjian_xiangmu.addItems(self.zongjian_xiangmu_list)

    def SetZongjianShoufeixiangmu_2(self):
        self.zongjian_xiangmu_2.clear()
        self.zongjian_xiangmu_2.addItem('--')
        self.zongjian_xiangmu_2.addItems(self.zongjian_xiangmu_list)

    def SetZongjianCheliangleixing(self):
        self.zongjian_cheliangleixing.clear()
        self.zongjian_cheliangleixing.addItems(self.zongjian_cheliangleixing_list)

    def Click_anjianshoufeixiangmu(self):
        #cheliang_leixing_val = unicode(self.cheliang_leixing.currentText())
        anjianshoufeixiangmu_val = unicode(self.anjianshoufei_xiangmu.currentText())
        if anjianshoufeixiangmu_val != '--':
            #self.anjian_jine = self.anjianshoufei_xiangmu_jine_dic[self.CheliangleixingToInt(cheliang_leixing_val)][anjianshoufeixiangmu_val]
            self.anjian_jine = int(anjianshoufeixiangmu_val.split('-')[1])#将金额的获取方式更改为由项目后的数字部分直接提供
            values = self.GetValue()
            cph = values.get('chepaihao')
            cheliangleixingint = values.get('cheliangleixing_id')
            jylb = anjianshoufeixiangmu_val.split('-')[0]
            self.VerifRePay(jylb,cph,cheliangleixingint)
        self.ChangeLcd()

    #点击尾气收费项目下拉列表
    def Click_weiqishoufeixiangmu(self):
        weiqishoufeixiangmu_val = unicode(self.weiqishoufei_xiangmu.currentText())
        if weiqishoufeixiangmu_val != '--':
            self.weiqi_jine = int(weiqishoufeixiangmu_val.split('-')[1])#将尾气收费金额的获取方式更改为直接读取收费项目的数字部分
            values = self.GetValue()
            cph = values.get('chepaihao')
            cheliangleixingint = values.get('cheliangleixing_id')
            is_zhuanru = values.get('is_zhuanru')
            if cheliangleixingint == '16':
                cph = cph + u'学'
            elif cheliangleixingint == '23':
                cph = cph + u'警'
            if is_zhuanru == True:
                cph = u'转' + cph
            jylb = weiqishoufeixiangmu_val.split('-')[0]
            self.VerifRePay(jylb,cph,cheliangleixingint)

        self.ChangeLcd()

    def Click_zongjianshoufeixiangmu(self):
        zongjianshoufeixiangmu_val = unicode(self.zongjian_xiangmu.currentText())
        if zongjianshoufeixiangmu_val != '--':
            values = self.GetValue()
            cph = values.get('chepaihao')
            cheliangleixingint = values.get('cheliangleixing_id')
            jylb = zongjianshoufeixiangmu_val.split('-')[0]
            #self.zongjian_jine = self.zongjian_xiangmu_jine_dic[zongjianshoufeixiangmu_val]
            self.zongjian_jine = int(zongjianshoufeixiangmu_val.split('-')[1])
            self.VerifRePay(jylb, cph, cheliangleixingint)
        self.ChangeLcd()


    def Click_zongjianshoufeixiangmu_2(self):
        zongjianshoufeixiangmu_2_val = unicode(self.zongjian_xiangmu_2.currentText())
        if zongjianshoufeixiangmu_2_val != '--':
            values = self.GetValue()
            cph = values.get('chepaihao')
            cheliangleixingint = values.get('cheliangleixing_id')
            self.zongjian_jine_2 = int(zongjianshoufeixiangmu_2_val.split('-')[1])
            jylb = zongjianshoufeixiangmu_2_val.split('-')[0]
            self.VerifRePay(jylb, cph, cheliangleixingint)
        self.ChangeLcd()

    def Click_qitashoufeixiangmu1(self):
        qitashoufeixiangmu_val = unicode(self.qita_xiangmu1.currentText())
        if qitashoufeixiangmu_val != '--':
            self.qitajine_1.setDisabled(False)
            self.qitajine_1.setText('0')

    def Click_fukuanfangshi(self):
        fukuanfangshi_val = unicode(self.fukuanfangshi.currentText())
        if fukuanfangshi_val != '--':
            panduan = self.PanDuanValue()
            if panduan.get('panduan') == True:
                self.button_shoukuan.setEnabled(True)
            else:
                self.tixingkuang.setText(panduan.get('cuowu'))
                self.tixingkuang.exec_()

    def Click_qitashoufeixiangmu2(self):
        qitashoufeixiangmu_val = unicode(self.qita_xiangmu2.currentText())
        if qitashoufeixiangmu_val != '--':
            self.qitajine_2.setDisabled(False)
            self.qitajine_2.setText('0')

    def Click_qitashoufeixiangmu3(self):
        qitashoufeixiangmu_val = unicode(self.qita_xiangmu3.currentText())
        if qitashoufeixiangmu_val != '--':
            self.qitajine_3.setDisabled(False)
            self.qitajine_3.setText('0')

    def Click_qitashoufeixiangmu4(self):
        qitashoufeixiangmu_val = unicode(self.qita_xiangmu4.currentText())
        if qitashoufeixiangmu_val != '--':
            self.qitajine_4.setDisabled(False)
            self.qitajine_4.setText('0')
    #验证车牌号数字字母部分
    def FinishiChePaiHou(self):
        Chepai_zimu = self.chepai_zimu.currentText()#新车注册时不输入车牌后字母部分
        ChePai_hou = self.chepai_hou.text()
        """
        try:
            str(ChePai_hou).upper()
        except:
            self.chepai_hou.clear()
            self.tixingkuang.setText(u"只能使用数字和字母组合且不区分大小写")
            self.tixingkuang.exec_()
            return
        """
        if Chepai_zimu != '--':

            if len(ChePai_hou) > 6:
                self.chepai_hou.clear()
                self.tixingkuang.setText(u'车牌号码长度不正确')
                self.tixingkuang.exec_()
        elif Chepai_zimu == '--':
            if len(ChePai_hou) != 6:
                self.chepai_hou.clear()
                self.tixingkuang.setText(u'新车注册输入六位车牌号')
                self.tixingkuang.exec_()

    def FinishDianHua(self):
        dianhua = self.dianhua.text()
        re_dianhua = ur"[0-9]*$"
        if not re.match(re_dianhua,dianhua):
            self.tixingkuang.setText(u'只能输入电话号码')
            self.tixingkuang.exec_()
            self.dianhua.clear()
        if len(dianhua) != 11 or dianhua[0] != '1':
            self.tixingkuang.setText(u'电话号码位数不对')
            self.tixingkuang.exec_()
            self.dianhua.clear()

    def FinishQitajine1(self):
        try:
            self.qita_jine1 = int(self.qitajine_1.text())
        except:
            self.tixingkuang.setText(u'只能输入整数')
            self.tixingkuang.exec_()
            self.qitajine_1.clear()
            self.ChangeLcdToZero()
        self.ChangeLcd()

    def FinishQitajine2(self):
        try:
            self.qita_jine2 = int(self.qitajine_2.text())
        except:
            self.tixingkuang.setText(u'只能输入整数')
            self.tixingkuang.exec_()
            self.qitajine_2.clear()
            self.ChangeLcdToZero()
        self.ChangeLcd()

    def FinishQitajine3(self):
        try:
            self.qita_jine3 = int(self.qitajine_3.text())
        except:
            self.tixingkuang.setText(u'只能输入整数')
            self.tixingkuang.exec_()
            self.qitajine_3.clear()
            self.ChangeLcdToZero()
        self.ChangeLcd()

    def FinishQitajine4(self):
        try:
            self.qita_jine4 = int(self.qitajine_4.text())
        except:
            self.tixingkuang.setText(u'只能输入整数')
            self.tixingkuang.exec_()
            self.qitajine_4.clear()
            self.ChangeLcdToZero()
        self.ChangeLcd()

    def CheXiao(self):
        global TJRNAME
        TJRNAME = ''
        self.chaxun_chepai_hou.clear()
        self.chepai_hou.clear()
        self.cheliang_leixing.clear()
        self.cheliang_leixing.addItems(self.cheliang_leixing_list)
        self.dianhua.clear()
        self.anjianshoufei_xiangmu.clear()
        self.is_kefu.setChecked(False)
        self.weiqishoufei_xiangmu.clear()
        self.zongjian_xiangmu.clear()
        self.zongjian_xiangmu_2.clear()
        self.is_zhuanru.setChecked(False)
        self.qita_xiangmu1.clear()
        self.qitajine_1.clear()
        self.qitajine_1.setDisabled(True)
        self.qita_xiangmu2.clear()
        self.qitajine_2.clear()
        self.qitajine_2.setDisabled(True)
        self.qita_xiangmu3.clear()
        self.qitajine_3.clear()
        self.qitajine_3.setDisabled(True)
        self.qita_xiangmu4.clear()
        self.qitajine_4.clear()
        self.qitajine_4.setDisabled(True)
        self.fukuanfangshi.clear()
        self.pingzhenghao.clear()
        self.ChangeLcdToZero()
        self.button_shoukuan.setDisabled(True)
        self.button_chexiao.setDisabled(True)
        self.tuijianren.clear()

    def MarkTheInvoice(self):#标记开发票
        id_list = []
        rows = self.SelectRow()
        model = self.liebiao_table.model()
        for row in rows:
            index = model.index(row,0)
            id_list.append(int((model.data(index))))
        data = {'jczid': jcz_id, 'czry': skr_username, 'czry_pass': user_pass,'id_list':id_list}
        lianjie = self.LianJie('biaojikaipiao/', data)
        shibai_list = lianjie.get('shibai_list')
        shibai_str = ''
        if shibai_list != None:
            shibai_str = ','.join(shibai_list)
        if shibai_str != '':
            self.tixingkuang.setText(u'失败车辆：'+shibai_str+u'可能已经开过发票了，请检查')
            self.tixingkuang.exec_()
        self.ReMoveRow()
        self.FreTableOnRun()

    def tuikuan(self):
        global ID_LIST

        id_list = []
        rows = self.SelectRow()
        model = self.liebiao_table.model()
        for row in rows:
            index = model.index(row,0)
            id_list.append(int((model.data(index))))
        if len(id_list) == 0 or len(id_list) != 1:
            self.tixingkuang.setText(u'一次只能选择一条记录')
            self.tixingkuang.exec_()
            return
        ID_LIST = id_list
        self.tuikuanyuanyin()

    def tuikuanyuanyin(self):
        self.tuikuanyuanyin_chuankou = tuikuanyuanyin_chuangkou()
        self.tuikuanyuanyin_chuankou.exec_()

    def en_cn_upper(self,str_input):
        """将中英文混合字符串转化为大写"""
        tmplist = []
        for i in str_input:
            try:
                i.upper()
            except:
                tmplist.append(i)
            tmplist.append(i.upper())
        return ''.join(tmplist)


    def GetValue(self):
        self.chepai_qian_value = unicode(self.chepai_qian.currentText())#车牌前
        self.chepai_zimu_value = str(self.chepai_zimu.currentText())#车牌字母
        if self.chepai_zimu_value == '--':
            self.chepai_zimu_value = ''
        #self.chepai_hou_value = str(self.chepai_hou.text()).upper()#车牌后组合部分
        #self.chepai_hou_value = self.chepai_hou.text()  # 车牌后组合部分
        self.chepai_hou_value = self.en_cn_upper(self.chepai_hou.text())
        self.chepaihao = self.chepai_qian_value+self.chepai_zimu_value+self.chepai_hou_value
        self.cheliang_leixing_value_str = unicode(self.cheliang_leixing.currentText())#车辆类型字符串
        self.cheliang_leixing_value_id = self.CheliangleixingToInt(self.cheliang_leixing_value_str)#车辆类型ID
        self.dianhua_value = self.dianhua.text()#电话，返回字符串
        if len(self.dianhua_value) == 0:
            self.dianhua_value = ''
        #判断安检收费项目并得到金额
        self.anjianshoufei_xiangmu_value = unicode(self.anjianshoufei_xiangmu.currentText())
        if self.anjianshoufei_xiangmu_value != '--':
            self.anjianshoufei_xiangmu_value_str = self.anjianshoufei_xiangmu_value.split('-')[0]
            self.anjianshoufei_xiangmu_value_jine = int(self.anjianshoufei_xiangmu_value.split('-')[1])
        else:
            self.anjianshoufei_xiangmu_value_str = None
            self.anjianshoufei_xiangmu_value_jine = None
        self.is_kefu_value = self.is_kefu.isChecked()#是否客服
        #判断尾气收费项目并得到金额
        self.weiqishoufei_xiangmu_value = unicode(self.weiqishoufei_xiangmu.currentText())
        if self.weiqishoufei_xiangmu_value != '--':
            self.weiqishoufei_xiangmu_value_str = self.weiqishoufei_xiangmu_value.split('-')[0]
            self.weiqishoufei_xiangmu_value_jine = int(self.weiqishoufei_xiangmu_value.split('-')[1])
        else:
            self.weiqishoufei_xiangmu_value_str = None
            self.weiqishoufei_xiangmu_value_jine = None
        self.is_zhuanru_value = self.is_zhuanru.isChecked()#是否转入
        #判断综检收费项目并得到金额
        self.zongjianshoufeixiangmu_value = unicode(self.zongjian_xiangmu.currentText())
        if self.zongjianshoufeixiangmu_value != '--':
            self.zongjianshoufeixiangmu_value_str = self.zongjianshoufeixiangmu_value.split('-')[0]
            self.zongjianshoufeixiangmu_value_jine = int(self.zongjianshoufeixiangmu_value.split('-')[1])
        else:
            self.zongjianshoufeixiangmu_value_str = None
            self.zongjianshoufeixiangmu_value_jine = None
        #判断综检收费项目2并得到金额
        self.zongjianshoufeixiangmu_2_value = unicode(self.zongjian_xiangmu_2.currentText())
        if self.zongjianshoufeixiangmu_2_value != '--':
            self.zongjianshoufeixiangmu_2_value_str = self.zongjianshoufeixiangmu_2_value.split('-')[0]
            self.zongjianshoufeixiangmu_2_value_jine = int(self.zongjianshoufeixiangmu_2_value.split('-')[1])
        else:
            self.zongjianshoufeixiangmu_2_value_str = None
            self.zongjianshoufeixiangmu_2_value_jine = None
        self.zongjiancheliangleixing = unicode(self.zongjian_cheliangleixing)
        if self.zongjianshoufeixiangmu_value == '--' and self.zongjianshoufeixiangmu_2_value == '--':
            self.zongjian_cheliangleixing_str = None
        else:
            self.zongjian_cheliangleixing_str = unicode(self.zongjian_cheliangleixing.currentText())
        #判断综检是否需要立即打印
        #self.zongjianisdayin = self.zongjian_is_dayin.isChecked()

        #判断其他收费项目和金额
        self.qita_xiangmu1_value = unicode(self.qita_xiangmu1.currentText())
        if self.qita_xiangmu1_value != '--':
            self.qitajine_1_value = int(self.qitajine_1.text())#返回整数
        else:
            self.qitajine_1_value = 0
        self.qita_xiangmu2_value = unicode(self.qita_xiangmu2.currentText())
        if self.qita_xiangmu2_value != '--':
            self.qitajine_2_value = int(self.qitajine_2.text())#返回整数
        else:
            self.qitajine_2_value = 0
        self.qita_xiangmu3_value = unicode(self.qita_xiangmu3.currentText())
        if self.qita_xiangmu3_value != '--':
            self.qitajine_3_value = int(self.qitajine_3.text())#返回整数
        else:
            self.qitajine_3_value = 0
        self.qita_xiangmu4_value = unicode(self.qita_xiangmu4.currentText())
        if self.qita_xiangmu4_value != '--':
            self.qitajine_4_value = int(self.qitajine_4.text())#返回整数
        else:
            self.qitajine_4_value = 0
        #判断付款方式
        self.fukuanfangshi_value = unicode(self.fukuanfangshi.currentText())
        #判断凭证号
        if self.fukuanfangshi_value != u'现金':
            self.pingzhenghao_value = str(self.pingzhenghao.text())
        else:
            self.pingzhenghao_value = None
        self.tuijianren_input = self.tuijianren.text()
        value =  {'chepaihao':self.chepaihao,
               'cheliangleixing_str':self.cheliang_leixing_value_str,
               'cheliangleixing_id':self.cheliang_leixing_value_id,
               'dianhua':self.dianhua_value,
               'anjianshoufei_xiangmu':self.anjianshoufei_xiangmu_value_str,
               'anjianshoufei_jine':self.anjianshoufei_xiangmu_value_jine,
               'weiqishoufei_xiangmu':self.weiqishoufei_xiangmu_value_str,
               'weiqishoufei_jine':self.weiqishoufei_xiangmu_value_jine,
               'zongjianshoufei_xiangmu':self.zongjianshoufeixiangmu_value_str,
               'zongjianshoufei_jine':self.zongjianshoufeixiangmu_value_jine,
               'zongjianshoufei_xiangmu_2':self.zongjianshoufeixiangmu_2_value_str,
               'zongjianshoufei_jine_2':self.zongjianshoufeixiangmu_2_value_jine,
               'zongjian_cheliangleixing':self.zongjian_cheliangleixing_str,
               'is_kefu':self.is_kefu_value,
               'is_zhuanru':self.is_zhuanru_value,
               'qita_xiangmu1':self.qita_xiangmu1_value,
               'qitajine_1':self.qitajine_1_value,
               'qita_xiangmu2': self.qita_xiangmu2_value,
               'qitajine_2': self.qitajine_2_value,
               'qita_xiangmu3': self.qita_xiangmu3_value,
               'qitajine_3': self.qitajine_3_value,
               'qita_xiangmu4': self.qita_xiangmu4_value,
               'qitajine_4': self.qitajine_4_value,
               'fukuanfangshi':self.fukuanfangshi_value,
               'pingzhenghao':self.pingzhenghao_value,
                'tuijianren':self.tuijianren_input}
        return value

    def PanDuanValue(self):
        value = self.GetValue()
        if value.get('anjianshoufei_xiangmu') == None and value.get('weiqishoufei_xiangmu') == None and value.get('zongjianshoufei_xiangmu') == None \
                and value.get('qita_xiangmu1') == '--' and value.get('zongjianshoufei_xiangmu_2') == None \
                and value.get('qita_xiangmu2') == '--' and value.get('qita_xiangmu3') == '--' and value.get('qita_xiangmu4') == '--':
            return {'panduan':False,'cuowu':u'没有任何收费项目'}
        qitaxiangmu_list = [value.get('qita_xiangmu1'),value.get('qita_xiangmu2'),
                            value.get('qita_xiangmu3'),value.get('qita_xiangmu4')]
        if len([i for i,x in enumerate(qitaxiangmu_list) if x==u'服务费']) > 1:
            return {'panduan':False,'cuowu':u'有多个服务费项目'}
        if self.lcdNumber.value() != 0:
            return {'panduan':True}
        #if value.get('fukuanfangshi') != u'现金' and value.get('pingzhenghao') == None:
            #return {'panduan':False,'cuowu':u'非现金支付必须填写凭证号'}

        else:
            return {'panduan':False,'cuowu':u'检查收费项目是否为0'}

    def ZuHeValue(self):

        if self.verifTellNum():
            self.tixingkuang = QMessageBox()
            panduan = self.PanDuanValue()
            if panduan.get('panduan') != True:

                self.tixingkuang.setText(u'判断值时发生错误：'+panduan.get('cuowu'))
                self.tixingkuang.exec_()
                return
            values = self.GetValue()
            if values.get('fukuanfangshi') != u'现金' and values.get('pingzhenghao') == '':
                self.tixingkuang.setText(u'非现金支付必须填写凭证号!')
                self.tixingkuang.exec_()
                return

            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,
                'cph':values.get('chepaihao'),'pzlb':values.get('cheliangleixing_id'),
                'pzlb_str':values.get('cheliangleixing_str'),'chezhudh':values.get('dianhua'),
                'fkfs':values.get('fukuanfangshi'),'tuijianren':values.get('tuijianren'),'data':{}}
            if values.get('anjianshoufei_xiangmu') != None:
                qitaxiangmu_list = [values.get('qita_xiangmu1'), values.get('qita_xiangmu2'),
                                values.get('qita_xiangmu3'), values.get('qita_xiangmu4')]
                fuwufei_jine = 0
                if u'服务费' in qitaxiangmu_list:
                    fuwufei_index = qitaxiangmu_list.index(u'服务费')
                    if fuwufei_index == 0:
                        fuwufei_jine = values.get('qitajine_1')
                    elif fuwufei_index ==1:
                        fuwufei_jine = values.get('qitajine_2')
                    elif fuwufei_index ==2:
                        fuwufei_jine = values.get('qitajine_3')
                    elif fuwufei_index ==3:
                        fuwufei_jine = values.get('qitajine_4')
                data['data']['anjian'] = {'jylb':values.get('anjianshoufei_xiangmu'),
                                      'jfje':values.get('anjianshoufei_jine')+fuwufei_jine,
                                      'is_kefu':values.get('is_kefu')}
            if values.get('weiqishoufei_xiangmu') != None:
                data['data']['weiqi'] = {'jylb':values.get('weiqishoufei_xiangmu'),
                                     'jfje':values.get('weiqishoufei_jine'),
                                     'is_zhuanru':values.get('is_zhuanru')}
            if values.get('zongjianshoufei_xiangmu') !=None:
                data['data']['zongjian1'] = {'jylb':values.get('zongjianshoufei_xiangmu'),
                                            'jfje':values.get('zongjianshoufei_jine'),
                                            'zongjian_cheliangleixing':values.get('zongjian_cheliangleixing'),
                                            }
            if values.get('zongjianshoufei_xiangmu_2') !=None:
                data['data']['zongjian2'] = {'jylb':values.get('zongjianshoufei_xiangmu_2'),
                                             'jfje':values.get('zongjianshoufei_jine_2'),
                                             'zongjian_cheliangleixing':values.get('zongjian_cheliangleixing')}

            qita_tijiao = {}
            if values.get('qita_xiangmu1') != '--' and values.get('qita_xiangmu1') !=u'服务费':
                qita_tijiao[values.get('qita_xiangmu1')]=values.get('qitajine_1')
            if values.get('qita_xiangmu2') != '--' and values.get('qita_xiangmu2') !=u'服务费':
                qita_tijiao[values.get('qita_xiangmu2')]=values.get('qitajine_2')
            if values.get('qita_xiangmu3') != '--' and values.get('qita_xiangmu3') !=u'服务费':
                qita_tijiao[values.get('qita_xiangmu3')]=values.get('qitajine_3')
            if values.get('qita_xiangmu4') != '--' and values.get('qita_xiangmu4') !=u'服务费':
                qita_tijiao[values.get('qita_xiangmu4')]=values.get('qitajine_4')
            data['data']['qita'] = qita_tijiao
            self.tixingkuang.setText(u'请核对所有信息，是否提交？')
            self.tixingkuang.setStandardButtons(QMessageBox.Save |  QMessageBox.Cancel)
            self.tixingkuang.setDefaultButton(QMessageBox.Save)
            ret = self.tixingkuang.exec_()
            if ret == QMessageBox.Save:
                lianjie = self.LianJie('shoufei/',data)
                if lianjie:
                    self.ReMoveRow()
                    self.FreTableOnRun()
                else:
                    self.tixingkuang.setText(u'lianjie返回不正确')
                    self.tixingkuang.exec_()
            if ret == QMessageBox.Cancel:
                return
    #程序开始运行时刷新列表并更新收款统计数据
    def FreTableOnRun(self):
        data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass}
        lianjie = self.LianJie('shuaxin/',data)
        self.qs_list = lianjie.get('qs')
        groupbypaysum = lianjie.get('groupsum')
        #self.liebiao_table = QTableWidget()
        self.SetLable(groupbypaysum)
        self.CheXiao()
        Header_list = ['ID', u'车牌号', u'车辆类别', u'收款项目', u'检验项目', u'收款金额', u'收款日期', u'收款人', u'支付方式',
                            u'发票开具日期',u'客服',u'结账日期']
        liekuan_list = [40, 70, 70, 50, 110, 50, 150, 80, 80, 130, 50,140]
        self.FillTable(Header_list,liekuan_list,self.qs_list)

    def fretable(self):
        self.chaxun_chepai_hou.clear()
        self.ReMoveRow()
        self.FreTableOnRun()

    def VerifRePay(self,jylb_str,cph,cheliangleixingint):
        data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'jylb_str':jylb_str,'cph':cph,
                'cheliangleixingint':cheliangleixingint}
        lianjie = self.LianJie('verifrepay/',data)
        if lianjie.get('skrq') != None:
            self.tixingkuang.setText(u'该车已于'+unicode((lianjie.get('skrq'))+u'缴费，是否继续缴费'))
            self.tixingkuang.addButton(u'是',QMessageBox.AcceptRole)
            self.tixingkuang.addButton(u'否',QMessageBox.RejectRole)
            ret = self.tixingkuang.exec_()
            if ret == QMessageBox.AcceptRole:
                return
            if ret == QMessageBox.RejectRole:
                self.CheXiao()

    def verifTellNum(self):
        tellNum = self.dianhua.text()
        if tellNum:
            data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'tellnum':tellNum}
            lianjie = self.LianJie('veriftellnum/',data)
            guishudi = lianjie.get('guishudi')#归属地
            cishu = lianjie.get('cishu')#出现次数
            if guishudi and cishu:
                if guishudi != u'内蒙古' or cishu >10:
                    self.tixingkuang = QMessageBox()
                    self.tixingkuang.setText(u'该电话号码归属地为'+guishudi+u'或者此电话号码已出现过'+str(cishu)+u',是否继续？')
                    self.tixingkuang.addButton(u'是', QMessageBox.AcceptRole)
                    self.tixingkuang.addButton(u'否', QMessageBox.RejectRole)
                    ret = self.tixingkuang.exec_()
                    if ret == QMessageBox.AcceptRole:
                        return True
                    if ret == QMessageBox.RejectRole:
                        self.dianhua.clear()
                        return False
                else:
                    return True
            else:
                self.tixingkuang.setText('guishudi or cishu is None')
                self.tixingkuang.exec_()
                return False
        else:
            return True





    def filltell(self):
        getval = self.GetValue()
        chepaihao = getval.get('chepaihao')
        cheliangleixing_id = getval.get('cheliangleixing_id')
        data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'cph':chepaihao,
                'cheliangleixingint':cheliangleixing_id}
        lianjie = self.LianJie('searchtell/',data)
        dianhua = lianjie.get('dianhua')
        tjr = lianjie.get('tjr')
        if dianhua:
            self.dianhua.setText(dianhua)
        if tjr:
            self.tuijianren.setText(tjr)




    def FillTable(self,Header_list,liekuan_list,qs_list):
        self.liebiao_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.liebiao_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.liebiao_table.setColumnCount(len(Header_list))

        for i in liekuan_list:
            self.liebiao_table.setColumnWidth(liekuan_list.index(i), i)
        self.liebiao_table.setHorizontalHeaderLabels(Header_list)
        if qs_list != None:

            for a in qs_list:
                jyxm = ''
                if a.get('jyxm') == 'anjian':
                    jyxm = u'安检'
                elif a.get('jyxm') == 'weiqi':
                    jyxm = u'尾气'
                elif a.get('jyxm') == 'qita':
                    jyxm = u'其他'
                elif a.get('jyxm') == 'zongjian':
                    jyxm = u'综检'
                is_kefu = ''
                if a.get('is_kefu') == True:
                    is_kefu =u'客服'
                jiezhangriqi = a.get('jiezhangriqi')
                if jiezhangriqi == None:
                    jiezhangriqi = ''
                rowPosition = self.liebiao_table.rowCount()
                self.liebiao_table.insertRow(rowPosition)
                self.liebiao_table.setItem(rowPosition, 0, QTableWidgetItem(str(a.get('id'))))
                self.liebiao_table.setItem(rowPosition, 1, QTableWidgetItem(a.get('paizhaohao')))
                self.liebiao_table.setItem(rowPosition, 2, QTableWidgetItem(a.get('cheliangleibie_str')))
                self.liebiao_table.setItem(rowPosition, 3, QTableWidgetItem(jyxm))
                self.liebiao_table.setItem(rowPosition, 4, QTableWidgetItem(a.get('jylb')))
                self.liebiao_table.setItem(rowPosition, 5, QTableWidgetItem(str(a.get('skje'))))
                self.liebiao_table.setItem(rowPosition, 6, QTableWidgetItem(str(a.get('skrq'))[:19].replace('T',' ')))
                self.liebiao_table.setItem(rowPosition, 7, QTableWidgetItem(a.get('skr')))
                self.liebiao_table.setItem(rowPosition, 8, QTableWidgetItem(a.get('zhifufangshi_str')))
                self.liebiao_table.setItem(rowPosition, 9, QTableWidgetItem(a.get('fapiao_qiri')))
                self.liebiao_table.setItem(rowPosition, 10, QTableWidgetItem(is_kefu))
                self.liebiao_table.setItem(rowPosition, 11, QTableWidgetItem(str(jiezhangriqi)[:19].replace('T',' ')))

    def ReMoveRow(self):
        shu = self.liebiao_table.rowCount()
        for i in range(shu):
            self.liebiao_table.removeRow(0)

    def SelectRow(self):
        return_list =[]
        row = self.liebiao_table.selectionModel().selectedRows()
        if len(row) == 0:
            self.tixingkuang.setText(u'至少选择一行,可多选')
            self.tixingkuang.exec_()
            return
        for i in row:
            return_list.append(i.row())
        return return_list

    def SetLable(self,groupbypaysum):#设置总计分类显示在主屏幕上
        if groupbypaysum == None:
            xianjin = 0
            weixin = 0
            zhifubao = 0
            yufufei = 0
            yinhangka = 0
            self.label_xianjin.setText(str(xianjin))
            self.label_weixin.setText(str(weixin))
            self.label_zhifubao.setText(str(zhifubao))
            self.label_yufufeika.setText(str(yufufei))
            self.label_yinhangka.setText(str(yinhangka))
        else:
            for i in groupbypaysum:
                if i.get('zhifufangshi_zimu') == '01':
                    self.label_xianjin.setText(str(i.get('skje')))
                elif i.get('zhifufangshi_zimu') == '02':
                    self.label_weixin.setText(str(i.get('skje')))
                elif i.get('zhifufangshi_zimu') == '03':
                    self.label_zhifubao.setText(str(i.get('skje')))
                elif i.get('zhifufangshi_zimu') == '04':
                    self.label_yufufeika.setText(str(i.get('skje')))
                elif i.get('zhifufangshi_zimu') == '05':
                    self.label_yinhangka.setText(str(i.get('skje')))
                elif i.get('zhifufangshi_zimu') == '06':
                    self.label_naerjian.setText(str(i.get('skje')))

        '''
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
        '''

    def Search(self):
        #TODO:需要完成加时间的综合查询,完成多项选择后的打印功能
        chepaiqian = unicode(self.chaxun_chepai_qian.currentText())
        chepaizimu = str(self.chaxun_chepai_zimu.currentText())
        chepaihou = str(self.chaxun_chepai_hou.text()).upper()
        shoufeixiangmu = unicode(self.chaxun_shoufeixiangmu.currentText())
        if len(chepaihou) == 0 :
            if self.is_time.isChecked() != True and shoufeixiangmu == '--':
                self.tixingkuang = QMessageBox()
                self.tixingkuang.setText(u'需要输入车牌号，按时间与检验类别查询不需输入车牌号')
                self.tixingkuang.exec_()
                return

        cph = chepaiqian+chepaizimu+chepaihou
        if chepaizimu == '--':
            cph = chepaiqian+chepaihou
        if shoufeixiangmu == '--':
            shoufeixiangmu = None

        elif shoufeixiangmu == u'安检':
            shoufeixiangmu = 'anjian'
        elif shoufeixiangmu == u'尾气':
            shoufeixiangmu = 'weiqi'
        elif shoufeixiangmu == u'其他':
            shoufeixiangmu = 'qita'

        data = {'jczid':jcz_id,'czry':skr_username,'czry_pass':user_pass,'cph':cph,
                'shoufeixiangmu':shoufeixiangmu}
        lianjie = self.LianJie('search/', data)
        if lianjie.get('qs') == None:
            self.tixingkuang=QMessageBox()
            self.tixingkuang.setText(u'没有查询结果')
            self.tixingkuang.exec_()
        else:
            self.ReMoveRow()
            Header_list = ['ID', u'车牌号', u'车辆类别', u'收款项目', u'检验项目', u'收款金额', u'收款日期', u'收款人', u'支付方式',
                           u'发票开具日期', u'客服',u'结账日期']
            liekuan_list = [40, 70, 70, 50, 110, 50, 150, 80, 80, 130, 50,140]
            qs_list = lianjie.get('qs')
            self.FillTable(Header_list,liekuan_list,qs_list)
    def PrintBill(self):
        id_list=[]
        rows=self.SelectRow()
        if len(rows) >1:
            self.tixingkuang = QMessageBox()
            self.tixingkuang.setText(u'不能多选，只能单选，多张单据依次打印。')
            self.tixingkuang.exec_()
        else:
            model = self.liebiao_table.model()
            for row in rows:
                index = model.index(row, 0)
                id_list.append(int((model.data(index))))
            id = id_list[0]
            url = 'shoufeidandayin/%d/' % id
            filename = self.SaveHtml(url,'shoufeidan.html')
            #self.HtmlToPDF(filename)
            self.shoufeidanyulan_chuankou = shoufeidanyulan_chuangkou()
            self.shoufeidanyulan_chuankou.exec_()


    def SaveHtml(self,url_in,filename):
        url = dizhi+url_in
        resp = requests.post(url, verify=False)
        result_rep = resp.content
        with open(filename, 'wb') as f:
            f.write(result_rep)
            f.close()
        return filename

    def HtmlToPDF(self,filename):
        sourceHtml = open(filename, 'rb')
        outputFilename = filename.split('.')[0]+'.pdf'
        resultFile = open(outputFilename, "w+b")
        pisa.CreatePDF(
            sourceHtml,  # the HTML to con,vert
            dest=resultFile)  # file handle to recieve result
        resultFile.close()





    def LianJie(self,str_lianjie,data):
        self.tixingkuang = QMessageBox()
        fasong_data = data
        url = dizhi + str_lianjie
        try:  # 处理连接时候的异常
            resp = requests.post(url, verify=False, data=json.dumps(fasong_data),timeout=3)
        except Exception, e:
            e = repr(e)  # 避免出现中文字符
            f = open('error.log', 'a')  # 文件追加模式
            s1 = str(datetime.datetime.now()) + '--' + e + '\n'
            f.write(s1)
            f.close()
            self.tixingkuang.setText(u'连接出现错误，查看日志文件')
            self.tixingkuang.exec_()
            sys.exit(app.exit())
        result_rep = resp.content
        try:  # 处理接受json的异常
            result = json.loads(result_rep)
        except:
            f = open('error.log', 'a')
            f.write(result_rep)
            f.close()
            self.tixingkuang.setText(u'返回结果格式不正确,注意查看日志')
            self.tixingkuang.exec_()
            sys.exit(app.exit())
        if result.get('chenggong') == None:
            self.tixingkuang.setText(u'字段为空')
            self.tixingkuang.exec_()
            sys.exit(app.exit())
        elif result.get('chenggong') != True:
            self.tixingkuang.setText(result.get('cuowu'))
            self.tixingkuang.exec_()
            sys.exit(app.exit())

        elif result.get('chenggong') == True:
            data = result.get('data')
            if data is None:
                self.tixingkuang.setText(u'data为空')
                self.tixingkuang.exec_()
                sys.exit(app.exit())
            else:
                return data

class tuijianren_chuangkou(QDialog,Ui_TuiJianRen_UI_Dialog):
    def __init__(self, parent=None):
        super(tuijianren_chuangkou, self).__init__(parent)
        self.setupUi(self)
        self.xinhao = xinhao_class()
        self.tishikuang = QMessageBox()
        self.recommenderlist = self.getrecommenderlist()
        #print 'recommenderlist',self.recommenderlist
        #设置自动完成
        completer = QCompleter()
        self.tjrname_input.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.get_data(model)
        self.queding_Button.clicked.connect(lambda: self.queding())
        self.zengjia_Button.clicked.connect(lambda :self.zengjia())

    def getrecommenderlist(self):
        data = {'jczid': jcz_id}
        lianjie = Window().LianJie('getrecommenderlist/', data)
        recommenderlist = lianjie.get('recommenderlist')
        return recommenderlist

    def get_data(self,model):
        model.setStringList(self.recommenderlist)

    def queding(self):
        self.nameinput = unicode(self.tjrname_input.text())
        if self.nameinput not in self.recommenderlist:
            self.tishikuang.setText(u'没有该人员的信息，请在输入人员电话号码后点击“添加”按钮！')
            self.tishikuang.exec_()
            return
        global TJRNAME
        TJRNAME = self.nameinput
        self.fasongxinhao()
        self.close()

    def fasongxinhao(self):
        #在需要发送信号的类中声明信号，然后在接收信号的类中先加入发送类的实例然后连接信号，发送类中只发送，接收类中只接收
        self.xinhao.speak.emit('genggaituijianren')

    def zengjia(self):
        name = unicode(self.tjrname_input.text())
        if name in self.recommenderlist:
            self.tishikuang.setText(u'该人员已经存在于列表中，不能再添加！')
            self.tishikuang.exec_()
            return
        tellnumber = self.tjrtellnumber_input.text()
        data = {'jczid': jcz_id,'name':name,'tellnumber':tellnumber}
        lianjie = Window().LianJie('addrecommender/', data)
        q = lianjie.get('chenggong')
        if q :
            global TJRNAME
            TJRNAME = name
            self.fasongxinhao()
            self.close()









if __name__ == '__main__':

    app = QApplication(sys.argv)

    if denglu_chuangkou().exec_() == QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
