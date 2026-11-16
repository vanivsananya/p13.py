from flask import Flask, jsonify
app=Flask(__name__)
users=[
    {"id":1,"name":"anu","email":"anu@example.com"},
    {"id":2,"name":"manu","email":"manu@example.com"},
    {"id":3,"name":"dru","email":"dru@example.com"},
    {"id":4,"name":"bob","email":"bob@example.com"},
    {"id":5,"name":"vani","email":"vani@example.com"}
]
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"]==user_id:
            return jsonify(user)
    return jsonify({"error":"user not found"}),404

if __name__ == "__main__":
    app.run(debug=True)
    
    
