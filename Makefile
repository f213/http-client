test:
	rm -Rf testing
	mkdir -p testing
	cd testing && cookiecutter  --no-input ../
