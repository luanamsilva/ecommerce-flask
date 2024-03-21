from flask import Flask
from flask import Flask, request, jsonify
from database import db
from models.product import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db.init_app(app)

@app.route('/api/products/add', methods=['POST'])
def add_product():
   data = request.json
   if "name" in data and "price" in data:
     product = Product(name=data['name'], price= data['price'], description= data.get("description", ""))
     db.session.add(product)
     db.session.commit()
     return jsonify({"message": "Produto cadastrado com sucesso!"})
   return jsonify({"message": "Dados inválidos."}),400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
   product = Product.query.get(product_id)
   if product:
      db.session.delete(product)
      db.session.commit()
      return jsonify({"message": "Produto deletado com sucesso"})
   return jsonify({"message":"Produto não encontrado!"}),404

@app.route('/' , methods = ['GET'])
def initial():
    return 'rota inicial'

if __name__ == '__main__':
  app.run(debug=True)