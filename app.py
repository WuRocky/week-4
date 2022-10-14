from cgitb import reset
from flask import Flask,render_template,url_for,request,redirect,session

app=Flask(
  __name__,
  static_url_path="/"
)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/signin",methods=['GET',"POST"])
def signin():
  if request.method == 'POST':
    username = request.form["username"]
    password = request.form["password"]
    if username=="test" and password=="test":
      session["username"] = username
      session["password"] = password
      return  redirect("/member")
    elif username == "" or password== "":
      return  redirect(url_for("error",message=request.args.get("message","請輸入帳號、密碼")))
    else:
      return  redirect(url_for("error",message=request.args.get("message","帳號、或密碼輸入錯誤")))
  return render_template('index.html') 

@app.route("/member")
def member():
  if not session.get("username") and not session.get("password"):
    return  redirect("/")
  return render_template('member.html')

@app.route("/signout")
def logout():
  session.pop('username', None)
  session.pop('password', None)
  return  redirect("/")

@app.route("/error")
def error():
  data=request.args.get("message","自訂錯誤訊息")
  session.pop('username', None)
  session.pop('password', None)
  return render_template('error.html',message=data)


@app.route("/operation",methods=["POST"])
def operation():
  dataTest = request.form["number"]
  return redirect(url_for('square',urlData=dataTest))


@app.route("/square/<urlData>")
def square(urlData):
  test = int(urlData)
  reuslt =test ** 2
  return render_template("square.html",data=reuslt)



#################test#########################
# @app.route("/square",methods=["POST"])
# def square():
#   inputData=request.form["number"]
#   mumber=int(inputData)
#   result = mumber ** 2
#   return render_template("square.html",data=result)



# @app.route("/square/<data2>",methods=["POST"])
# def square(data2):
#   inputData=request.form["number"]
#   mumber=int(inputData)
#   result = mumber ** 2
#   return render_template("square.html",data=result,data2=mumber)  




if __name__ == "__main__": 
  app.run(port=3000,debug=True)