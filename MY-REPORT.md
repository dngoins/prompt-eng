![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)


* Authors: [Dwight Goins](http://www.github.com/dngoins) 
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

# Use an LLM to Choose the LLM for a task or best prompt to execute

With the diverse LLMs in existence today, it is difficult to choose the best LLM for a task. This project aims to use an LLM to choose the best LLM for a task or the best prompt to execute.


## Overall Goal

Most LLMs have a one-line description to explain the overall scope of their function. LLMs also have descriptions with examples on how to best use the LLM from a native speaking language.

We should be able to use an LLM that will be trained to select the best LLM based on the description, speed, and knowledge base of the LLM. The LLM will also generate a prompt for the selected LLM to execute the task.

### Hypothesis: There exists a way to use an LLM to choose the best LLM for a task or the best prompt to execute.

# Research Question 

Is there a way to use an LLM to choose the best LLM for a task or the best prompt to execute?

## Arguments

* prompt
* system_instructions
* model
* format_response

#### What is already known about this topic

* There are models that already contain descriptions and examples on how to use the LLM.
* You could ask an LLM to see specific examples about a model or its description.
* The challenges of asking an LLM to choose the best LLM for a task or the best prompt to execute include the possibility that some registered models don't have descriptions or examples, nor do they accurately describe the model.
* The possibility of finding the best LLM for a task or the best prompt to execute is that there may be a way to use an LLM to choose the best LLM for a task or the best prompt to execute.

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->
* We assume a properly registered model describes its behavior and accurately provides examples on how to use the LLM.
* With this assumption in mind, we employ a dynamic approach to choose the best LLM for a task or the best prompt to execute.
* We query the description and example and dynamically use the prompt template approach to generate a prompt for the selected LLM to execute the task.
* We are building an Agent that will be trained to select the best LLM based on the description, speed, and knowledge base of the LLM. The Agent will also generate a prompt for the selected LLM to execute the task.
* We are exploring the idea of a general-purpose LLM that can be used to choose the best LLM for a task or the best prompt to execute.

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* If the assumption holds true, then we can use an LLM to choose the best LLM for a task or the best prompt to execute.
* It will be easier to prompt and execute tasks with the best LLM for the task.
By accomplishing the aforementioned, we can optimize an orchestration for choosing LLMs for a task or the best prompt to execute.
* This will allow us to better understand various LLMs and their capabilities and limitations.


# Research Method

## Data Collection

Ollama has a /docs endpoint that provides a list of all the models and their descriptions and examples. We will use this endpoint to collect the data for the models and their descriptions and examples.

Different models have different descriptions and examples on how to use the LLM. We will use the descriptions and examples to train the Agent to select the best LLM for a task or the best prompt to execute.

The challenge is that not all the properties of a model are populated with data. For example, the parameter size is not populated for all models.

When we do have data, we use the English worded description to send to the phi4:latest model to help us select which model to use based on the list of models loaded in Ollama.

The assumption is the public model is trained on information about each loaded model's public description and example set. We ask the model to select the best model for a task based on the description and examples of the models and provide an explanation of why the model was selected.

# Results

The process starts with determining which models are loaded and available in Ollama. A simple API call to the Ollama servers determines the list of models available. The list of models is then used to determine which model to use for the task. 

A prompt is created for the model of choice to ask it to select from the downloaded list of models. The prompt asks the model to selects the best model based on the description and examples of the models, and best fit. The prompt alsl asks the model of choice to provide an explanation or reason of why the model was selected.

Below is the full output of the process:

**********
Ollama Registered Parameter Size BestModel:
mistral-large:latest
*******

Choose Model Prompt: You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: ['Llama-3.2-3B-Instruct', 'Llama-3.2-11B-Vision-Instruct', 'tinyllama:latest', 'codestral:latest', 'llava:latest', 'phi4:latest', 'gemma2:27b', 'qwen2:latest', 'mistral-large:latest']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.
Can you help me write a C++ application that uses Ollama to invoke the phi3 LLM? Please try to use the LlamaCPP library as well.
Only return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}


Payload:

