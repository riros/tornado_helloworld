PROJECT_NAME ?= tornado_hello_world


run:
	@python run.py

requirements-install:
	@pip install -r requirements.txt

genereate-requirements-from-installed:
	@pip install pipdeptree
	@pipdeptree | grep -P '^\w+' > ./dev.requirements.txt

reinstall-requirements:
	@pip freeze | grep -v "pkg-resources" | grep -v "github.com" | xargs -r pip uninstall -y
	@pip install -r dev.requirements.txt
	@make freeze

freeze:
	@pip freeze > ./requirements.txt
	@cat ./requirements.txt

docker:
	@sudo chmod 777 -R ./_mounted/
	@docker-compose build
	@docker-compose up

