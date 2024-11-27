from helpers import hashing


def part2(puzzle_input):
    boxes = {}

    for step in puzzle_input[0].split(","):
        if "=" in step:
            label, focal_length = step.split("=")
            box = hashing(label)
            boxes.setdefault(box, {}).update({label: int(focal_length)})
        elif "-" in step:
            label = step.split("-")[0]
            box = hashing(label)
            if box in boxes and label in boxes[box]:
                del boxes[box][label]

    ans = 0
    for i_box, box in boxes.items():
        for i_slot, (_, focal_length) in enumerate(box.items(), 1):
            ans += (i_box + 1) * i_slot * focal_length

    return ans
