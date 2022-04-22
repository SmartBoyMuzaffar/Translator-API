"""
# With only flask

# Using flask to make an api
# import necessary libraries and functions

from googletrans import Translator
from flask import Flask, jsonify, request




trans = Translator()

# creating a Flask app

app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        return jsonify({"Description" : "Hello My Friend! What can this api? This api can translate entered text to Uzbek!"})




# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)

@app.route('/Muzaffar/<text>', methods = ['GET'])
def desp(self, name):

    self.my_text = my_text

    result = trans.translate(my_text, dest='uz').text
    return jsonify({'-->' : result})


# driver function
if __name__ == '__main__':

    app.run(debug = True)

"""

from googletrans import Translator

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


trans = Translator()


class HelloWorld(Resource):
    def get(self):
        return {"Description" : "Hello My Friend! What can this api? This api can translate entered text to Uzbek!"}


class Muzaffar(Resource):
    def get(self, my_text):
        self.my_text = my_text
        
        result = trans.translate(my_text, dest='uz').text
        return {'-->' : result}
        #return {'-->' : result.text}

api.add_resource(HelloWorld, '/')
api.add_resource(Muzaffar, '/Muzaffar/<my_text>')

if __name__ == '__main__':
    app.run(debug=True)

