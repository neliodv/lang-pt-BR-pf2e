import json
import sys
import deepdiff

def comparar_arquivos_json(arquivo1, arquivo2):
  """
  Compara dois arquivos JSON e marca os itens novos e modificados no segundo arquivo com um asterisco (*) na primeira coluna.

  Argumentos:
    arquivo1: Caminho para o primeiro arquivo JSON.
    arquivo2: Caminho para o segundo arquivo JSON.

  Retorno:
    None.
  """

  # Lê os dados JSON dos dois arquivos
  with open(arquivo1, "r") as f1:
    dados1 = json.load(f1)
  with open(arquivo2, "r") as f2:
    dados2 = json.load(f2)

  # Compara os dados usando DeepDiff
  diferencas = deepdiff.DeepDiff(dados1, dados2, ignore_order=True)

  # Itera pelas diferenças e marca os itens novos e modificados no segundo arquivo
  modificado = False
  for key, diff in diferencas.items():
    if diff["type"] in ("added", "modified"):
      modificado = True
      path = diff["path"]
      # Converte o caminho para uma string com formatação JSON
      path_str = ".".join(str(item) for item in path)
      # Adiciona o asterisco (*) ao início da string
      dados2[path_str] = "* " + str(dados2[path_str])

  # Se o segundo arquivo foi modificado, grava o conteúdo atualizado
  if modificado:
    with open(arquivo2, "w") as f2:
      json.dump(dados2, f2, indent=2)

# Exemplo de uso
comparar_arquivos_json("..\\translation\\en\\compendium\\classes.json", "..\\translation\\en\\compendium\\classescopy.json")
