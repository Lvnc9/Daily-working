#! python3.9.9
# Start
# explaining working with Data structure and it Calculeses
# Modules
from collections import namedtuple, defaultdict, Counter
from functools import total_ordering
from operator import itemgetter, methodcaller, attrgetter

# Settly Hood
t1 = {'you', 'me', 'they', 'we'}
t2 = {'you' , 'how', 'what', 'when'}
t3 = t1 | t2
print(t3)

t3 = t1 & t2
print(f"This is interaction functions between {t1.__str__} and {t2.__str__}\t", t3)

bullshit = {1, 2, 3}
true_bullshit = {1, 2, 3, 4, 5}
#print(bullshit.issubset(true_bullshit))

# End