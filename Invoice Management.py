from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DATABASE = "invoice.db"
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS invoices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        amount INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
init_db()

@app.route("/invoices", methods=["POST"])
def add_invoice():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Data required"
        }), 400

    customer = data.get("customer_name")
    amount = data.get("amount")

    if not customer or amount is None:

        return jsonify({
            "error":
            "customer_name and amount required"
        }), 400

    try:

        conn = get_db()

        cursor = conn.execute(
            """
            INSERT INTO invoices(
            customer_name,
            amount
            )
            VALUES(?,?)
            """,
            (customer, amount)
        )

        conn.commit()

        invoice_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message": "Invoice created",
            "invoice_id": invoice_id
        }), 201

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500

@app.route("/invoices", methods=["GET"])
def get_invoices():

    try:

        conn = get_db()

        rows = conn.execute(
            "SELECT * FROM invoices"
        ).fetchall()

        conn.close()

        return jsonify([
            dict(row)
            for row in rows
        ])

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500

@app.route("/invoices/<int:id>", methods=["GET"])
def get_invoice(id):

    try:

        conn = get_db()

        row = conn.execute(
            """
            SELECT * FROM invoices
            WHERE id=?
            """,
            (id,)
        ).fetchone()

        conn.close()

        if row is None:

            return jsonify({
                "error":
                "Invoice not found"
            }), 404

        return jsonify(
            dict(row)
        )

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500

@app.route("/invoices/<int:id>", methods=["DELETE"])
def delete_invoice(id):

    try:

        conn = get_db()

        conn.execute(
            """
            DELETE FROM invoices
            WHERE id=?
            """,
            (id,)
        )

        conn.commit()

        conn.close()

        return jsonify({
            "message":
            "Invoice deleted"
        })

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500
if __name__ == "__main__":
    app.run(debug=True)