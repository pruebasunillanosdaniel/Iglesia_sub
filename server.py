from queue import Queue
from threading import Lock
import threading

from flask import Flask
from sd_list import  Speaker_text
Change_value=Queue()


lock = Lock()
 

app = Flask(__name__)
t2 = threading.Thread(target=Speaker_text, args=[lock,Change_value])
t2.start()
@app.route("/")
def hello_world():
        b=str(Change_value.get())
        print(b)
        a="<h1>"+"Change_value"+""+b+"</h1>" 
        return a



app.run(debug=False,port=5050,threaded=True)

 


while True:
     pass
