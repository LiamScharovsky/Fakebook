from app import app
#MAIN APPLICATION ROUTES
@app.route("/")
def home():
    return "Home Page"



@app.route("/users")
def users():
    return "Home Page"

@app.route("/users/<int:id>")
def userSingle():
    return "User Page"

#SHOP ROUTE
@app.route("/shop")
def shopPage():
    return "Shop Page"

@app.route("/shop/<int:id>")
def singleProduct():
    return "Single Product"

@app.route("/checkout")
def checkout():
    return "checkout Page"

@app.route("/contact")
def contact():
    return "Contact Page"
