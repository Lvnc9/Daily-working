#! python3.9.9
# Start
# Talking about data structures and attributes of using them
# Modules
import queue
import time

# Where to start
quetest = queue.Queue(maxsize=3)
quetest.put("how")
quetest.put("you")
quetest.put("Dont")
#quetest.put("Laugh")
print(quetest.full())

while quetest:
    print(quetest.get())
    if quetest.empty():
        break


# End