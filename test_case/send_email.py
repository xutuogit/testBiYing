# coding = utf -8
import smtplib
import time
from email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os,sys

# 定义发邮件
class sendEmail():
    def sentmail(self,file_name):
        # 用来发送邮件的邮箱
        mail_from = '417915431@qq.com'
        # 用来接收邮件
        mial_to = '610717047@qq.com'
        # 定义正
        msg = MIMEText('haha', _subtype='html', _charset="utf-8")
        # 定义标题
        msg['Subject'] = u'私有云测试报告'
        # 定义发送时间
        msg['data'] = time.strftime("%H-%m-%D-%H_%M_%S", time.localtime(time.time()))
        # 连接服务器
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        # 用户名密码
        #smtp.login('417915431@qq,com', 'rcqixbzgawgjcaij.')
        smtp.login('417915431@qq,com', 'hllxxwchczphbgca.')
        smtp.sendmail(mail_from, mial_to, msg.as_string())
        smtp.quit()
        print("email has send out")



if __name__ == '__main__':
    # print(sys.path[0])#打印当前路径
    # # name = open(sys.path[0] + os.path.sep +".."+os.path.sep+ "report" + os.path.sep + "bao.html")
    # # # name = open('qwe.html','r')
    # # print(name.readlines())
    send = sendEmail()
    send.sentmail()

