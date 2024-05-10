from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS  # new import
import json
from openai import OpenAI
client = OpenAI()
  


app = Flask(__name__)
CORS(app)  # enable CORS
limiter = Limiter(app=app, key_func=get_remote_address)

@app.route('/generate', methods=['POST'])
@limiter.limit("10/minute")  # adjust as needed
def generate():
    prompt = request.json['prompt']
    print(prompt)
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt
    )
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id="asst_4SmbBUSMKbKPImAq3UBkhOlg",
    instructions="You are an assistant that has the job to enhance and improve chat GPT prompts that are sent to you. You should identify the main idea of the prompt and elaborate on it. Create detailed yet concise prompts. They should be at most 4 sentences. Do not respond with anything besides revised prompt."
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        
        resp = messages.data[0].content[0].text.value
        print(f"Response: {resp}")
        datas = {
        "prompt": resp
        }
        return datas, 200
    else:
        print(run.status)

if __name__ == "__main__":
    app.run(debug=True)
