from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import json
import sys

# Carregar o modelo e o tokenizer
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name) 
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cpu")

def traduzir(english_text):
    # Frase em inglês para traduzir
    # english_text = "<p>Your synthetic body resists ailments better than those of purely biological organisms. You gain a +1 circumstance bonus to saving throws against diseases, poisons, and radiation.</p>"

    # Tokenizar a frase em inglês
    inputs = tokenizer(english_text, return_tensors="pt").to("cpu")

    # Obter o ID do token BOS para português
    por_bos_token_id = tokenizer.convert_tokens_to_ids("por_Latn")

    # Gerar a tradução, especificando o idioma de destino com decoder_input_ids
    translated_tokens = model.generate(**inputs, decoder_input_ids=torch.tensor([[por_bos_token_id]]).to("cpu"), max_length=1000)

    # Decodificar a tradução para português do Brasil
    portuguese_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

    print(portuguese_text)
    # Imprimir a tradução
    return portuguese_text  # Output: Olá, como vai?


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
        return traduzir(obj)
      else:
        return obj

    dados_traduzidos = traduzir_recursivamente(dados)

    with open('traducao.json', 'w', encoding='utf-8') as f:
      json.dump(dados_traduzidos, f, indent=4, ensure_ascii=False)

  except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
  except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo JSON '{nome_arquivo}'.")

#traduzir_json('..\\translation\\en\\compendium\\conditions.json')
traduzir_json('teste.json')

