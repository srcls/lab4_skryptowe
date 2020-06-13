import sys

if len(sys.argv) != 2: exit("Usage: python "+sys.argv[0]+" file");
fileName = sys.argv[1];

with open(fileName, 'r') as file:
    data = file.read().upper()

hist = [];
for c in list(map(chr, range(ord('A'), ord('Z')+1))):
	count = data.count(c)
	if count != 0: hist.append((c, count))

hist.sort(key=lambda tup: tup[1], reverse=True)
histSum = sum(count for _, count in hist)

for rec in hist:
	print(" {0} {1: 5} {2: 8.2f}%".format(rec[0],rec[1],rec[1]/histSum*100))
