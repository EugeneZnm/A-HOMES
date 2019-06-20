# A-HOMES

Django based real estate platform allowing a real estate firm to upload property listings with their respective properties and traits along with the specific realtor handling the property. 


------------------------------------------------------------------------
## BY: [Eugene Nzioki](https://github.com/EugeneZnm)

## User Requirements

+ [x] Realtor sign in with the application to start using.
+ [x] Set up a profile about realtors.
+ [x] Creation of property listings by admin.
+ [x] Property search or filter by users accoring to location, pricing, rooms and other properties.
+ [x] Sending of email messages to realtors.
+ [x] Setting of realtor as MVP realtor.
+ [x] viewing of single individual listing.
+ [x] Alerting of user when contacting realtor about a property already viewed.

## Admin Dashboard

 Use django admin to post photos to the database and manage the photos
## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/EugeneZnm/A-Homes.git && cd A-Homes
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip install -r requirements.txt
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Running the server 
```bash
python manage.py runserver
```
## Contributing

- Git clone [https://github.com/EugeneZnm/A-Homes.git](https://github.com/EugeneZnm/A-Homes.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

### Deploying to heroku
Refer to this guide: [deploying to heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)
Set the configuration to production mode

## Live Demo

The web app can be accessed from the following link: 
[Majirani](https://majirani.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 2](https://docs.djangoproject.com/en/2/)
* [Heroku](https://heroku.com)
* [PostrgeSql]
* [Bootstrap 4]


## License
MIT License

Copyright(c) 2019

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
