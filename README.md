# EireWheels Car Rental

## Table of Contents

- [Overview](#overview)
- [UX](#ux)
   * [Strategy](#strategu)
   * [Database structure](#database-structure)
   * [Design](#design)
- [Features](#features)
   * [Responsive Navbar](#responsive-navbar)
   * [Footer](#footer)
   * [Home Page](#home-page)
   * [Car Search](#car-search)
   * [Our Locations](#our-locations)
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

## Features

### Account Management

- Account Creation: New users can sign up, with email confirmation required to ensure security and prevent spam.

![](static/images/readme_images/features/sign-up.png)

- Login System: Existing users can log in to access their profiles and manage their bookings.

![](static/images/readme_images/features/sign-in.png)

- Password Recovery: If users forget their password, they can reset it through a secure process.

![](static/images/readme_images/features/reset-password.png)

### Responsive Navbar

EireWheels boasts a sophisticated and user-friendly navigation bar that enhances your browsing experience across all devices.

- Seamless Branding: The navbar proudly displays our brand logo, ensuring a consistent and professional identity. The logo is visible on all devices, enhancing brand recognition.

- Mobile-First Design: Optimized for mobile, the navbar includes a responsive toggler button that collapses the menu for a cleaner view on smaller screens. The intuitive toggle feature allows users to easily access the menu without clutter.

- Dynamic Navigation Links: The navigation bar includes clearly defined links to essential pages like Home, Booking, Locations, and Contact Us. These links dynamically highlight based on the current page, providing users with clear navigation cues.

- User Authentication: For authenticated users, the navbar provides additional personalized options. On desktop, a dropdown menu reveals links to the user’s profile, bookings, and reviews, along with a logout option. On mobile, these options are accessible directly from the menu, ensuring seamless access regardless of device.

- Sign in and Sign up: For new users or those not yet signed in, easy access to sign-in and sign-up pages is provided, ensuring a smooth onboarding experience.

![](static/images/readme_images/features/navbar-desktop.png)

![](static/images/readme_images/features/navbar-mobile.png)

### Footer

The footer of our website is thoughtfully designed to provide users with essential information and easy access to important policies.

- Contact Information: Stay connected with us through various channels. Our footer includes direct links to email support, our physical address, and a phone number for immediate assistance. Whether you're reaching out for support or visiting us in Dublin, our contact details are conveniently placed.

- Location Details: Find us effortlessly on Google Maps with a direct link to our location. Our address is clearly stated, making it easy for you to visit us or plan your journey.

- Copyright Notice: The footer proudly displays the copyright notice, affirming that all content is owned by EireWheels. The notice reflects our commitment to providing quality service for educational purposes.

- Legal Information: Access our Privacy Policy and Terms and Conditions directly from the footer. These links open modals that provide comprehensive details about your privacy rights, data protection, and the terms of service. This ensures transparency and easy access to critical information without navigating away from the page.

![](static/images/readme_images/features/footer-desktop.png)

![](static/images/readme_images/features/footer-mobile.png)

### Home Page

#### "Why Choose Us?" section

Discover the unparalleled benefits of choosing our services for your travel needs.

![](static/images/readme_images/features/why-choose-us.png)

#### "How It Works" section

Booking a rental car with us is simple and seamless. Follow these easy steps to get started.

![](static/images/readme_images/features/how-it-works.png)

#### "What Our Customers Are Saying" section

We value the feedback from our customers and are proud to share their experiences with you. Here’s what some of them have to say about our service:

Customer Reviews
- Step into our review carousel and discover real stories from those who have traveled with us:

- Ratings & Feedback: Our carousel showcases a range of customer reviews, complete with ratings and comments. Each review is dated and highlights the experiences of our users.

- Authentic Experiences: Whether it's praise for our seamless service or suggestions for improvement, our reviews offer genuine insights into what makes our service stand out.

- User-Friendly Carousel: Navigate through the reviews easily with our interactive carousel. Use the previous and next controls to explore different testimonials.

- Want to read more? View All Reviews and see why our customers choose us for their travel needs!

![](static/images/readme_images/features/customer-reviews.png)

#### "About us" section

We are committed to delivering an exceptional car rental service that caters to both business and leisure travelers in Ireland. Whether you're here for a short visit or an extended stay, our diverse fleet of vehicles is designed to meet your every need.

![](static/images/readme_images/features/about-us.png)

#### Frequently Asked Questions

Have questions? We’ve got answers! Here are some of the most common queries we receive.

![](static/images/readme_images/features/faq.png)

### Car Search

#### Search Form 

Users can search for available cars.

![](static/images/readme_images/features/car-search.png)

#### Filters and Sorting

Refine search results using various filters and sort the list of cars by price per day.
Filters and sorting options dynamically update the list of available cars.

![](static/images/readme_images/features/car-filter.png)

#### Car Details

View detailed information about each car.

![](static/images/readme_images/features/car-detail.png)

#### Reservations

Authenticated users can reserve a car by:
- Clicking the Reserve button to book the car with selected rental details.
- If not authenticated, users are prompted to Login to continue.

![](static/images/readme_images/features/car-reserve.png)




### Our Locations

Discover our convenient car rental offices located at airports across Ireland. 

- Dynamic Dropdown: Easily switch between different airport locations to view relevant information.
- Detailed Office Info: Get comprehensive details about each airport office, including contact information and operating hours.
- Interactive Map: Our map, powered by Leaflet, shows the selected airport office's location with a marker..
- Google Maps: Click the link to open the location in Google Maps.
Ready to find the nearest airport office? Use the dropdown menu to select your location and get all the information you need.

![](static/images/readme_images/features/locations.png)

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



