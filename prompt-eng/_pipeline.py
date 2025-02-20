import requests
import json
import os
import time
import argparse

def list_models():
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_BASE', None)
    api_key = os.getenv('API_KEY', None)
    
    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    # Send out request to Model Provider
    try:
        response = requests.get(f'{url}/api/models', headers=headers)
        models = response.json()
        models = models["data"]
        # the models json looks like this: 
                
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    # Checking the response and extracting the 'response' field
    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:
        return models
   
def extractParameterSize(parameter_size):
    if parameter_size.endswith("M"):
        return float(parameter_size[:-1])
    elif parameter_size.endswith("B"):
        return float(parameter_size[:-1]) * 1000


def evaluate_models(models):
    best_model = None
    best_score = float('-inf')
    
    for model in models:
        description = model['info']['meta']['description']
        
        examples = model['info']['meta']['suggestion_prompts']
        # Example evaluation logic: prioritize models with higher parameter count
        if 'ollama' in model:
            score = extractParameterSize(model['ollama']['details']['parameter_size'])
        else:
            score = 0
       
        if score > best_score:
            best_score = score
            best_model = model
    
    return best_model


def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    # Find CONFIG
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Load CONFIG
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

def create_payload(model, prompt, target="ollama", **kwargs):
    """
    @NOTE: 
    Need to adjust here to support multiple target formats
    target can be only ('ollama-local', 'ollama-remote' or 'open-webui')
    """
    payload = None
    if target == "ollama" or target == "ollama-local" or target == "ollama-remote":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}

    elif target == "open-webui-remote":
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }

        payload.update({key: value for key, value in kwargs.items()})
    
    else:
        print(f'!!ERROR!! Unknown target: {target}')
    return payload

def model_req(payload=None):
    """
    COMPLETE
    """
        
    # CUT-SHORT Condition
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    print(f'Payload:\n{payload}')
    # Send out request to Model Provider
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    # Checking the response and extracting the 'response' field
    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:

        ## @NOTE: Need to adjust here to support multiple response formats
        result = ""
        delta = round(delta, 3)

        response_json = response.json()
        if 'response' in response_json: ## ollama
            result = response_json['response']
        elif 'choices' in response_json: ## open-webui
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return delta, result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the model pipeline")
    parser.add_argument("prompt", type=str, default="", nargs='?', help="The prompt to be used")
    parser.add_argument("--target", choices=["ollama-local", "ollama-remote", "open-webui-remote"], default="open-webui-remote", nargs='?', help="The target to be used")
    parser.add_argument("--model", type=str, default="phi4:latest", nargs='?', help="The model name to be used")
    parser.add_argument("--system_instructions", type=str, default="", nargs='?', help="The system message or instructions to be used")
    parser.add_argument("--format_response", type=str, default="", nargs='?', help="Tells the agent how to format the response")
    parser.add_argument("--logging", type=bool, default=False, nargs='?', help="writes out logs for the process steps")
    args = parser.parse_args()

    from _pipeline import create_payload, model_req
    _PROMPT = args.prompt
    TARGET = args.target
    MODEL = args.model
    
    TEMPLATE_BEFORE = args.system_instructions
    TEMPLATE_AFTER = args.format_response
    LOGGING = args.logging
    
    models =   list_models()
    # if LOGGING: print(models)

    model_names = [model['name'] for model in models]
    
    MODEL = evaluate_models(models)
    MODEL = MODEL['name']
    if LOGGING: print(f'BestModel: {MODEL}')

    # If TEMPLATE_BEFORE is empty or blank then use the following prompt:
    # 'You are an agent that searches for LLMs and selects the best LLM based on its description, speed, and knowledge  base. You also creates LLM prompts for the selected LLM'
    if not TEMPLATE_BEFORE:
        TEMPLATE_BEFORE = f'You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: {model_names}. Based on the parameter size, {MODEL} is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.'    
        TEMPLATE_AFTER = 'Only return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}'

    PROMPT = TEMPLATE_BEFORE + '\n' + _PROMPT + '\n' + TEMPLATE_AFTER
    if LOGGING: print(f'Prompt: {PROMPT}')

    payload = create_payload(
                         target=TARGET,   
                         model="phi4:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

    time, response = model_req(payload=payload)
    if time: print(f'{MODEL} Selection Time taken: {time}s')
    if LOGGING: print(response);
    
    # first remove the 'json' prefix from the response
    response = response.replace('json', '')

    # now remove the ``` from the response
    response = response.replace('```', '')  


    # extract the Model name from the Json formatted response. The response looks like this 'json{"model": "LLM Name", "prompt": "LLM Prompt"}'
    if response:
        try:
            json_response = json.loads(response)
            MODEL = json_response['model']
            PROMPT = json_response['prompt']
            REASON = json_response['reason']
            
            # if MODEL doesn't have : in it then add :latest to it
            #if ':' not in MODEL:
            #    MODEL = MODEL + ':latest'
        
            if LOGGING:
                print(f"Model: {MODEL}")
                print(f"Prompt: {PROMPT}")
                print(f"Reason: {REASON}")
           
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response content: {response}")
        

    real_payload = create_payload( target = TARGET,
                         model=MODEL, 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

    real_time, real_response = model_req(payload=real_payload)

    print(real_response)
    if real_time: print(f'Total Time taken: {real_time + time}s')