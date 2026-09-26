from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello DevOps!</h1>
    <h2>CI/CD Version 2</h2>
    <p>Application deployed successfully using CI/CD.</p>
    <p>GitHub → Jenkins → Docker → Docker Hub → AWS EC2</p>
    <p>New code change deployed automatically.</p>
    """

@app.route("/health")
def health():
    return "Application is healthy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)