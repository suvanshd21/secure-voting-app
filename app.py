from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, flash
from db import create_connection, insert_candidate, select_all_candidates, update_vote, select_user, update_user, select_candidate
from flask_cors import CORS, cross_origin
from pusher import Pusher
import simplejson
import pyotp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = '211096'

# configure pusher object
pusher = Pusher(
app_id = "625173",
key = "4756882ee036ff91c865",
secret = "82ca8f7c17656b0c8e8d",
cluster = "ap2",
ssl=True)

database = "./pythonsqlite.db"
conn = create_connection(database)
c = conn.cursor()
key = 'JBSWY3DPEHPK3PXP'
voter_id = ""

def main():
    global conn, c, key

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validate',methods=['POST'])
def validate():
    global key,voter_id
    voter_id = request.form['voter_id']
    phone_number = request.form['phone_number']
    result = select_user(conn,voter_id,phone_number)
    data = voter_id + "/" + phone_number
    if result is None:
        flash("Invalid credentials!")
        return redirect("/", code=302)
    otp=pyotp.totp.TOTP(key).provisioning_uri(data, issuer_name="Voting App")
    return render_template('qrvalidate.html',otp=otp,result=result)   

@app.route('/verify-otp',methods=["POST"])
def verify_otp():
    global key
    entered_otp = request.form["otp"]
    result = eval(request.form["result"])
    print(result)
    totp = pyotp.TOTP(key)
    otp=totp.now()
    print("Current OTP:", otp)
    if otp == entered_otp:
        if result["candidate_id"] is None:
            return redirect("/select", code=302)
        else:
            return redirect("/user-results", code=302)
    else:
        flash("Incorrect OTP. Please login again!")
        return redirect("/",code=302)

@app.route('/select',methods=['GET'])
def select():
    candidate_list = select_all_candidates(conn)
    return render_template('vote.html',candidate_list = candidate_list)

@app.route('/admin')
def admin():
    return render_template('admin-login.html')

@app.route('/admin-validate', methods=["POST"])
def admin_validate():
    if request.form['admin_id'] != "admin" or request.form['admin_pw'] != "admin123":
        flash("Invalid credentials!")
        return redirect('/admin', code=302)
    return render_template('admin-menu.html')

@app.route('/admin-results',methods=["POST"])
def admin_results():
    candidate_list = select_all_candidates(conn)
    return render_template('admin.html', candidates = candidate_list)

@app.route('/admin-insert',methods=["POST"])
def admin_insert():
    return render_template('admin-insert-form.html')

@app.route('/insert_new_cand', methods=["POST"])
def insert_new_cand():
    sql = """
    INSERT INTO candidates(name,party) VALUES ('{0}','{1}')
    """.format(request.form["name"],request.form["party"])
    print(sql)
    insert_candidate(conn,sql)
    flash("New candidate inserted!")
    return render_template('admin-menu.html')

@app.route('/user-results')
def user_results():
    candidate_list = select_all_candidates(conn)
    result = select_user(conn,voter_id)
    result = select_candidate(conn,int(result["candidate_id"]))
    return render_template('user-results.html',candidates = candidate_list,cand_name=result["name"])

@app.route('/vote', methods=['POST'])
def vote():
    global voter_id
    cand_id = request.form['cand_id']
    print(voter_id,cand_id)
    update_vote(conn, int(cand_id))
    update_user(conn, voter_id, int(cand_id))
    return redirect("/confirmation", code=302)

@app.route('/confirmation')
def confirmation():
    candidate_list = select_all_candidates(conn)
    return render_template("index.html",candidate_list = candidate_list)

@app.route('/disp_progress', methods=['POST'])
def disp_progress():
    output = select_all_candidates(conn)
    return request.data

if __name__ == '__main__':
    main()
    app.run(debug=True)