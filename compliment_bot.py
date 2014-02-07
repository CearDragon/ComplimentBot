import praw
import time
import random as rand
rand.seed()
comp = praw.Reddit(user_agent='Compliment')
comp.login(ADD USER NAME HERE,ADD PASSWORD HERE)
ins = open( "Compliments.txt", "r" )
array = []
for line in ins:
    array.append(line)
while True:
    try:
        print "Initializing..."
        print "Generating Subreddit: Rising"
        subs = comp.get_subreddit('random')
        for submission in subs.get_rising(limit=2):
            Type = rand.randint(0,5)
            if Type == 0:
                submission.add_comment("[a compliment for you](http://ourstereo.com/compliment/rotate.php)")
                print 'Human Complimented'
                time.sleep(350)
            else:
                index = rand.randint(0,234)
                msg = array[index]
                submission.add_comment(msg)
                print 'Human Complimented'
                time.sleep(350)
        print "Initializing..."
        print "Generating Subreddit: New"
        subs = comp.get_subreddit('random')
        for submission in subs.get_new(limit=2):
            Type = rand.randint(0,5)
            if Type == 0:
                submission.add_comment("[a compliment for you](http://ourstereo.com/compliment/rotate.php)")
                print 'Human Complimented'
                time.sleep(350)
            else:
                index = rand.randint(0,234)
                msg = array[index]
                submission.add_comment(msg)
                print 'Human Complimented'
                time.sleep(350)
        print "Initializing..."
        print "Generating Subreddit: New"
        subs = comp.get_subreddit('random')
        for submission in subs.get_hot(limit=2):
            Type = rand.randint(0,8)
            if Type == 0:
                submission.add_comment("[a compliment for you](http://ourstereo.com/compliment/rotate.php)")
                print 'Human Complimented'
                time.sleep(350)
            else:
                index = rand.randint(0,234)
                msg = array[index]
                submission.add_comment(msg)
                print 'Human Complimented'
                time.sleep(350)
        print "Done complimenting. Sleeping..."
        time.sleep(500)
    except:
        print "Oops!"
        continue
