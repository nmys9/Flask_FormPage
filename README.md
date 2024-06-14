# Flask_FormPage

This project is a Flask web application that provides multiple pages for user login and signup functionalities.

## Download and Installation

1. Make sure you have Python and pip installed on your computer.
2. Download the project either through its link or by using the following command in the terminal:

### Installation
- mkdir Flask_FormPage
- cd Flask_FormPage

* install and activate virtualenv

```bash
python3 -m venv venv 
```

or

```cmd
python -m venv venv 
```

If you are using the Windows platform

```cmd
venv\Scripts\activate.bat 
```

But if you are using linux or unix

```bash
source ./venv/bin/activate 
```

- now clone from this repo

```cmd
git clone https://github.com/nmys9/Flask_FormPage.git
```
```cmd
cd Flask_FormPage
```

- install all Flask_FormPage dependencies 

```bash
pip install -r requirements.txt
```
- create .env file

```cmd
touch .env
```

copy data from .env.example to .env

And write these values into the .env file

- FLASK_ENV= development 
- FLASK_APP= run.py

- run app

```cmd
flask run
```

