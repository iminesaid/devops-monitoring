from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
visits = Counter('visits', 'Number of visits')

@app.route('/')
def home():
    visits.inc()
    return "Hello DevOps!"

@app.route('/metrics')
def metrics():
    return generate_latest(visits), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
