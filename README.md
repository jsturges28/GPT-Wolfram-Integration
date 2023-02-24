# Chat-GPT and Wolfram Alpha as a single, but distinct LLM

## Table of Contents
+ [About](#about)
+ [Prerequisites](#prerequisites)
+ [Usage](#usage)
+ [Authors](#authors)

## About <a name = "about"></a>

This program is a first attempt at making use of merging ChatGPT and Wolfram Alpha through the use of the LangChain Python library. The program makes use of "agents," which are entities that are powered by an LLM (such as ChatGPT) and given a list of rules to follow in order to choose which model to use (in this case, referencing itself (ChatGPT)) or Wolfram Alpha to answer a question.

## Prerequisites <a name = "prerequisites"></a>

Ensure you have **openai**, **wolframalpha**, and **langchain** installed.

```
pip install langchain
pip install openai
pip install wolframalpha
```

You also need to obtain your personal API keys from OpenAI and Wolfram Alpha. The following links should will let you create and account and register for these keys:

[Link to OpenAI Registration](https://openai.com/api/)<br />
[Link to Wolfram Alpha Registration](https://account.wolfram.com/login/create)

Register for a Wolfram Alpha App ID to obtain a key:

[Wolfram Alpha App ID](https://developer.wolframalpha.com/portal/myapps/)

Once you have both of your API keys, you can set them as environmental variables on your system:

**Windows**:

1. Run the following in the cmd prompt, replacing <yourkey> with your API key:

```
setx OPENAI_API_KEY “<yourkey>”
```
  
2. This will apply to future cmd prompt window, so you will need to open a new one to use that variable with curl. You can validate that this variable has been set by opening a new cmd prompt window and typing in
  
```
echo %OPENAI_API_KEY%
```

**Mac/Linux**:

1. Run the following command in your terminal, replacing yourkey with your API key:

```
echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
```

2. Update the shell with the new variable:

```
source ~/.zshrc
```

3. Confirm that you have set your environment variable using the following command:

```
echo $OPENAI_API_KEY
```
  
To set up your Wolfram Alpha APP ID key, perform the exact same steps above, except replace "OPENAI_API_KEY" with "WOLFRAM_ALPHA_APPID".

If done properly, you don't have to specify --openai_key and --wolfram_key arguments every time you run the program. This will be automatically handled by the program.

## Usage <a name = "usage"></a>

If you want to run through your terminal, you must provide the following arguments:
  - **--ask**: The question to ask the program. 
  - **--openai_key**: Your personal OpenAI API key string you must provide. 
  - **--wolfram_key**: Your personal Wolfram Alpha App ID key string you must provide.

**Example:**
```
python run.py --ask "How deep is the Mariana Trench?" --openai_key "some_key_string" --wolfram_key "some_key_string" 
```

## Authors <a name = "authors"></a>

- [@jsturges28](https://github.com/jsturges28) 
