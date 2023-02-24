import os
import langchain
import argparse
from langchain.llms import OpenAI
from langchain.agents import load_tools, load_agent, initialize_agent

def create_parser():
    '''
    Creates an argument parser for the program to run in command line.
    '''

    parser = argparse.ArgumentParser(description='ChatGPT/WolframAlpha Engine')

    requiredNamed = parser.add_argument_group('Required named arguments')

    parser.add_argument('--ask', type=str, help='Question to ask engine', required=True)
    #parser.add_argument('--openai_key', type=str, help='API key for OpenAI', required=True)
    #parser.add_argument('--wolfram_key', type=str, help='API key for WolframAlpha', required=True)

    return parser 

parser = create_parser()
args = parser.parse_args()

# set environment variables to access openAI and wolframalpha APIs

#os.environ["OPENAI_API_KEY"] = args.openai_key
#os.environ["WOLFRAM_ALPHA_APPID"] = args.wolfram_key

tool_names = ['wolfram-alpha']

llm = OpenAI(temperature=0.5)

tools = load_tools(tool_names)

agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

agent.run(args.ask)
#agent.run("What is the asthenosphere?")
#text = "What would be a good company name a company that makes colorful socks?"
#print(llm(text))