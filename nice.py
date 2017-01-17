from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

LOSERNESS = [
    'are moronic', 'are foolish', "are 'smart' as a Donald", "have the 'best' words",
    "are despicable", "are deluded", "have clearly fake hair"]


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
            <a href="/hello">Hello</a><html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    words = ""

    for compliment in AWESOMENESS:
        words = words + "<option name=" + compliment + ">" + compliment + "</option>"

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <div>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <label>Select your compliment:
            <select name="compliment">""" + words + """</select>
          </label>
          <input type="submit">
        </form>
        </div>

              """  # <option value="awesome">awesome</option>
              # <option value="terrific">terrific</option>
              # <option value="fantastic">fantastic</option>
              # <option value="neato">neato</option>
              # <option value="fantabulous">fantastic</option>
              # <option value="oh-so-not-meh">oh-so-not-meh</option>
              # <option value="wowza">wowza</option>
              # <option value="brilliant">brilliant</option>
              # <option value="ducky">ducky</option>
              # <option value="coolio">coolio</option>
              # <option value="incredible">incredible</option>
              # <option value="wonderful">wonderful</option>
              # <option value="smashing">smashing</option>
              # <option value="lovely">lovely</option>
    """

        <h1>We don't like you</h1>
        <div>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <p> Prepare to be burned </p>
          <input type="submit">
        </form>
        </div>
      </body>
    </html>
    """


@app.route('/diss')
def be_mean():
    """Be mean to the user"""

    player = request.args.get("person")

    diss = choice(LOSERNESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Sick Burn</title>
      </head>
      <body>
        Hi %s I think you %s!
      </body>
    </html>
    """ % (player, diss)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, port=8000)
