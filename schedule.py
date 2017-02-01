from urllib.request import urlopen
from bs4 import  BeautifulSoup
from  urllib.error import HTTPError
from  urllib.error import URLError
import  datetime
import  config
dirpass = "/Users/takumi/PycharmProjects/schedule/"

##################################### Schedule Class ###############################################
class Schedule:
 td = datetime.datetime.today()


 def Connection(self):

    try:
        self.momo_html = urlopen("http://dimora.jp/talent-info/18/70000/?areaId=03")
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The sever could not be found!")

    else:
        print("CONNECTION SUCCESS!!\n")

 def Get_detail(self,select_num,tgt):
    pgm_title = tgt.findAll("span",{"class":"appPgmTitle"}) #get program title
    pgm_date = tgt.findAll("span",{"class":"appPgmDate"}) #get program date
    self.rel_tarent = tgt.findAll("a",{"class":"linkCoStar"}) #get related tarent
    self.f_pgm_title = pgm_title[select_num].get_text().replace('\n','').replace(' ','')
    self.f_pgm_date = pgm_date[select_num].get_text().replace('\n','').replace(' ','')


 def Get_title_num(self,tgt):
     pgm_title = tgt.findAll("span", {"class": "appPgmTitle"})
     config.title_num = len(pgm_title)

 def check_isPlan(self,filename,tgt):
    fw = open(filename,'w')
    self.plan = tgt.find("article",{"id":"trpa_null"})  #distinguisch tag
    if self.plan is None:
        fw.write("%d月%d日%d時%d分%d秒現在、ももちの出演予定はありません。"%(self.td.month,self.td.day,self.td.hour,self.td.minute,self.td.second))
        fw.close()
    else:
        return  1

 def Print(self,talent,filename,cnt):
    fw = open(filename,'w')
    fa = open(filename,'a')
    fw.write("#%d\n【%sの出演情報です♪】(%d時%d分現在)\n番組名:%s\n\n時間/分類:%s\n\n共演タレント:" % (cnt,talent,self.td.hour,self.td.minute,self.f_pgm_title, self.f_pgm_date))
    fw.close()
    for i in range(len(self.rel_tarent)):
        f_rel_tarent = self.rel_tarent[i].get_text().replace('\n', '').replace(' ', '')
        fa.write("%s " % f_rel_tarent)
    fa.close()

 def __init__(self):
     self.Connection()

##################################### File operation Class ###############################################
class File_operation:

 def Read_file(self,filename):
     fr = open(filename, 'r')
     self.contents = fr.read()
     fr.close()

 def Rounding(self,filename):
     fa = open(filename, 'w')
     for i in range(135):
        fa.write("%s"%self.contents[i])
        if i > 130 and self.contents[i]==" ":
            fa.write("等")
            break
     fa.close()

 def Write_file(self,filename):
     fa = open(filename,'w')
     fa.write("%s"%self.contents)

###################################################  main  ##################################################################
momo_schedule = Schedule()

fop = File_operation()

bsObj = BeautifulSoup(momo_schedule.momo_html.read(),"lxml")
momo_schedule.Get_title_num(tgt=bsObj)

if(momo_schedule.check_isPlan(dirpass+'Schedule1.txt',tgt=bsObj)==1):
 for i in range(config.title_num):
  momo_schedule.Get_detail(i,bsObj)
  momo_schedule.Print("ももち",dirpass+'Schedule'+str(i+1)+'.txt',i+1)
  fop.Read_file(dirpass+'Schedule'+str(i+1)+'.txt')
  if(len(fop.contents)>140):
   fop.Rounding(dirpass+'Schedule'+str(i+1)+'.txt')
  else:
   fop.Write_file(dirpass+'Schedule'+str(i+1)+'.txt')


