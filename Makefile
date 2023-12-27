include aoc/c/Makefile
include aoc/cpp/Makefile
include aoc/csharp/Makefile
include aoc/go/Makefile
include aoc/java/Makefile
include aoc/js/Makefile
include aoc/python/Makefile

prepare:
	$(call install-dependencies-python)

load-puzzle: check_year_and_day
	@python3 aoc/python/load_puzzle.py $(year) $(day)

lint: check_year_and_day
ifneq ($(wildcard $(year)/day$(day)/part1.py),)
ifndef fix
	$(call lint-python)
else
	$(call lint-python-fix)
endif
endif

run: check_year_and_day check_directory
# ifneq ($(wildcard $(year)/day$(day)/part1.c),)
# 	$(call run-c)
# endif
# ifneq ($(wildcard $(year)/day$(day)/part1.cpp),)
# 	$(call run-cpp)
# endif
# ifneq ($(wildcard $(year)/day$(day)/Part1.cs),)
# 	$(call run-csharp)
# endif
# ifneq ($(wildcard $(year)/day$(day)/part1.go),)
# 	$(call run-go)
# endif
# ifneq ($(wildcard $(year)/day$(day)/Part1.java),)
# 	$(call run-java)
# endif
# ifneq ($(wildcard $(year)/day$(day)/part1.js),)
# 	$(call run-js)
# endif
ifneq ($(wildcard solutions/$(year)/day$(day)/part1.py),)
	$(call run-python, "data/$(year)/day$(day)/data.json")
endif

check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif

check_directory:
ifeq ($(wildcard solutions/$(year)/day$(day)),)
	@echo "directory does not exist"
	@exit 1
endif