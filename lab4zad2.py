import sys

if len(sys.argv) != 2: exit("Usage: python "+sys.argv[0]+" file")
fileName = sys.argv[1]

with open(fileName, 'r') as file:
    data = file.read()

targetHist = data.split('\n',1)[0]
data = data[len(targetHist)+1:]
hist = []
for c in (chr(x) for x in range(ord('A'), ord('Z')+1)):			#list(map(chr, range(ord('A'), ord('Z')+1))):
	count = data.count(c)
	if count != 0: hist.append((c, count))

hist.sort(key=lambda tup: tup[1], reverse=True)
data = data.translate(str.maketrans(targetHist,''.join(t[0] for t in hist)))
print(data)
