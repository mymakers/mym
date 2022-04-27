from db_model.mogodb import conn_mongodb
from datetime import datetime

class WebSession():
    web_page = {'A':'index.html', 'B':'index.html'}
    session_count = 0
    
    @staticmethod
    def save_session_info(session_ip, email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")
        
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'user_email': email,
            'page': webpage_name,
            'access_time': now_time
        })
        
    @staticmethod
    def get_web_page(web_id=None):
        if web_id == None:
            if WebSession.session_count == 0:
                WebSession.session_count = 1
                return 'index.html'
            else:
                WebSession.session_count = 0
                return 'index.html'
        else:
            return WebSession.blog_page[web_id]

