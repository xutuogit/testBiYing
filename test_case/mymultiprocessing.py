#coding = utf-8
import unittest,time,os,multiprocessing
import HTMLTestRunner
import sys
from email.mime.text import MIMEText


def Ecraetsuitel():
    #建立数组
    casedir=[]
    #找到文件夹
    lista = os.listdir('D:\\')
    #遍历文件夹
    for xx in lista:
        if 'thread' in xx:#找到文件夹下所有有thread的文件夹
            casedir.append(xx)#将文件加入数组中
    print(casedir)
    suite = []#建立数组
    for n in casedir:#遍历数组
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(n,pattern='test*.py')#找到thread文件夹中的每个有test的文件
        for test_suit in discover:#遍历每一个test文件
            for test_case in test_suit:#遍历test文件里面的每一个用例
                testunit.addTests(test_case)#将每一个用例加入到测试套件中
        suite.append(testunit)#把建好的套件加入到素组中
    return suite,casedir#返回每一个test文件中所有的用例组成一个测试套件，然后都加入到suit数组中；所有的含有thread的文件夹都在casedir数组中
def EEmultiruncase(suit,casedir):
    nowtime = time.strftime('%Y-%m-%D-%H_%M_%S',time.localtime(time.time()))
    reportdir = 'D:\\dasdq\\'+ nowtime +'report.html'
    fp = open(reportdir,'wb')
    proclist = []
    s=0
    for i in suit:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况')
    proc = multiprocessing.Process(target=runner.run(),args=(i,))
    proclist.append(proc)
    s=s+1
    for proc in  proclist:proc.start()
    for proc in proclist: proc.join()
if  __name__ == '__main__':
    runtmp = Ecraetsuitel()
    EEmultiruncase(runtmp[0],runtmp[1])
