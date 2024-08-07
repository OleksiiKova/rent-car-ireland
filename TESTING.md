# Table of Contents

<!-- - [User Story Testing](#user-story-testing) -->
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Responsiveness and Device Testing](#responsiveness-and-device-testing)
- [Browser Testing](#browser-testing)


## Code Validation

### HTML

All HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/), and no errors were detected.
| Page                                                                                                                                     | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>Home</summary><img src="static/images/readme_images/testing/html_validations/home.png"></details>                      | <mark>PASS</mark>   |
| <details><summary>Booking</summary><img src="static/images/readme_images/testing/html_validations/booking.png"></details>                | <mark>PASS</mark>   |
| <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/html_validations/booking-form.png"></details>      | <mark>PASS</mark>   |
| <details><summary>Locations</summary><img src="static/images/readme_images/testing/html_validations/locations.png"></details>            | <mark>PASS</mark>   |
| <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/html_validations/contact-us.png"></details>          | <mark>PASS</mark>   |
| <details><summary>My profile</summary><img src="static/images/readme_images/testing/html_validations/my-profile.png"></details>          | <mark>PASS</mark>   |
| <details><summary>My bookings</summary><img src="static/images/readme_images/testing/html_validations/my-bookings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/html_validations/edit-booking.png"></details>      | <mark>PASS</mark>   |
| <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/html_validations/delete-booking.png"></details>  | <mark>PASS</mark>   |
| <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/html_validations/leave-review.png"></details>      | <mark>PASS</mark>   |
| <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/html_validations/all-reviews.png"></details>        | <mark>PASS</mark>   |
| <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/html_validations/my-reviews.png"></details>          | <mark>PASS</mark>   |
| <details><summary>Edit Review</summary><img src="static/images/readme_images/testing/html_validations/edit-review.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Delete Review</summary><img src="static/images/readme_images/testing/html_validations/delete-review.png"></details>    | <mark>PASS</mark>   |
| <details><summary>Sign In</summary><img src="static/images/readme_images/testing/html_validations/login.png"></details>                  | <mark>PASS</mark>   |
| <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/html_validations/signup.png"></details>                 | <mark>PASS</mark>   |
| <details><summary>Log Out</summary><img src="static/images/readme_images/testing/html_validations/logout.png"></details>                 | <mark>PASS</mark>   |

### CSS

During the CSS validation process for this project, a couple of issues were identified that are related to the external CSS resource provided by Leaflet. Specifically:

- Mix-blend-mode Value: The plus-lighter value used in the Leaflet CSS file is not recognized as a valid mix-blend-mode value.
- Behavior Property: The behavior property with the value url(#default#VML) is not supported.
These issues are due to the external Leaflet CSS file hosted at https://unpkg.com/leaflet@1.9.4/dist/leaflet.css, and not from the custom CSS within this project. As such, they cannot be resolved directly within this project.

If you encounter validation issues or errors related to these external resources, please be aware that they originate from the external library and not from the project's own CSS.

![](static/images/readme_images/testing/css_validations.png)

### JavaScript

| File JS                                                                                                                                              | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>script.js</summary><img src="static/images/readme_images/testing/js_validations/main-script.png"></details>        | <mark>PASS</mark>   |
| <details><summary>rating.js</summary><img src="static/images/readme_images/testing/js_validations/rating-script.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the Home Page</summary><img src="static/images/readme_images/testing/js_validations/home.png"></details>               | <mark>PASS</mark>   |
| <details><summary>Embedded within the Locations Page</summary><img src="static/images/readme_images/testing/js_validations/locations.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the My Bookings Page</summary><img src="static/images/readme_images/testing/js_validations/my-bookings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the Edit Review Page</summary><img src="static/images/readme_images/testing/js_validations/edit-review.png"></details>        | <mark>PASS</mark>   |


Some of the JavaScript files in this project include Django template variables. When these files are validated using JSHint or similar tools, errors may occur due to the validator not recognizing these Django variables.
For instance, you might encounter errors like:
- 2	Expected '}' to match '{' from line 2 and instead saw '{'.
- 2	Missing semicolon.
- 2	Expected an assignment or function call and instead saw an expression.
- 2	Missing semicolon.
- 2	Unrecoverable syntax error. (2% scanned).

This error occurs because the validator doesn't interpret the Django template syntax correctly. When the Django variables are removed, the validation errors disappear.

| File JS                                                                                                                                              | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>Embedded within the Booking-form Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-booking-form.png"></details>        | <mark>ERROR</mark>   |
| <details><summary>Embedded within the Car Search Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-car-search.png"></details>        | <mark>ERROR</mark>   |
| <details><summary>Embedded within the Edit Booking Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-edit-booking.png"></details>        | <mark>ERROR</mark>   |

### Python

All Python files were processed using the [CI Python Linter](https://pep8ci.herokuapp.com/), and no errors were found.

#### Bookings app

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>cron.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/cron.png"></details>        | <mark>PASS</mark>   |
| <details><summary>forms.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_forms.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/test-forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/views.png"></details>        | <mark>PASS</mark>   |

#### Cars app
| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/views.png"></details>        | <mark>PASS</mark>   |

#### Offices app
| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/views.png"></details>        | <mark>PASS</mark>   |

#### Userprofile app

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>forms.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>signal.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/signal.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_data.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-data.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_forms.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/views.png"></details>        | <mark>PASS</mark>   |

#### Car rental project

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>asgi.py</summary><img src="static/images/readme_images/testing/python_validations/project/asgi.png"></details>        | <mark>PASS</mark>   |
| <details><summary>settings.py</summary><img src="static/images/readme_images/testing/python_validations/project/settings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/project/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>wsgi.py</summary><img src="static/images/readme_images/testing/python_validations/project/wsgi.png"></details>        | <mark>PASS</mark>   |


## Responsiveness and Device Testing

Throughout the development process, the website was rigorously tested across a range of devices, including desktops, laptops, smartphones, and tablets. This testing ensured that the website displayed correctly on screens of various sizes and orientations, both portrait and landscape. Additionally, the responsive design was validated using Google Chrome's developer tools to confirm that the layout remained structurally sound and adaptable across different screen dimensions. No issues were noted, affirming that the site functions as expected across diverse environments.

## Browser Testing

The website was tested across Google Chrome, Safari, and Microsoft Edge, and no issues were found.

## Lighthouse Testing

Lighthouse validation was run on all pages (both mobile and desktop) in order to check performance, accessibility, best practices and CEO.

| Page            | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| --------------- | :---------: | :-----------: | :------------: | :-: | --------------------------------------------------------------------------------------------------------------------------- |
|                 |             |               |                |     |
| **Desktop**     |             |               |                |     |
| Home            |     99      |      98      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/desktop/home.png"></details>                    |
| Booking            |     100      |      92      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking.png"></details>                    |
| Locations            |     97      |      96      |      100       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/desktop/locations.png"></details>                    |
| Contact Us            |     100      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/desktop/contact-us.png"></details>                    |
| Booking Form            |     100      |      89      |      78       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking-form.png"></details>                    |
| Edit Booking            |     99      |      89      |      78       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-booking.png"></details>                    |
| Delete Booking            |     100      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-booking.png"></details>                    |
| All Reviews            |     100      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/all-reviews.png"></details>                    |
| Leave Review            |     100      |      96      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/desktop/leave-review.png"></details>                    |
| Edit Review            |     99      |      96      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-review.png"></details>                    |
| Delete Review            |     99      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-review.png"></details>                    |
| My Profile            |     100      |      100      |      100       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-profile.png"></details>                    |
| My Bookings            |     97      |      92      |      78       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-bookings.png"></details>                    |
| My Reviews            |     99      |      87      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-reviews.png"></details>                    |
| Sign In            |     100      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-in.png"></details>                    |
| Sign Up            |     100      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-up.png"></details>                    |
| Sign Out            |     100      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-out.png"></details>                    |
|                 |             |               |                |     |
| **Mobile**      |             |               |                |     |
| Home            |     93      |      98      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/mobile/home.png"></details>                    |
| Booking            |     96      |      91      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking.png"></details>                    |
| Locations            |     77      |      96      |      96       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/mobile/locations.png"></details>                    |
| Contact Us            |     94      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/mobile/contact-us.png"></details>                    |
| Booking Form            |     92      |      86      |      79       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking-form.png"></details>                    |
| Edit Booking            |     93      |      86      |      79       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-booking.png"></details>                    |
| Delete Booking            |     93      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-booking.png"></details>                    |
| All Reviews            |     92      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/all-reviews.png"></details>                    |
| Leave Review            |     92      |      95      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/mobile/leave-review.png"></details>                    |
| Edit Review            |     96      |      95      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-review.png"></details>                    |
| Delete Review            |     91      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-review.png"></details>                    |
| My Profile            |     94      |      100      |      96       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-profile.png"></details>                    |
| My Bookings            |     87      |      90      |      79       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-bookings.png"></details>                    |
| My Reviews            |     93      |      85      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-reviews.png"></details>                    |
| Sign In            |     92      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-in.png"></details>                    |
| Sign Up            |     93      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-up.png"></details>                    |
| Sign Out            |     92      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-out.png"></details>                    |
