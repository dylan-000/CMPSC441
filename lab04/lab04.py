from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

lab04_params = {
    'template_file':'lab04/lab04_trader_chat.json',
    'sign': 'Dylan Fisher', 
    'end_regex': r'TRADE(.*)DONE'
    }

if __name__ ==  '__main__':
    trader_template_file = 'lab04/lab04_trader_chat.json'
    run_console_chat(template_file = trader_template_file, 
                     inventory = "['Apple', 'Banana', 'Great Sword']",
                     sign = 'Dylan Fisher',
                     end_regex=r'TRADE(.*)DONE')
    pass