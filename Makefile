setup:
		pipenv install -r requirements.txt

virtual:
		pipenv shell

run:
		pipenv run python3 app.py

help:
		# read up on these:
		pipenv --help
		open https://github.com/kennethreitz/pipenv

about:
		pipenv --version
		pip --version
