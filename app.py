from flask import Flask,url_for
from views.home import home
from views.login import login
from views.register import registre

app=Flask(__name__)
app.config.from_object('config.config')
app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(registre)

if __name__=='__main__':
    app.run(debug=True)