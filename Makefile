setup:
		pipenv --three
		pipenv install -r requirements.txt

virtual:
		pipenv shell
		ENV | grep -i DATABASE_URL

run:
		echo "refresh your browser"
		open http://localhost:5000
		pipenv run python3 app.py

help:
		# read up on these:
		pipenv --help
		open https://github.com/kennethreitz/pipenv

about:
		pipenv --version
		pip --version

createdb:
		psql -a -f postgresql_setup.sql
		python3 db_create.py

seed:
		python3 seed.py

all:
		make createdb
		make seed
		make run
