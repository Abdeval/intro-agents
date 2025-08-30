import asyncio
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from retriever import guest_info_tool
from llama_index.core.workflow import Context
from tools import *


# todo: the model
# Initialize the Hugging Face model
llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")

# ? Create Alfred, our gala agent, with the guest info tool
alfred = AgentWorkflow.from_tools_or_functions(
    [guest_info_tool, search_tool, weather_info_tool, hub_stats_tool],
    llm=llm,
)

# ! remembering state by using context 

# Remembering state
ctx = Context(alfred)


async def main():
    # ! examples

    query = "Tell me about Lady Ada Lovelace. What's her background?"
    response = await alfred.run(query)

    print("🎩 Alfred's Response:")
    print(response.response.blocks[0].text)

# todo: Run the async function
asyncio.run(main())
