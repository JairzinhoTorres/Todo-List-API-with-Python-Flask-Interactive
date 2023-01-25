from flask import Flask, jsonify,request,json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text
    

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE']) #declaramos un parametro que es donde esta el menor y mayor, y le declaramos un spacio de memoria que se llama posicion y el tipo de dato es entero porque esta especificado
def delete_todo(position):#aca se le pasa el valor que declaramos, y a esto le hacemos print
    print("This is the position to delete: ",position) #aca hacemos el print
    todos.pop(position)
    return jsonify(todos)



if __name__ == '__main__': #el if va siempre de ultimo 
  app.run(host='0.0.0.0', port=3245, debug=True)
    
\

