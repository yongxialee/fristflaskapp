from random import randint,choice
from flask import Flask,request ,render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = "ThisisHappy123"
debug = DebugToolbarExtension(app)

# responde with a from
@app.route('/form')
def show_from():
    return render_template("form.html")

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')



@app.route('/spell/<word>')
def spell(word):
    caps=word.upper()
    return render_template("spell.html",word=caps)

@app.route('/hello')
def say_hello():
    return render_template("hello.html")

COMPLIMENTS=['cool','clever','awesome','pythonic','tenacious']

@app.route('/greet')
def greet():
    username=request.args["username"]
    nice_thing=choice(COMPLIMENTS)
    return render_template("greet.html",username=username,compliment=nice_thing)

@app.route("/goodbye")
def say_goodbye():
    return "Good Bye!!"
    
@app.route('/lucky')
def lucky_number():
    num =randint(1,20)
    return render_template("lucky.html",lucky_num=num)

# exctracting  datta in the Get request from the query string using request.args
@app.route('/search')
def search():
    term = request.args['term']
    sort =request.args['short']
    return f"<h1>Search Result For: {term} </h1> <p> Sort by: {sort}</p>"

# @app.route("/post",methods=["POST","GET"])
# def post_demo():
#     return "youre sending POST request!"


# respond to get request for the same pass as the post request 
@app.route("/add-comment")
def add_comment_form():
    return """
        <h1>Add Comment Form</h1>
        <form method="POST">
            <input type = 'text' placeholder ='comment' name='comment'/>
            <input type='text' placeholder='username' name='username' />
            <button>Submit</button>
        </form>
    """
# post request
# extracting data from a POST request form data using request.form
@app.route("/add-comment", methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username=request.form["username"]
    print(request.form)
    return f"""
        <h1>Save your comment</h1>
        <ul>
        <li> Username:{username}</li>
        <li>Comment: {comment}</li>
    """

# variable 
POSTS={
    1: "I like chicken",
    2: "I also like mango",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}
@app.route('/posts/<int:id>')
def find_post(id):
    post =POSTS.get(id,"Post is not found")
    return f"<p>{post}</p>"
# variable can be more multiple 
# @app.route(/r/<subreddit>/comment/<int:id>)
# def show_comment(subreddit,id):