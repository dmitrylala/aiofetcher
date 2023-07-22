import asyncio
from typing import List

import aiohttp


async def fetch_url(url: str, session: aiohttp.ClientSession) -> dict:
    try:
        async with session.get(url=url) as response:
            return await response.json()
    except Exception:
        return {}


async def fetch_async(urls: List[str], **session_kwargs) -> List[dict]:
    async with aiohttp.ClientSession(**session_kwargs) as session:
        return await asyncio.gather(*[fetch_url(url, session) for url in urls])


def fetch(urls: List[str], **session_kwargs) -> List[dict]:
    return asyncio.run(fetch_async(urls, **session_kwargs))
