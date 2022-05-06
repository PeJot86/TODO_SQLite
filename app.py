
from flask import Flask, make_response, jsonify
from models import todos


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
todos.create_table()


@app.route("/api/todos/", methods=["GET"])
def todos_list():
    return jsonify (todos.show_all("todos"))


@app.route("/api/todos/<int:id>", methods=["GET"])
def get_todo_id(id): 
    return jsonify (todos.show_where("todos", todos_id = id ))


@app.errorhandler(404)
def not_found(error):
    return make_response(({error: "Not found", "status_code": 404}), 404)


@app.route("/api/todos/add", methods=["POST"])
def create_todo():
    task = (
        1,
        "Zabierz parasol",
        "Będzie niezła ulewa",
        "started"
    )
    return jsonify (todos.add_todos(task))


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({error : "Bad request", "status_code": 400}), 400)


@app.route("/api/todos/del", methods=["DELETE"])
def delete_todo():
    return jsonify (todos.delete_all("todos"))


@app.route("/api/todos/del/<int:id>", methods=["DELETE"])
def delete_todo_id(id): 
    return jsonify (todos.delete_where("todos", todos_id = id ))


@app.route("/api/todos/update/<int:id>", methods=["PUT"])
def update_todo_id(id): 
    return jsonify (todos.update_todo("todos", todos_id = id, title ="Kup chleb"))
   

if __name__ == "__main__":
    app.run(debug=True)
    
