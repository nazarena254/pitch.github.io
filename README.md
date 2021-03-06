# pitch
### It is a python web application that allows users to submit their pitches. 

## pitch Homepage
![](./app/static/images/pitch.png "pitch homepage")

## Description
pitch web application is built using Python framework (Flask). It allows users to use that one minute wisely. The users will submit their one minute pitches and other users will view them, vote on them and leave comments to give their feedback on them.

## Author
Nazarena Wambura.</br>
[Github](https://github.com/nazarena254)

## Technologies used
* Python3.9
* Flask2.1.1
* Heroku7.60.2
* Markdown


## Requirements
The user can perform the following functions:

- A user can submit and view the pitches other people have posted or view based on categories
- A user has to be signed in to leave a comment
- A user will receive a welcoming email once they sign up.
- A user can view the pitches I have created in my profile page.
- A user can comment on the different pitches and leave feedback.


 ## Installed packages
* Install code editor of your choice.
* Run `sudo apt-get update`,`sudo apt-get install python3.6` in terminal to install python.
* Install python extension in code editor(VScode) to run python modules easily.
* Run `python3.9 -m venv --without-pip virtual` in terminal to install virtual environment.
* Run `source virtual/bin/activate` to activate and `.../deactivate` to deactivate virtual env.
* Run `curl https://bootstrap.pypa.io/get-pip.py | python` to install pip in virtual env.
* Run `pip install <packagename>` to install other dependencies.
* Run `pip install flask` in terminal to install flask.
* Run `manage their personalities when working with a team.` to install postgresql its packages.
* Run `python3.9 manage.py server` to start server.
* Run `heroku run python3 manage.py db upgrade` to update heroku server. 
* To deploy on heroku, you will need to install/do the following:
   - outline dependencies `pip freeze`  
   - add dependencies in requirements.txt file `pip freeze > requirements.txt`
   - heroku cli `npm install -g heroku`
   - gunicorn  `python3.9 -m pip install gunicorn`
* To enable migrations:
   - Initialize migration `python3.9 manage.py db init`
   - Create migration `python3.9 manage.py db migrate -m "migration message"`  
   - Upgrade migration `python3.9 manage.py db upgrade` 

 

## Installation / Setup instruction
* Open Terminal {Ctrl+Alt+T}
* create and cd to the directory where you want to have your project
* git clone `https://github.com/nazarena254/pitches.github.io.git` to have it locally.
* code . or atom . based on the text editor you have and work on it.

## License
Distributed under [MIT license](https://github.com/nazarena254/pitch.github.io/blob/master/LICENSE).</br>
Copyright (c) 2022 Nazarena Wambura

## Support and Contact
Incase of another bug email me.</br>
Email:<nancyngunjiri1@gmail.com>
