from groq import Groq
from dotenv import load_dotenv
import os
from user_vectorizer_handler import main_function


load_dotenv() #Carrega o arquivo .env



agent_api_key = os.getenv("GROQ_API_KEY")



client = Groq(api_key=agent_api_key)




with open("ai_prompt.txt", "r") as file:
    prompt = file.read()



def chat_with_ai(ai_prompt, answer_to_refine):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": ai_prompt,
            },

            {
                "role": "user",
                "content": answer_to_refine,
            }

        ],
        #modelo a ser usado
        model = "llama-3.1-8b-instant",

        #temperatura do modelo (0.7, valor medio padrao) - depois passar isso aqui como variavel
        temperature = 0.7, 
    )

    return chat_completion.choices[0].message.content


#Loop Principal

while True:
    answer_output = main_function()

    output = chat_with_ai(prompt, answer_output)

    if output == 0:
        break
    
    print(f"RESPOSTA REFINADA PELA IA-> {output}")
