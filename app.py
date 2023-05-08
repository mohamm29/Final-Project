
import os

from flask import Flask


app = Flask(__name__)


@app.route('/')
def final_project():
   target = os.environ.get('TARGET', 'Hello Everyone !!')
   return 'Welcome to Our IT-590  Final Project, {}!'.format(target)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',8080)), debug=True)
