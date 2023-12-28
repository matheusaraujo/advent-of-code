define run-python
	@python3 aoc/python/run.py $(1) $(2)
endef

define install-dependencies-python
	@pip install -r aoc/python/requirements.txt
endef

define lint-python
	@isort --check-only $(1)
	@black --check $(1)
	@pylint $(1)/*.py
endef

define lint-python-fix
	@isort $(1)
	@black $(1) -l 88
	@pylint $(1)/*.py
endef