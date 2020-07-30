import logging
import os
import time

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）__file__指当前文件

data_path = os.path.join(prj_path,'data')  # 数据目录
test_path = os.path.join(prj_path,'act')  # 用例目录

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

log_file = os.path.join(prj_path, 'log','log_{}.txt'.format(today))  # # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report','report_{}.html'.format(now))  # 更改路径到report目录下

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


if __name__ == '__main__':
    logging.info("hello")