from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from werkzeug import exceptions

app= Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Welcome home'

@app.route('/goals', methods=['GET','POST'])
def goals():
    # if request.method == 'GET':
        return jsonify({'Goals': ['Aquire many moneys', 'become a competent coder', 'more healthy', 'have some cats and dogs', 'bulk up', 'tan']}
        )
    # if request.method == 'POST':
    #     data = request.form
    #     goal = data["goal"]

    #     goal_list = [{"goal": goal}]
    #     return render("index.html", goal_list = goal_list)

    # return render("index.html")

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Uh ohh... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}. I swear this never normally happens!!"})

if __name__ == '__main__':
    app.run(debug = True)
