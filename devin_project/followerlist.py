from instagrapi import Client
import random, time, sys

# create an instance of the client
client = Client()

# Get the username and check it
username = input("username: ")
if not username:
    sys.exit("Please enter a username")

# Get the password and check it
password = input("password: ")
if not password:
    sys.exit("Please enter a password")

# log in to the client
try:
    client.login(username, password)
    print("logged in")
except:
    sys.exit("Failed to login")

# get the user ID of my user
my_id = client.user_id_from_username(username)
myfollowers = client.user_followers(my_id)
myFollowerId = list(myfollowers.keys())
myfollowernames = []
for ID in myFollowerId:
    myfollowername = myfollowers[ID].username
    myfollowernames.append(myfollowername)

# get the user ID of the target user
target_username = "dasantha_td"
user_id = client.user_id_from_username(target_username)

# get the list of followers of the target user
followers = client.user_followers(user_id)
follower_ids = list(followers.keys())

for id in follower_ids:
    follower_username = followers[id].username
    if not follower_username in myfollowernames:
        userToFollow = client.search_users(follower_username)[0]
        client.user_follow(userToFollow.pk)
        print(f"{follower_username} has been followed")
        timeToWait = random.randint(1,6)
        print(f"waintng {timeToWait} seconds")
        time.sleep(timeToWait)