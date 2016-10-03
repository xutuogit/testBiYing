# conding = utf-8
import os
from test_case.send_email import sendEmail


class send_TestResult():
    def sendreport(self):
        result_dir = 'C:\\Users\Administrator\PycharmProjects\\xutuotest\report'
        list = os.listdir(result_dir)
        list.sort(
            key=lambda fn: os.path.getmtime(result_dir + '\\' + fn) if not os.path.isdir(result_dir + '\\' + fn) else 0)
        print(u'生成测试报告：' + list[-2])
        # 找到最新生成的文件
        file_new = os.path.join(result_dir, list[-2])
        print(file_new)
        sendEmail(file_new)


if __name__ == '__main__':
    send_TestResult.sendreport()
