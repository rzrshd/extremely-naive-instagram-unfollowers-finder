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
