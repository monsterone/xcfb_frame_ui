
import unittest
import HTMLTestReportCN
#ʵ�����׼�����
from Common.dir_config import testcase_dir, htmlreport_dir

s = unittest.TestSuite()
#TestLoader���÷�
#1��ʵ����TestLoader����
#2��ʹ��discoverȥ�ҵ�һ��Ŀ¼�µ����в�������
#3��ʹ��S

loader = unittest.TestLoader()
s.addTests(loader.discover(testcase_dir))
## ����
runner = unittest.TextTestRunner()
s.run(s)

fp = open(htmlreport_dir + '/autoTest_report.html')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="���Ա���",
                                         description="cs����",
                                         tester="monster")
runner.run(s)