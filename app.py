from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
second=[]        
@app.route('/')
def home():
     return render_template("sample.html",s=second)

@app.route('/hai',methods=["POST","GET"])
def form1():
     if request.method=="POST":
          thumbnail=request.form.get("thumbnail")
          photos=request.form.get("photos")
          description=request.form.get("description")
          views=request.form.get("views")
          channel=request.form.get("channel")
          uploaded=request.form.get("uploaded")
          dic={}
          dic.update({"thumbnail":thumbnail})
          dic.update({"photos":photos})
          dic.update({"description":description})
          dic.update({"views":views})
          dic.update({"channel":channel})
          dic.update({"uploaded":uploaded})
          second.append(dic)
          print(dic)
          return redirect("/")
     return render_template("form1.html", s=second)



if __name__=="__main__":
    app.run(debug=True)
    