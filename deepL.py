#!/usr/bin/env python3

import json
import random
import time

import click
import requests
from colorama import Back, Fore, Style, init

init()

@click.command()
@click.argument("text")
@click.option("--source_language", default="auto", help="Source language")
@click.option("--target_language", default="ZH", help="Target language")
def deepl_translate(text, source_language, target_language):    
    print(f"{source_language} --> {target_language}: {text}\n")
    
    params = json.dumps({
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
    })
    # print("params:" + params)

    # Sometimes the request fails because the same IP is requested too many times, so we can try to use a proxy.
    proxies = { "http":"http://127.0.0.1:6152", "https": "http://127.0.0.1:6152", } 
    response = requests.post('https://www2.deepl.com/jsonrpc',
                      headers={'content-type': 'application/json'},
                      data=params,
                      proxies=proxies).json()
    
    if 'error' in response:
        # error: {'code': 1042912, 'message': 'Too many requests'}
        print("error:", response['error']) 
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
python3 deepL.py log  

python3 deepL.py 优雅 --target_language EN  

python3 deepL.py heel

python3 deepL.py heel --source_language EN --target_language ZH 

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
