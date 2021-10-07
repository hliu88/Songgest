LINTER = flake8
APP_DIR = app

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

tests: lint unit

unit: FORCE
	cd $(APP_DIR); nosetests --with-coverage --cover-package=$(APP_DIR)

lint: FORCE
	$(LINTER) $(APP_DIR)/*.py