import sys
import MapReduce


inputdata = open(sys.argv[1])

#Part 1
mr = MapReduce.MapReduce()

#Part 2
def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

#Part 3
def reducer(key, list_of_values):
    order = list_of_values[0]
    for v in list_of_values:
        if v != order:
            mr.emit(order+v)

#Part 4
mr.execute(inputdata, mapper, reducer)