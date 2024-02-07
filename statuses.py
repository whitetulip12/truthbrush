import truthbrush
import os
import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = fastapi.FastAPI()

tb = truthbrush.Api(
    username=os.environ["USERNAME"], password=os.environ["PASSWORD"])

count = 1


@app.get("/")
def start_brush():
    global count
    JSONResponse(status_code=200, content=jsonable_encoder({"message": f"Truthsocial extraction started"}), media_type="application/json")
    response = tb.search(searchtype="statuses", query="the", limit=40)
    for r in response:
        posts = r['statuses']
        sorted_list = sorted(posts, key=lambda x: x['created_at'])
        for post in sorted_list:
            print(f"{count}: {post['id']}")
            count = count+1
