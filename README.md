# Blog App with Django X React.
## This blog app is my attempt at integrating [Django-REST](<https://www.django-rest-framework.org/>) with [React.js](<https://reactjs.org/docs/getting-started.html>) using documentations.
This is a normal blog that supports Login, Registeration, Making a Post, Editing, Updating and Deleting. Again this is just more of a visual project and learning project so some things are incomplete.\
The authentication is done by Django-REST Framework and Authorization using JWT. Frontend uses Axios Instance to communicate with backend.
The app is not deployed yet. After cloning, App can be run locally using these commands in order:
```
pip install requirements.txt
cat npm_requirements.txt | xargs npm install -g
npm start
py manage.py runserver
```
# Some Basic and Salient Features
# Home Page 
Home page contains every post that was published to the blog. The frontend was coded using Material-UI components and documentations.
![Home_Full](https://user-images.githubusercontent.com/78678620/135619877-d8800af6-98bb-4ddb-b188-147ac9a794b4.png)

## Register Page
Here new users can register themselves and start their journey with the app.
<img width="960" alt="Register" src="https://user-images.githubusercontent.com/78678620/135620377-e0cb1592-09ea-40af-9a39-8f781abc4d22.png">

## Login In
After making a new account Users can login in to their account. After loging in JWT kicks in and creates tokens for sessions of 5 minutes. Supported with refresh tokens.
<img width="960" alt="Sign_In" src="https://user-images.githubusercontent.com/78678620/135620819-502962b5-04e3-4586-94e9-552629aa5c0e.png">

## Individual Post
By clicking on the posts on the home page, one can view individual posts in their entirety.
<img width="960" alt="individual post" src="https://user-images.githubusercontent.com/78678620/135621361-9b6a8d8d-05c8-4d5f-9c43-6b7639aa8ac8.png">

## Flexible search
Blog allows to serach posts by their title or keyword in their title.
<img width="960" alt="Flexible_Search" src="https://user-images.githubusercontent.com/78678620/135622151-37e9b93d-d168-48a3-a1ee-98bcafebaa84.png">

## Post Control
Admin can control the posts made by everyone. Further I will try to authorize users to edit, update and delete their own posts.
<img width="959" alt="Admin_Post_Full" src="https://user-images.githubusercontent.com/78678620/135622610-fbda73e3-1c1c-482c-9d8c-67abd3ac8368.png">

## New Post
Page for Users to create new posts.
<img width="960" alt="Create" src="https://user-images.githubusercontent.com/78678620/135623402-5f54dd82-120d-4899-97c5-71b393262e57.png">

## Delete Posts
User can delete their posts using this page.
<img width="960" alt="Delete" src="https://user-images.githubusercontent.com/78678620/135623535-bd209abe-e75b-4f90-b4c2-481ed038733d.png">

## Update Posts
Users can update their exisitng posts on this view.
![Update](https://user-images.githubusercontent.com/78678620/135623679-09cb5c79-34be-4a32-a497-86c99303855d.jpeg)

## API Docs
Something new I learned with this project is API documentation wiht the help of schema. This is pure backend which helps other developers to understand the different end points.
<img width="960" alt="Docs" src="https://user-images.githubusercontent.com/78678620/135624323-6b186771-9fe7-497f-8b8e-ade4df304110.png">




