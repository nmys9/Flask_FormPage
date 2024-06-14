from flask import Blueprint,render_template,request
from views.forms import LoginForm

login=Blueprint('login',__name__,url_prefix='/login')

@login.route('/',methods=["GET","POST"])
def login_form():
    form=LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email=form.email.data
            return render_template('user.html',title='User Page',email=email)
    return render_template('login.html',title='Login Page',form=form)