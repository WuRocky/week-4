from flask import Flask,render_template,request,redirect,session


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
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]
    if session["username"]=="test" and session["password"]=="test":
      return  redirect("/member")
    else:
      return redirect("/error")  
  return render_template('index.html') 

@app.route("/member")
def member():
  if not session.get("username") or not session.get("password"):
    return  redirect("/")
  return render_template('member.html')

@app.route("/signout")
def logout():
  session.pop('username', None)
  return  redirect("/")

@app.route("/error")
def error():
  if session["username"] == "" or session["password"] == "":
    message=request.args.get("message","請輸入帳號、密碼")
    result = message
  else:
    message=request.args.get("message","帳號、或密碼輸入錯誤")
    result = message
  session.pop('username', None)
  return render_template('error.html',data=result)

@app.route("/square")
def square():
  mumber=request.args.get("number","")
  mumber=int(mumber)
  result = mumber ** 2
  return render_template("square.html",data=result)


if __name__ == "__main__": 
  app.run(port=3000,debug=True)