
from flask import Flask, abort, make_response, request, jsonify
from models import todos


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
todos.create_table()


@app.route("/api/todos/", methods=["GET"])
def todos_list():
    conn = todos.create_connection()
    return str (todos.show_all(conn, "todos"))


@app.route("/api/todos/<int:id>", methods=["GET"])
def get_todo_id(id): 
    conn = todos.create_connection()
    return str(todos.show_where(conn, "todos", todos_id = id ))


@app.errorhandler(404)
def not_found(error):
    return make_response(({"error": "Not found", "status_code": 404}), 404)


@app.route("/api/todos/add", methods=["POST"])
def create_todo():
    conn = todos.create_connection()
    task = (
        4,
        "Zabierz parasol",
        "Będzie niezła ulewa",
        "started"
    )
    conn.commit()
    return str(todos.add_todos(conn, task))


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


@app.route("/api/todos/del", methods=["DELETE"])
def delete_todo():
    conn = todos.create_connection()
    return str (todos.delete_all(conn, "todos"))


@app.route("/api/todos/del/<int:id>", methods=["DELETE"])
def delete_todo_id(id): 
    conn = todos.create_connection()
    return str(todos.delete_where(conn, "todos", todos_id = id ))


@app.route("/api/todos/update/<int:id>", methods=["PUT"])
def update_todo_id(id): 
    conn = todos.create_connection()
    conn.close()
    return str (todos.update_todo(conn, "todos", todos_id = id, title ="Kup chleb"))
   

if __name__ == "__main__":
    app.run(debug=True)
    
