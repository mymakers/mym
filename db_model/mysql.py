import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    port = 3306,
    user = 'root',
    passwd='john1225*',
    db='db',
    charset='utf8'
)

def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN