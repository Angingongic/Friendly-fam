# im skidding this bro's project so hard :fire:

# guys this was made by me trustffff

# @dareddd_ on discord yayayayay 🤑🤑😭😭

import flask
from flask import request, render_template, session

app = flask.Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host='localhost', port=8080)
  import os
  host=os.environ.get("SERVER_HOST", "localhost")
  try:
    port = int(os.environ.get("SERVER_PORT", "5555"))
  except:
     port = 5555
    
  app.run(host, port, debug=True)
