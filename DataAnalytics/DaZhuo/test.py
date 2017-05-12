from threading import Thread
from time import sleep

tagA1 = 0           # timer
tagA1_count = True  # flag


# ----------- Timer -----------
def timerA1():
    global tagA1_count
    global tagA1
    # for i in range(240):
    for i in range(5):
        print 'Sleeping for a second...'
        sleep(1)
        tagA1 += 1
        print 'tagA1: ' + str(tagA1)

    # after 4 mins, no motion, turn off aircon

    print "\nCounting complete"
    print "tagA1: " + str(tagA1)
    print "tagA set back to True"

    tagA1_count = True
    return;
# ---------------------------------


# creates a thread that points to timerA1
t1 = Thread(target=timerA1)

# calls run method of thread
t1.start()  # Calls first function, count for 240s
# t1.join()
