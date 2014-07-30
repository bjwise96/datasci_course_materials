import sys
import MapReduce


inputdata = open(sys.argv[1])

#Part 1
mr = MapReduce.MapReduce()

#Part 2
def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, (key))

#Part 3
def reducer(key, list_of_values):
    total = []
    for v in list_of_values:
        if v not in total:
            total.append(v)
    mr.emit((key, total))

#Part 4
mr.execute(inputdata, mapper, reducer)