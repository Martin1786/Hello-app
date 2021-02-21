from flask import Flask, render_template
from flask import request

app = Flask(__name__)


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )
# localhost:8080/user/John
@app.route("/user/<name>")
def user(name):
   return render_template("user.html",user_name=name)


# localhost:8080/pizza
@app.route("/pizza")
def pizza():
    favourite_pizza = ["mushroom", "Cheese", "Anchovy", 41]
    return render_template("pizza.html",favourite_pizza=favourite_pizza)
    
    
#Create Custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404
        
#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500
  

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)