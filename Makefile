# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

#  Lint using
## flake8: PEP8 based lint
### there is an error in pytest-flake8
## mypy  : type check
lint:
	flake8 chap*
	mypy chap*

#  formatting
## black: formatting
## isort: import formatting
format:
	black chap*
	isort chap*