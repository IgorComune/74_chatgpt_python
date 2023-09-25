import openai
import dotenv
import os

dotenv.load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

resposta = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            'role' : 'system',
            'content' : 'Gere nomes de produtos fictícios sem descricaão de acordo com a requisição do usuário'
        },
        {
            'role' : 'user',
            'content' : 'Gere 5 produtos'
        }
    ]
)

print(resposta)