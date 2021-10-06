LINTER = flake8

FORCE:

# prod: tests

dev_env: FORCE
	#enable virtual env
	pip install -r requirements.txt

github: FORCE
	-git commit -a
	git push origin master

docs: 
	pydoc3 -w main.py

#export FLASK_APP=main.py
# export FLASK_ENV=development
# flask run