from flask import Blueprint, jsonify, request
from db import mysql

user_bp = Blueprint('user_bp', __name__)


# =========================
# GET ALL USERS
# =========================
@user_bp.route('/api/user', methods=['GET'])
def get_users():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT
            id,
            username,
            useremail,
            mobile,
            country,
            state,
            created_date
        FROM users
    """)

    users = cur.fetchall()

    result = []

    for user in users:

        mobile = str(user[3]) if user[3] else ""

        masked_mobile = "XXXXXX" + mobile[-4:] if mobile else ""

        result.append({
            "id": user[0],
            "username": user[1],
            "useremail": user[2],
            "mobile": masked_mobile,
            "country": user[4],
            "state": user[5],
            "created_date": str(user[6])
        })

    cur.close()

    return jsonify(result)


# =========================
# ADD USER
# =========================
@user_bp.route('/api/user', methods=['POST'])
def add_user():

    data = request.get_json()

    username = data.get('username')
    useremail = data.get('useremail')
    password = data.get('password')
    mobile = data.get('mobile')
    country = data.get('country')
    state = data.get('state')

    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO users
        (
            username,
            useremail,
            userpassword,
            mobile,
            country,
            state
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        username,
        useremail,
        password,
        mobile,
        country,
        state
    ))

    mysql.connection.commit()
    cur.close()

    return jsonify({
        "message": "User added successfully"
    })


# =========================
# EDIT USER BY ID
# =========================
@user_bp.route('/api/user/edit/<int:id>', methods=['GET'])
def edit_user(id):

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT
            id,
            username,
            useremail,
            mobile,
            country,
            state
        FROM users
        WHERE id=%s
    """, [id])

    user = cur.fetchone()

    cur.close()

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify({
        "id": user[0],
        "username": user[1],
        "useremail": user[2],
        "mobile": user[3],
        "country": user[4],
        "state": user[5]
    })


# =========================
# UPDATE USER
# =========================
@user_bp.route('/api/user/update/<int:id>', methods=['PUT'])
def update_user(id):

    data = request.get_json()

    username = data.get('username')
    useremail = data.get('useremail')
    mobile = data.get('mobile')
    country = data.get('country')
    state = data.get('state')

    cur = mysql.connection.cursor()

    cur.execute("""
        UPDATE users
        SET
            username=%s,
            useremail=%s,
            mobile=%s,
            country=%s,
            state=%s
        WHERE id=%s
    """, (
        username,
        useremail,
        mobile,
        country,
        state,
        id
    ))

    mysql.connection.commit()
    cur.close()

    return jsonify({
        "message": "User updated successfully"
    })


# =========================
# DELETE USER
# =========================
@user_bp.route('/api/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM users WHERE id=%s",
        [id]
    )

    mysql.connection.commit()
    cur.close()

    return jsonify({
        "message": "User deleted successfully"
    })