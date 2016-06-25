init:
	pip install -r requirements/development.txt
	pip install -e .
test:
	py.test --cov=talkzoho tests/
