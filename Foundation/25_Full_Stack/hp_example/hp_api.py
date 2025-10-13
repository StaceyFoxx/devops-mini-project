"""
This is your server - Flask goes here
"""
from flask import Flask, jsonify, request
from db_utils import get_all_characters_db, delete_student_by_id, add_new_character_db
# from flask_cors import CORS  # IGNORE THIS - IT'S ONLY FOR HAMED DEMO

app = Flask(__name__)
# CORS(app)  # IGNORE THIS - IT'S ONLY FOR HAMED DEMO


@app.route("/characters", methods=["GET"])
def get_all_characters():
    # return jsonify("TESTING ENDPOINT")
    return jsonify(get_all_characters_db())


@app.route("/characters/add", methods=["POST"])
def add_new_characters():
    new_student_dict = request.get_json()
    return jsonify(add_new_character_db(new_student_dict))


@app.route("/characters/remove/<int:id>", methods=["DELETE"])
def del_user_by_id(id):
    return jsonify(delete_student_by_id(id))


if __name__ == "__main__":
    app.run(debug=True)
