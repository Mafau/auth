import app

@app.route('/user')
def get(id):
    user = User.query.get(id)
    return jsonify
