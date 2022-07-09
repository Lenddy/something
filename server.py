from flask import Flask,render_template


app = Flask(__name__)


@app.route("/loop/<int:num>")
def hello(num):

    student = [{
        "name":"michael","age":35},
        {"name":"john","age":30},
        {"name":"mark","age":25},
        {"name":"kb","age":27}
]
    return render_template("index.html",student = student,num = num)






if __name__ == "__main__":
    app.run(debug=True)