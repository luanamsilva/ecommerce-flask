from flask import Flask

app = Flask(__name__)

@app.route('/' , methods = ['GET'])
def initial():
    return 'rota inicial'

if __name__ == '__main__':
  app.run(debug=True)