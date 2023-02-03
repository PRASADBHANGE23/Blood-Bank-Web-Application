from views import *
from flask import Flask,render_template,request,url_for,redirect,session
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='abc456'
app.config['MYSQL_DB']='flask'

mysql=MySQL(app)
app.secret_key="Prasadbhange"


@app.route("/logout",methods=["GET","POST"])
def a1():
	res1=logout()
	return res1


@app.route("/",methods=["GET","POST"])
def a2():
	res2=home()
	return res2


@app.route("/a_admin",methods=["GET","POST"])
def a3():
	res3=a_admin()
	return res3
	

@app.route("/reques",methods=["GET","POST"])
def a4():
	res4=reques()
	return res4


@app.route("/add_admin",methods=["GET","POST"])
def a5():
	res5=add_admin()
	return res5


@app.route("/reque",methods=["GET","POST"])
def a6():
	res6=reque()
	return res6


@app.route("/add_bb",methods=["GET","POST"])
def a7():
	res7=add_bb()
	return res7


@app.route("/edit_bb",methods=["GET","POST"])
def a8():
	res8=edit_bb()
	return res8


@app.route("/del_admin",methods=["GET","POST"])
def a9():
	res9=del_admin()
	return res9


@app.route("/del_bb",methods=["GET","POST"])
def a10():
	res10=del_bb()
	return res10


@app.route("/usr_home",methods=["GET","POST"])
def a11():
	res11=usr_home()
	return res11


@app.route("/user",methods=["GET","POST"])
def a12():
	res12=user()
	return res12


@app.route("/login",methods=["GET","POST"])
def a13():
	res13=login()
	return res13


@app.route("/signup",methods=["GET","POST"])
def a14():
	res14=signup()
	return res14


@app.route("/admin_menu",methods=["GET","POST"])
def a15():
	res15=admin_menu()
	return res15


@app.route("/ad_admin",methods=["GET","POST"])
def a16():
	res16=ad_admin()
	return res16


@app.route("/ad_bb",methods=["GET","POST"])
def a17():
	res17=ad_bb()
	return res17


@app.route("/edi_bb",methods=["GET","POST"])
def a18():
	res18=edi_bb()
	return res18


@app.route("/de_admin",methods=["GET","POST"])
def a19():
	res19=de_admin()
	return res19


@app.route("/de_bb",methods=["GET","POST"])
def a20():
	res20=de_bb()
	return res20


@app.route("/show_home",methods=["GET","POST"])
def a21():
	res21=show_home()
	return res21


@app.route("/re_bb",methods=["GET","POST"])
def a22():
	res22=re_bb()
	return res22




if __name__=="__main__":
	app.run(debug=True,use_reloader=True)