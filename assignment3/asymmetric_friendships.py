import MapReduce
import sys
import json
import tempfile

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(tuple(record),1)
    mr.emit_intermediate(tuple(list(reversed(record))), -1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list(set(list_of_values)):
        total += v
    if total != 0:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
