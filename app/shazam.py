import aiohttp
from shazamio import Shazam

class ShazamAPI:
    def __init__(self):
        self.shazam = Shazam()

    async def recognize_song(self, url: str):
        """ Audio faylini URL'dan olib, musiqani tanish """
        
        file_bytes = await ShazamAPI.read(url)
        song = await self.shazam.recognize(file_bytes)
        return song

    @staticmethod
    async def read(url: str) -> bytes:
        """ Urldagi faylni baytlarga o'tkazish """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()
