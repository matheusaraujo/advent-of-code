hello-world:
	@echo "hello-world!"

prepare:
	@cd aoc && pip install -r requirements.txt

get-data:
	@python aoc/load_puzzl_json.py 2015 1
	# run the program using generated json file