from flask import Blueprint, render_template, request, send_file, send_from_directory, redirect, url_for, session

 # from flask import Response, stream_with_context 
 # WORK IN PROGRESS

import uuid
import os
import shutil
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import urllib.parse
import requests

from flask_login import current_user, login_required

from .models import User, File

views = Blueprint("views", __name__)

#Models import


from . import db

base_url = "/Users/grandguymc/Code/Tunneling/Uploads/"

@views.route("/")
def home():
    
    
    return render_template("/Container-Pages/main.html", user=current_user)

@views.route('/success', methods = ['POST'])  

def success():  
    if request.method == 'POST':  
        code1 = request.form["password"]
        
        code = uuid.uuid4()
        url= base_url+str(code)
        f = request.files.getlist("file[]")
        


        os.makedirs(url)
        for i in f:

            i.save(url+"/"+i.filename)  

        shutil.make_archive(url, 'zip', url)
        with open(base_url+str(code) +".txt", "w") as b:
            b.write(code1)
            b.close()
        shutil.rmtree(url+"/")

        domain = request.url_root      # Get the current domain name

        url_done = f"{domain}downloadrequest?url={code}&pass={code1}"

        if code1 == "":
            code1 = None
        else:
            pass

        

        file = File(display_name = f"{f[0].filename} [{len(f)}  File(s)].zip", key=str(code), url=url_done, passkey=code1, user = current_user.get_id()) # Key is name
        db.session.add(file)
        db.session.commit()

        return render_template("/Container-Pages/success.html", name = str(code), url = url_done, user=current_user)


@views.route("/download", methods = ['POST', "GET"])
def download():
    if request.method == "POST":  
        key = request.form["key"]
        path = base_url+str(key)+".zip"

        file = File.query.filter_by(key=key).first()
        if file:
            
            if file.user == current_user.id:
                return send_file(path, as_attachment=True, download_name = file.display_name)
            else:
                code = request.form["pass"]
                if code == file.passkey:
                    
                    return send_file(path, as_attachment=True, download_name = file.display_name)
                else:
                    return render_template("/Container-Pages/download.html", problem="user", user=current_user)
        else:
            return render_template("/Container-Pages/download.html", problem="file", user=current_user)
    else:
        return render_template("/Container-Pages/download.html", user=current_user)

@views.route("/upload")

def upload():
    return render_template("/Container-Pages/upload.html", user=current_user)

@views.route("/downloadrequest")
def downloadrequest():
    args = request.args
    if args:
        key = args.get("url")
        code = args.get("pass")
        code = None if code == "" else code
    file = File.query.filter_by(key=key).first()

    
    if file and (code == file.passkey):
        path = base_url+str(key)+".zip"
        return send_file(path, as_attachment=True, download_name = file.display_name)
    else:
        return render_template("/Container-Pages/download.html", problem="File does not exist or invalid password", user=current_user)

@views.route("/downloadanonym", methods = ['POST', "GET"])
def downloadanonym():
    #Work in progress
    """
    if request.method == "POST":
        url = request.form["url"]
        try:
            r = requests.get(url, stream=True)
        except:
            return render_template("/Container-Pages/main.html")
        else:
            
            filename = request.form["name"]
            if filename == "":
                filename = "File"
            else:
                pass

            open(f"./Uploads/{filename}", 'wb').write(r.content)

            path = f"./Uploads/{filename}"

            return send_file(path, as_attachment=True)
    """

        

        

@views.route("/page1", methods = ['POST', "GET"])
def page1():
    return render_template("/Container-Pages/howdoesitwork.html", user=current_user)

@views.route("/page3", methods = ['POST', "GET"])
def page3():
    return render_template("/Container-Pages/privacy.html", user=current_user)

# Files

@views.route("/files", methods = ['POST', "GET"])
@login_required
def files():
    return render_template("/Container-Pages/files.html", user=current_user)

# Delete

@views.route("/delete", methods = ["POST"])
@login_required
def delete():

    key = request.form["key"]
    file = File.query.filter_by(key=key).first()
    if file:

        if file.user == current_user.id:

            db.session.delete(file)
            db.session.commit()
            return redirect("/files")
        else:
            return redirect("/files")
    else:
        return redirect("/files")




