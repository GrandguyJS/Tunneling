from flask import Blueprint, render_template, request, send_file, send_from_directory
import uuid
import os
import shutil
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

views = Blueprint("views", __name__)

def senddata(key, code=""):
    path = "C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+str(key)+".zip"
    path2 = "C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+key+".txt"
    if os.path.exists(path):
        with open(path2, "r") as b:
            if b.read() == str(code):
                return "OK" 
            else:
                return "NO"
    else:
        return "NO"


@views.route("/")
def home():
    return render_template("main.html")

@views.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        code1 = request.form["password"]
        
        code = uuid.uuid4()
        url= "C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+str(code)
        f = request.files.getlist("file[]")
        
        os.makedirs(url)
        for i in f:

            i.save(url+"/"+i.filename)  

        shutil.make_archive(url, 'zip', url)
        with open("C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+str(code) +".txt", "w") as b:
            b.write(code1)
            b.close()
        shutil.rmtree(url+"/")
        return render_template("main2.html", name = str(code), url = f"http://carrycode.us.to:5000/downloadrequest?url={code}&pass={code1}")


@views.route("/download", methods = ['POST', "GET"])
def download():
    if request.method == "POST":
        key = request.form["url"]
        code = request.form["pass"]
        path = "C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+str(key)+".zip"

        request1 = senddata(key,code)

        if request1 == "OK":
            return send_file(path, as_attachment=True)
        elif request1 == "NO":
            return render_template("download.html", problem="Wrong Password or Tunnel Key")
    else:
        return render_template("download.html")

@views.route("/upload")
def upload():
    return render_template("upload.html")

@views.route("/downloadrequest")
def downloadrequest():
    args = request.args
    if args:
        key = args.get("url")
        code = args.get("pass")
        if code == "":
            code = ""
        path = "C:/Users/GrandguyMC/Documents/Tunneling/Uploads/"+str(key)+".zip"

        request1 = senddata(key,code)

        if request1 == "OK":
            return send_file(path, as_attachment=True)
        elif request1 == "NO":
            return render_template("download.html", problem="Wrong Password or Tunnel Key")
    else:
        return render_template("download.html")

@views.route("/page1", methods = ['POST', "GET"])
def page1():
    return render_template("howdoesitwork.html")
@views.route("/page2", methods = ['POST', "GET"])
def page2():
    return render_template("howdoesitwork.html")
@views.route("/page3", methods = ['POST', "GET"])
def page3():
    return render_template("privacy.html")
