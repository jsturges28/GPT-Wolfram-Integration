# Chat-GPT and Wolfram Alpha as a single, but distinct LLM

## Table of Contents
+ [About](#about)
+ [Prerequisites](#prerequisites)
+ [Usage](#usage)
+ [Authors](#authors)

## About <a name = "about"></a>

This program is a first attempt at making use of merging ChatGPT and Wolfram Alpha through the use of the LangChain Python library. The program makes use of "agents," which are entities that are powered by an LLM (such as ChatGPT) and given a list of rules to follow in order to choose which model to use (in this case, referencing itself (ChatGPT) or Wolfram Alpha to answer a question.

## Prerequisites <a name = "prerequisites"></a>

Ensure you have **openai**, **wolframalpha**, and **langchain** installed.

```
pip install langchain
pip install openai
pip install wolframalpha
```

You also need to obtain your personal API keys from OpenAI and Wolfram Alpha. The following links should will let you create and account and register for these keys:

[Link to OpenAI Registration](https://openai.com/api/)
[Link to Wolfram Alpha Registration](https://openai.com/api/](https://account.wolfram.com/login/create)

Register for a Wolfram Alpha App ID to obtain a key:

[Wolfram Alpha App ID](https://developer.wolframalpha.com/portal/myapps/)

## Usage <a name = "usage"></a>

If you want to run through your terminal, you must provide the following arguments:
  - **--ask**: The question to ask the program. 
  - **--openai_key**: Your personal OpenAI API key string you must provide. 
  - **--wolfram_key**: Your personal Wolfram Alpha App ID key string you must provide.

**Example:**
```
python RSS-scraper.py --ask "How deep is the Mariana Trench?" --openai_key "some_key_string" --wolfram_key "some_key_string" 
```

## Authors <a name = "authors"></a>

- [@jsturges28](https://github.com/jsturges28) 