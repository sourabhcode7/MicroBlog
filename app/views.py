# The views are the handlers that respond to requests from web browsers or other clients. In Flask 
# handlers are written as Python functions. Each view function is mapped to one or more request URLs.
from app import app
from flask import render_template, redirect, flash
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}

    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },

        {
            'author': {'nickname': 'jiji'},
            'body': 'The Avengewas so cool!'
        },
        {
            'author': {'nickname': 'hhhh'},
            'body': 'The Avengso cool!'
        }
    ]

    return render_template(
        'index.html',
        title='Home',
        user=user,
        posts=posts
    )
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))

#flash() – Displays a temporary notification message to the user.

# %s – A placeholder that gets replaced with a value.

# % – Connects the string with the values that replace its placeholders (string formatting).

# form.openid.data – Gets the value entered in the OpenID field.

# form.remember_me.data – Gets the Remember Me checkbox value (True or False).

# str() – Converts a value into text. It's unnecessary here because %s already does that conversion.

# ( ) – Holds the values in a tuple, supplied in the same order as the placeholders.

        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


