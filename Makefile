setup:
		pip3 install pipenv
		pipenv --three
		pipenv shell
		pipenv install -r requirements.txt


autovirtualenv:
		echo "if you have autoenv installed and the source line below in your dot files"
		echo "your virtual environment will start automagically when you cd into your dir"
		pipenv install autoenv
		echo "source /usr/local/bin/activate.sh" >> ~/.bash_profile
		echo "source /usr/local/bin/activate.sh" >> ~/.zshrc

virtual:
		echo "cd into your project directory autoenv will start your virtual env using .env"
		pipenv shell

checkenv:
		ENV | grep -i DATABASE_URL

run:
		echo "refresh your browser"
		open http://localhost:5000/show_all
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
		echo "first start your virtual env"
		make createdb
		make run
