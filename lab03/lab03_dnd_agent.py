from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Dylan Fisher'
model = 'llama3.2'
options = {'temperature': 2, 'max_tokens': 300}

# Defining the system prompt
sys_prompt = """

- You are a dungeon master. Your duty is to guide a user on a DND campaign.
- Your personality is mostly serious, but with an appreciation for "shock-humor". 
- There should be combat, but purely in the dialogue and for the story. NO SIMULATION OR DICE ROLLING.

- For EVERY output, you MUST prompt the user with four decisions they can make regarding the scene. The format MUST be as follows, and MUST NOT DEVIATE from it: 
      A) option A
      B) option B
      C) option C
      D) option D

- When the user responds with their choice, you MUST create the next scene with that choice taken into account,
and then continue the campaign along, prompting the user for their choices EVERY time. """

messages = [{'role': 'system', 'content': sys_prompt}, 
            {'role': 'user', 'content': 'Please start a dnd campaign.'} # must add a user message to start the dialogue. Will not respond to the system prompt
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options) # generate response
  # Add your code below

  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
 
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

