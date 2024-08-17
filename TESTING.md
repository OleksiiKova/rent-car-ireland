# Table of Contents

- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Responsiveness and Device Testing](#responsiveness-and-device-testing)
- [Browser Testing](#browser-testing)
- [Accessibility](#accessibility)
- [Lighthouse Testing](#lighthouse-testing)
- [User Story Testing](#user-story-testing)
- [Bugs](#bugs)



## Automated Testing

To ensure the robustness and reliability of the application, a comprehensive testing strategy was employed, combining both manual and automated testing methods.

Leveraging Django's built-in testing framework, automated tests were written to cover critical aspects of the application's functionality. This includes views and forms tests to verify that the application behaves as expected under various conditions.

To run the tests, I executed the following command in the terminal:

`python3 manage.py test`

Total Count of Automated Tests: 41

![screenshot](static/images/readme_images/testing/automated_testing/screen-terminal.png)  

To create the coverage report, I run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

Below are the reports on automated tests.

| App                                   | Screenshot                                   | 
| ------------------------------------- | -------------------------------------------- | 
| Bookings  | ![screenshot](static/images/readme_images/testing/automated_testing/report-bookings.png)   |
| Car rental  | ![screenshot](static/images/readme_images/testing/automated_testing/report-car-rental.png)   |
| Cars  | ![screenshot](static/images/readme_images/testing/automated_testing/report-cars.png)   |
| Offices  | ![screenshot](static/images/readme_images/testing/automated_testing/report-offices.png)   |
| Userprofile  | ![screenshot](static/images/readme_images/testing/automated_testing/report-userprofile.png)   |

[Back To Top](#table-of-contents)

## Manual Testing

To enhance quality and increase confidence in the correctness of the application, I conducted manual testing in addition to automated tests. This manual testing also targeted areas not covered by the automated tests, ensuring comprehensive validation.


| Page                              | User Action                                                | Expected Result                                                              | Pass/Fail | Comments |
|-----------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------|-----------|----------|
| Nav links                         |                                                            |                                                                              |           |          |
|                                   | Click on Logo                                              | Redirection to Home page                                                     | Pass      |          |
|                                   | Click on Home link in navbar                               | Redirection to Home page                                                     | Pass      |          |
|                                   | Click on Booking link in navbar                            | Redirection to Booking page                                                  | Pass      |          |
|                                   | Click on Locations link in navbar                          | Redirection to Locations page                                                | Pass      |          |
|                                   | Click on My Profile link in navbar                         | Redirection to My Profile page                                               | Pass      |          |
|                                   | Click on My Bookings link in navbar                        | Redirection to My Bookings page                                              | Pass      |          |
|                                   | Click on My Reviews link in navbar                         | Redirection to My Reviews page                                               | Pass      |          |
|                                   | Click on Sign In link in navbar                            | Redirection to Login page                                                    | Pass      |          |
|                                   | Click on Sign Up link in navbar                            | Redirection to Sign Up page                                                  | Pass      |          |
|                                   | Click on Log Out link in navbar                            | Redirection to Logout confirm page                                           | Pass      |          |
| Home Page                         |                                                            |                                                                              |           |          |
|                                   | Click on "Get A Quote Now" button in advantages section    | Redirection to Booking page                                                  | Pass      |          |
|                                   | Click on "View All Reviews" button in the Reviews section  | Opens page with all customer reviews                                         | Pass      |          |
|                                   | Click the forward arrow in the Reviews section             | Navigate to the next item in the carousel                                    | Pass      |          |
|                                   | Click the backward arrow in the Reviews section            | Navigate to the previous item in the carousel                                | Pass      |          |
|                                   | Click on the accordion buttons in the FAQ section          | Expand or collapse the associated content                                    | Pass      |          |
| Footer                            |                                                            |                                                                              |           |          |
|                                   | Click on the email link                                    | Open a new email draft addressed to support@eirewheels.ie                    | Pass      |          |
|                                   | Click on the map link                                      | Open a new tab displaying Google Maps with the location                      | Pass      |          |
|                                   | Click on the phone number link                             | Open the default phone application with the number +353 1 234 5678           | Pass      |          |
|                                   | Click on the Privacy Policy link                           | Open a modal window displaying the privacy policy content                    | Pass      |          |
|                                   | Click on the Terms and Conditions link                     | Open a modal window displaying the terms and conditions content              | Pass      |          |
| Log In                            |                                                            |                                                                              |           |          |
|                                   | Enter valid password                                       | Field will only accept password format                                       | Pass      |          |
|                                   | Click the "Login" button                                   | Redirection to home page                                                     | Pass      |          |
|                                   | Click the "Create account" button                          | Redirection to Sign Up page                                                  | Pass      |          |
|                                   | Click the "Forgot password?" button                        | Redirection to Password reset page                                           | Pass      |          |
| Register                          |                                                            |                                                                              |           |          |
|                                   | Enter valid email address                                  | Field will only accept email address format                                  | Pass      |          |
|                                   | Enter valid password (twice)                               | Field will only accept password format                                       | Pass      |          |
|                                   | Click on the "Sign In" button                              | Redirection to blank Login page                                              | Pass      |          |
|                                   | Click on the "Sign Up" button                              | Redirection to page with message about email confirmation and sends email    | Pass      |          |
| Password Reset                    |                                                            |                                                                              |           |          |
|                                   | Click on the "Reset My password" button                    | Receive a confirmation message indicating that a password reset email sent   | Pass      |          |
|                                   | Check the email account associated with the user’s account | Receive an email containing a password reset link                            | Pass      |          |
|                                   | Click on the password reset link provided in the email     | Redirection to a change password page on the website                         | Pass      |          |
| Change password                   |                                                            |                                                                              |           |          |
|                                   | Enter a new password and confirm it by re-entering the same| Submit the form, see a confirmation message indicating that password updated | Pass      |          |
|                                   | Attempt to log in using the newly set password             | Log in successfully with the new password                                    | Pass      |          |
| Log Out                           |                                                            |                                                                              |           |          |
|                                   | Click the "Sign out" button                                | Redirection user  to a confirmation page for logging out                     | Pass      |          |
|                                   | Click the "Sign out" button on the confirmation page       | Logged out of the account                                                    | Pass      |          |
| Booking                           |                                                            |                                                                              |           |          |
|                                   | Click on the dropdown menus for Pickup and Return Office   | Display a list of available offices                                          | Pass      |          |
|                                   | Use the date and time picker to select a date and time     | The date and time should be selectable                                       | Pass      |          |
|                                   | Click the "Search" button after selecting all fields       | The form submitted, the page displayed results of available cars             | Pass      |          |
|                                   | Click the "Filter" button to open the filter options       | Displayed a list of filter options                                           | Pass      |          |
|                                   | Select various filter options                              | The list of cars automatically update to reflect the selected filters        | Pass      |          |
|                                   | Click the "Reset Filters" button                           | All applied filters should be cleared                                        | Pass      |          |
|                                   | Click on the car name in a car listing                     | Open a modal window displaying detailed information about the selected car   | Pass      |          |
|                                   | Click the "Close" button on the modal window               | Close the modal window and return to the search results page                 | Pass      |          |
|                                   | Click the "Reserve" button for a car listing               | Redirection to the Booking form                                              | Pass      |          |
| Booking Form                      |                                                            |                                                                              |           |          |
|                                   | Navigate to the booking form after selecting a car         | The form automatically display the previously entered dates, times, offices  | Pass      |          |
|                                   | Click on the accordion button for detailed car information | The accordion should expand to show detailed information about the car       | Pass      |          |
|                                   | Enter the following details into the form fields           | Each field accept, validate the input according to its format requirements   | Pass      |          |
|                                   | Check the "Child Seat" checkbox                            | A dropdown list become active, allowing to select the type of child seat     | Pass      |          |
|                                   | Click on the More About Extra Insurance link               | Open a modal window with the info about Extra Insurance                      | Pass      |          |
|                                   | Click the "X" (close) button in the modal window           | The modal should close                                                       | Pass      |          |
|                                   | Check the "Extra Insurance" checkbox                       | The total rental amount automatically increase by €5 per day (max of €50)    | Pass      |          |
|                                   | Click on the Read Terms and Conditions link                | Open a modal window with the terms and conditions                            | Pass      |          |
|                                   | In the modal, click the "I have read and agree" button     | The modal close, and the checkbox should remain checked                      | Pass      |          |
|                                   | Click the "X" (close) button in the modal window           | The modal should close without checking the checkbox                         | Pass      |          |
|                                   | Click the "Book Now" button after completing fields        | Displayed a success message and the user redirected to the "My Bookings"     | Pass      |          |
| Locations                         |                                                            |                                                                              |           |          |
|                                   | Navigate to the locations page                             | The page should display a dropdown menu with a list of available offices     | Pass      |          |
|                                   | Select an office from the dropdown menu                    | The page should update to display information about the selected office      | Pass      |          |
|                                   | After selecting an office, check the displayed information | The page should show details about the office                                | Pass      |          |
|                                   | Review the map displayed on the page                       | The map should correctly display the office location with a marker           | Pass      |          |
|                                   | Click the link to Google Maps provided on the page         | Open a new browser window or tab with the Google Maps location of the office | Pass      |          |
| My bookings                       |                                                            |                                                                              |           |          |
|                                   | Navigate to the "My Bookings" page                         | The page should display a list of all bookings made by the user              | Pass      |          |
|                                   | Click on the booking title in the list                     | A modal window should open displaying detailed information about the booking | Pass      |          |
|                                   | Click the "Edit" button (booking that is not completed)    | Redirection to the Edit Booking page                                         | Pass      |          |
|                                   | Click the "Delete" button (booking that is not completed)  | Redirection to the delete confirmation page                                  | Pass      |          |
|                                   | Check a booking's status one day after the booking end date| The booking status change to "Completed", "Edit" and "Delete" no available   | Pass      |          |
|                                   | Сheck the "Leave a Review" link (if booking "Completed")   | The "Leave a Review" link should be visible                                  | Pass      |          |
|                                   | Click the "Leave a Review" link                            | Redirection to the "Leave a Review" page                                     | Pass      |          |
| Leave a Review                    |                                                            |                                                                              |           |          |
|                                   | Navigate to the "Leave Review" page                        | The page should display two fields: rating and comment                       | Pass      |          |
|                                   | Submit the form without check a rating or writing a comment| The form should not be submitted                                             | Pass      |          |
|                                   | Complete the form by checking a rating, entering a comment | The form should be successfully submitted                                    | Pass      |          |
|                                   | Check the redirection after form submission                | The user should be redirected to the "My Reviews"                            | Pass      |          |
|                                   | Check the status of the submitted review                   | The review status should be "Awaiting Approval"                              | Pass      |          |
|                                   | Navigate to the "All Reviews" page                         | Only approved reviews should be visible on the "All Reviews" page            | Pass      |          |
| My Reviews                        |                                                            |                                                                              |           |          |
|                                   | Navigate to the "My Reviews" page                          | The page should display all reviews submitted by the user                    | Pass      |          |
|                                   | Check the presence of "Edit" and "Delete" buttons          | Each review should have both "Edit" and "Delete" buttons available page      | Pass      |          |
|                                   | Click the "Edit" button on a review                        | The user should be able to modify the rating and/or comment of the review    | Pass      |          |
|                                   | Check the status of the edited review                      | The review should display a status of "Awaiting Approval"                    | Pass      |          |
|                                   | Click the "Delete" button on any review                    | Redirection to the delete confirmation page                                  | Pass      |          |
| My Profile                        |                                                            |                                                                              |           |          |
|                                   | Navigate to the "My Profile" page                          | The page should display a form (all fields are non-mandatory)                | Pass      |          |
|                                   | Fill in only any one field and leave the others blank      | The form successfully submitted with only the filled field(s) updated        | Pass      |          |
|                                   | Fill in all available fields                               | The form should be successfully submitted with all fields updated            | Pass      |          |
|                                   | Leave all fields blank and submit the form                 | The form should still be submitted successfully with no data updated         | Pass      |          |
|                                   | Navigate to the "Booking Form" after filling in My profile | Data entered in the "My Profile" populate the fields in the "Booking Form"   | Pass      |          |

[Back To Top](#table-of-contents)

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
| <details><summary>Reset Password</summary><img src="static/images/readme_images/testing/html_validations/password-reset.png"></details>  | <mark>PASS</mark>   |
| <details><summary>Change Password</summary><img src="static/images/readme_images/testing/html_validations/change-password.png"></details>| <mark>PASS</mark>   |

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

[Back To Top](#table-of-contents)

## Responsiveness and Device Testing

Throughout the development process, the website was rigorously tested across a range of devices, including desktops, laptops, smartphones, and tablets. This testing ensured that the website displayed correctly on screens of various sizes and orientations, both portrait and landscape. Additionally, the responsive design was validated using Google Chrome's developer tools to confirm that the layout remained structurally sound and adaptable across different screen dimensions. No issues were noted, affirming that the site functions as expected across diverse environments.

[Back To Top](#table-of-contents)

## Browser Testing

The website was tested across Google Chrome, Safari, and Microsoft Edge, and no issues were found.

[Back To Top](#table-of-contents)

## Accessibility

Using the Wave Accessibility tool for continuous development and final testing involves the following checks:

- Ensure all forms are equipped with proper labels or aria-labels.
- Verify that color contrast ratios comply with the WCAG 2.1 Contrast Guidelines.
- Check that heading levels are correctly used to represent content hierarchy.
- Confirm that content is structured within landmarks to facilitate navigation with assistive technology.
- Provide descriptive alternative text or titles for non-text elements.
- Set the lang attribute for HTML pages.
- Implement ARIA properties following WCAG 2.1 best practices.
- Adhere to established coding standards for WCAG 2.1 compliance.

[Back To Top](#table-of-contents)

## Lighthouse Testing

Lighthouse validation was run on all pages (both mobile and desktop) in order to check performance, accessibility, best practices and CEO.

| Page            | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| --------------- | :---------: | :-----------: | :------------: | :-: | --------------------------------------------------------------------------------------------------------------------------- |
|                 |             |               |                |     |
| **Desktop**     |             |               |                |     |
| Home            |     99      |      100      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/desktop/home.png"></details>                    |
| Booking            |     100      |      100      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking.png"></details>                    |
| Locations            |     98      |      100      |      100       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/desktop/locations.png"></details>                    |
| Contact Us            |     100      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/desktop/contact-us.png"></details>                    |
| Booking Form            |     99      |      100      |      100       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking-form.png"></details>                    |
| Edit Booking            |     100      |      100      |      100       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-booking.png"></details>                    |
| Delete Booking            |     100      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-booking.png"></details>                    |
| All Reviews            |     100      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/all-reviews.png"></details>                    |
| Leave Review            |     100      |      100      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/desktop/leave-review.png"></details>                    |
| Edit Review            |     100      |      100      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-review.png"></details>                    |
| Delete Review            |     100      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-review.png"></details>                    |
| My Profile            |     100      |      100      |      100       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-profile.png"></details>                    |
| My Bookings            |     99      |      91      |      100       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-bookings.png"></details>                    |
| My Reviews            |     99      |      96      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-reviews.png"></details>                    |
| Sign In            |     100      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-in.png"></details>                    |
| Sign Up            |     100      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-up.png"></details>                    |
| Sign Out            |     100      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-out.png"></details>                    |
|                 |             |               |                |     |
| **Mobile**      |             |               |                |     |
| Home            |     95      |      100      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/mobile/home.png"></details>                    |
| Booking            |     96      |      100      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking.png"></details>                    |
| Locations            |     76      |      100      |      96       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/mobile/locations.png"></details>                    |
| Contact Us            |     95      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/mobile/contact-us.png"></details>                    |
| Booking Form            |     93      |      100      |      100       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking-form.png"></details>                    |
| Edit Booking            |     95      |      100      |      100       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-booking.png"></details>                    |
| Delete Booking            |     95      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-booking.png"></details>                    |
| All Reviews            |     94      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/all-reviews.png"></details>                    |
| Leave Review            |     96      |      100      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/mobile/leave-review.png"></details>                    |
| Edit Review            |     96      |      100      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-review.png"></details>                    |
| Delete Review            |     95      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-review.png"></details>                    |
| My Profile            |     95      |      100      |      100       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-profile.png"></details>                    |
| My Bookings            |     90      |      90      |      100       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-bookings.png"></details>                    |
| My Reviews            |     93      |      95      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-reviews.png"></details>                    |
| Sign In            |     95      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-in.png"></details>                    |
| Sign Up            |     95      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-up.png"></details>                    |
| Sign Out            |     95      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-out.png"></details>                    |

[Back To Top](#table-of-contents)

## User Story Testing

| User Story                                                                                                                                                                                                                        | Screenshot                                                                                                                                                                                              | 
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| As a new user I can create an account so that I can access the rental services.  | ![screenshot](static/images/readme_images/testing/user_stories/create-account.png)                                                                                                                                                                    | 
| As a registered user I can log in to my account so that I can view and manage my rentals.  | ![screenshot](static/images/readme_images/testing/user_stories/sign-in.png)                                                                                                                                                           | 
| As a registered user I can view and update my profile information so that my personal data is accurate and up-to-date.  | ![screenshot](static/images/readme_images/testing/user_stories/my-profile.png)                                                                                                                                                                 | 
| As a user I can search for available cars so that I can find a car that fits my needs.  | ![screenshot](static/images/readme_images/testing/user_stories/car-search.png)                                                                                                                                                                    | 
| As a user I can filter cars by type, price so that I can narrow down my search to the most suitable options.  | ![screenshot](static/images/readme_images/testing/user_stories/car-filter.png)                                                                                                                                                                 | 
| As a user I can view detailed information about a car so that I can make an informed decision before booking.  | ![screenshot](static/images/readme_images/testing/user_stories/detail-info.png)                                                                                                                                                           |
| As a user I can book a car for a specified period so that I can rent it for the time I need.  | ![screenshot](static/images/readme_images/testing/user_stories/book-car.png)                                                                                                                                                                   | 
| As a registered user I can view my current and past bookings so that I can keep track of my rental history.  | ![screenshot](static/images/readme_images/testing/user_stories/my-bookings.png)                                                                                                                                                                 | 
| As a registered user I can cancel an upcoming booking so that I can change my plans if necessary.  | ![screenshot](static/images/readme_images/testing/user_stories/delete-booking.png)                                                                                                                                                               | 
| As a user I can contact customer support so that I can get help with any issues or questions regarding my rental.  | ![screenshot](static/images/readme_images/testing/user_stories/contact-us.png)                                                                                                                                                     |
| As a admin I can add, update, or remove cars from the inventory so that the list of available cars is accurate.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-add-car.png)                                                                                                                                                                   | 
| As a admin I can manage user accounts so that I can maintain the integrity of the platform.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-users.png)                                                                                                                                                                    | 
| As a user I can leave a review and rating for a car I rented so that I can share my experience with other users.  | ![screenshot](static/images/readme_images/testing/user_stories/leave-review.png)                                                                                                                                                                   | 
| As a user I can view reviews and ratings left by other users so that I can make an informed decision before renting a car.  | ![screenshot](static/images/readme_images/testing/user_stories/customer-reviews.png)                                                                                                                                                                | 
| As a Site Owner I can store customer support form in the database so that I can review them.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-messages.png)                                                                                                                                                                     | 
| As a Site Owner I can mark user requests as "read" so that I can see how many I still need to process.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-messages-read.png)                                                                                                                                                               | 
| As a user I can view the location of each office on a Map so that I can easily find and navigate to the office.  | ![screenshot](static/images/readme_images/testing/user_stories/locations.png)                                                                                                                                                                   | 
| As a admin I can add and update the office locations on Google so that users can see the accurate location of each office.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-offices.png)                                                                                                                                                                 | 
| As a user I can read and accept the terms and conditions before confirming my booking so that I am aware of the rental policies and my responsibilities.  | ![screenshot](static/images/readme_images/testing/user_stories/terms.png)                                                                                                                                                                     | 
| As a user who has forgotten their password, I can be able to reset my password, so that I can regain access to my account.  | ![screenshot](static/images/readme_images/testing/user_stories/reset-password.png)                                                                                                                                                                     |
| As a newly registered user I can verify my email address, so that I can complete my registration and access my account.  | ![screenshot](static/images/readme_images/testing/user_stories/verification-email.png)                                                                                                                                                                     |

[Back To Top](#table-of-contents)

## Bugs

All known bugs and issues have been thoroughly addressed and resolved. The application is currently functioning as intended, with no outstanding errors reported.

[Back To Top](#table-of-contents)