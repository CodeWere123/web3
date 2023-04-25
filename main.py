from flask import Flask, url_for, request, redirect, render_template, session

from use_db import anti_sqli, reg_account, login_user, add_token_to_db, session_get_token

from rk_get import prem_search, nerfed_search

from vki import vk_info, vk_iD2

app = Flask(__name__)

app.secret_key = 'ShaRedKey'
IS_LOGGED = ""


@app.route('/')
def greeting():
    return render_template('index.html')


@app.route('/hacker')
def hack_attemped():
    return render_template('hacker.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password, username)
        if not anti_sqli(username, password):
            return redirect("/hacker")
        else:
            is_ok = login_user(username, password)
            if is_ok:
                session['username'] = username
                print(session['username'])
                print(session)
                return redirect(f"/user/{username}")
            else:
                return render_template('incorrect.html')


@app.route('/register', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        return render_template('reg_acc.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password, username)
        if not anti_sqli(username, password):
            return redirect("/hacker")
        else:
            is_ok = reg_account(username, password)
            if is_ok:
                session['username'] = username
                return redirect(f"/user/{username}")
            else:
                return render_template('incorrect2.html')


@app.route('/user/<username>')
def profile(username):
    if session['username'] == username:
        token = session_get_token(username)

        if token:
            session["token"] = token
        else:
            session["token"] = "серверный"
        if username != "admin":
            return render_template('LK.html', username=username, token=session["token"])
        else:
            return "<h1>ВЫ админ флаг: kiranewerseethis</h1>"

    else:
        return render_template('403.html')


@app.route('/logout')
def logout():
    if not session:
        return render_template('403.html')
    else:
        session.pop('username', None)
        return redirect("/")


@app.route('/reset_token')
def reset():
    if not session:
        return render_template('403.html')
    else:
        session["token"] = "серверный"
        add_token_to_db(session["token"], session["username"])
        return redirect(f"/user/{session['username']}")


@app.route('/f2', methods=['POST', 'GET'])
def f2():
    if not session:
        return render_template('403.html')
    elif request.method == 'GET':
        return render_template("f2.html")
    elif request.method == 'POST':
        try:
            vk1 = request.form['input1']

            (shool, shool_p, vile, vile_p, vuse, vuse_p) = vk_info(vk1)
            return render_template("return_text.html", shool=shool, shool_p=shool_p, vile=vile, vile_p=vile_p,
                                   vuse=vuse,
                                   vuse_p=vuse_p)
        except:
            return render_template("eror_f1.html")


@app.route('/f1', methods=['POST', 'GET'])
def f1():
    if not session:
        return render_template('403.html')
    elif request.method == 'GET':
        return render_template("f1.html")
    elif request.method == 'POST':
        try:
            vk1 = request.form['input1']
            vk2 = request.form['input2']
            if not session["token"] or session["token"] == "серверный":
                res = nerfed_search(vk1, vk2)
                return render_template("f1_nerfed.html", res=res)
            else:
                print("тут")
                res = prem_search(vk1, vk2, session["token"])
                return render_template("res_f1.html", res=res)
        except:
            return render_template("eror_f1.html")

@app.route('/f3', methods=['POST', 'GET'])
def f3():
    if not session:
        return render_template('403.html')
    elif request.method == 'GET':
        return render_template("f3.html")
    elif request.method == 'POST':
        try:
            vk1 = request.form['input1']
            res = vk_iD2(vk1)
            return render_template("f3_res.html", res=res)
        except:
            return render_template("eror_f1.html")

@app.route('/metods')
def metods():
    if not session:
        return render_template('403.html')
    else:
        return render_template("main.html", username=session["username"])


@app.route('/add_token', methods=['POST'])
def add_token():
    if not session:
        return render_template('403.html')
    else:
        token = request.form.get('token')

        print(f"Добавлен токен: {token}")
        session["token"] = token
        add_token_to_db(session["token"], session["username"])
        return redirect(f'/user/{session["username"]}')


@app.route("/change_password")
def info():
    if not session:
        return render_template('403.html')
    else:
        return render_template('change_password.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
