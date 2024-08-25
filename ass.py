
"""
with open("followers.txt", "r", encoding="utf-8") as file:
	followers = [line.strip() for line in file.readlines()]

with open("following.txt", "r", encoding="utf-8") as file:
	following = [line.strip() for line in file.readlines()]
"""


##########################################################################################
# approach 1:

with open("followers.txt", "r", encoding="utf-8") as file:
	followers = [line.split("'")[0] for line in file.readlines() if "'s profile picture" in line]

with open("following.txt", "r", encoding="utf-8") as file:
	following = [line.split("'")[0] for line in file.readlines() if "'s profile picture" in line]

print()
print("Bitches:", set(following) - set(followers)) # who don't follow back
print()
print("Kewl:", set(followers) - set(following)) # whom I don't follow back

print()
print(f"{len(followers) = }")
print()
print(f"{len(list(set(followers))) = }")


##########################################################################################
# approach 2:


import pandas as pd


followers = pd.read_csv("followers.txt", encoding="utf-8", header=None)
following = pd.read_csv("following.txt", encoding="utf-8", header=None)

followers.columns = ["followers"]
following.columns = ["following"]

#print(followers.head())
#print(following.head())

indices_followers = followers[followers["followers"].str.contains("'s profile picture")].index + 1
indices_following = following[following["following"].str.contains("'s profile picture")].index + 1

#print(indices_followers)
#print(indices_following)

followers = followers.loc[indices_followers]
following = following.loc[indices_following]

followers = followers.reset_index(drop=True)
following = following.reset_index(drop=True)

#print(followers.head())
#print(following.head())

followers = set(followers["followers"])
following = set(following["following"])

beches = following - followers
beches = pd.DataFrame(beches, columns=["accounts"])
print(beches)

kewl = followers - following
kewl = pd.DataFrame(kewl, columns=["accounts"])
print(kewl)
