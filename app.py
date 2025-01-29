from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
"""
    simple api task to retrieve info
"""

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_info():
    """
        retrieves the info of an intern at HNG and returns it.
    """
    email = "shalomzymike@gmail.com"
    present_time = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    git_url = "https://github.com/Khiingleo/hng12-backend-api-task"
    response = {
        "email": email,
        "current_datetime": present_time,
        "github_url": git_url
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()