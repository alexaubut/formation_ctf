from fastapi import FastAPI
import re
from fastapi import FastAPI
from pydantic import BaseModel

flag = "666c61677b52656745785f31355f337a7a7a7a7d"
app = FastAPI()

class Poem(BaseModel):
    poem: str

#uvicorn web:app --reload pour exécuter le server
@app.post("/")
async def challenge1(input: Poem):
    if re.match('^[a-zA-Z0-9_]+$', input.poem, re.MULTILINE):
        if not input.poem.isalnum():
            return bytes.fromhex(flag)
    return None