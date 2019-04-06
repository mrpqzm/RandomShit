

sorted = lambda l: [x for y in [[i]*l.count(i) for i in range(min(l), max(l)+1)] for x in y]
