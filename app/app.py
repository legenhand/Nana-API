from flask import Flask, jsonify

app = Flask(__name__)

repo = {
  "Nana-bot" : {
    "Author" : "Legenhand",
    "repo-link" : "https://github.com/legenhand/Nana-Bot",
    "version" : {
      "latest" : {
        "is-beta" : False,
        "dockerfile" : "https://raw.githubusercontent.com/legenhand/Nana-Bot/master/Dockerfile",
        "description" : "blablablaaa"
      },
      "v1.1.1b" : {
        "is-beta" : False,
        "dockerfile" : "https://raw.githubusercontent.com/legenhand/Nana-Bot/v1.1.1b/Dockerfile",
        "description" : "old version of nana"
      },
      "v2.1" : {
        "is-beta" : False,
        "dockerfile" : "https://raw.githubusercontent.com/legenhand/Nana-Bot/v2.1/Dockerfile",
        "description" : "Version of Nana Using pyrogram 0.18"
      }
    }
  },
  "Nana-Remix" : {
    "Author" : "Pokurt",
    "repo-link" : "https://github.com/pokurt/Nana-Remix",
    "version" : {
      "latest" : {
        "is-beta" : False,
        "dockerfile" : "https://raw.githubusercontent.com/pokurt/Nana-Remix/master/Dockerfile",
        "description" : "blablablaaa"
      }
    }
  }
}

@app.route('/')
def hello_world():
    return {'hello': 'world'}

@app.route('/repo')
def repo_list():
    return jsonify(repo)


if __name__ == '__main__':
    app.run()
