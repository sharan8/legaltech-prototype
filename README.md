# LawDirect (Prototype) #

- This is a prototype of the LawDirect web application
- Note that not all features/paths are currently functional

## User Guide ##
1. Select the language
2. Identify the classification of problem that best describes your situation
3. May need to follow additional steps to narrow down the scope for the course of action to take
4. Course of action will provide clear instructions to guide users to seek help or take action if required
5. Book a meeting with pro-bono lawyers at the nearest Community Centre

## Features ##
- Language Selection
  - Users can choose a language with which they are most comfortable
- Step-by-step button view pages
  - Users will have a selection of conditional statements which propagates them to a final course of action page. This will help to narrow down to potentially identify problems that users may be facing
- Booking Manager for pro-bono lawyers at Community Centres
  - Serves as a common pool to manage booking schedules of all pro-bono lawyers at all Community Centres. This creates awareness and improves efficiency for users to seek advice from these lawyers should they need to.
- Google Maps search of address of Community Centre
  - Users can do a quick search on the location of the Community Centre. This is a functional tool that supports user experience

## Prototype Guide ##
You will need Python 3 and Django 2.1 to run the LawDirect application on your local machine.

* Python 3 Installation: <https://www.python.org/downloads/>
* Django 2.1 Installation: <https://www.djangoproject.com/download/>

Clone this repository onto your local machine and run the following command to load the migrations:

`python manage.py makemigrations`

Then migrate the models:

`python manage.py migrate`

Next, create a superuser account to update the database manually with following command:

`python manage.py createsuperuser`

To run LawDirect run the following command:

`python manage.py runserver`

Open the link provided in your local browser to access the application.

## Updating Database ##
These are the model descriptions:
- Problem - a path button to be displayed that can either lead to a link/booking manager or more children paths
- Location - a community club location
- Session - a session that can be booked
