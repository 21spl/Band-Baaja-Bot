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

# Function to interact with the agent
def agent_response(prompt):
    response = agent.run(prompt)
    return response  # Gradio will handle Markdown rendering






# ✅ Define function BEFORE using it
def process_request(user_input):
    response = agent.run(user_input)
    return response

# Build UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🤖 AI Wedding Planner Agent")
    gr.Markdown("Ask the agent anything about wedding planning, catering, and more!")

    with gr.Row():
        user_input = gr.Textbox(label="Enter your request...", interactive=True)
        submit_button = gr.Button("Submit")

    output = gr.Markdown("")  # Output area

    submit_button.click(process_request, inputs=user_input, outputs=output)

# Launch UI
if __name__ == "__main__":
    demo.launch()