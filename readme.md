```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
```
celery -A core.compiler worker -l debug
To run background: nohup ... &
```
```
To solve MySQL problem:
sudo apt-get install libmysqld-dev
```
TODO: Chinese character => ? in submission
