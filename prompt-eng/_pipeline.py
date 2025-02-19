import requests
import json
import os
import time
import argparse

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
    args = parser.parse_args()

    from _pipeline import create_payload, model_req
    _PROMPT = args.prompt
    TARGET = args.target
    MODEL = args.model
    
    TEMPLATE_BEFORE = args.system_instructions
    TEMPLATE_AFTER = args.format_response
    
    PROMPT = TEMPLATE_BEFORE + '\n' + _PROMPT + '\n' + TEMPLATE_AFTER

    payload = create_payload(
                         target=TARGET,   
                         model=MODEL, 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

    time, response = model_req(payload=payload)
    print(response)
    if time: print(f'Time taken: {time}s')