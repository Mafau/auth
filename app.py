from main import app
import os, json

@app.route('/')
def get_user():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
