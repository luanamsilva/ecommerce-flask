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

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
   product = Product.query.get(product_id)
   if product:
      return jsonify({"id": product_id,
                      "name": product.name,
                      "price": product.price,
                      "description": product.description
                      })
   return jsonify({"message":"Produto não encontrado"}),404

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
   product = Product.query.get(product_id)
   if not product:
      return jsonify({"message" : "Produto não encontrado"}), 404
   
   data = request.json
   if "name" in data:
      product.name = data['name']
   if "price" in data:
      product.price = data['price']
   if "description" in data:
      product.description = data['description']
   db.session.commit()
   return jsonify({"message": "Produto atualizado com sucesso!"})

@app.route('/api/products', methods=['GET'])
def get_products():
   products = Product.query.all()
   product_list = []
   for product in products:
       product_data = {
         "id": product.id,
         "name": product.name,
         "price": product.price,
       }
       product_list.append(product_data)
   return jsonify(product_list)
if __name__ == '__main__':
  app.run(debug=True)