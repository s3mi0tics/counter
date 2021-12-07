in# one time events
```
pip install pipenv
```
# Flask app checklist
1. create assignment folder
2. navigate into assingnment folder from terminal
3. install flask
```
pipenv install flask
```
-type ls into terminal make sure you see pip file and pipfile.lock

4. launch virtual environment
```
python3 -m pipenv install flask
#THEN
pipenv shell

```
5. server.py
```
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

if __name__=="__main__":
    app.run(debug=True)

# all app routes and functions WILL MOVE later!!!!
```

6. paste to server
7. test server.py file

8. use "local host" @port

9. create file structure
    * pipfile
    * pipfilelock
    * server.py
    * templates
        * text.html
    * static
        * css
            * style.css
    * img
    * js
        * script.js