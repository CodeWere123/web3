import sqlite3


def reg_account(login, password):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id FROM users
                WHERE username == "{login}" """).fetchall()
    if result:
        con.close()
        return False
    else:
        cur.execute("INSERT INTO users (username, password, is_banned, score) VALUES (?, ?, ?, ?)",
                    (login, password, False, 0))

    con.commit()
    con.close()
    return True


def add_token_to_db(token, username):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tokens
                            WHERE username = ? """, (username,)).fetchall()

    if result:
        cur.execute("""UPDATE tokens SET token = ? WHERE username = ?""", (token, username))
        con.commit()
    else:
        cur.execute("INSERT INTO tokens (username, token) VALUES (?, ?)",
                    (username, token))
        con.commit()
    con.close()


def login_user(login, user_password):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute("""SELECT id FROM users
                            WHERE username = ? AND password = ?""", (login, user_password)).fetchall()

    if result:
        con.close()
        return result[0][0]
    con.close()
    return False

def session_get_token(username):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tokens
                                WHERE username = ? """, (username, )).fetchall()
    if result:
        return result[0][1]
    return False
def anti_sqli(name, password):
    to_check = str(name + password)
    if len(to_check) != len((to_check.replace("\"", "")).replace("\'", "")):
        return False
    return True
