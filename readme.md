```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
```
celery -A compile.compiler worker -l debug
To run background: nohup ... &
```
```
To solve MySQL problem:
sudo apt-get install libmysqld-dev
```
