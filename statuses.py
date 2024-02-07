import truthbrush
import os
import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = fastapi.FastAPI()

tb = truthbrush.Api(
    username=os.environ["USERNAME"], password=os.environ["PASSWORD"])

count = 1

queries: ["Donald Trump", "the", "cricket", "election", "is", "Drake", "Toby",
          "Jose", "court", "for", "today", "U.S", "United", "america", "breaking"]

@app.get("/ping")
def ping():
    return JSONResponse(status_code=200, content=jsonable_encoder({"message": f"Woke up service"}), media_type="application/json")

@app.get("/run")
def start_brush():
    global count
    for query in queries:
        response = tb.search(searchtype="statuses", query=query, limit=40)
        for r in response:
            posts = r['statuses']
            sorted_list = sorted(posts, key=lambda x: x['created_at'])
            if len(sorted_list) == 0:
                break
            for post in sorted_list:
                print(f"{count}: {post['id']}")
                count = count+1
