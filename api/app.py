from flask import Flask

from task.routes import bp

app = Flask(__name__)
app.register_blueprint(bp, url_prefix="/api/task")

if __name__ == "__main__":
    app.run(debug=True)
