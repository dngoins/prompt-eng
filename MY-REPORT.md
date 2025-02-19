![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Use an LLM to Choose the LLM for a task or best prompt to execute

1-liner description of your project

# With the adverse LLM in existence today, it is difficult to choose the best LLM for a task. This project aims to use an LLM to choose the best LLM for a task or the best prompt to execute.


## Overall Goal:

### Most LLMs will have a 1 line description to explain the overall scope of it function. LLMs also have a description with examples on how to best use the LLM from a native speaking language.

### We should be able to use an LLM that will be trained to select the best LLM based on the description, speed, and knowledge base of the LLM. The LLM will also generate a prompt for the selected LLM to execute the task.

### Hypothesis: There exists a way to use an LLM to choose the best LLM for a task or the best prompt to execute.

  
* Authors: [Dwight Goins](http://www.github.com/dngoins) 
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

  
# Research Question 

Is there a way to use an LLM to choose the best LLM for a task or the best prompt to execute?

## Arguments

prompt
system_instructions
model
format_response

#### What is already known about this topic

* there are models that already contain descriptions and examples on how to use the LLM
* you could do ask an LLM to see specific examples about a model or it's description
* the challenges of asking an LLM to choose the best LLM for a task or the best prompt to execute is that there may be some registered models that don't have descriptions or examples, nor do they accurately descibe the model.
* the possibility of finding the best LLM for a task or the best prompt to execute is that there may be a way to use an LLM to choose the best LLM for a task or the best prompt to execute.


#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

* we assume a properly registered model describes its behavior and accurate provides examples on how to use the LLM.
* with this assumption in minde we employ a dynamic approach to choose the best LLM for a task or the best prompt to execute. 
* We query the description and example and dynamically use the prompt template approach to generate a prompt for the selected LLM to execute the task.
* we are building an Agent that will be trained to select the best LLM based on the description, speed, and knowledge base of the LLM. The Agent will also generate a prompt for the selected LLM to execute the task.
* we are exploring the idea of a general purpose LLM that can be used to choose the best LLM for a task or the best prompt to

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* if the assumption holds true, then we can use an LLM to choose the best LLM for a task or the best prompt to execute.
* it will be easier to prompt and execute tasks with the best LLM for the task.
* By accomplishing the aforementioned, we can optimize an orchestration for choosing LLMs for a task or the best prompt to execute.
* This will allow us to better understand various LLMs and their capabilities and limitations.
* ...

# Research Method

Describe how you are building this research process.

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

Describe the results achieved through your research process.

# Further research

Describe what we could do next and propose new ideas for further research.


# Code References - Examples
    
    ```bash
         output=$(python _pipeline.py "Generate a prompt for phi LLM which can provide step by step instructions on how to create scented candles" --system_instructions 'You are an agent that creates LLM prompts' --model 'tinyllama:latest' --format_response 'Only return the prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE PROMPT!'); python _pipeline.py "$output" --model "phi4:latest"
    
          output=$(python _pipeline.py "Select the best LLM and Generate a prompt for the selected LLM to answer questions on physics" --system_instructions 'You are an agent that searches for LLMs and selects the best LLM based on its description, speed, and knowledge  base. You also creates LLM prompts for the selected LLM' --format_response 'Only return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT!');
    
    ``` 
    