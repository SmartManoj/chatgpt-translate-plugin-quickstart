# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def talk(msg):
    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "user", "content": msg}
    ],
    temperature=1,
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    print(talk('If there are 10 books in a room and I read 2, how many books are still in the room?'))