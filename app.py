from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    
    mars = mongo.db.mars_collection.find()
    print(mars[1])

    
    return render_template("index.html", mars=mars)



@app.route("/scrape")
def scrape():

    
    scrape_mars.scrape()

    
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)