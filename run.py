from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwertyuiop'

@app.route("/")
@app.route('/login.html', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login Successful for {form.username.data}!')
		return redirect(url_for('home'))
	return render_template('login.html', form=form)

if __name__ == '__main__':
	app.run(debug =True)