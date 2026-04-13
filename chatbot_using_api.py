from groq import Groq

client = Groq(api_key = "PUT YOUR API KEY HERE !!")

conversation_history = []

print("HI SIR, I'M AN AI CHATBOT MADE BY SONU SIR.\n")

while True:
    user_input = input("YOU :")
    
    if user_input.lower() == "quit":
        print("THANKS FOR COMING !!")
        break

    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = conversation_history
    )
    
    reply = response.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    print(f"Bot: {reply}\n")