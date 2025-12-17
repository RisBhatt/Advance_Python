from openai import OpenAI

# Create client (API key is read from environment variable)
client = OpenAI()

print("ChatGPT AI — type 'exit' to quit\n")

while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    print("AI:", answer)

    # Performed in Google Colab