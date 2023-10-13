from queue import Queue
from threading import Lock
import threading

from flask import Flask,render_template
from sd_list import  SPeaker
import json
Change_value=Queue()

app = Flask(__name__)


 
 


"""
SS=SPeaker()

@app.route("/data")
def Speaker():
        return json.dump(json.loads(json.loads(SS.Get_data())))

"""

SS=SPeaker()

@app.route("/")
def Index():
       return render_template("index.html")


@app.route("/data")
def Speaker():
        return SS.Get_data()
        #return 
        
app.run(debug=False,port=5050,threaded=True)

 


while True:
     pass
