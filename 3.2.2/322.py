from Post import Post

all_posts_archive = []

# your code here
username = input("Please select a username: ")

print(f"Welcome, {username}")

userinput = None

while userinput != "quit":
    userinput = input("What would you like to do? ")
    if userinput == "new":
        new_post = Post(username, input("What would you like to post? "))
        all_posts_archive.append(new_post)
        userinput = "None"
    elif userinput == "remove":
        post_to_remove = input("Which post would you like to remove? ")
        del all_posts_archive[int(post_to_remove)]
        userinput = "None"
    elif userinput == "changeuser":
        username = input("Please select a username: ")
        print(f"Welcome, {username}")
        userinput = "None"
    elif userinput == "print":
        for post in all_posts_archive:
            print(post)
        userinput = "None"
    elif userinput == "quit":
        print("Goodbye!")
        quit()
    else:
        print("Invalid command. Please try again.")
