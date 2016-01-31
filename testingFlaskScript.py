from flask.ext.script import Manager
from flask import Flask
#import hello
app = Flask(__name__)
#from myapp import app
#import hello

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()
