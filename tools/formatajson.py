import json
import os
import sys

EN_PATH = '..\\translation\\en\\'
PTBR_PATH = '..\\translation\\pt-BR\\'
ACTORS_EN_PATH = '..\\translation\\en\\actors\\'
ACTORS_PTBR_PATH = '..\\translation\\pt-BR\\actors\\'
COMPENDIUM_EN_PATH = '..\\translation\\en\\compendium\\'
COMPENDIUM_PTBR_PATH = '..\\translation\\pt-BR\\compendium\\'

def merge_dicts(dict1, dict2):
    for key, value in dict1.items():
        if (key in dict2) and (key != 'source'):
            if isinstance(value, dict) and isinstance(dict2[key], dict):
                merge_dicts(value, dict2[key])
            else:
                if isinstance(value, str) and value.startswith("<*>"):
                    dict1[key] = dict1[key]  #.replace('<*>','')
                else:
                    dict1[key] = dict2[key]
        else:
            if (key in dict2) and isinstance(value, str) and (key == 'source'):
                dict1[key] = dict1[key].replace('<*>','')

def merge_json_files(file1_path, file2_path):
    """Mescla o conteúdo de dois arquivos JSON."""
    print(file1_path + ' => ' + file2_path)  
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            dict1 = json.load(file1)
            dict2 = json.load(file2)
            merge_dicts(dict1, dict2)

        with open(file2_path, 'w', encoding='utf-8') as outfile:
            json.dump(dict1, outfile, indent=2, ensure_ascii=False)
    except (FileNotFoundError, JSONDecodeError) as e:
        print(f"Erro ao processar os arquivos: {e}")

def process_folder(folder_en_path, folder_ptBR_path):
    """Processa todos os arquivos JSON em uma pasta."""
    for filename in os.listdir(folder_en_path):
        if filename.endswith(".json"):
            portugues = 'pf2e.'+filename    
            if filename == 'actions.json':
                portugues = 'pf2e.actionspf2e.json'
            if filename == 'conditions.json':
                portugues = 'pf2e.conditionitems.json'
            if filename == 'equipment.json':
                portugues = 'pf2e.equipment-srd.json'
            if filename == 'feats.json':
                portugues = 'pf2e.feats-srd.json'
            if filename == 'macros.json':
                portugues = 'pf2e.pf2e-macros.json'
            if filename == 'spells.json':
                portugues = 'pf2e.spells-srd.json'
            if filename == 'action-en.json':
                portugues = 'action-pt-BR.json'
            if filename == 'dictionary.json':
                portugues = 'dictionary.json'
            if filename == 'en.json':
                portugues = 'pt-BR.json'
            if filename == 're-en.json':
                portugues = 're-pt-BR.json'
            if filename == 'kingmaker-en.json':
                portugues = 'kingmaker-pt-BR.json'
            original = os.path.join(folder_en_path, filename)
            # Define o caminho do arquivo traduzido (adapte conforme necessário)
            traduzido = os.path.join(folder_ptBR_path, portugues)  
            merge_json_files(original, traduzido)

process_folder(EN_PATH, PTBR_PATH)
process_folder(ACTORS_EN_PATH, ACTORS_PTBR_PATH)
process_folder(COMPENDIUM_EN_PATH, COMPENDIUM_PTBR_PATH)
sys.exit(0)



