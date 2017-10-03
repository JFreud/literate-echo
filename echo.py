from flask import Flask, render_template, request


echo_app = Flask(__name__)


@echo_app.route("/")
def root():
    return render_template('base.html')

@echo_app.route("/response/", methods = ["POST"])
def response():
    print request.form
    return render_template("response.html", osis = request.form["username"], requester = request.method)



if __name__ == "__main__":
    echo_app.debug = True
    echo_app.run()
