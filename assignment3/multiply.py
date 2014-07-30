import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0] == 'a':
        for x in range(5):
            mr.emit_intermediate((record[1],x),record)
    else:
        for y in range(5):
            mr.emit_intermediate((y,record[2]),record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {}
    b = {}
    for r in list_of_values:
        if r[0] == 'a':
            a[r[2]] = r[3]
        else:
            b[r[1]] = r[3]
    total = 0
    for x in range(5):
        if x in a and x in b:
            total += a[x]*b[x]
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
