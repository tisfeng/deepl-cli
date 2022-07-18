import random
import time

import click
import requests


# Use click to define the command line interface.
@click.command()
@click.argument("text")
@click.option("--source_language", default="auto", help="Source language")
@click.option("--target_language", default="ZH", help="Target language")
def deepLTranslate(text, source_language, target_language):    
    print(f"{source_language} --> {target_language}: {text}")
    print()
    
    text = '"' + text + '"'
    source_language = '"' + source_language + '"'
    target_language = '"' + target_language + '"'

    data = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","sentences":[{"text": ' + text + ', "id": 0, "prefix": ""}],"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4}],"lang":{"preference":{"weight": {},"default": "default"},"source_lang_computed":' + source_language + ',"target_lang":' + target_language + '},"priority":1,"commonJobParams":{ "browserType": 1, "formality": null },"timestamp":' + str(
        int(time.time() * 10000)) + '},"id":' + str(
            random.randint(1, 100000000)) + '}'
    # print("data:" + data)

    result = requests.post('https://www2.deepl.com/jsonrpc',
                      headers={'content-type': 'application/json'},
                      data=data.encode()).json()
    
    if 'error' in result:
        print("error:", result.json()['error'])
        return   
    
    
    # print("result:", result)
    beams = result['result']['translations'][0]['beams']
    translations = []    
    for beam in beams:
        translation = beam['sentences'][0]['text']
        print(translation)
        translations.append(translation)
        
    return translations

  
if __name__ == '__main__':    
    deepLTranslate()


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
