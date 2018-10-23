import MySQLdb
import time
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read("private/oauth.cfg")

host = "127.0.0.1"
user = cfg.get('MySQL', 'MYSQL_ROOT')
password = cfg.get('MySQL', 'MYSQL_ROOT_PASSWORD')
port = int(cfg.get('MySQL', 'MYSQL_PORT'))
db = cfg.get('MySQL', 'MYSQL_DATABASE')

msg = """
    \n\n\n
    ######################################
    database connect:
        host = {}
        user = {}
        password = {}
        port = {}
        db = {}
    ######################################
""".format(host, user, password, port, db)
print(msg)

while True:
    try:
        conn = MySQLdb.connect(host=host, user=user, password=password, port=port)

        while True:
            cur = conn.cursor()
            cur.execute("show databases like'" + db + "'")
            res = cur.fetchone()

            if res and len(res) > 0:
                print("database {} create successful".format(db))
                break
            else:
                print("database {} is creating...".format(db))
                time.sleep(1.0)
            cur.close()
        conn.close()
        break
    except Exception as e:
        print("MySQL not responds.. waiting for mysql up: {}".format(e))
        time.sleep(1.0)
