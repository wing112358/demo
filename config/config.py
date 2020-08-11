import logging
import os
import time
from optparse import OptionParser

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）__file__指当前文件

test_path = os.path.join(prj_path,'act','case','onecase')  # 用例目录

log_file = os.path.join(prj_path, 'log','log_{}.txt'.format(today))  # # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report','report_{}.html'.format(now))  # 更改路径到report目录下


data_path = os.path.join(prj_path,'data')  # 数据目录

test_list_file=os.path.join(test_path,'testlist.txt')

last_fails_file = os.path.join(prj_path, 'last_failures.pickle')

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

#数据库配置
test_db_host = 'rm-uf66y4084tjzznfp7o.mysql.rds.aliyuncs.com'   # 自己的服务器地址
test_db_port = 3306
test_db_user = 'root'
test_db_passwd = '56gHy6&&-5BUyr'


# 邮件配置

send_email_after_run = True

smtp_server = 'smtp.qq.com'
smtp_user = '3373363301@qq.com'
smtp_password = 'pyhdaeqbnvjzdaed'

sender = smtp_user  # 发件人
receiver = 'wangt@shumei.ai'  # 收件人
subject = '接口测试报告'  # 邮件主题


# 命令行选项
parser = OptionParser()
parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')


(options, args) = parser.parse_args()