import re

def extract_line(line):
    sr = re.search('\d+(?= red)', line)
    sg = re.search('\d+(?= green)', line)
    sb = re.search('\d+(?= blue)', line)

    r = int(sr.group()) if sr != None else 0
    g = int(sg.group()) if sg != None else 0
    b = int(sb.group()) if sb != None else 0

    return [r, g, b]

def extract_game(line):
    sg = re.search('[Game ]\d+', line)
    g = int(sg.group()) if sg != None else 0

    return g;
