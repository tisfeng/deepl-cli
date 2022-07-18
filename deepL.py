import random
import sys
import time

import requests


def deepl_translator(translateText, sourceLanguage, targetLanguage):
    translateText = '"' + translateText + '"'
    sourceLanguage = '"' + sourceLanguage + '"'
    targetLanguage = '"' + targetLanguage + '"'
    data = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":' + translateText + ',"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4,"quality":"fast"}],"lang":{"user_preferred_langs":["EN","ZH"],"source_lang_computed":"auto","target_lang":"EN"},"priority":-1,"commonJobParams":{},"timestamp":' + str(int(time.time() * 10000)) + '},"id":' + str(random.randint(1, 100000000)) + '}'

    data = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","sentences":[{"text": ' + translateText + ', "id": 0, "prefix": ""}],"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4}],"lang":{"preference":{"weight": {},"default": "default"},"source_lang_computed":' + sourceLanguage + ',"target_lang":' + targetLanguage + '},"priority":1,"commonJobParams":{ "browserType": 1, "formality": null },"timestamp":' + str(
        int(time.time() * 10000)) + '},"id":' + str(
            random.randint(1, 100000000)) + '}'


    r = requests.post('https://www2.deepl.com/jsonrpc',
                      headers={'content-type': 'application/json'},
                      data=data.encode())
    # print("data:" + data)

    # print new line
    print()

    print(r.text)

    return r.json()['result']['translations']
    return r.json()['result']['translations'][0]['beams']

  
if __name__ == '__main__':
	# print(deepl_translator('摸鱼就开心'))

    # get params from deepl.py
    translateText = sys.argv[1]
    sourceLanguage = sys.argv[2] # EN
    targetLanguage = sys.argv[3] # ZH
    print(deepl_translator(translateText, sourceLanguage, targetLanguage))

# python3 deepl.py good EN ZH
# python3 deepl.py 开心 ZH EN