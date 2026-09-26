from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello DevOps!</h1>
    <h2>AWS DevOps CI/CD Pipeline Project</h2>
    <p>GitHub → Jenkins → Docker → Docker Hub → AWS EC2</p>
    """

@app.route("/health")
def health():
    return "Application is healthy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)