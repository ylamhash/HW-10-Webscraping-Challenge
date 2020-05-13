# MongoDB and Flask Application
#################################################

# Dependencies and Setup
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_mars
from pymongo import MongoClient
import pymongo
 
# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo Connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

# Run the scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.replace_one({}, mars_data, upsert=True)
    return "Scraping Successful!"

# Redirect back to home page\n",
    return redirect("/", code=302)

    if __name__ == "__main__":
        app.run(debug=True)