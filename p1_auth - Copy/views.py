from flask_mysqldb import MySQL
from flask import Flask,render_template,request,url_for,redirect,session


app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='abc456'
app.config['MYSQL_DB']='flask'


mysql=MySQL(app)
app.secret_key="Prasadbhange"


def logout():
	session.clear()
	return redirect (url_for("a2"))


def home():
	return render_template ("home.html")


def a_admin():
	return render_template ("a_login.html")	



def reques():
	return render_template ("request.html")	


def add_admin():
	if request.method=="POST":
		un=request.form["un"]
		pw1=request.form["pw1"]
		pw2=request.form["pw2"]
		if pw1==pw2:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="insert into admin values('%s','%s')"
				cursor.execute(sql%(un,pw1))
				mysql.connection.commit()
				return render_template("add_admin.html",msg="added successfully")

			except Exception as e:
				mysql.connection.rollback()
				return render_template("add_admin.html",msg="Admin already exists")
		else:
			return render_template("add_admin.html",msg="password did not match")
	else:
		return render_template("add_admin.html")


def reque():
	if request.method=="POST":
		type=request.form["blood_type"]
		loc=request.form["loc"]
		num=int(request.form["cont"])
		try:
			#cursor=db.cursor()
			cursor=mysql.connection.cursor()
			sql="insert into request values('%s','%s','%d')"
			cursor.execute(sql%(type,loc,num))
			mysql.connection.commit()
			return render_template("request.html",msg="Requested successfully")
		except Exception as e:
			mysql.connection.rollback()
			return render_template("request.html",msg=e)
		
	else:
		return render_template("request.html")


def add_bb():
	if request.method=="POST":
		ch=request.form["choice1"]
		id=int(request.form["id"])
		blood=request.form["blood_type"]
		loc=request.form["loc"]
		bb_name=request.form["bb_name"]
		cont=int(request.form["cont"])
		if ch=="bb":
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="insert into blood_bank values('%d','%s','%s','%s','%d')"
				cursor.execute(sql%(id,blood,loc,bb_name,cont))
				mysql.connection.commit()
				return render_template("add_bb.html",msg="added successfully")
			except Exception as e:
				mysql.connection.rollback()
				return render_template("add_bb.html",msg=e)
		else:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="insert into blood_donor values('%d','%s','%s','%s','%d')"
				cursor.execute(sql%(id,blood,loc,bb_name,cont))
				mysql.connection.commit()
				return render_template("add_bb.html",msg="added successfully")
			except Exception as e:
				mysql.connection.rollback()
				return render_template("add_bb.html",msg=e)
			
	else:
		return render_template("add_bb.html")



def edit_bb():
	if request.method=="POST":
		ch=request.form["choice1"]
		id=int(request.form["id"])
		blood=request.form["blood_type"]
		loc=request.form["loc"]
		bb_name=request.form["bb_name"]
		cont=int(request.form["cont"])
		if ch=="bb":
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="update blood_bank set blood='%s',loc='%s',bb_name='%s',cont='%d' where id='%d'"
				cursor.execute(sql%(blood,loc,bb_name,cont,id))
				mysql.connection.commit()
				return render_template("edit_bb.html",msg="edited successfully")
			except Exception as e:
				mysql.connection.rollback()
				return render_template("edit_bb.html",msg=e)
		else:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="update blood_donor set blood='%s',loc='%s',bb_name='%s',cont='%d' where id='%d'"
				cursor.execute(sql%(blood,loc,bb_name,cont,id))
				mysql.connection.commit()
				return render_template("edit_bb.html",msg="edited successfully")
			except Exception as e:
				mysql.connection.rollback()
				return render_template("edit_bb.html",msg=e)
			
	else:
		return render_template("edit_bb.html")



def del_admin():
	if request.method=="POST":
		username=request.form["username"]
		try:
			#cursor=db.cursor()
			cursor=mysql.connection.cursor()
			sql="delete from admin where username='%s'"
			cursor.execute(sql%(username))
			mysql.connection.commit()
			return render_template("del_admin.html",msg="deleted successfully")

		except Exception as e:
			mysql.connection.rollback()
			return render_template("del_admin.html",msg="admin doesn't exists")
	else:
		return render_template("del_admin.html",msg="admin doesn't exists")



