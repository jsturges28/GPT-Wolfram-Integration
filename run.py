import os
import langchain
import argparse
from langchain.llms import OpenAI
from langchain.agents import load_tools, load_agent, initialize_agent

# set environment variables to access openAI and wolframalpha APIs

os.environ["OPENAI_API_KEY"] = "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"
os.environ["WOLFRAM_ALPHA_APPID"] = "A36LWL-RRVWVG5UJU"

def create_parser():
    '''
    Creates an argument parser for the program to run in command line.
    '''

    parser = argparse.ArgumentParser(description='ChatGPT/WolframAlpha Engine')

    requiredNamed = parser.add_argument_group('Required named arguments')

    parser.add_argument('--ask', type=str, help='Question to ask engine', required=True)

parser = create_parser()
args = parser.parse_args()

tool_names = ['wolfram-alpha']

llm = OpenAI(temperature=0.5)

tools = load_tools(tool_names)

agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

agent.run(args.ask)
#agent.run("What is the asthenosphere?")
#text = "What would be a good company name a company that makes colorful socks?"
#print(llm(text))