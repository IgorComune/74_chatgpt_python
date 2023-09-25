import openai
import dotenv
import os

def categoriaProduto(nome_do_produto, categorias_validas):
    prompt_sistema = f"""
    você é um categorizador de produtos
    você deve escolher uma categoria da lista abaixo:
    Se as categorias informadas não forem categorias validas, responda com "Não posso ajuda-lo com isso"
    #### lista de categorias validas ####
    {categorias_validas}
    #### exemplo de saída #####
    bola de tênis
    Esporte
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt_sistema
            },
            {
                "role": "user",
                "content": nome_do_produto
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1
    )

    print(resposta.choices[0].message.content)

dotenv.load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

print('Digite as categorias validas')
categorias_validas = input()
while True:
    print('Digite o nome do produto: ')
    nome_do_produto = input()
    categoriaProduto(nome_do_produto=nome_do_produto, categorias_validas=categorias_validas)