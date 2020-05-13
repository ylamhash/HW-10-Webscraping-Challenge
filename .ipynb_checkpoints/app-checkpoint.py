{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# MongoDB and Flask Application\n",
    "#################################################"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "from flask import Flask \n",
    "from flask import render_template\n",
    "from flask import redirect\n",
    "from flask import request\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n",
    "from pymongo import MongoClient\n",
    "import pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an instance of Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use PyMongo to establish Mongo Connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Route to render index.html template using data from Mongo\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars = mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Route that will trigger the scrape function    \n",
    "@app.route(\"/scrape\")\n",
    "def scrape():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run the scrape function\n",
    "    mars = mongo.db.mars\n",
    "    mars_web = scrape_mars.scrape_news()\n",
    "    mars_web = scrape_mars.scrape_marsImage()\n",
    "    mars_web = scrape_mars.scrape_marsTwitter()\n",
    "    mars_web = scrape_mars.scrape_marsFacts()\n",
    "    mars_web = scrape_mars.scrape_marsH1Cerberus()\n",
    "    mars_web = scrape_mars.scrape_marsH2Schiaparelli()\n",
    "    mars_web = scrape_mars.scrape_marsH3SyrtisMajor()\n",
    "    mars_web = scrape_mars.scrape_marsH4VallesMarineris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Update the Mongo Database using update and upsert=True\n",
    "    mars.update({}, mars_web, upsert=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Redirect back to home page\n",
    "    return redirect(\"/\", code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
