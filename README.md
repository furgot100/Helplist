# Helplist
Helplist is a web app that is meant to provide help with school related topics.
Provides a way to find help in a quick and concise way.

## Requirements
The only requirements for this project are [Django](https://docs.djangoproject.com/en/3.2/topics/install/) and a virtual enviorment.

## Getting Started
There are two ways to run the app
1. The product is live at https://helperlist.herokuapp.com/


2. First clone the repo on to your local machine. Then create and activate a [virtual enviornment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).

When that is done run:
```
$ pip install -r requirements.txt
```
After that we have make sure the models are creted so run the following commands:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
When that is all done, simply run the following command to start the app:
```
$ python3 manage.py runserver
```

## Known Issue
1. Admin panel is not working properly
2. 



