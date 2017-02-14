```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
```
To solve MySQL problem:
sudo apt-get install libmysqld-dev
```
TODO: Chinese character => ? in submission

Sass required!

## Server
`http://api.aiplayground.online/`

## Sign up / sign in
```json
{
  "info": {
    "username": "xxx",
    "password": "xxx",
    "email": "xxx",
    "address": "xxx"
    // ......
  },
  "token": "xxx"
}
```
```json
// response
{
  "status": 0, // or 1 if failed
  "error": {
    "username": "Username is wrong...",
    "password": "Password is wrong..."
  }
}
```

## Data
