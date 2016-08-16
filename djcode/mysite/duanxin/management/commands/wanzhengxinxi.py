#coding=utf-8

from django.core.management.base import BaseCommand, CommandError
from duanxin.models import *
import datetime
import pymssql

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'
    def handle(self, *args, **options):
        qs = DX_CarInfo.objects.filter(iswanzheng=False)
        print len(qs)
        conn = pymssql.connect('172.18.130.50', 'sa', 'svrcomputer', 'hbjcdb','uft8')
        if not len(qs)==0:
            for i in qs:
                #print i.paizhaohao
                #print i.paizhaoleibie_id
                if DX_Tongbu.objects.filter(paizhaohao=i.paizhaohao,paizhaoleibie_id=i.paizhaoleibie_id).exists():
                #print biaoda
                    tongbuku = DX_Tongbu.objects.get(paizhaohao=i.paizhaohao,paizhaoleibie_id=i.paizhaoleibie_id)
                    print len(tongbuku)
                    #tongbuku = DX_Tongbu.objects.get(paizhaohao=i.paizhaohao)

                    cheliangleibie_id = tongbuku.cheliangleibie_id
                    cheliangleibie_str = tongbuku.cheliangleibie_str
                    paizhaoleibie_id = tongbuku.paizhaoleibie_id
                    paizhaoleibie_str = tongbuku.paizhaoleibie_str
                    yingyunleibie_id = tongbuku.yingyunleibie_id
                    yingyunleibie_str = tongbuku.yingyunleibie_str
                    chezhu = tongbuku.chezhu
                    dipanhao = tongbuku.dipanhao
                    dengjiriqi = tongbuku.dengjiriqi
                    next_riqi = self.next_riqi_def(dengjiriqi,paizhaoleibie_id,yingyunleibie_id)
                    q = DX_CarInfo.objects.filter(paizhaohao=i.paizhaohao,paizhaoleibie_id=paizhaoleibie_id)
                    q.update(cheliangleibie_id=cheliangleibie_id,cheliangleibie_str=cheliangleibie_str,paizhaoleibie_id=paizhaoleibie_id,
                             paizhaoleibie_str=paizhaoleibie_str,yingyunleibie_id=yingyunleibie_id,yingyunleibie_str=yingyunleibie_str,
                             chezhu=chezhu,dipanhao=dipanhao,dengjiriqi=dengjiriqi,iswanzheng=True,next_riqi=next_riqi,
                             editriqi=datetime.datetime.now())
                    up = DX_Tongbu.objects.filter(paizhaohao=i.paizhaohao,paizhaoleibie_id=paizhaoleibie_id)
                    up.update(istongbu=True)
                else:

                    paizhaohao = i.paizhaohao
                    #print paizhaohao
                    paizhaoleibie_id = i.paizhaoleibie_id
                    #conn = pymssql.connect('172.18.130.50', 'sa', 'svrcomputer', 'hbjcdb')
                    cursor = conn.cursor()
                    cursor.execute('SELECT COUNT (*) FROM carinfo WHERE Car_CPH=%s AND Car_PZLBID=%s' ,(paizhaohao,paizhaoleibie_id))
                    qs_num = cursor.fetchall()[0][0]

                    if qs_num == 0:
                        continue
                    cursor = conn.cursor(as_dict=True)
                    cursor.execute('SELECT * FROM carinfo WHERE Car_CPH=%s AND Car_PZLBID=%s' ,(paizhaohao,paizhaoleibie_id))
                    for a in cursor:
                        paizhaohao = a.get('Car_CPH')
                        paizhaoleibie_id = a.get('Car_PZLBID')
                        #print paizhaoleibie_id
                        paizhaoleibie_str = a.get('Car_PZLBStr')
                        cheliangleibie_id = a.get('Car_CLLxID')
                        cheliangleibie_str = self.CheLiangLieBieIDToStr(cheliangleibie_id)
                        chezhu = a.get('Car_DW')
                        dipanhao = a.get('Car_DPH')
                        dengjiriqi = a.get('Car_DJDate')

                        next_riqi = self.next_riqi_def(dengjiriqi,cheliangleibie_id)

                        q_1 = DX_CarInfo.objects.filter(paizhaohao=paizhaohao,paizhaoleibie_id__contains=paizhaoleibie_id)
                        #print paizhaoleibie_id
                        #print len(q_1)

                        q_1.update(cheliangleibie_id=cheliangleibie_id,cheliangleibie_str=cheliangleibie_str,
                                   paizhaoleibie_id=paizhaoleibie_id,
                                   paizhaoleibie_str=paizhaoleibie_str,chezhu=chezhu,dipanhao=dipanhao,dengjiriqi=dengjiriqi,
                                   iswanzheng=True,next_riqi=next_riqi,editriqi=datetime.datetime.now())
                        #print 'save'
            conn.close()
        else:
            pass

    def next_riqi_def(self,dengjiriqi,paizhaoleibie_id,yingyunleibie_id=None):
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
        if korh == 'M':#摩托车
            if today_year - dengjiriqi_year < 4:
                next_year = today_year + 2
            else:
                next_year = today_year + 1
            return str(next_year)+dengjiriqi_month
        else:
            next_year = today_year+1
            next_riqi_str = str(next_year)+dengjiriqi_month
            return next_riqi_str



            #dengjiriqi_str_year = int(str(dengjiriqi)[:4])
            #dengjiriqi_str_month = str(dengjiriqi)[5:7]
    def CheLiangLieBieIDToStr(self,cheliangleibieid):
        cheliangleibieid_dic = {'B11':u'重型普通半挂车',
                                'B12':	u'重型厢式半挂车',
                                'B13':	u'重型罐式半挂车',
                                'B14':	u'重型平板半挂车',
                                'B15':	u'重型集装箱半挂车',
                                'B16':	u'重型自卸半挂车',
                                'B17':	u'重型特殊结构半挂车',
                                'B18':	u'重型仓栅式半挂车',
                                'B19':	u'重型旅居半挂车',
                                'B1A':	u'重型专项作业半挂车',
                                'B1B':	u'重型低平板半挂车',
                                'B21':	u'中型普通半挂车 ',
                                'B22':	u'中型厢式半挂车',
                                'B23':	u'中型罐式半挂车',
                                'B24':	u'中型平板半挂车',
                                'B25':	u'中型集装箱半挂车',
                                'B26':	u'中型自卸半挂车',
                                'B27':	u'中型特殊结构半挂车',
                                'B28':	u'中型仓栅式半挂车',
                                'B29':	u'中型旅居半挂车',
                                'B2A':	u'中型专项作业半挂车',
                                'B2B':	u'中型低平板半挂车',
                                'B31':	u'轻型普通半挂车',
                                'B32':	u'轻型厢式半挂车',
                                'B33':	u'轻型罐式半挂车',
                                'B34':	u'轻型平板半挂车',
                                'B35':	u'轻型自卸半挂车',
                                'B36':	u'轻型仓栅式半挂车',
                                'B37':	u'轻型旅居半挂车',
                                'B38':	u'轻型专项作业半挂车',
                                'B39':	u'轻型低平板半挂车',
                                'D11':	u'无轨电车',
                                'D12':	u'有轨电车',
                                'G11':	u'重型普通全挂车',
                                'G12':	u'重型厢式全挂车',
                                'G13':	u'重型罐式全挂车',
                                'G14':	u'重型平板全挂车',
                                'G15':	u'重型集装箱全挂车',
                                'G16':	u'重型自卸全挂车',
                                'G17':	u'重型仓栅式全挂车',
                                'G18':	u'重型旅居全挂车',
                                'G19':	u'重型专项作业全挂车',
                                'G21':	u'中型普通全挂车',
                                'G22':	u'中型厢式全挂车',
                                'G23':	u'中型罐式全挂车',
                                'G24':	u'中型平板全挂车',
                                'G25':	u'中型集装箱全挂车',
                                'G26':	u'中型自卸全挂车',
                                'G27': 	u'中型仓栅式全挂车',
                                'G28':	u'中型旅居全挂车',
                                'G29':	u'中型专项作业全挂车',
                                'G31':	u'轻型普通全挂车',
                                'G32':	u'轻型厢式全挂车',
                                'G33':	u'轻型罐式全挂车',
                                'G34':	u'轻型平板全挂车',
                                'G35':	u'轻型自卸全挂车',
                                'G36':	u'轻型仓栅式全挂车',
                                'G37':	u'轻型旅居全挂车',
                                'G38':	u'轻型专项作业全挂车',
                                'H11':	u'重型普通货车',
                                'H12':	u'重型厢式货车',
                                'H13':	u'重型封闭货车',
                                'H14':	u'重型罐式货车',
                                'H15':	u'重型平板货车',
                                'H16':	u'重型集装货车',
                                'H17':	u'重型自卸货车',
                                'H18':	u'重型特殊结构货车',
                                'H19':	u'重型仓栅式货车',
                                'H21':	u'中型普通货车',
                                'H22':	u'中型厢式货车',
                                'H23':	u'中型封闭货车',
                                'H24':	u'中型罐式货车',
                                'H25':	u'中型平板货车',
                                'H26':	u'中型集装货车',
                                'H27':	u'中型自卸货车',
                                'H28':	u'中型特殊结构货车',
                                'H29':	u'中型仓栅式货车',
                                'H31':	u'轻型普通货车',
                                'H32':	u'轻型厢式货车',
                                'H33':	u'轻型封闭货车',
                                'H34':	u'轻型罐式货车',
                                'H35':	u'轻型平板货车',
                                'H36':	u'轻型集装货车',
                                'H37':	u'轻型自卸货车',
                                'H38':	u'轻型特殊结构货车',
                                'H39':	u'轻仓栅式货车',
                                'H41':	u'微型普通货车',
                                'H42':	u'微型厢式货车',
                                'H43':	u'微型罐式货车',
                                'H44':	u'微型封闭货车',
                                'H45':	u'微型自卸货车',
                                'H46':	u'微型特殊结构货车',
                                'H47':	u'微型仓栅式货车',
                                'H51':	u'普通低速货车',
                                'H52':	u'厢式低速货车',
                                'H53':	u'罐式低速货车',
                                'H54':	u'自卸低速货车',
                                'H55':	u'仓栅式低速货车',
                                'H5B':	u'厢式自卸低速货车',
                                'H5C':	u'罐式自卸低速货车',
                                'J11':	u'轮式装载机械',
                                'J12':	u'轮式挖掘机械',
                                'J13':	u'轮式平地机械',
                                'K11':	u'大型普通客车',
                                'K12':	u'大型双层客车',
                                'K13':	u'大型卧铺客车',
                                'K14':	u'大型铰接客车',
                                'K15':	u'大型越野客车',
                                'K16':	u'大型轿车',
                                'K17':	u'大型专用客车',
                                'K21':	u'中型普通客车',
                                'K22':	u'中型双层客车',
                                'K23':	u'中型卧铺客车',
                                'K24':	u'中型铰接客车',
                                'K25':	u'中型越野客车',
                                'K26':	u'中型轿车',
                                'K27':	u'中型专用客车',
                                'K31':	u'小型普通客车',
                                'K32':	u'小型越野客车',
                                'K33':	u'小型轿车',
                                'K34':	u'小型专用客车',
                                'K39':	u'小型面包车',
                                'K41':	u'微型普通客车',
                                'K42':	u'微型越野客车',
                                'K43':	u'微型轿车',
                                'K49':u'微型面包车',
                                'M11':	u'普通正三轮摩托车',
                                'M12':	u'轻便正三轮摩托车',
                                'M13':	u'正三轮载客摩托车',
                                'M14':	u'正三轮载货摩托车',
                                'M15':	u'侧三轮摩托车',
                                'M21':	u'普通二轮摩托车',
                                'M22':	u'轻便二轮摩托车',
                                'N11':	u'三轮汽车',
                                'Q11':	u'重型半挂牵引车',
                                'Q12':	u'重型全挂牵引车',
                                'Q21':	u'中型半挂牵引车',
                                'Q22':	u'中型全挂牵引车',
                                'Q31':	u'轻型半挂牵引车',
                                'Q32':	u'轻型全挂牵引车',
                                'T11':	u'大型轮式拖拉机',
                                'T21':	u'小型轮式拖拉机',
                                'T22':	u'手扶拖拉机',
                                'T23':	u'手扶变形运输机',
                                'X99':	u'其它',
                                'Z11':	u'大型专项作业车',
                                'Z21':	u'中型专项作业车',
                                'Z31':	u'小型专项作业车',
                                'Z41':	u'微型专项作业车',
                                'Z51':	u'重型专项作业车',
                                'Z71':	u'轻型专项作业车'}
        return cheliangleibieid_dic.get(cheliangleibieid)





