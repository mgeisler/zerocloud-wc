import os
import math

inp_dir = '/dev/in'

counts = []
paths = []

for inp_file in os.listdir(inp_dir):
    with open(os.path.join(inp_dir, inp_file)) as fp:
        data = fp.read()
        count, path = data.split()
        counts.append(int(count))
        paths.append(path)

size = int(math.log10(max(counts))) + 2

for count, path in zip(counts, paths):
    print '%*d %s' % (size, count, path)
print '%*d total' % (size, sum(counts))
