# Peaks and Troughs
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p>
    <img src="./app/static/images/logo.png" alt="Logo">
</p>

## Learn the basics about investing
<hr>

Welcome to Peaks and Troughs! A place where you can learn the basics about investing. Work through the four sections of Stocks, Derivatives, Cryptocurrency, and the Risks of investing, before testing your knowledge with our assessment. You can see your feedback after the assessmsent to review how much your learnt, and can attempt as many times as you want. The assessment contains five multiple choice questions, so choose your answers wisely.

Peaks and Troughs is a Flask application that builds the content on the server and presents it in your browser. It is running a SQLite database to store the data, and utilises a Model-View-Controller structure to link everything together.

## Setup and Access
In order to utilise the Peaks and Troughs application locally, please follow the next steps:

1. Get a copy of the source code and go to the top level of the directory
```
$ git clone https://github.com/danielchegwidden/peaks-and-troughs.git
$ cd peaks-and-troughs
```
2. Ensure you are running Python 3 and install virtualenv
```
$ python --version
$ python -m pip install virtualenv
or
$ python3 --version
$ python3 -m pip install virtualenv
```
3. Create a Python virtual environment
```
$ python -m venv venv
or
$ python3 -m venv venv
or #if using conda
$ conda env create -f environment.yml
```
4. Activate the virtual environment
```
$ source venv/bin/activate
or
$ conda activate peaks-env
```
5. Install the required packages
```
$ python -m pip install -r requirements.txt
or
$ python3 -m pip install -r requirements.txt
```
6. Run the application
```
$ flask run
```
The application will now be running on port 5000 accessible at the following link:
```
http://localhost:5000
```
Once you go to this link, you will be directed to the index page and can navigate around the application. For the initial use, click login to access the content, which is also where you can register if you are a new user.

There are buttons to navigate to the content on the learn page as well as to access the assessment and feedback. You will only be able to access feedback if you have completed at least one assessment.

For admin users, you will also have access to the statistics page where you can see the summary results of all users, as well as who those users are and what questions are available to be in the assessment.

## Testing
Testing has been completed using the [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) package (which in turn uses Python unittest) for unit tests and the [Selenium](https://www.selenium.dev) package for system tests.

To run the unit tests, run the following whilst having your virtual environment active from the top level of the application.
```
$ coverage run -m tests.unittest
$ coverage report -m
```
This will run the unit tests and display the coverage report. The unit tests aim to have coverage of as much of the application as possible, with a focus on the ```models.py``` file, with the ```routes.py``` and ```controllers.py``` being tested in the system tests. To run the system test, ensure that you have Mozilla Firefox installed and run the following (using the venv virtual environment).
```
$ python -m tests.systemtest
```
The following is a snippet of the current coverage report, which shows the unit tests cover almost 80% of the code.
```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
app/controllers.py     123     92    25%   14-25, 29-30, 34-50, 54, 58-79, 83-87, 102-106, 110-126, 132-146, 152-167
app/forms.py            43      8    81%   24-26, 29-31, 34-35
app/models.py          140      0   100%
app/routes.py           49     14    71%   14, 19-21, 26, 31-33, 39, 45, 51, 57, 63, 69
config.py                6      0   100%
tests/unittest.py      171      0   100%
--------------------------------------------------
TOTAL                  532    114    79%
```

## Development
The development of Peaks and Troughs followed an agile approach, utilising the Issues and Projects sections of GitHub to identify where work was required and who was responsible for delivering it. Each change was created on a personal development branch and a Pull Request was raised that had to be reviewed by the other developer prior to it being merged into the ```main``` branch. This process was complimented by regular meetings with the client to show progress and get feedback on features.

A [STYLE.md](STYLE.md) file has been created to specifiy the style that has been used throughout the application, both on the code side and on the design side. Any new additions will need to follow this guide. A ```.env``` file has been created as well to set local environment variables. Pre-commit hooks were used to ensure that the code was of a consistent quality before being merged into the ```main``` branch.

The content for the relevant sections is stored in the static directory and AJAX is used to populate the application. This allows for additions to be easily tracked and managed separate to the page that displays them.
