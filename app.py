from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  
  #### Return a rendered index.html file
  return render_template("index.html")

# THE FOLLOWING CODE IS FOR THE RENDERING TEMPLATES EXERCISE:
#@app.route("/recipe/<int:id>")
#def recipe(id):
    
  #### Return a rendered fried_egg.html file
#  return render_template("fried_egg.html")

# THE FOLLOWING CODE IS FOR TEMPLATE VARIABLES EXERCISE:
#@app.route("/recipe/<int:id>")
#def recipe(id):
  #### Add template variables as 
  #### variable assignment arguments
  #return render_template("recipe.html", 
                         #template_recipe=recipes[id], 
                         #template_description=descriptions[id], 
                         #template_ingredients=ingredients[id])

# THE FOLLOWING CODE IS FOR VARIABLE FILTERS EXERCISE:
@app.route("/recipe/<int:id>")
def recipe(id):
  return render_template("recipe.html", 
                         template_recipe=recipes[id], 
                         template_ingredients=ingredients[id], 
                         template_instructions=instructions[id])