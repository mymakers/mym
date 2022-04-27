from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from web_view import web
from web_control.user_mgmt import User
import os

# http 에서 테스트용
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'yousei_server'
 
app.register_blueprint(web.web_abtest, url_prefix='/web')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
 
@login_manager.user_loader
def load_user(email):
    return User.get(email)
 
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)