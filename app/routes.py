import aiocache
import aiocache.serializers
from fastapi import APIRouter
from app.shazam import ShazamAPI

router = APIRouter()

@router.get("/recognize")
@aiocache.cached(
    ttl=100,
    cache=aiocache.Cache.REDIS,
    serializer=aiocache.serializers.JsonSerializer(),
    port=6379,
    namespace="shazam_api",
)
async def recognize_song(file: str):
    try:
        shazam_api = ShazamAPI()
        result = await shazam_api.recognize_song(file)
        return result
    except Exception as e:
        return {"message": str(e), "status_code": 500}