#! python3
# Start
# Modules
import time

# Display the program's instructions.
print("""Press ENTER to begin.
Afterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.""")

input('-->')                 # press Enter to begin
print('Started.')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the time laps
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {totalTime} {lapTime}", end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
    # Handle th ctrl-c Exception to keep its error message from displaying.
    print("\nDone.")

# End