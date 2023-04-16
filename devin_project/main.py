from instagrapi import Client
import sys
import random
import time


# Get the username form the user
userName = input("Enter the username of your instagram: ")
if not userName:
    sys.exit("Please enter a username and try again.")

# Get the password form the user
password = input("Enter the password of your instagram: ")
if not password:
    sys.exit("Please enter a password and try again.")

# Initialize the client instagram connection
client = Client()

# Log into the instagram using the given username and password
try:
    client.login(userName, password)
except:
    sys.exit("Something went wrong when trying to login to instagram. Please try again and check your credentials")

# Go to the notification list
inbox = client.direct_pending_inbox()
notifications = inbox["pending"]


# Filter and get the new followers
new_followers = [n for n in notifications if n.type == 'follow']

# Get the usernames of new followers
follower_usernames = [f.user.username for f in new_followers]

# print the followed member
for follower in follower_usernames:
    print(f" {follower} has followed you!")
    client.user_follow(follower)
    print(f" {follower} has been followed.")
    print("-" * 225)
    print(f"following the followers of {follower}")
    
    # Go to the followers page
    user = client.search_username(follower)
    user_id = user.pk
    
    # Get the followers list of that user
    user_followers = client.user_followers(user_id)
    user_followers_usernames = [flwer.username for flwer in user_followers]

    # follow the users
    for user_followers_username in user_followers_usernames:
        client.user.follow(user_followers_username)
        print(f"{user_followers_username} has been followed.")
        time_to_sleep = random.randint(1,60)
        print(f"Sleeping for {time_to_sleep} seconds")
        time.sleep(time_to_sleep)