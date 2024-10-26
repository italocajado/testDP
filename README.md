CRUD of user management system
A system for management of users that uses Flask for backend and Vue using Vuetify for frontend.
The connection for the backend happen between the procedures of parse.py that send the udata.json to the MongoDB system and the app.py controls the interactions between the mongoDb database and the front end.
This System allows you to create, edit and delete users, all of this integrating with the MongoDB

Description
This project allows:
-Creation and management of users with details such as username, password, roles, and timezone.
-CRUD (Create, Read, Update, Delete) operations on users.
-A user-friendly interface using Vuetify (Material Design).
-Backend communication through a Flask API connected to a MongoDB database.

Requirements:
- NodeJS
- python 3.12
- MongoDB
- GIT (Just for cloone the repo)

MongoDB
Download and install the MongoDB
into the code already have the link for my db in the mongo, doesn't need create a local host

python:
instal this depencies:
  pip install Flask Flask-CORS pymongo

FrontEnd
- Vue.js: JavaScript framework.
- Vuetify: UI library based on Material Design.
- Axios: HTTP client for API communications.
- Vue Router: Route management.
- SCSS: Advanced styling.
in bash or terminal run: npm install vue-router axios vuetify sass 

running:
- In Bash/terminal run: app.py or flask run
- The API will be available at: http://localhost:5000
In the front end directory (testDP\vue-flask-crud):
- In Bash/terminal run: npm run serve
- The frontend will be available at: http://localhost:8080

Any doubts just send me a email
italocajado@gmail.com



