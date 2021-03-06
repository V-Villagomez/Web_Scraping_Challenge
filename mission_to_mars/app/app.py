# import Flask, pymongo, and scrape_mars (your python file)
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Instantiate a Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection; the creation of the database if not necessary if coded as: 
conn = "mongodb://localhost:27017/mission_to_mars"
client = PyMongo(app, uri=conn)

# Create a base '/' route that will query your mongodb database and render the `index.html` template
@app.route("/")
def index():
    mars_info = client.db.mars.find_one()
    #print(mars_info)
    return render_template("index.html", mars_info = mars_info)

# Create a '/scrape' route that will create the mars collection, run your scrape() function from scrape_mars, and update the mars collection in the database
# The route should redirect back to the base route '/' with a code 302.
@app.route("/scrape")
def scraper():
    mars_info = client.db.mars
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

# Run your app
if __name__ == "__main__":
    app.run(debug=True)