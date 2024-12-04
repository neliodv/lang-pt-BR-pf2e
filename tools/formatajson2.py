import json
import sys

actors = [
    'blog-bestiary.json'                   ,
    'pathfinder-bestiary-2.json'           ,
    'pathfinder-bestiary-3.json'           ,
    'pathfinder-bestiary.json'             ,
    'pathfinder-monster-core.json'
]

compendium = [
    'abomination-vaults-bestiary.json'     ,
    'action-macros.json'                   ,
    'actions.json'                         ,
    'adventure-specific-actions.json'      ,
    'age-of-ashes-bestiary.json'           ,
    'agents-of-edgewatch-bestiary.json'    ,
    'ancestries.json'                      ,
    'ancestryfeatures.json'                ,
    'backgrounds.json'                     ,
    'bestiary-ability-glossary-srd.json'   , 
    'bestiary-effects.json'                , 
    'bestiary-family-ability-glossary.json',
    'book-of-the-dead-bestiary.json'       , 
    'boons-and-curses.json'                , 
    'campaign-effects.json'                , 
    'classes.json'                         , 
    'classfeatures.json'                   , 
    'conditions.json'                      , 
    'criticaldeck.json'                    ,
    'crown-of-the-kobold-king-bestiary.json', 
    'deities.json'                         , 
    'equipment-effects.json'               , 
    'equipment.json'                       ,
    'extinction-curse-bestiary.json'       , 
    'fall-of-plaguestone.json'             ,
    'familiar-abilities.json'              , 
    'feat-effects.json'                    , 
    'feats.json'                           ,
    'fists-of-the-ruby-phoenix-bestiary.json',
    'gatewalkers-bestiary.json'             ,
    'hazards.json'                         ,
    'heritages.json'                       ,
    'highhelm-bestiary.json'               ,
    'howl-of-the-wild-bestiary.json'       , 
    'iconics.json'                         ,
    'impossible-lands-bestiary.json'       , 
    'journals.json'                        ,
    'kingmaker-bestiary.json'              , 
    'kingmaker-features.json'              ,
    'macros.json'                          ,
    'malevolence-bestiary.json'            , 
    'menace-under-otari-bestiary.json'     ,
    'monsters-of-myth-bestiary.json'       ,
    'mwangi-expanse-bestiary.json'         ,
    'night-of-the-gray-death-bestiary.json',
    'npc-gallery.json'                     ,
    'other-effects.json'                   ,
    'outlaws-of-alkenstar-bestiary.json'   ,
    'paizo-pregens.json'                   ,
    'pathfinder-dark-archive.json'         ,
    'quest-for-the-frozen-flame-bestiary.json',
    'rage-of-elements-bestiary.json'       , 
    'rollable-tables.json'                 , 
    'rusthenge-bestiary.json'              ,
    'season-of-ghosts-bestiary.json'       , 
    'seven-dooms-for-sandpoint-bestiary.json',
    'shadows-at-sundown-bestiary.json'     ,
    'sky-kings-tomb-bestiary.json'         ,
    'spell-effects.json'                   , 
    'spells.json'                          ,
    'strength-of-thousands-bestiary.json'  ,
    'the-enmity-cycle-bestiary.json'       ,
    'the-slithering-bestiary.json'         ,
    'travel-guide-bestiary.json'           ,
    'troubles-in-otari-bestiary.json'      , 
    'vehicles.json'                        
    ]

def merge_dicts(dict1, dict2):
    """
    Recursively merge two dictionaries.

    If a key exists in both dictionaries, the value from dict2 is used.
    """
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
    """
    Merge the contents of two JSON files.

    Any keys in file1 that also exist in file2 will have their values
    overwritten with the corresponding values from file2.
    """
    print(file1_path + ' => ' + file2_path)  

    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        dict1 = json.load(file1)
        dict2 = json.load(file2)
        merge_dicts(dict1, dict2)

    with open(file2_path, 'w', encoding='utf-8') as outfile:
        json.dump(dict1, outfile, indent=2, ensure_ascii=False)

if len(sys.argv) == 1:
    # Percorre a matriz actors e apresenta cada coluna lado a lado
    for ingles in actors:
        portugues = 'pf2e.'+ingles    
        original  = '..\\translation\\en\\actors\\'+ingles
        traduzido = '..\\translation\\pt-BR\\actors\\'+portugues
        merge_json_files(original, traduzido)
    # Percorre a matriz compendium e apresenta cada coluna lado a lado
    for ingles in compendium:
        portugues = 'pf2e.'+ingles    
        if ingles == 'actions.json':
            portugues = 'pf2e.actionspf2e.json'
        if ingles == 'conditions.json':
            portugues = 'pf2e.conditionitems.json'
        if ingles == 'equipment.json':
            portugues = 'pf2e.equipment-srd.json'
        if ingles == 'feats.json':
            portugues = 'pf2e.feats-srd.json'
        if ingles == 'macros.json':
            portugues = 'pf2e.pf2e-macros.json'
        if ingles == 'spells.json':
            portugues = 'pf2e.spells-srd.json'
        original  = '..\\translation\\en\\compendium\\'+ingles
        traduzido = '..\\translation\\pt-BR\\compendium\\'+portugues
        merge_json_files(original, traduzido)
    merge_json_files('..\\translation\\en\\action-en.json','..\\translation\\pt-BR\\action-pt-BR.json')
    merge_json_files('..\\translation\\en\\dictionary.json','..\\translation\\pt-BR\\dictionary.json')
    merge_json_files('..\\translation\\en\\en.json','..\\translation\\pt-BR\\pt-BR.json')
    merge_json_files('..\\translation\\en\\re-en.json','..\\translation\\pt-BR\\re-pt-BR.json')
    merge_json_files('..\\translation\\en\\kingmaker-en.json','..\\translation\\pt-BR\\kingmaker-pt-BR.json')
    sys.exit(0)

# Verifica se foram informados os dois arquivos JSON como parâmetros de linha de comando
#if len(sys.argv) < 2:
#    print("Informe o nome dos dois arquivos JSON como parâmetros de linha de comando")
#    sys.exit(1)


# Lê os dois arquivos JSON informados como parâmetros de linha de comando
if len(sys.argv) >= 2:
    original  = sys.argv[1]
    traduzido = sys.argv[2]
    merge_json_files(original, traduzido)


#sorted_data = json.dumps(data, ensure_ascii=False, indent=2)

# Salva o resultado em outro arquivo JSON com codificação UTF-8
#with open('resultado.json', 'w', encoding='utf-8') as f:
 #   f.write(sorted_data)


