from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from getMongoDB import get_database

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    # allows cross origin requests from specific origins (domains) to access your server's resources.
    CORSMiddleware,
    allow_origins=["*"],  # list of allowed (above)
    allow_credentials=True,  # authorization, cookies, etc
    allow_methods=["*"],  # specific http methods etc
    allow_headers=["*"],  # http headers
)

if app:
    hydb = get_database()


# handles get requests that go to path '/'
@app.get('/')
# when using libraries that want you to await define them as async
async def root():
    return {"message": "Hello world"}


@app.get('/bets/{bet_id}')
async def bet_info(bet_id):
    return {"bet_info": bet_id}


@app.get('/user/me')
async def user_info():
    return {"userinfo": ["userstuff"]}


@app.get('/bets/')
async def bets_info() -> list[dict]:
    coll = hydb['bets']
    items = coll.find()
    bets = [{**bet, "_id": str(bet["_id"])} for bet in items]
    return bets
