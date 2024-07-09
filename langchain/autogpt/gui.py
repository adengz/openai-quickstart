import sys

import faiss
import gradio as gr
from langchain.agents import Tool
from langchain_community.tools.file_management.read import ReadFileTool
from langchain_community.tools.file_management.write import WriteFileTool
from langchain_community.utilities import SerpAPIWrapper
from langchain.docstore import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_experimental.autonomous_agents import AutoGPT


class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        self.terminal.flush()
        self.log.flush()
        
    def isatty(self):
        return False
    

def read_logs():
    sys.stdout.flush()
    with open("output.log", "r") as f:
        return f.read()


def initiate_agent() -> AutoGPT:
    search = SerpAPIWrapper()
    tools = [
        Tool(
            name="search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        WriteFileTool(),
        ReadFileTool(),
    ]

    embeddings_model = OpenAIEmbeddings()

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

    agent = AutoGPT.from_llm_and_tools(
        ai_name="Tom",
        ai_role="Assistant",
        tools=tools,
        llm=ChatOpenAI(temperature=0),
        memory=vectorstore.as_retriever(),
    )
    agent.chain.verbose = True
    return agent


if __name__ == '__main__':
    sys.stdout = Logger("output.log")
    agent = initiate_agent()

    with gr.Blocks() as demo:
        with gr.Row():
            input = gr.Textbox(label='Assign me a goal')
            output = gr.Textbox(label='')
        btn = gr.Button("Run")
        btn.click(lambda q: agent.run([q]), input, output)
        
        logs = gr.Textbox(label='Log')
        demo.load(read_logs, None, logs, every=1)

    demo.queue().launch()
