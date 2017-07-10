#!/usr/bin/python3
import fileinput

counts = {}
for term in fileinput.input():
  term = term.strip()
  counts[term] = 1 if not term in counts else counts[term] + 1

for term, count in sorted(counts.items(), key=lambda t: t[1]):
  print('{}: {}'.format(count, term))
