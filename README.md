
# Civicideahub Backend
REST API Backend for the [civicideahubV2](https://github.com/CodeForBaltimore/civicideahubV2) project.  The foundation for this API followed the approach highlighted in this TDD driven [tutorial](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1).  

## Installation & Server Initialization
1. Install Python 3 if you haven't already
2. In root directory, run theses terminal commands
```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
```
3. Change to the ideahubrest directory (cd ideahubrest/) 
4. Start the dev server
```
python3 manage.py runserver
```

## Helpful Commands
5. Update model (If you make changes to models.py)
```
python3 manage.py makemigration
python3 manage.py migrate
```
6. Validate tests
```
python3 manage.py test
```

###### Original Tutorial Followed:

[Authentication](http://v1k45.com/blog/modern-django-part-4-adding-authentication-to-react-spa-using-drf/)

[Oauth2](https://yeti.co/blog/oauth2-with-django-rest-framework/)
