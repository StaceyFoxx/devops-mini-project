# Note students, that whatever file has the Flask(__name__) in it, is the "api server" file.
from flask import Flask, jsonify, request
from mock_database import characters

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify("THIS IS ROOT")


@app.route("/characters", methods=["GET"])
def get_all_characters():
    return jsonify(characters)


# With route parameter 'an_id'
@app.route("/characters/<int:an_id>", methods=["GET"])
def get_character_by_id(an_id):
    char = [char for char in characters if char["id"] == an_id]
    return jsonify(char)


@app.route("/characters/<int:an_id>", methods=["DELETE"])
def remove_character_by_id(an_id):
    characters[:] = [char for char in characters if char["id"] != an_id]
    return jsonify(characters)


@app.route("/characters/add", methods=["POST"])
def add_new_character():
    new_char = request.get_json()
    characters.append(new_char)
    return jsonify(characters)


if __name__ == "__main__":
    app.run(debug=True)
