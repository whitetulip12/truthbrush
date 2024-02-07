import truthbrush
import os

tb = truthbrush.Api(username=os.environ["USERNAME"], password=os.environ["PASSWORD"])

response = tb.search(searchtype="statuses", query="the", limit=40)

count = 1

for r in response:
    posts = r['statuses']
    sorted_list = sorted(posts, key=lambda x: x['created_at'])
    for post in sorted_list:
        print(f"{count}: {post['id']}")
        count = count+1
