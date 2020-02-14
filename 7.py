import os
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys

# δηλωνουμε τα κλειδια που μας παρεχει το API
consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'


# κανουμε το authentication του API με τα κλειδια που εχουμε
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)


# δινονται χρηστες προς εξεταση απο τον χρηστη και γινεται ελεγχος
account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)


# αν δωθηκαν χρηστες
if len(account_list) > 0:
    sums = {}
    max = -1
    for target in account_list: # για κάθε χρήστη
        sums[target] = 0
        print("Getting data for " + target)
        item = auth_api.get_user(target)
        # για κάθε ένα post, από τα τελευταία 50, που έχει κάνει ο χρήστης
        for status in Cursor(auth_api.user_timeline, id=target).items(50):
            post = status._json["text"].split(" ") # μετατρέπουμε το post σε λίστα λέξεων
            # για καθε λεξη του post
            for word in post:
                # προσθέτουμε τον αριθμό των λέξεων στο άθροισμα του χρήστη
                sums[target] += 1

        # βρίσκουμε ποιος έχει χρησιμοποιήσει τις περισσότερες λέξεις
        if sums[target] > max:
            max = sums[target]

    # εκτυπώνουμε τον χρήστη με τις περισσότερες λέξεις
    for user in sums:
        if sums[user] == max:
            print("Ο χρήστης "+user+" έχει χρησιμοποιήσει τις περισσότερες λέξεις.")
            print("Συγκεκριμένα, έχει χρησιμοποιήσει", sums[user], "λέξεις.")