def del_bb():
	if request.method=="POST":
		id=int(request.form["id"])
		ch=request.form["choice1"]
		if ch=="bb":
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="delete from blood_bank where id='%d'"
				cursor.execute(sql%(id))
				mysql.connection.commit()
				return render_template("del_bb.html",msg="deleted successfully")

			except Exception as e:
				mysql.connection.rollback()
				return render_template("del_bb.html",msg=e)
		else:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="delete from blood_donor where id='%d'"
				cursor.execute(sql%(id))
				mysql.connection.commit()
				return render_template("del_bb.html",msg="deleted successfully")

			except Exception as e:
				mysql.connection.rollback()
				return render_template("del_bb.html",msg=e)
	else:
		return render_template("del_bb.html")



def usr_home():
	if request.method=="POST":
		loc=request.form["loc"]
		ch=request.form["choice1"]
		if ch=="bb":
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="select blood,bb_name,cont from blood_bank where loc='%s'"
				cursor.execute(sql%(loc))
				data=cursor.fetchall()
				mysql.connection.commit()
				return render_template("usr_home.html",msg=data,name=session["username"])

			except Exception as e:
				mysql.connection.rollback()
				return render_template("usr_home.html",msg=e)
		else:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="select blood,bb_name,cont from blood_donor where loc='%s'"
				cursor.execute(sql%(loc))
				data=cursor.fetchall()
				mysql.connection.commit()
				return render_template("usr_home.html",msg=data,name=session["username"])

			except Exception as e:
				mysql.connection.rollback()
				return render_template("usr_home.html",msg=e)
	else:
		return render_template("usr_home.html")



def user():
	return render_template ("login.html")



def login():
	if request.method=="POST":
		un=request.form["un"]
		pw=request.form["pw"]
		try:
			#cursor=db.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor=mysql.connection.cursor()
			cursor.execute(sql%(un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("login.html",msg="invalid login")
			else:
				session["username"]=un
				return redirect(url_for("a11"))
		except Exception as e:
			return render_template("login.html",msg=e)

	else:
		return render_template("login.html")



def signup():
	if request.method=="POST":
		un=request.form["un"]
		pw1=request.form["pw1"]
		pw2=request.form["pw2"]
		if pw1==pw2:
			try:
				#cursor=db.cursor()
				cursor=mysql.connection.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql%(un,pw1))
				mysql.connection.commit()
				return redirect(url_for("a13"))
			except Exception as e:
				mysql.connection.rollback()
				return render_template("signup.html",msg="user already exists")
		else:
			return render_template("signup.html",msg="password did not match")
	else:
		return render_template("signup.html")



def admin_menu():
	if request.method=="POST":
		un=request.form["un"]
		pw=request.form["pw"]
		try:
			#cursor=db.cursor()
			sql="select * from admin where username='%s' and password='%s'"
			cursor=mysql.connection.cursor()
			cursor.execute(sql%(un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("a_login.html",msg="invalid login")
			else:
				return render_template("admin_menu.html")
		except Exception as e:
			return render_template("a_login.html",msg=e)

	else:
		return render_template("a_login.html")




def ad_admin():
	return render_template("add_admin.html")



def ad_bb():
	return render_template("add_bb.html")


def edi_bb():
	return render_template("edit_bb.html")


def de_admin():
	return render_template("del_admin.html")


def de_bb():
	return render_template("del_bb.html")



def show_home():
	if request.method=="POST":
		loc=request.form["loc"]
		try:
			#cursor=db.cursor()
			cursor=mysql.connection.cursor()
			sql="select * from request where loc='%s'"
			cursor.execute(sql%(loc))
			data=cursor.fetchall()
			mysql.connection.commit()
			return render_template("show.html",msg=data)
		except Exception as e:
			mysql.connection.rollback()
			return render_template("show.html",msg=e)
	else:
			return render_template("show.html")



def re_bb():
	return render_template("show.html")


