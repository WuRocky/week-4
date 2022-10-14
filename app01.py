from flask import Flask,render_template,url_for,request,redirect,make_response
import time

app=Flask(
  __name__,
  static_url_path="/"
)


@app.route("/")
def index():
  return render_template('index.html')

@app.route("/signin",methods=['GET',"POST"])
def signin():
  if request.method == 'POST':
    username = request.form["username"]
    password = request.form["password"]
    if username=="test" and password=="test":
      resp = make_response(redirect("/member"))
      resp.set_cookie(key='framework', value='flask', expires=time.time()+6*60)
      return  resp
    elif username == "" or password== "":
      return  redirect(url_for("error",message=request.args.get("message","請輸入帳號、密碼")))
    else:
      return  redirect(url_for("error",message=request.args.get("message","帳號、或密碼輸入錯誤")))
  return render_template('index.html') 

@app.route("/member")
def member():
  if not request.cookies.get('framework') :
    return  redirect("/")
  return render_template('member.html')

@app.route("/signout")
def logout():
  res = make_response(redirect("/"))
  res.set_cookie(key='framework', value='', expires=0)
  return  res

@app.route("/error")
def error():
  data=request.args.get("message","自訂錯誤訊息")
  res = make_response(render_template('error.html',message=data))
  res.set_cookie(key='framework', value='', expires=0)
  return res


@app.route("/operation",methods=["POST"])
def operation():
  dataTest = request.form["number"]
  return redirect(url_for('square',urlData=dataTest))


@app.route("/square/<urlData>")
def square(urlData):
  test = int(urlData)
  reuslt =test ** 2
  return render_template("square.html",data=reuslt)

if __name__ == "__main__": 
  app.run(port=3000,debug=True)