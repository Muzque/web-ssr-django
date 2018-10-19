python manage.py collectstatic --no-input
mkdir volumes
python manage.py makemigrations
python manage.py migrate
