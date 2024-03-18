from flask import Flask
from flask import Flask, request, jsonify
from database import db
from models.product import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db.init_app(app)

@app.route('/' , methods = ['GET'])
def initial():
    return 'rota inicial'

if __name__ == '__main__':
  app.run(debug=True)