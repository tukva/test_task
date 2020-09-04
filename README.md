## Run project

Install `docker` and `docker-compose`   

Run via `docker-compose up --build`       

Apply migrations via `docker-compose exec web python manage.py migrate --noinput` 
   
Create superuser via `docker-compose exec web python manage.py createsuperuser`

You can follow the link http://localhost:8000/api/

## Deploy API version

Follow the link https://fast-oasis-42889.herokuapp.com/api  

## Postman collection link

https://www.getpostman.com/collections/27628bf9cecff86619e4 
