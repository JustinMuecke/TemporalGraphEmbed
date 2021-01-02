
import instaloader

L = instaloader.Instaloader()

# Login or load session
L.login("my_mtg_collection", "hallodudepp")        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "justiiin_m")

# Print list of followees
count = 0
for followee in profile.get_followers():
    print(followee.username)
    count = count +1


print(count)
