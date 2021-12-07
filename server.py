from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key="root"

@app.route('/')
def hello_world():
    if "refresh" in session:
        session["refresh"]+=1
    else: session['refresh']=1
    return render_template('index.html')

@app.route('/plus2')
def plus_two():
    session['refresh']+=1
    return redirect ('/')

@app.route('/reset')
def reset():
    session['refresh']=0
    return redirect ('/')

@app.route('/increment')
def increment():
    session['refresh']+= int(session['times'])
    return redirect('/')

@app.route('/destroy_session')
def count_0():
    if 'refresh' in session:
        session.clear()
        return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)