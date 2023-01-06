from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template("read.html", all_users = users)
# ------------------------------


@app.route('/add/user')
def add_user():
    return render_template("create.html")


# ------------------------------

@app.route('/create/user', methods=['POST'])
def create_user():


    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/')

# ------------------------------


@app.route('/show_user/<int:id>')
def show_user(id):
    data = { "id": id }

    user = User.show_user(data)

    return render_template("show_user.html", user=user)

# ------------------------------


@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = { "id": id }

    user = User.show_user(data)

    return render_template("edit_user.html", user=user)

# ------------------------------

#  create route to process updated data

@app.route('/user/update', methods=['POST'])
def update_user():
    User.update_user(request.form)
    return redirect('/')

# ------------------------------


@app.route('/user/delete_user/<int:id>')
def delete_user(id):
    data = { "id": id }

    User.delete_user(data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)