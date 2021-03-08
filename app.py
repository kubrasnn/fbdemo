import urllib
import pyrebase
from flask import Flask
from pyrebase.pyrebase import Storage

app = Flask(__name__)

firebaseConfig= {'apiKey': "AIzaSyBjsxZYpDCRXUEOAoYAFDrt5cHQttjyprk",
    'authDomain': "fir-demo-6b29a.firebaseapp.com",
    'databaseURL': "https://fir-demo-6b29a-default-rtdb.firebaseio.com",
    'projectId': "fir-demo-6b29a",
    'storageBucket': "fir-demo-6b29a.appspot.com",
    'messagingSenderId': "317388361340",
    'appId': "1:317388361340:web:f7d5070fe32e90c34dc3f9",
    'measurementId': "G-13NVC7YSYY"}

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
#auth=firebase.auth()
#storage=firebase.storage()

#Authentication
#Login
#email= input("Mail adresinizi giriniz: ")
#password= input("Şifrenizi giriniz: ")
#try:
#    auth.sign_in_with_email_and_password(email,password)
#    print("Başarılı şekilde giriş yapıldı!")
#except:
#    print("Email ya da şifre yanlış!")

#Signup
#email= input("Mail adresinizi giriniz: ")
#password= input("Şifrenizi giriniz: ")
#confirmpass= input("Şifrenizi tekrar giriniz: ")
#if password==confirmpass:
#    try:
#        auth.create_user_with_email_and_password(email,password)
#        print("Kullanıcı başarılı bir şekilde oluşturuldu!")
#    except:
#        print("Kullanıcı oluşturulamadı!")

#Storage
#Upload
#filename= input("Yüklemek istediğiniz dosya adını giriniz: ")
#cloudfilename= input("Buluta yüklemek istediğiniz dosya adını giriniz: ")
#Storage.child(cloudfilename).put(filename)
#print(Storage.child(cloudfilename).get_url(None))

#download
#cloudfilename= input("İndirmek istediğiniz dosya adını giriniz: ")
#Storage.child(cloudfilename).download("","downloaded.txt")

#reading file
#cloudfilename= input("İndirmek istediğiniz dosya adını giriniz: ")
#url= Storage.child(cloudfilename).get_url(None)
#f= urllib.request.urlopen(url).read()
#print(f)

#Database
#Create
#data={'yaş':26,'adres':"İstanbul",'çalışan':True,'isim':"Kübra Sinan"}
#db.push(data)
#db.child("Kullanıcılar").push(data)
#db.child("Kullanıcılar").set(data)

#Update
#db.child("Kullanıcılar").update({'adres':"Çekmeköy"})

#kullanıcılar=db.child("Kullanıcılar").get()
#for kullanıcı in kullanıcılar.each():
#    print(kullanıcı.val())
#    print(kullanıcı.key())

#Delete
#db.child("Kullanıcı").child("isim").remove()

#Read
#kullanıcı=db.child("Kullanıcı").get()
#print(kullanıcı.val())

#kullanıcı=db.child("Kullanıcı").order_by_child("yaş").equal_to(30).get()
#for k in kullanıcı.each():
#    print(k.val())

@app.route('/')
def index():
    return "Merhaba Dünyalı"

@app.route('/hi')
def hi():
    return "Merhaba Kübra"

if __name__ == '__main__' :
    app.run(debug=True)
    