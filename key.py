import praw

reddit = praw.Reddit(
    client_id="ybQFldEE-LNa4btBHppbLQ",
    client_secret="oouoOFDC03knAJbRRvBhojpAjuKFKw",
    password="fak3account",
    user_agent="testscript by u/fakebot3",
    username="inazumaelevn",
)

print(reddit.user.me())