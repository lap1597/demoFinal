import git
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)

proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY']='0ab21496af69faf9cdab7e47762d3ae5'

@app.route('/', methods=['GET','POST'])
def register():
  form=RegistrationForm()
  if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!','success')
      return redirect(url_for('/home'))
  return render_template('register.html', title='Register',form=form)

@app.route("/home")
def hello_world():
    return render_template('home.html', subtitle='Hello Lap', text='This is the home page')





@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/lap1597/demoFinal')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__=='__main__':
  app.run(debug=True, host='0.0.0.0')








