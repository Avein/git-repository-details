from flask import Flask
import json
import requests

GIT_API_URL = 'https://api.github.com'
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello to Get Repository script"


@app.route('/repositories/<owner>/<repository_name>')
def get_repo_info(owner, repository_name):
    url = '{}/repos/{}/{}'.format(GIT_API_URL, owner, repository_name)

    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        response = response.json()
        repo_info = {
            "fullName": response['full_name'],
            "description": response['description'],
            "cloneUrl": response['clone_url'],
            "stars": response['stargazers_count'],
            "createdAt": response['created_at']
        }
        return json.dumps(repo_info)
    elif response.status_code == requests.codes.NOT_FOUND:
        return "Sorry given user or repository does not exist"


if __name__ == "__main__":
    app.run()
