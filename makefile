PACKAGE_NAME=actions

.PHONY: tests install

install:
	pip install -r requirements.txt

tests:
	pytest tests/$(PACKAGE_NAME)

lint:
	black $(PACKAGE_NAME)
	black tests

lint-ci:
	flake8 actions --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 actions --count --max-complexity=10 --max-line-length=127 --statistics

	flake8 tests --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 tests --count --max-complexity=10 --max-line-length=127 --statistics

tests-cov:
	coverage run -m --source=actions pytest tests
	coverage report --fail-under=100
