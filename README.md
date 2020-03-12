# CSE312Project
Github repo for CSE312 Project

#### Django Instructions ####
This project is built in Django with Materialize CSS.
To run it you will need Django and Python Installed.
Make sure you have Python 3.xx installed. You will also need pip installed.
- To install pip : https://pip.pypa.io/en/stable/installing/
Download the "get-pip.py" script and run it with "python get-pip.py".
- To install Django, check out : https://docs.djangoproject.com/en/3.0/topics/install/#installing-official-release.
A virtual environment is useful if you don't want to install systemwide packages.
- To activate a virtual environment : run "pipenv shell" in a terminal and then use "python -m pip install Django".

Once you have Django installed, open a terminal and go into the cse312 directory where the manage.py script is located.
- To run the server : "python manage.py runserver" and open a browser and go to "localhost:8000".

#### Docker Instructions ####
For Testing :
- To build Docker use : "sudo docker-compose build", the sudo part is required for root access unless you have another usergroup set up.
- To run Docker after its done building : "sudo docker-compose up"
- And then open localhost:8000 on your browser.

For Production:
- To Build the container : "sudo docker build -t <name> ."
- To run the container : "sudo docker container run --publish 8000:8000 --detach <name>"
- Open a browser and go to localhost:8000

### Project Description ###
Our site will provide a social media experience where users can share photos, interact with followed users’ posts, and direct message friends. A user can sign up for an account if they don’t already have one. Once an account has been created, they can sign into the site to personalize their experience and use features that are only available when logged in, such as making posts on their page, following other users, using direct messaging features, and interacting with posts. The direct messaging feature allows the user to send a private message to their friend. The user can view someone’s profile, which includes a profile picture, their name, username, bio, and posts. They can also follow the person if they choose, which will help personalize their feed and other features. A user’s feed will populate with posts from their friends, in which they can like and comment on. Overall, our site will help people connect with their friends through sharing content and messaging.
