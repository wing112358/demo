import pymysql
import sys
sys.path.append('..')  # 提升一级到项目更目录下
from config.config import *



class DB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=test_db_host,
            port=test_db_port,
            user=test_db_user,
            passwd=test_db_passwd,
            db='atwk',
            charset='utf8')

        self.cur = self.conn.cursor()




    def query(self,sql):
        self.cur.execute(sql)
        logging.debug(sql)

        result = self.cur.fetchall()
        logging.debug(result)
        return result





