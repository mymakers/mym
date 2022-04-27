from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class User(UserMixin):
    
    def __init__(self, email, password):
        self.id = email
        self.password = password
        
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE email = '" + str(email) + "'"
        
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None # 해당 레코드가 없음
        
        user = User(email=user[0], password=user[1])
        return user