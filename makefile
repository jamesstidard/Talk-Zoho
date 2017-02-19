init:
	pip install -r requirements/development.txt --no-cache-dir --upgrade
test:
	# example `make test` to test all or `make test m=crm` to test module
	py.test --nocapturelog --cov=talkzoho tests/$(shell X="${m}"; echo "$m" | tr '[:upper:]' '[:lower:]')
test_fail:
	py.test --cov=talkzoho --ff -x tests/
deploy:
	pip install pypandoc
	python setup.py sdist upload
