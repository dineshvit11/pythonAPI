from flask import Blueprint, jsonify
from db import mysql

product_bp = Blueprint('product_bp', __name__)


# =====================================
# GET ALL PRODUCTS
# =====================================

@product_bp.route('/api/product', methods=['GET'])
def get_products():

    cur = mysql.connection.cursor()

    cur.execute("""

        SELECT

            p.id,
            p.product_name,
            p.brand_name,
            p.price,
            p.discount_price,
            p.stock,
            p.rating,
            p.product_image,

            c.category_name

        FROM products p

        JOIN product_categories c
        ON c.id = p.category_id

    """)

    products = cur.fetchall()

    result = []

    for p in products:

        result.append({

            "id": p[0],

            "product_name": p[1],

            "brand_name": p[2],

            "price": float(p[3]),

            "discount_price": float(p[4]),

            "stock": p[5],

            "rating": float(p[6]),

            "product_image": p[7],

            "category": p[8]

        })

    cur.close()

    return jsonify(result)


# =====================================
# PRODUCT DETAILS
# =====================================

@product_bp.route('/api/product/details/<int:id>', methods=['GET'])
def product_details(id):

    cur = mysql.connection.cursor()

    cur.execute("""

        SELECT

            p.id,
            p.product_name,
            p.brand_name,
            p.short_description,
            p.full_description,
            p.price,
            p.discount_price,
            p.stock,
            p.color,
            p.size,
            p.rating,
            p.product_image,

            c.category_name

        FROM products p

        JOIN product_categories c
        ON c.id = p.category_id

        WHERE p.id=%s

    """, [id])

    product = cur.fetchone()

    cur.close()

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    return jsonify({

        "id": product[0],

        "product_name": product[1],

        "brand_name": product[2],

        "short_description": product[3],

        "full_description": product[4],

        "price": float(product[5]),

        "discount_price": float(product[6]),

        "stock": product[7],

        "color": product[8],

        "size": product[9],

        "rating": float(product[10]),

        "product_image": product[11],

        "category": product[12]

    })