define run-python
	@python3 aoc/python/run.py ${ARGS}
endef

define install-dependencies-python
	@pip install -r aoc/python/requirements.txt
endef

define lint-python
	@isort --check-only $(year)/day$(day)
	@black --check $(year)/day$(day)
	@pylint $(year)/day$(day)/*.py
endef

define lint-python-fix
	@isort $(year)/day$(day)
	@black $(year)/day$(day) -l 88
	@pylint $(year)/day$(day)/*.py
endef