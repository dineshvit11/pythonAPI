from flask import Blueprint, request, jsonify
from db import mysql
from middleware import token_required
cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/api/addcart', methods=['POST'])
@token_required
def add_cart():

    data = request.get_json()

    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    cur = mysql.connection.cursor()

    cur.execute(
        '''
        INSERT INTO cart(user_id, product_id, quantity)
        VALUES(%s,%s,%s)
        ''',
        (user_id, product_id, quantity)
    )

    mysql.connection.commit()
    cur.close()

    return jsonify({
        "message": "Product added to cart"
    })


@cart_bp.route('/api/cart', methods=['GET'])
@token_required
def get_cart():

    cur = mysql.connection.cursor()

    cur.execute(
        '''
        SELECT c.id, p.product_name, p.product_price, c.quantity
        FROM cart c
        JOIN products p ON p.id = c.product_id
        '''
    )

    items = cur.fetchall()

    result = []

    for item in items:
        result.append({
            "cart_id": item[0],
            "product_name": item[1],
            "price": float(item[2]),
            "quantity": item[3]
        })

    cur.close()

    return jsonify(result)
