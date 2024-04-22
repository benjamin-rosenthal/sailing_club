from hello import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"