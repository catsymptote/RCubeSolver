default:
	@echo "Nah, bro"


test:
	pytest
	mypy src
	flake8 src


testfull:
	make test
	tox


clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .tox
