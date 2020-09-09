import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

from os import path
if path.exists("envvar.py"):
  import envvar


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route("/recipe_info/<recipe_id>")
def recipe_info(recipe_id):
    that_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine_type = mongo.db.cuisine.find_one({"_id": ObjectId(that_recipe["cuisine"])})
    return render_template("recipeinfo.html", recipe=that_recipe, cuisine=cuisine_type)


@app.route("/create_recipe")
def create():
    return render_template("create.html", categories=mongo.db.categories.find(), cuisine=mongo.db.cuisine.find())


@app.route("/your_recipe")
def yourrecipe():
    return render_template("yourrecipe.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
