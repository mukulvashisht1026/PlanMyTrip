# django

## How to setup project?

first clone the repo
```
cd django
pip install virtualenv
virtualenv env
source env/lib/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


To run the tests use the following command
```
api endpoints 

localhost:8000/api/data   

use get request with key 'Budget' and value buget value

```