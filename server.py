"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
              <html>Hi! This is the home page.
              <a href="/hello">Hello</a>
              </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label for="name">What's your name?</label>
          <input id="name" type="text" name="person">
          <label for='compliments'>Choose a compliment:</label>
          <select id='compliments' name="compliments">
            <option value='awesome'> Awesome </option>
            <option value='terrific'> Terrific </option>
            <option value='fantastic'> Fantastic </option> 
            <option value='neato'> Neato </option>
            <option value='fantabulous'> Fantabulous </option>
            <option value='wowza'> Wowza </option> 
            <option value='oh-so-not-meh'> Oh-so-not-meh </option> 
            <option value='brilliant'> Brilliant </option> 
            <option value='ducky'> Ducky </option> 
            <option value='coolio'> Coolio </option> 
            <option value='incredible'> Incredible </option> 
            <option value='wonderful'> Wonderful </option> 
            <option value='smashing'> Smashing </option>       
            <option value='lovely'> Lovely </option>                                          
          </select>  
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          <label for="name">What's your name?</label>
          <input id="name" type="text" name="person_too">
          <label for='disses'>Choose a diss:</label>
          <select id='disses' name="disses">
            <option value='not awesome'> Not awesome </option>
            <option value='not terrific'> not terrific </option>
            <option value='not fantastic'> not fantastic </option> 
            <option value='not neato'> not neato </option>
            <option value='not fantabulous'> not fantabulous </option>
            <option value='not wowza'> not wowza </option> 
            <option value='oh-so-meh'> Oh-so-meh </option> 
            <option value='not brilliant'> not brilliant </option> 
            <option value='not ducky'> not ducky </option> 
            <option value='not coolio'> not coolio </option> 
            <option value='not incredible'> not incredible </option> 
            <option value='not wonderful'> not wonderful </option> 
            <option value='not smashing'> not smashing </option>       
            <option value='not lovely'> not lovely </option>                                                       
          </select>  
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route("/diss")
def diss_person():
    """Get user by name."""

    player = request.args.get("person_too")

    diss = request.args.get("disses")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
