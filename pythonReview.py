def create_youtube_video(title, description):
    youtube_video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return youtube_video

def like(youtube_video):
    if "likes" in youtube_video:
        youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video):
    if "dislikes" in youtube_video:
        youtube_video["dislikes"] += 1
    return youtube_video

def add_comment(youtube_video, username, comment_text):
    if username in youtube_video["comments"]:
        youtube_video["comments"][username].append(comment_text)
    else:
        youtube_video["comments"][username] = [comment_text]
    return youtube_video

my_youtube_video = create_youtube_video("how to drink water", "a video explaining the art of drinking water")

for i in range(495):
    my_youtube_video = like(my_youtube_video)

username = "user123"
comment_text = "Great video!"
my_youtube_video = add_comment(my_youtube_video, username, comment_text)

my_youtube_video = dislike(my_youtube_video)

print(my_youtube_video)