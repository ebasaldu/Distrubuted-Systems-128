#Edbel Basaldua
# cruzid:ebasaldu
# implements a simple REST api using flask and python

from flask import Flask
from flask import request

app = Flask(__name__)

#@app.route("/")
#def ex():
# return "Testing app"


# accepts a GET request with no query string
# returns string "Hello, world!"
# also reutrn the succes status code
# performs error handling for POST

@app.route("/hello", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return "Hello, world!",200
    else:
        return "This method is unsupported", 405

#accepts both GET and POST
# if GET then return a succes code
# if POST and Msg then  returns success with given message
# else it performs error handling
@app.route("/test", methods=['GET','POST'])
def test():
    if request.method == 'GET':   
        return "GET message recieved",200
    if request.method =='POST' and request.args.get('msg')!= None:
        #Holds in the msg  string foo
        message = "POST message received: " + request.args.get('msg')
        return message , 200
    else: 
         return "This method is unspported",405

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
