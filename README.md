# tic_tac_toe
========
## setup environment
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## start api server

### local access only (for testing)
```
gunicorn main:api
```

### allow public access
```
gunicorn main:api -b 0.0.0.0:8000
```

## testing commands

### install http request tool
```
sudo apt-get install httpie
```

### POST / GET command
```
http POST 127.0.0.1:8000/ user=test1 pass=test123 mail=test@mail.com
http GET 127.0.0.1:8000/
```
