import pal.pal
from pal.pal.prompt import math_prompts

interface = pal.pal.interface.ProgramInterface(
  model='gpt-5.4',
  stop='\n\n\n', # stop generation str for Codex API
  get_answer_expr='solution()' # python expression evaluated after generated code to obtain answer 
)

question = 'Vicy ate 7 apples. Before she had 10. How many apples does she have now?'
prompt = math_prompts.MATH_PROMPT.format(question=question)
answer = interface.run(prompt)

print(answer)
# Output is 3