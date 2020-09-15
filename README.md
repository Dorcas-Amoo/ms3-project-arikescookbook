# Welcome to Arike's Cookbook!

![Page Screenshot](static/images/sitescreenshot.jpg)

## [Visit Site](https://ms3-project-arikescookbook.herokuapp.com/)

The idea of creating this project was birthed from my passion for cooking. I have always had the desire and vision to publish a cookbook someday, so when the opportunity for this project came along, I thought this is a great opportunity to make my long awaited dream happen. I have chosen the African-Caribbean theme as I believe it will help many from these groups to overcome the day-to-day challenge of what to prepare for the family due to some known limitations in food varieties.

Given that the World has become a global village through the internet, I strongly believe having a pool of recipes that could be easily accessed online will help many wives, mothers, husbands, fathers, young or old and many more to combat the above mentioned challenge. Besides this, it will also help many people from all walks of life, races, ethnic groups, backgrounds e.t.c who may want to explore cooking dishes from Africa or the Caribbean. 

I believe, Arike's cookbook will become and is the place to visit in this regard cause we are passionate about good food. :smile:

Thank you and enjoy the ride. :rocket:


## UX

This project was created to meet the needs of a vast majority of people. Below are a few _User Stories_:

* 'As a potential user who is looking for some Afro-Caribbean recipes, on visiting your site, I want to be able to view some simple and easy to make recipes with the freedom to possibly create and share my own idea.'

* 'As a wife/mother who wants to create a food timetable, I need a list of African or Caribbean recipes that will help me to easily achieve this'

* 'As a cookery tutor, I need some recipes to help teach my class a new dish from some specific continents and I will also require them to be able to come up with their own ideas by creating a recipe I can view and edit online.'

* 'As a developer, I want to meet the above needs by creating a cookbook site to help a wide range of people who will be able to create, read, update or delete any recipe from the site.'

In order to meet the requirements of the users, I began to brainstorm on what to do and how to go about it so as to deliver the desired result. I then visited similar sites online and those created by other code institute students which helped me to make an informed decision. After which I began creating the wireframe designs of my proposed website on Balsamiq [please see file attached under uxdesign folder located in the static folder](https://github.com/Dorcas-Amoo/ms3-project-arikescookbook). This helped me to really put a deeper thought into the idea, the layout, colour-scheme and many more and I am pleased with the result so far. Please note, the final product may not be an exact replica of the wireframes. Thank you.


## Features
1. **Home Page:** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click) and the "View Recipes" and "Create Recipes" pages.
  + The Carousel (Image Slider).
  + The Welcome message.
  + The Navigation button to access Recipes page.
  + The Footer which displays the copyright content.
2. **The Recipes Page:** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click) and the "View Recipes" and "Create Recipes" pages.
  + The Carousel (Image Slider).
  + The page header ("Recipes").
  + The search feature (Which displays existing recipes when certain related words are entered in the search bar).
  + The Navigation button to access Create Recipe page.
  + The collapsible accordion (Displays all created recipes and on click, reveals the description. Details are generated from the database).
  + The "Read More" button on the accordion (Serves a link to view the "Recipe Info" page).
  + The Footer which displays the copyright content
3. **The Recipes Info Page:** contains the following:
  + The Navbar which displays the Logo (links to the homepage on click) and the "View Recipes" and "Create Recipes" pages.
  + The Carousel (Image Slider).
  + The page header (The Recipe_Name generated from the database).
  + The icons and other recipe details section (Details generated from the database).
  + The Ingredients and Instructions section (Details generated from the database).
  + The Navigation buttons to access Edit Recipe page or to return to Recipes page.
  + The Footer which displays the copyright content
4. **The Create Recipe Page:** contains the following:
  + The Navbar which displays the Logo (links to the homepage on click) and the "View Recipes" and "Create Recipes" pages.
  + The Carousel (Image Slider).
  + The page header.
  + An empty Recipe Form which contains the following:
     + Category Name (A dropdown list generated from the database)
     + Recipe Name
     + Description
     + Cuisine (A dropdown list generated from the database)
     + Ingredients
     + Instructions
     + Cooking time
     + Servings
     + Created By
     + Date Created (Features a datepicker powered by a script from Materialize)
  + The buttons to "Create" a recipe or "Close" the form and return to Recipes page.
  + The Footer which displays the copyright content
5. **The Edit Recipe Page:** contains the following:
  + The Navbar which displays the Logo (links to the homepage on click) and the "View Recipes" and "Create Recipes" pages.
  + The Carousel (Image Slider).
  + The page header.
  + A pre-filled Recipe Form which contains the following that are editable information generated from the database:
     + Category Name (With dropdown option)
     + Recipe Name
     + Description
     + Cuisine type (With dropdown option)
     + A list of Ingredients
     + Instructions
     + Cooking time
     + Servings
     + Created By
     + Date Created (Features a datepicker powered by a script from Materialize) 
6. **The Error Page:** This feature was added as a last resort so was not included in the wireframe but it is to ensure users are able to get back to the right page in the case of any error on visiting the site especially if the wrong url is being entered in the browser.

NOTES: The Create and Edit forms feature multiple validations to prompt users to complete an input field or to insert a required format.
       The Navbar on mobile view changes to a sideNav (Burger bar) where the pages link can be accessed.


## Technologies Used
The following technologies were used to achieve the requirements of this project:

+ [Heroku](https://www.heroku.com/)
  + This was used to host my website
+ [Github](https://github.com/)
  + This was used as the project repository. 
+ [Gitpod](https://www.gitpod.io/) 
  + This was used to develop the site and [Git](https://git-scm.com/) for version control.
+ [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  + CSS3 was used to custom sytle my website to my desired outcome.
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
  + HTML5 was used as the markup language to structure and present my website on the Web.
+ [Javascript](https://www.javascript.com/)
  + This was used to achieve the interactive part of the site.
+ [JQuery](https://www.jquery.com/)
  + These scripts from the Materialize were used to initialise some features on my site.
+ [Python](https://www.python.org/)
  + I used this as the backend language to help manipulate data.
+ [Flask](https://palletsprojects.com/p/flask/)
  + The web framework written in python used for building my application.
+ [Jinja](https://pypi.org/project/Jinja2/)
  + This serves as the templating language used with flask.
+ [MongoDB](https://www.mongodb.com/cloud/atlas)
  + This was used to host my stored database. Serves as a repository for my database.
+ [Pymongo](https://pymongo.readthedocs.io/en/stable/)
  + This serves as the communication link between my application and the mongoDB database.
+ [Materialize](http://archives.materializecss.com/0.100.2/)
  + This frontend framework was used to build the site and then customised to my desired outcome.
+ [Material Icons](https://material.io/resources/icons/?style=baseline)
  + Icons used throughout the site were generated from here.

## Testing

## Deployment

## Credits & References

### Content

### Media

### Acknowledgements

Many thanks to my Mentor **Dick Vlaanderen** for his guidance

--------

Thank you for visiting! :smile:
