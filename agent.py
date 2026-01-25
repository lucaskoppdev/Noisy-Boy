#Fazer Conexao com a API do GROQ

from groq import Groq
from dotenv import load_dotenv
import os



load_dotenv() #Carrega o arquivo .env

#Chave da API do agente, contida no arquivo .env
agent_api_key = os.getenv("GROQ_API_KEY")


#faz a conexao com o client
client = Groq(api_key=agent_api_key)



#Funcao inicial pra testar se a API ta funcionando



def chat_with_ai():
    pergunta_user = input('Digite a sua pergunta ->:')
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "Voce e um assistente de IA legal e simpatico"
            },

            {
                "role": "user",
                "content": pergunta_user,
            }

        ],
        #modelo a ser usado
        model = "llama-3.1-8b-instant",

        #temperatura do modelo (0.7, valor medio padrao) - depois passar isso aqui como variavel
        temperature = 0.7, #nao faco ideia do porque, mas precisa dessa virgula
    )

    return chat_completion.choices[0].message.content

