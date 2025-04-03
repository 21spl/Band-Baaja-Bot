import yaml
import os
from smolagents import GradioUI, CodeAgent, LiteLLMModel

# Get current directory path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from tools.web_search import DuckDuckGoSearchTool as WebSearch
from tools.find_best_catering_service import SimpleTool as FindBestCateringService
from tools.suggest_menu import SimpleTool as SuggestMenu
from tools.visit_webpage import VisitWebpageTool as VisitWebpage
from tools.final_answer import FinalAnswerTool as FinalAnswer



model = LiteLLMModel(
max_tokens=8192,
model_id='gemini/gemini-2.0-flash',
api_base=None,
)

web_search = WebSearch()
find_best_catering_service = FindBestCateringService()
suggest_menu = SuggestMenu()
visit_webpage = VisitWebpage()
final_answer = FinalAnswer()


with open(os.path.join(CURRENT_DIR, "prompts.yaml"), 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[web_search, find_best_catering_service, suggest_menu, visit_webpage],
    managed_agents=[],
    max_steps=10,
    verbosity_level=2,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    executor_type='local',
    executor_kwargs={},
    max_print_outputs_length=None,
    prompt_templates=prompt_templates
)




import gradio as gr

import gradio as gr

def agent_response(user_input):
    return agent.run(user_input)

with gr.Blocks() as demo:
    gr.Markdown("# 🎩 Band Baaja Bot - Your Wedding Assistant! 💍")
    
    user_input = gr.Textbox(label="Your Request", placeholder="Ask me anything about wedding planning...")  
    submit = gr.Button("Submit")  # Submit button below the input box  
    output = gr.Textbox(label="Agent Response")  # Output space below the button  

    submit.click(agent_response, inputs=user_input, outputs=output)

demo.launch()
