from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
        </head>
        <body>
            <h1>🚀 DevOps CI/CD Pipeline Working!</h1>
            <p>GitHub → Jenkins → Docker → DockerHub</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
