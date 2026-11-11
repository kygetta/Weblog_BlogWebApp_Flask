#Author: Kylie Hall
#Date: 11/7/26
# Script creates the application object as an instance of class Flask imported from the flask package.



from flask import Flask

app = Flask(__name__) # __name__ is a predefined variable, which is set to the name of the module in which it is used
# Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as temple files


from apphost import routes #routes module handles URLs that the app supports. Handlers for the app are called "view functions"