{'model': 'phi4:latest', 'messages': [{'role': 'user', 'content': 'You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: [\'Llama-3.2-3B-Instruct\', \'Llama-3.2-11B-Vision-Instruct\', \'tinyllama:latest\', \'codestral:latest\', \'llava:latest\', \'phi4:latest\', \'gemma2:27b\', \'qwen2:latest\', \'mistral-large:latest\']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.\nCan you help me write a C++ application that uses Ollama to invoke the phi3 LLM? Please try to use the LlamaCPP library as well.\nOnly return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}


phi4:latest Selected Time taken: 12.791s

```json
{
  "model": "phi4:latest",
  "prompt": "Please provide instructions for writing a C++ application that utilizes Ollama to invoke the phi3 LLM. The implementation should integrate the LlamaCPP library for communication and demonstrate proper setup, initialization, and usage of the language model. Include sample code snippets and explanations where necessary.",
  "reason": "phi4:latest is selected due to its balance between parameter size and performance capabilities. With a large number of parameters like GPT-3 models, it excels in generating high-quality text outputs while maintaining reasonable inference speeds. Although 'mistral-large:latest' has the largest parameter size among the options listed, phi4:latest offers a strong compromise with efficient speed and robust understanding required for complex tasks such as programming-related prompts. It is particularly well-suited to applications requiring advanced language comprehension and generation in software development contexts."
}
```

phi4:latest Selected Model: phi4:latest

Prompt: Please provide instructions for writing a C++ application that utilizes Ollama to invoke the phi3 LLM. The implementation should integrate the LlamaCPP library for communication and demonstrate proper setup, initialization, and usage of the language model. Include sample code snippets and explanations where necessary.

Reason: phi4:latest is selected due to its balance between parameter size and performance capabilities. With a large number of parameters like GPT-3 models, it excels in generating high-quality text outputs while maintaining reasonable inference speeds. Although 'mistral-large:latest' has the largest parameter size among the options listed, phi4:latest offers a strong compromise with efficient speed and robust understanding required for complex tasks such as programming-related prompts. It is particularly well-suited to applications requiring advanced language comprehension and generation in software development contexts.

Payload:

{'model': 'phi4:latest', 'messages': [{'role': 'user', 'content': 'Please provide instructions for writing a C++ application that utilizes Ollama to invoke the phi3 LLM. The implementation should integrate the LlamaCPP library for communication and demonstrate proper setup, initialization, and usage of the language model. Include sample code snippets and explanations where necessary.'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}

********

Final Response:

Creating a C++ application using Ollama with the `phi3` Large Language Model (LLM) involves several steps including setting up your development environment, integrating LlamaCPP, initializing the Ollama model, and then making requests to the language model. Below is a step-by-step guide along with code snippets to help you through this process.

### Prerequisites

1. **Install C++ Development Tools:** Ensure you have a C++ compiler installed (like `g++` or `clang`). On Linux, these tools are typically available via package managers (`sudo apt install build-essential` for Debian-based systems).

2. **Get LlamaCPP Library:** Download and set up the LlamaCPP library which will facilitate communication with Ollama.

3. **Ollama Model Setup:** Ensure you have access to the `phi3` model through Ollama and it's correctly configured on your machine.

### Step-by-Step Guide

#### 1. Setting Up Your Project

Create a new directory for your project:

```bash
mkdir my_llm_app
cd my_llm_app
```

#### 2. Initialize CMake Project

Create a `CMakeLists.txt` file to manage the build process:

```cmake
cmake_minimum_required(VERSION 3.10)
project(LLMApp)

set(CMAKE_CXX_STANDARD 17)

# Add include directories for LlamaCPP
include_directories(${LLAMA_CPP_INCLUDE_DIR})

add_executable(llm_app main.cpp)

# Link against LlamaCPP and any necessary libraries
target_link_libraries(llm_app PRIVATE ${LLAMA_CPP_LIBRARIES})
```

Replace `${LLAMA_CPP_INCLUDE_DIR}` and `${LLAMA_CPP_LIBRARIES}` with the actual paths for your LlamaCPP installation.

#### 3. Writing the Application

Create a `main.cpp` file:

```cpp
#include <iostream>
#include "llamacpp/llamacpp.hpp" // Adjust path if necessary

int main() {
    try {
        std::string model_path = "/path/to/phi3/model"; // Set your Ollama phi3 model path
        lla::ModelOptions options;
        options.vocab_file = model_path + "/vocab.json";
        options.merge_file = model_path + "/merge.txt";
        options.scorer_file = model_path + "/scorer.bin";

        auto model = std::make_shared<lla::LLM>(options);

        // Prepare input
        lla::Prompt prompt;
        prompt.set_input("Hello, I am a language model. How can I assist you today?");
        
        // Generate response
        auto results = model->generate(prompt);

        // Print out the generated text
        for (const auto& token : results.tokens) {
            std::cout << token.value << " ";
        }
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```

#### 4. Building the Application

Make sure you have CMake installed:

```bash
cmake -S . -B build
cmake --build build
```

This will generate an executable in the `build` directory.

### Explanation of Code Snippets

- **Model Initialization:** We create a `ModelOptions` object to specify paths for essential model files (`vocab.json`, `merge.txt`, and `scorer.bin`). These are necessary for loading the LLM into memory.
  
- **Prompt Setup:** A prompt is created with input text. This demonstrates how you would interact with the language model.

- **Generation:** We call the `generate` method on our model object, which takes a prompt and returns generated tokens (the output from the model).

- **Error Handling:** Basic exception handling captures any errors that occur during the process, providing a useful error message to help diagnose issues.

### Additional Considerations

- **Model Path Configuration:** Ensure that you correctly point to where your `phi3` Ollama model files are stored on disk.
  
- **Dependencies Management:** If LlamaCPP or other dependencies require additional libraries, ensure they're linked in the CMake file.

- **Platform Specifics:** Paths and library linking might differ slightly across platforms (Windows, macOS vs Linux).

By following these steps, you should have a basic yet functional application that integrates Ollama's `phi3` LLM with LlamaCPP to generate text responses. Adjust paths and configurations as needed based on your setup.
********

Total Time taken: 43.802s


# Further research

We could further research the following:
    
* Utilize different prompting styles to select a diffent model and measure it's speed and accuracy.

# Code References - Examples
    
    ```bash
         PS C:\Users\dngoi\source\repos\github\dngoins\prompt-eng> python .\prompt-eng\_pipeline.py "help me with building a flying car" > Results.txt
    ``` 
    