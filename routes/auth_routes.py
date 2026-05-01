from flask import Blueprint, request, jsonify
from db import mysql
from flask_bcrypt import Bcrypt
from auth import create_token

bcrypt = Bcrypt()

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    cur = mysql.connection.cursor()

    cur.execute(
        '''
        INSERT INTO users(username, useremail, userpassword)
        VALUES(%s,%s,%s)
        ''',
        (username, email, hashed_password)
    )

    mysql.connection.commit()
    cur.close()

    return jsonify({
        "message": "User registered successfully"
    })


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT id, username, useremail, userpassword FROM users WHERE useremail=%s",
        [email]
    )

    user = cur.fetchone()
    cur.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    user_id = user[0]
    username = user[1]
    useremail = user[2]
    hashed_password = user[3]

    if bcrypt.check_password_hash(hashed_password, password):
        token = create_token(user_id)

        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user_id,
                "username": username,
                "email": useremail
            }
        })

    return jsonify({"message": "Invalid credentials"}), 401


@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    return jsonify({
        "message": "Logout successful"
    })
