init:
	pip install -r requirements/development.txt --no-cache-dir --upgrade
test:
	py.test --cov=talkzoho tests/
test_fail:
	py.test --cov=talkzoho --ff -x tests/
deploy:
	pip install pypandoc
	python setup.py register sdist upload
