from flask import Flask, render_template,request
import speech_recognition as sr
import requests
import json
f= open('readme.txt', 'w')
f.write('"')
r = sr.Recognizer()
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/speech")
def speech():
    while True:
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                code = r.recognize_google(audio)
                if code == 'exit':
                    break
                if code == 'print':
                    f.write('print("hello")')
                print("You said : {}".format(code))
            except:
                print("Sorry could not recognize what you said")

    f.write('"')
    return render_template("index.html",speech = f)

@app.route("/compile")
def compile(code):
    url = "https://codexweb.netlify.app/.netlify/functions/enforceCode"
    payload = json.dumps({
        "code": code,
        "language": "py",
        "input": ""
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()

    return render_template("index.html",output = res)
@app.route("/result",methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("index.html",name = name)
if __name__ == '__main__':
    app.run(debug=True,port=5001)