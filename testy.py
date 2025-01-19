from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);


if __name__ == '__main__':
    print ("test file")
    print(completion.choices[0].message);