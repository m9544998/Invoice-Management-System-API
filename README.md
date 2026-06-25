
# Invoice Management System API
---
A RESTful API built using Flask and SQLite to manage customer invoices.

This project allows users to create, view, and delete invoices.
```
---
- Python 3
- Flask
- SQLite3
- REST API

---

##  Project Structure

```text
invoice-management-api/
│
├── app.py
├── invoice.db
├── README.md

Install dependencies:

```bash
pip install flask
```

Run project:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```
---

##  Create Invoice

Request

```json
{
 "customer_name":"Maheen",
 "amount":5000
}
```

Response

```json
{
 "message":"Invoice created",
 "invoice_id":1
}
```

---

##  Get All Invoices

Request

```http
GET /invoices
```

Response

```json
[
 {
  "id":1,
  "customer_name":"Maheen",
  "amount":5000
 }
]
```

---

## Get Invoice By ID

Request

```http
GET /invoices/1
```

Response

```json
{
 "id":1,
 "customer_name":"Maheen",
 "amount":5000
}
```

---

##  Delete Invoice

Request

```http
DELETE /invoices/1
```

Response

```json
{
 "message":"Invoice deleted"
}
```
##  Author

**Maheen Asad**

Flask • SQLite • REST API
