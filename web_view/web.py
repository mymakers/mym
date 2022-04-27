from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for

web_abtest = Blueprint('web', __name__)


@web_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('email'))
        return redirect(url_for('web.test_web'))
    else:
        # print('set_email', request.headers)
        # content type 이 application/json 인 경우
        # print('set_email', request.get_json())
        print('set_email', request.form['email'])

        return redirect(url_for('web.test_web'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@web_abtest.route('/test_web')
def test_web():
    return render_template('index.html')
