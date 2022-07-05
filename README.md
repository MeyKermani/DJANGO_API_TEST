# DJANGO API TEST
Install requirements by below command;
```
pip install -r requirements.txt
```
You can use 2 GET API endpoints via these urls to get list of users.
```
  - users/
  - users-with-address-count/ 
```

The second one accepts a query string "address_limit" which determines the address count per each user in the response.

You can use a POST API endpoint via this url to create an address for a user.
```
  - address/
```
Notification part works with a simple django 'post_save' signal. We can use Celery and a RabbitMQ or Redis backend to improve this part.
