from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = {
    0: {
        "name": "Tarak",
        "content": "Whats happening today"
    }
}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/post/<int:post_id>")
def post(post_id):
    poster = posts.get(post_id)
    if not poster:
        return render_template("404.html", message="Post not Found")

    return render_template(
        "post.html",
        name=poster["name"],
        content=poster["content"]
    )

@app.route("/post/create")
def create_post():
    return render_template("create.html")

@app.route("/post/final_create", methods=["POST"])
def final_create_post():
    name = request.form["name"]
    content = request.form["content"]

    posts[len(posts)] = {
        "name": name,
        "content": content
    }

    return redirect(url_for("post", post_id=len(posts)-1))

if __name__ == "__main__":
    app.run(debug=True)