#!/usr/bin/env python3

import random
import time
from copy import deepcopy

import click
from prompt_toolkit import prompt
import requests
from colorama import Back, Fore, Style, init

init()

target_languages = ['zh', 'en', 'ja', 'fr', 'es', 'pt', 'it', 'de', 'ru', 'sv', 'ro', 'sk', 'nl', 'hu', 'el', 'da', 'fi', 'pl', 'cs']
source_languages = deepcopy(target_languages)
source_languages.append('auto')

@click.command()
@click.argument("text", nargs=-1)
@click.option("--source-language", "-s", show_default=True, default="auto", help="Source language", type=click.Choice(source_languages))
@click.option("--target-language", "-t", show_default=True, default="zh", help="Target language", type=click.Choice(target_languages))

# Default is to translate to Chinese. If no source language is specified, it will autodetect the source language.
def deepl_translate(text, source_language, target_language): 
    # text is a tuple, so we need to join it
    text = " ".join(text)
    if len(text) == 0:
      text = 'hello'
    print(f"{source_language} --> {target_language}: {text}\n")
    
    params = {
      "jsonrpc": "2.0",
      "method": "LMT_handle_jobs",
      "params": {
            "jobs": [
              {
                  "kind": "default",
                  "sentences": [
                    {
                        "text": text,
                        "id": 0,
                        "prefix": ""
                    }
                  ],
                  "raw_en_context_before": [],
                  "raw_en_context_after": [],
                  "preferred_num_beams": 4
              }
            ],
            "lang": {
              "preference": {
                  "weight": {},
                  "default": "default"
              },
              "source_lang_computed": source_language,
              "target_lang": target_language
            },
            "priority": -1,
            "commonJobParams": {
              "browserType": 1,
              "formality": None
            },
            "timestamp": int(time.time() * 10000)
        },
      "id": random.randint(1, 100000000)
    }
    # print("params:" + params)

    # Sometimes the request fails because the same IP is requested too many times, so we can try to use a proxy.
    # proxies = { "http":"http://127.0.0.1:6152", "https": "http://127.0.0.1:6152", } 
    response = requests.post('https://www2.deepl.com/jsonrpc',
                      json=params,  # use json type means set the header 'content-type' to 'application/json'
                      # proxies=proxies  # uncomment this line to use a proxy
                      ).json()
    
    if 'error' in response:
        # error: {'code': 1042912, 'message': 'Too many requests'}
        print(Fore.RED +"error:", response['error']) 
        return   
        
    # print("result:", result)
    beams = response['result']['translations'][0]['beams']
    translations = []
    
    for i, beam in enumerate(beams):
        translation = beam['sentences'][0]['text']
        if i == 0:
            print(Fore.GREEN + Style.BRIGHT + translation + '\n')
        else:
            print(Fore.YELLOW + Style.DIM + translation)
        translations.append(translation)
     
    print(Style.RESET_ALL)

    detected_source_language = response['result']['source_lang']
    if detected_source_language != source_language:
        print("Detected source language:", Fore.CYAN + detected_source_language)
        
    return translations

  
if __name__ == '__main__':    
    deepl_translate()


#==================================== Test ==================================== 
"""
python3 deepL.py good

python3 deepL.py 优雅 -s en

python3 deepL.py heel

python3 deepL.py heel -s en -t zh

python3 deepL.py My heart is slightly larger than the whole universe.

#error
python3 deepL.py 优雅 -t ff
"""

#==================================== Params ==================================== 
"""
{
  "jsonrpc": "2.0",
  "method": "LMT_handle_jobs",
  "params": {
    "jobs": [
      {
        "kind": "default",
        "sentences": [
          {
            "text": "good",
            "id": 0,
            "prefix": ""
          }
        ],
        "raw_en_context_before": [],
        "raw_en_context_after": [],
        "preferred_num_beams": 4
      }
    ],
    "lang": {
      "preference": {
        "weight": {},
        "default": "default"
      },
      "source_lang_computed": "EN",
      "target_lang": "ZH"
    },
    "priority": -1,
    "commonJobParams": {
      "browserType": 1,
      "formality": null
    },
    "timestamp": 1657606963196
  },
  "id": 11000045
}
"""

#==================================== Result ==================================== 
"""
{
  "jsonrpc": "2.0",
  "id": 23856610,
  "result": {
    "translations": [
      {
        "beams": [
          { "sentences": [{ "text": "很好", "ids": [0] }], "num_symbols": 4 },
          { "sentences": [{ "text": "不错", "ids": [0] }], "num_symbols": 3 },
          { "sentences": [{ "text": "好", "ids": [0] }], "num_symbols": 3 },
          { "sentences": [{ "text": "好的", "ids": [0] }], "num_symbols": 4 }
        ],
        "quality": "normal"
      }
    ],
    "target_lang": "ZH",
    "source_lang": "EN",
    "source_lang_is_confident": "False",
    "detectedLanguages": {}
  }
}
"""
