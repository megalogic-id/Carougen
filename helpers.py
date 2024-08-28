import os
from dotenv import load_dotenv
from flask import Response

load_dotenv()


from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(prompt):
    promptText = """
    Buatkan sebuah materi untuk konten Instagram yang singkat tentang {}
    dalam format Markdown
    Berikan juga caption di akhir dengan 20 hashtags
    """.format(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": promptText}
        ]
    )
    
    return response.choices[0].message.content

def sendMessage(prompt):
    promptText = """
    Buatkan sebuah materi untuk konten Instagram yang singkat tentang {}
    dalam format Markdown
    Berikan juga caption di akhir dengan 20 hashtags
    """.format(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": promptText}
        ],
        stream=True
    )
    return response

def generatedChunk(messages):
    def event_stream():
        for line in sendMessage(messages[0]["content"]):
            print(line)
            text = line.choices[0].delta.content
            if(text != None):
                yield text

    return Response(event_stream(), mimetype='text/event-stream')