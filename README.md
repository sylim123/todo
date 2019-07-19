# todo

virtualenv --python=python3.5 myvenv

source myvenv/bin/activate # 가상환경 실행

pip install django~=2.0

git clone https://github.com/sylim123/todo.git

cd todo

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
