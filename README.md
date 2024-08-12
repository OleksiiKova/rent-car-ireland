# EireWheels Car Rental

## Table of Contents

- [Overview](#overview)
- [UX](#ux)
   * [Strategy](#strategu)
   * [Database structure](#database-structure)
   * [Design](#design)
- [Features](#Features)
   * 
- [Technologies](#technologies)
- [Testing](#testing)




### Overview
EireWheels Car Rental is a web application for car rental developed with Django. The project allows users to view available cars at various airports in Ireland, book them, and manage rentals. This website was created as a learning exercise for my fourth portfolio project at Code Institute.

#### First Time User
- As a person who is visiting Ireland for vacation and is looking for a convenient car rental service.
- As a person who is searching for clear information about available cars and rental services.
- As a person who prefers to make bookings online rather than speaking with others.

#### Returning User
- As a returning user, I would like to review all my previous car rental bookings.
- As a returning user who already has an account, I would like to quickly and easily make a reservation for a specific car.
- As a returning user, I would like to see updates to the available vehicles and services on the site so that I can find new and interesting options (for example, new car models).

## UX

### Strategy

### Database structure
After deciding on the project's features, I used Lucidchart to plan the database structure. The diagram below serves as an initial guide, illustrating the types of data and their relationships.

![](static/images/readme_images/database_diagram.png)

### Design

#### Colours

The following colour palette was used from [Coolors](https://coolors.co/):

![](static/images/readme_images/colour_palette.png)

#### Wireframes

The website is designed to be clear and simple. To create a wireframe I used Balsamiq software. PDF file with my wireframe you cand find [here](static/images/readme_images/car_rental.pdf).

## Technologies

This project was created using the following:

### Languages Used
- HTML5
- CSS3
- JavaScript
- Python

### Frameworks Used
- Django - Python framework, used to create the full-stack web application
- Bootstrap 5 - front end framework, helps me with fast and efficient styling

### Databases Used
- PostgreSQL from Code Institute - used as the database
- Cloudinary - used to host the static files

### Validators Used
- W3C HTML Validator - used to validate HTML code
- W3C CSS Validator - used to validate CSS code
- JShint - used to validate JavaScript code
- CI Python Linter - used to validate the Python code

### Other
- Balsamiq - used to create a wireframe
- Lucid.app - used to create a Database ER diagram
- Сodeinstitute-ide - used to code the website
- Django Template Language - templating engine
- GitHub - for storing the code and for the projects Kanban board
- Heroku - for hosting and deployement of this project
- Google Chrome Developer Tools - used during testing, debugging and making the website responsive
- Google Fonts - used to import fonts
- Git - version control tool
- Font Awesome - used for the icons on the website
- Coolors.co - used to choose the colours
- Design.com - used to create logo
- Am I Responsive - to show the website image on a range of devices

## Testing

For a comprehensive overview of the testing strategy, including detailed information on both automated and manual testing, please refer to the [Testing Documentation](TESTING.md).

## Deployment

### Activate Your Gitpod Enterprise Account

1. Open Gitpod Enterprise:

- Go to the Gitpod Enterprise webpage and log in using Google.

2. Access User Settings:

- Once logged in, click on your avatar in the upper-right corner of the page and select User Settings from the dropdown menu.

3. Connect GitHub:

- Choose Git Providers from the sidebar (note: in this case, there will be only one option: GitHub).
- From the three-dot menu next to GitHub, select Connect.

4. Authorize Access:

- Authorize Code-Institute-Org to access your GitHub account. You will be redirected back to the Gitpod Enterprise site.

5. Edit Permissions:

- Again, from the three-dot menu next to GitHub, choose Edit Permissions.
- Check all the permissions checkboxes and click Update Permissions.

6. Re-authorize:

- After clicking Update Permissions, you will need to authorize Code-Institute-Org again, similar to step 4.

### Create a New Workspace

1. Open Workspaces:

- In the Gitpod interface, click on Workspaces in the sidebar.

2. Start a New Workspace:

- Click on New Workspace.

3. Select or Search for Repository:

- Choose a repository from the list of existing repositories.
- Alternatively, start typing the name of the repository you wish to open to find it in the search bar.

4. Launch Workspace:

- Select the desired repository from the list or search results and follow the prompts to open it in a new Gitpod workspace.

By following these steps, you'll be able to activate your Gitpod Enterprise account, configure GitHub permissions, and create a new workspace for your project.

### Pre-Deployment
To ensure a smooth deployment of your application on Heroku, please follow these pre-deployment steps:

1. Update requirements.txt:

- Ensure that your requirements.txt file is current and accurately lists all the Python modules your application depends on. This file is crucial for Heroku to install the correct packages.

2. Configure the Procfile:

- Create a Procfile in the root directory of your project. This file tells Heroku how to run your application. For a Python application, it typically contains:

`web: gunicorn your_app_name.wsgi`

- Replace your_app_name with the name of your Django project.

3. Adjust settings.py:

- Update the ALLOWED_HOSTS list in your settings.py file to include Heroku’s domain and localhost. It should look something like this:

`ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']`

- Ensure that all static files and directories are correctly configured to be served properly in a production environment.

4. Set Up Environment Variables:

- Configure all necessary environment variables in your Heroku app. These variables are critical for connecting to your database, cloud storage, and keeping your application secure.

- Add the following hidden variables to your env.py file (which should be gitignored):
SECRET_KEY: Your Django secret key.
DATABASE_URL: The URL for your database.
CLOUDINARY_URL: The URL for your Cloudinary storage.
EMAIL_HOST_USER: The email address used to send emails.
EMAIL_HOST_PASSWORD: The password for the email account used for sending emails.

### Deploying on Heroku

Follow these steps to deploy your application to Heroku:

1. Create a Heroku Account:

- Visit Heroku and sign up for a new account. If you’re a student, consider using the student account option to take advantage of free credits.

2. Set Up a New Heroku App:

- After logging in, go to the Heroku dashboard and click on "Create New App."
- Enter a unique name for your application and select the appropriate region.

3. Connect to GitHub:

- Choose the deployment method as "Connect to GitHub."
- Search for your repository, for example, "rent-car-ireland".

4. Configure Automatic Deploys (optional):

- Enable automatic deploys by selecting the main branch or the branch you wish to deploy from.

5. Set Config Vars:

- Navigate to the "Settings" tab of your Heroku app.
- Click "Reveal Config Vars" and enter the environment variables you previously configured, including SECRET_KEY, DATABASE_URL, CLOUDINARY_URL, EMAIL_HOST_PASSWORD and EMAIL_HOST_USER.

6. Deploy Your App:

- Click the "Deploy" button to start the deployment process.
- Heroku will build and deploy your application according to the configurations and dependencies specified.

7. Monitor Deployment:

- Check the deployment logs and ensure that there are no errors. You can access logs via the Heroku dashboard.

### Post-Deployment

1. Verify Application:

- After deployment, visit your Heroku app’s URL to confirm that your application is running correctly.
- Test key functionalities to ensure that everything is working as expected.

2. Debug Issues:

- If you encounter any issues, use the Heroku logs to troubleshoot. Access logs through the Heroku dashboard or run heroku logs --tail in your terminal.

3. Update Regularly:

- Keep your requirements.txt and Procfile updated with any changes in your application.
- Redeploy as needed to reflect updates or fixes.

By following these steps, you can ensure a successful deployment of your application on Heroku and maintain its proper functionality in a production environment.



