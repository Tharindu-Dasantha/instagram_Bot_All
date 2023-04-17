from instagrapi import Client
from getpass import getpass
import random
import sys
import time


# Get the credentials to log into the insta account
username = input("Username: ")
password = getpass(prompt="Enter your password")

# Loginto the account
client = Client
client.login(username, password)

my_id = client.user_id_from_username(username)

# Get the list of following accounts
my_following_as_dict = client.user_following(my_id)
my_following_id_as_list = list(my_following_as_dict.keys())
my_following_username_as_list = []
for user_id in my_following_id_as_list:
    users_username = client.username_from_user_id()
    my_following_username_as_list.append(users_username)

# Get the list of followers (who followed me)
my_followers_as_dict = client.user_following(my_id)
my_followers_userid_as_list = list(my_followers_as_dict.keys())
my_followers_username_as_list = []
for id_of_user in my_followers_userid_as_list:
    users_username = client.username_from_user_id(id_of_user)
    my_followers_username_as_list.append(users_username)