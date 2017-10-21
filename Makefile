setup:
		pip3 install pipenv
		pipenv --three
		pipenv shell
		pipenv install -r requirements.txt

		# autoenv # auto run virtual env
		pipenv install autoenv
		source /usr/local/bin/activate.sh
		ENV | grep -i DATABASE_URL

virtual:
		echo "cd into your project directory \
		autoenv will start your virtual env"
		pipenv shell

checkenv:
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
		python3 seed.py

all:
		make createdb
		make virtual
		make run
