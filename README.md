# Twitter-Like-Api-System
1) pip install -r requirements.txt
2) python manage.py makemigrations
3) python manage.py migrate
4) python manage.py createsuperuser
5) python manage.py runserver

### For login user:
http://127.0.0.1:8000/api-auth/login/

### For register user:
http://127.0.0.1:8000/accounts/register/

### List of url of tweeter system:
http://127.0.0.1:8000/api/v1/tweet/ 

http://127.0.0.1:8000/api/v1/tweet/likes/ 

http://127.0.0.1:8000/api/v1/tweet/comments/ 

http://127.0.0.1:8000/api/v1/tweet/comments/<int:pk>/ 

http://127.0.0.1:8000/api/v1/tweet/public/ 

http://127.0.0.1:8000/api/v1/tweet/<int:pk>/ 

http://127.0.0.1:8000/api/v1/users/ 

http://127.0.0.1:8000/api/v1/users/<int:pk>/ 
