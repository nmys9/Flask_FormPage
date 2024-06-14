from flask import Blueprint,render_template,request
from views.forms import RegistrationForm

registre=Blueprint('registre',__name__,url_prefix='/registre')

@registre.route('/',methods=["GET","POST"])
def registre_form():
    form=RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name=form.username.data
            email=form.email.data
            return render_template('new_user.html',title=f'{name} User',name=name,email=email)
    return render_template('register.html',title='Registre Page',form=form)