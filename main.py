
import speech_recognition as sr
import requests
import json
f= open('readme.txt', 'w')
f.write('"')
r = sr.Recognizer()
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
print(response.json())

