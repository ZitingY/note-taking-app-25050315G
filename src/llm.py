# import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv() # Loads environment variables from .env
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

# A function to call an LLM model and return the response
def call_llm_model(model, messages, temperature=1.0, top_p=1.0):
    client = OpenAI(base_url=endpoint,api_key=token)
    response = client.chat.completions.create(
        messages=messages,
        temperature=temperature, top_p=top_p, model=model)
    return response.choices[0].message.content

# A function to translate text using the LLM model
def translate(text, target_language):
    prompt = f"Translate the following text to {target_language}: \n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    return call_llm_model(model, messages)

system_prompt = '''

today's date and time: {current_date_time}
Extract the user's notes into the following structured fields:
1. Title: A concise title of the notes less than 5 words
2. Notes: The notes based on user input written in full sentences. If the input includes items to bring, list all items as a bullet or numbered list, and comlete specific items based on the scenario.
3. Tags: A list of keywords or tags that categorize the content of the notes (at most 3).
4. Event Date: The date of the event, if mentioned (format: YYYY-MM-DD)
5. Event Time: The time of the event, if mentioned (format: HH:MM)
Output in JSON format without ```json. Output title and notes in the language: {lang}.
Example:
Input: "Badminton tmr 5pm @polyu. Bring racket, shoes, water."
Output:
{{
 "Title": "Badminton at PolyU",
 "Notes": "Remember to play badminton at 5pm tomorrow at PolyU. Items to bring:\n1. Racket\n2. Shoes\n3. Water",
 "Tags": ["badminton", "sports"],
 "Event Date": "2024-06-21",
 "Event Time": "17:00"
}}
'''


from datetime import datetime
# A function to extract structured notes using the LLM model
def extract_notes(text, lang="English"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt = system_prompt.format(lang=lang, current_date_time=now) + f"\n\nInput: \"{text}\""
    messages = [
        {"role": "system", "content": system_prompt.format(lang=lang, current_date_time=now)},
        {"role": "user", "content": prompt}
    ]
    response = call_llm_model(model, messages)
    return response

# main function
if __name__ == "__main__":
    # test the extract notes feature
    text = "Badminton tmr 5pm @polyu"
    print("Extracting Structured Notes:")
    print(extract_notes(text, lang="Chinese"))
