define read-json
	$(eval ARGS := \
		"title=$(shell jq -r '.title' $(1))" \
		"year=$(shell jq -r '.year' $(1))" \
		"day=$(shell jq -r '.day' $(1))" \
		"input_file=$(shell jq -r '.inputFile' $(1))" \
		"part1_solved=$(shell jq -r '.part1.solved' $(1))" \
		"part1_output_file=$(shell jq -r '.part1.outputFile' $(1))" \
		"part2_solved=$(shell jq -r '.part2.solved' $(1))" \
		"part2_output_file=$(shell jq -r '.part2.outputFile' $(1))"
	)
endef