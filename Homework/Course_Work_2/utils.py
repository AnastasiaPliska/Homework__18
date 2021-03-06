import json
import pprint


def get_posts():
    with open("data/data.json", "r", encoding="utf-8") as fp:
        posts = json.load(fp)
    return posts


def get_comments():
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    return comments


def get_posts_with_comments_count():

    posts = get_posts()
    comments = get_comments()

    comments_count = {}

    for comment in comments:
        post_id = comment["post_id"]

        if post_id in comments_count:
            comments_count[post_id] += 1
        else:
            comments_count[post_id] = 1
    print(comments_count)

    for index, post in enumerate(posts):
        pk = post["pk"]
        if pk in comments_count:
            posts[index]["comments_count"] = comments_count[pk]
        else:
            posts[index]["comments_count"] = 0

    return posts


def get_post_by_pk(post_pk):
    posts = get_posts()
    for post in posts:
        if post["pk"] == post_pk:
            post["content"] = replace_hashtags_with_links(post["content"])
            return post
    return None


def get_comments_by_pk(post_pk):
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    post_comments = []
    for comment in comments:
        if comment["post_id"] == post_pk:
            post_comments.append(comment)
    return post_comments


def replace_hashtags_with_links(content):
    words = content.split(" ")
    for index, word in enumerate(words):
        if word.startswith("#"):
            tag = word[1:]
            words[index] = f"<a href='/tags/{{ tag }}'>{word}</a>"
    return " ".join(words)


def get_post_by_word(search_word):
    posts = get_posts_with_comments_count()
    detected_posts = []
    for post in posts:
        if search_word:
            if search_word.lower() in post["content"].lower():
                detected_posts.append(post)
        else:
            detected_posts = posts
    return detected_posts


def get_posts_by_user(username):
    posts = get_posts_with_comments_count()
    user_posts = []
    for post in posts:
        if post["poster_name"] == username:
            user_posts.append(post)
    return user_posts






