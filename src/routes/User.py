import jsonpickle
from src.base import app, db
from src.model.User import User


@app.route('/users', methods=['GET'])
def get_users():
    return jsonpickle.dumps(User.query.all())


@app.route('/users', methods=['POST'])
def post_user():
    user = User()
    user.name = "Jon"
    db.session.add(user)
    db.commit()
    return jsonpickle.dumps(user)
