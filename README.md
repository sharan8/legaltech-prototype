# LawDirect (Prototype) #

- This is a prototype for LawDirect web application
- Not all features/paths are working

## User Guide ##
1. Select the language
2. Identify the classification of problem that best describes your situation
3. May need to follow additional steps to narrow down the scope for the course of action to take
4. Course of action will provide clear instructions to guide users to seek help or take action if  required
5. Book a meeting with pro-bono lawyers at the nearest Community Centre

## Features ##
- Language Selection
  - Users can choose a language which they are most comfortable
- Step-by-step button view pages
  - Users will have a selection of conditional statements which propagates them to a final course of action page. This will help to narrow down to potentially identify problems that users may be facing
- Booking Manager for pro-bono lawyers at Community Centres
  - Serves as a common pool to manage booking schedules of all pro-bono lawyers at all Community Centres. This creates awareness and improves efficiency for users to seek advice from these lawyers should they need to.
- Google Maps search of address of Community Centre
  - Users can do a quick search on the location of the Community Centre. This is a functional tool that supports user experience

## Prototype Guide ##
You will need Python and Django to run LawDirect.

Clone the repo and run the command to load migrations:

`python manage.py makemigrations`

Then migrate the models:

`python manage.py migrate`

Create a superuser to update databases with foloowing command:

`python manage.py createsuperuser`

To run LawDirect run the following command:

`python manager.py runserver`

## Updating Database ##
These are the model descriptions:
- Problem - a path button to be displayed that can either lead to a link/booking manager or more children paths
- Location - a community club location
- Session - a session that can be booked
