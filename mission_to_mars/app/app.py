# import Flask, pymongo, and scrape_mars (your python file)
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# Instantiate a Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# Create a base '/' route that will query your mongodb database and render the `index.html` template
@app.route("/")
def index():
    print('msg that shows in the terminal')
    text_to_render = "New text!"
    return render_template("index.html", headline=text_to_render)

# Create a '/scrape' route that will create the mars collection, run your scrape() function from scrape_mars, and update the mars collection in the database
# The route should redirect back to the base route '/' with a code 302.
@app.route("/scrape")
def scraper():
    listing = mongo.db.listing
    listing_data = scrape_mars.scrape()
    listing.update({}, listing_data, upsert=True)
    return redirect("/", code=302)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    destination.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


# Run your app
if __name__ == "__main__":
    app.run(debug=True)