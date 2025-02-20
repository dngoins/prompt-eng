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

* We assume a properly registered model describes its behavior and accurately provides examples on how to use the LLM.
* With this assumption in minde we employ a dynamic approach to choose the best LLM for a task or the best prompt to execute. 
* We query the description and example and dynamically use the prompt template approach to generate a prompt for the selected LLM to execute the task.
* We are building an Agent that will be trained to select the best LLM based on the description, speed, and knowledge base of the LLM. The Agent will also generate a prompt for the selected LLM to execute the task.
* We are exploring the idea of a general purpose LLM that can be used to choose the best LLM for a task or the best prompt to

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* If the assumption holds true, then we can use an LLM to choose the best LLM for a task or the best prompt to execute.
* It will be easier to prompt and execute tasks with the best LLM for the task.
* By accomplishing the aforementioned, we can optimize an orchestration for choosing LLMs for a task or the best prompt to execute.
* This will allow us to better understand various LLMs and their capabilities and limitations.
* ...

# Research Method

## Data Collection
Ollama has a /docs endpoint that provides a list of all the models and their descriptions and examples. We will use this endpoint to collect the data for the models and their descriptions and examples.

Different models have different descriptions and examples on how to use the LLM. We will use the descriptions and examples to train the Agent to select the best LLM for a task or the best prompt to execute.

The challenge is that not all the properties of a Model are populated with data. For example, the parameter size is not populated for all models.

When we do have data, we use the english worded description to send to the phi4:latest model to help us select which model to use based on the list of models loaded in Ollama.

The assumption is the public model is trained on information about each loaded model public description and example set. We ask the model to select the best model for a task based on the description and examples of the models and provide an explanation of why the model was selected.

# Results

