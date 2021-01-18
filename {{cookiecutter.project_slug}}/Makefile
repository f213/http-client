lint:
	flake8
	test -x `which circleci` && circleci config validate .circleci/config.yml

test:
	py.test
