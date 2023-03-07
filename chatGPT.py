def chat_and_output():
    import openai
    import speech
    with open('./output.txt', 'r+', encoding='UTF-8') as fp:
        text = fp.read()
    openai.api_key = ""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    result = completion.choices[0].message['content']
    print(f"{result}")
    speech.say(result)