Describe the results achieved through your research process.
    ```bash
        PS C:\Users\dngoi\source\repos\github\dngoins\prompt-eng> python .\prompt-eng\_pipeline.py "help me with building a flying car" --logging=True > Results.txt
    BestModel: mistral-large:latest
    Prompt: You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: ['Llama-3.2-3B-Instruct', 'Llama-3.2-11B-Vision-Instruct', 'tinyllama:latest', 'llava:latest', 'codestral:latest', 'phi4:latest', 'gemma2:27b', 'qwen2:latest', 'mistral-large:latest']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.
    help me with building a flying car
    Only return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}
    Payload:
    {'model': 'phi4:latest', 'messages': [{'role': 'user', 'content': 'You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: [\'Llama-3.2-3B-Instruct\', \'Llama-3.2-11B-Vision-Instruct\', \'tinyllama:latest\', \'llava:latest\', \'codestral:latest\', \'phi4:latest\', \'gemma2:27b\', \'qwen2:latest\', \'mistral-large:latest\']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.\nhelp me with building a flying car\nOnly return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}
    mistral-large:latest Selection Time taken: 9.791s
    ```json
    {
    "model": "Llama-3.2-11B-Vision-Instruct",
    "prompt": "Explore innovative designs and technological advancements required for building a flying car, focusing on aerodynamics, propulsion systems, safety features, and regulatory challenges.",
    "reason": "The Llama-3.2-11B-Vision-Instruct model is selected because it integrates vision capabilities alongside its instruct-based framework, which can be advantageous in understanding and generating content related to designs and visual technology aspects of a flying car. Its 11 billion parameters offer substantial comprehension and generation abilities without being as computationally demanding as larger models like mistral-large:latest. This makes Llama-3.2-11B-Vision-Instruct a well-balanced choice, particularly for tasks that might benefit from visual understanding and detailed technical discussion."
    }
    ```
    Model: Llama-3.2-11B-Vision-Instruct
    Prompt: Explore innovative designs and technological advancements required for building a flying car, focusing on aerodynamics, propulsion systems, safety features, and regulatory challenges.
    Reason: The Llama-3.2-11B-Vision-Instruct model is selected because it integrates vision capabilities alongside its instruct-based framework, which can be advantageous in understanding and generating content related to designs and visual technology aspects of a flying car. Its 11 billion parameters offer substantial comprehension and generation abilities without being as computationally demanding as larger models like mistral-large:latest. This makes Llama-3.2-11B-Vision-Instruct a well-balanced choice, particularly for tasks that might benefit from visual understanding and detailed technical discussion.
    Payload:
    {'model': 'Llama-3.2-11B-Vision-Instruct', 'messages': [{'role': 'user', 'content': 'Explore innovative designs and technological advancements required for building a flying car, focusing on aerodynamics, propulsion systems, safety features, and regulatory challenges.'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}
    !!ERROR!! HTTP Response=400, {"detail":"Model not found"}      
    Total Time taken: 8.791s
    PS C:\Users\dngoi\source\repos\github\dngoins\prompt-eng>      
    *  History restored                                      python .\prompt-eng\_pipeline.py "help me with building a flying car" --logging=Truepos\github\dngoins\prompt-eng>
    BestModel: mistral-large:latest
    Prompt: You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: ['Llama-3.2-3B-Instruct', 'Llama-3.2-11B-Vision-Instruct', 'tinyllama:latest', 'codestral:latest', 'llava:latest', 'phi4:latest', 'qwen2:latest', 'gemma2:27b', 'mistral-large:latest']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.
    help me with building a flying car
    Only return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}
    Payload:
    {'model': 'phi4:latest', 'messages': [{'role': 'user', 'content': 'You are an agent that searches for LLMs and selects the best LLM based on its description, parameter size, speed, and knowledge base. Only select from the model names: [\'Llama-3.2-3B-Instruct\', \'Llama-3.2-11B-Vision-Instruct\', \'tinyllama:latest\', \'codestral:latest\', \'llava:latest\', \'phi4:latest\', \'qwen2:latest\', \'gemma2:27b\', \'mistral-large:latest\']. Based on the parameter size, mistral-large:latest is the best model, but choose another if its description better matches the prompt. As an agent, you also create LLM prompts for the selected LLM. When you select the LLM provide a detailed explanation of why you selected that LLM. Explain the strengths and weaknesses of the LLM and how it compares to other LLMs.\nhelp me with building a flying car\nOnly return the name of the LLM and corresponding prompt, nothing else, no metadata, no header, no comments, no dashes, ONLY THE LLM Name and PROMPT. Use the following format: {"model": "GPT-4:latest", "prompt": "LLM Prompt", "reason": "GPT uses a fast and efficient model that is able to generate text quickly and accurately on the most widely used topics dealing with science"}'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}
    mistral-large:latest Selection Time taken: 10.594s
    ```json
    {
    "model": "codestral:latest",
    "prompt": "Designing a flying car involves integrating elements of automotive engineering, aviation technology, and regulatory compliance. Consider key aspects such as propulsion systems, aerodynamics, lightweight materials, safety features, control mechanisms, energy efficiency, and certification processes for both road and air travel. What are the primary engineering challenges one must address to successfully create a functional flying car?",
    "reason": "Codestral:latest is designed with an emphasis on coding and technical tasks, which makes it particularly suited for tackling complex engineering projects such as building a flying car. While Mistral-large:latest might have a larger parameter size suggesting potentially broader general knowledge, Codestral's specialized focus on technology-related prompts allows it to more effectively address specific engineering challenges like propulsion systems and material considerations that are crucial in developing a functional flying car. This makes it better suited for this task compared to other models which may not be as tailored towards such technical depth."
    }
    ```
    Model: codestral:latest
    Prompt: Designing a flying car involves integrating elements of automotive engineering, aviation technology, and regulatory compliance. Consider key aspects such as propulsion systems, aerodynamics, lightweight materials, safety features, control mechanisms, energy efficiency, and certification processes for both road and air travel. What are the primary engineering challenges one must address to successfully create a functional flying car?
    Reason: Codestral:latest is designed with an emphasis on coding and technical tasks, which makes it particularly suited for tackling complex engineering projects such as building a flying car. While Mistral-large:latest might have a larger parameter size suggesting potentially broader general knowledge, Codestral's specialized focus on technology-related prompts allows it to more effectively address specific engineering challenges like propulsion systems and material considerations that are crucial in developing a functional flying car. This makes it better suited for this task compared to other models which may not be as tailored towards such technical depth.
    Payload:
    {'model': 'codestral:latest', 'messages': [{'role': 'user', 'content': 'Designing a flying car involves integrating elements of automotive engineering, aviation technology, and regulatory compliance. Consider key aspects such as propulsion systems, aerodynamics, lightweight materials, safety features, control mechanisms, energy efficiency, and certification processes for both road and air travel. What are the primary engineering challenges one must address to successfully create a functional flying car?'}], 'temperature': 1.0, 'num_ctx': 100, 'num_predict': 100}       
    1. **Propulsion Systems:** Flying cars would require both air and ground propulsion systems due to their dual-mode transportation functionality. This could include hybrid electric propeller drives, jet engines, or even solar-powered lifting technology. Developing efficient and safe propulsion systems is a significant challenge since traditional automobile engines produce too much noise for air travel, while conventional aircraft engines consume too much fuel for highway driving.

    2. **Aerodynamics:** Designing aerodynamically efficient vehicles requires addressing lift generation through wings or rotors to create upward thrust and minimize drag resistance during flight. Additionally, ground handling (steering, braking, cornering) might require unique techniques since standard automobile design principles may not apply in an aircraft-like configuration.

    3. **Lightweight Materials:** To increase energy efficiency, flying cars must be lightweight but durable. Fusing aluminum with carbon fiber composites or using new age light metals could help, but designing the structural integrity to handle both ground and aerial forces is an intricate task.

    4. **Safety Features:** Incorporating safety features like collision avoidance systems, parachutes, airbags, etc., would be critical for flying cars' success. However, ensuring these systems function seamlessly in both flight and driving modes might require sophisticated engineering solutions that can adapt to varying environments.

    5. **Control Mechanisms:** Developing control mechanisms compatible with both road and air travel is a significant challenge due to different physical environments. Implementing auto-landing technology for emergency situations could address this issue, but it also requires robust navigational systems.

    6. **Energy Efficiency:** Since battery or fuel capacity affects flight range and speed significantly, achieving high energy efficiency while maintaining enough power reserves is vital. This will require optimizing the use of energy storage solutions such as batteries, supercapacitors, or hydrogen fuel cells for long flights but also providing rapid recharging options when parked on the ground.

    7. **Certification Processes:** Complying with aviation regulations concerning flight safety, noise emissions, and airspace management is critical in creating a flying car. Furthermore, regulatory bodies must also consider the unique aspects of road and air transportation to develop certification standards suitable for such vehicles.

    8. **Pilotless Technology:** To allow for fully autonomous driving both on land and in the air, flying cars would require sophisticated artificial intelligence systems capable of recognizing and reacting to various scenarios present during aerial travel. Additionally, these AI solutions must conform to safety standards concerning passenger well-being while adhering to relevant regulations.

    9. **Legislative Framework:** Creating a legal framework for the safe and regulated operation of flying cars would require extensive cooperation between lawmakers, regulators, automotive engineers, aviation specialists, and consumers. Establishing rules for airspace management, pilot requirements, vehicle registration, insurance policies, etc., are all critical steps to ensure successful commercial adoption of flying cars.

    10. **Public Acceptance:** Convincing the public that flying cars are safe, practical, and desirable will be an essential element in their success. Developing a compelling business case for consumers while addressing concerns about affordability, noise pollution, infrastructure requirements, and overall environmental impact could help gain mass acceptance for this innovative mode of transportation.

    These engineering challenges require interdisciplinary collaboration and innovation, utilizing advanced research and development strategies to create functional flying cars that meet all necessary regulatory compliance standards while providing a superior user experience and addressing various socio-economic aspects related to its commercialization.
    Total Time taken: 38.018s
    ```

# Further research

We could further research the following:
    1. Utilize different prompting styles to select a diffent model and measure it's speed and accuracy.
    


# Code References - Examples
    
    ```bash
         PS C:\Users\dngoi\source\repos\github\dngoins\prompt-eng> python .\prompt-eng\_pipeline.py "help me with building a flying car" > Results.txt
    ``` 
    