file = open('sample.txt')
for line in file:
  line = line.rstrip()
  print(line)
file.close()
