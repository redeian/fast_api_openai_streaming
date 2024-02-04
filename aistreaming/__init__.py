from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from openai import OpenAI
from pydantic import BaseModel
import os

# Initialize FastAPI app
app = FastAPI()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class RequestData(BaseModel):
  api_key: str
  messages: list


@app.post("/chat/")
async def generate_text(request_data: RequestData):
  try:
    # Check if the API key is valid
    if request_data.api_key != os.environ["APP_KEY"]:
      raise HTTPException(status_code=401, detail="Invalid API key")

    messages = request_data.messages

    stream = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      stream=True,
    )

    # Generate a generator that yields the response text
    def generate():
      for chunk in stream:
        if chunk.choices[0].delta.content is not None:
          # print(chunk.choices[0].delta.content, end="")
          yield chunk.choices[0].delta.content

    return StreamingResponse(generate(), media_type="text/event-stream")

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)
