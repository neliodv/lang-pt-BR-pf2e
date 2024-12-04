import os
import google.generativeai as genai
import json

def traduzir_texto(texto):
  """Traduz um texto para o idioma especificado.

  Args:
    texto: O texto a ser traduzido.
    idioma_alvo: O idioma para o qual traduzir.

  Returns:
    A tradução do texto.
  """

  prompt = f"""Traduza para o português do Brasil o texto a seguir, seguindo estas regras:
* **Manter o formato original:** Se o texto tiver negrito, itálico, etc., mantenha na tradução.
* **Linguagem formal:** Utilize linguagem formal na tradução.
* **Manter as palavras-chave em inglês:** "name", "description", "source" e "target" devem permanecer em inglês.
* **Traduzir o conteúdo das chaves:** Traduza o texto dentro de cada chave, incluindo a chave "name".
* **Usar espaços em vez de tabulações:** Formate o JSON com espaços em vez de tabulações.:

  {texto}"""

  modelo = genai.GenerativeModel("gemini-pro")
  resposta = modelo.generate_content(prompt)
  return resposta._result

def traduzir_json(nome_arquivo):
  """
  Lê um arquivo JSON e traduz o conteúdo usando a função "traduzir".

  Args:
    nome_arquivo: O nome do arquivo JSON a ser lido.
    idioma_destino: O idioma para o qual traduzir.
  """
  try:
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
      dados = json.load(f)

    def traduzir_recursivamente(obj):
      if isinstance(obj, dict):
        return {k: traduzir_recursivamente(v) for k, v in obj.items()}
      elif isinstance(obj, list):
        return [traduzir_recursivamente(item) for item in obj]
      elif isinstance(obj, str):
        print(obj)
        print(traduzir_texto(obj))
        print("<*>")
        return obj #traduzir_texto(obj, idioma_alvo)
      else:
        return obj

    dados_traduzidos = traduzir_recursivamente(dados)

    with open('traducao.json', 'w', encoding='utf-8') as f:
      json.dump(dados_traduzidos, f, indent=4, ensure_ascii=False)

  except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
  except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo JSON '{nome_arquivo}'.")

  #print(dados_traduzidos)


os.environ['GOOGLE_API_KEY'] = '' 
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
idioma_alvo = "Português Brasil"

#traduzir_json('..\\translation\\en\\compendium\\conditions.json')
traduzir_json('teste.json')

# Exemplo de uso
# texto_original = "The book is on the table."
#traducao = traduzir_texto(texto_original, idioma_alvo)
#print(traducao)