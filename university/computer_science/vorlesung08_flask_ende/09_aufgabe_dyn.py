from typing import Dict
from flask import Flask, render_template

class User:
    def __init__(self, id: int, username: str, real_name: str, age: int):
        self.id: int = id
        self.username: str = username
        self.real_name: str = real_name
        self.age: int = age

all_users: Dict[int, User] = {
    1: User(1, 'j.bond', 'James Bond', 51),
    2: User(2, 'j.bourne', 'Jason Bourne', 56),
    3: User(3, 'j.bauer', 'Jack Bauer', 48)
}


app = Flask(__name__)

@app.route('/users')
def route_users():
    return render_template('09_users.html', users=all_users)

@app.route('/users/<int:id>')
def route_user_by_id(id: int):
    user = all_users.get(id)
    if user is None:
        return "TODO: no such user..."

    return render_template('09_user_id.html', user=user)