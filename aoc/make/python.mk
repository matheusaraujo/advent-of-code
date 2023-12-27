define run-python
	@python3 aoc/py/run.py ${year} ${day}
endef

define install-dependencies-python
	@pip install -r aoc/py/requirements.txt
endef

define lint-python
	@isort --check-only ${year}/day${day}
	@black --check ${year}/day${day}
	@pylint ${year}/day${day}/*.py
endef

define lint-python-fix
	@isort ${year}/day${day}
	@black ${year}/day${day} -l 88
	@pylint ${year}/day${day}/*.py
endef