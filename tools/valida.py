import json
import os
import sys
import copy

EN_PATH = '..\\translation\\en\\'
EN_TEMP_PATH = '..\\translation\\en-temp\\'
ACTORS_EN_PATH = '..\\translation\\en\\actors\\'
ACTORS_EN_TEMP_PATH = '..\\translation\\en-temp\\actors\\'
COMPENDIUM_EN_PATH = '..\\translation\\en\\compendium\\'
COMPENDIUM_EN_TEMP_PATH = '..\\translation\\en-temp\\compendium\\'

def merge_dicts(dict1, dict2):
    """Mescla dois dicionários recursivamente, priorizando os valores de dict2."""
    """Marca conteúdos diferentes com <*> no início"""
    for key, value in dict1.items():
        if key in dict2:
            if isinstance(value, dict) and isinstance(dict2[key], dict):
                merge_dicts(value, dict2[key])
            else:
                if dict1[key] != dict2[key]:
                    if type(dict1[key]) == str: 
                        dict1[key] = '<*>'+dict1[key]

def merge_json_files(file1_path, file2_path):
    """Mescla o conteúdo de dois arquivos JSON."""
    print(file1_path + ' => ' + file2_path)
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            dict1 = json.load(file1)
            dict2 = json.load(file2)
            dicttemp = copy.deepcopy(dict1)
            merge_dicts(dict1, dict2)

        with open(file2_path, 'w', encoding='utf-8') as outfile:
            json.dump(dicttemp, outfile, indent=2, ensure_ascii=False)
        with open(file1_path, 'w', encoding='utf-8') as outfile:
            json.dump(dict1, outfile, indent=2, ensure_ascii=False)
    except (FileNotFoundError, JSONDecodeError) as e:
        print(f"Erro ao processar os arquivos: {e}")

def process_folder(folder_path, folder_temp_path):
    """Processa todos os arquivos JSON em uma pasta."""
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            original = os.path.join(folder_path, filename)
            # Define o caminho do arquivo traduzido (adapte conforme necessário)
            traduzido = os.path.join(folder_temp_path, filename)  
            merge_json_files(original, traduzido)

process_folder(EN_PATH, EN_TEMP_PATH)
process_folder(ACTORS_EN_PATH, ACTORS_EN_TEMP_PATH)
process_folder(COMPENDIUM_EN_PATH, COMPENDIUM_EN_TEMP_PATH)

sys.exit(0)

