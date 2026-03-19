from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

print("🤖 Chatbot VISTORÉ - Restaurant Le Marrakchi")
print("Tapez 'quit' pour quitter\n")

messages = [
    {"role": "system", "content": """Tu es l'assistant virtuel du restaurant Le Marrakchi à Casablanca. 
    Tu réponds aux questions des clients sur :
    - Le menu : Tajine poulet (85 DH), Couscous royal (120 DH), Pastilla (95 DH), Thé à la menthe (15 DH)
    - Les horaires : Ouvert tous les jours de 12h à 23h
    - Les réservations : Par téléphone au 05 22 XX XX XX
    - L'adresse : Boulevard Zerktouni, Casablanca
    Réponds toujours en français, de manière chaleureuse et professionnelle."""}
]

while True:
    user_input = input("Vous : ")
    if user_input.lower() == "quit":
        print("Au revoir !")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Assistant : {reply}\n")