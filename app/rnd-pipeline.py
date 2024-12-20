#Pipeline

#This notebook goes over how to compose multiple prompts together. This can be useful when you want to reuse parts of prompts. This can be done with a PipelinePrompt. A PipelinePrompt consists of two main parts:
#   - Final prompt: The final prompt that is returned
#   - Pipeline prompts: A list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.

from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate


full_article_template = """
{title}

{intro}

{context}

{setup}

{guide}

{conclusion}
"""
full_prompt = PromptTemplate.from_template(full_article_template)


introduction_template = """You are a 100x python dev."""
introduction_prompt = PromptTemplate.from_template(introduction_template)


task_template = """Here's an example of an task chain:


"""
outline_prompt = PromptTemplate.from_template(task_template)


start_template = """Now, do this for real!

"""
start_prompt = PromptTemplate.from_template(start_template)


input_prompts = [
    ("introduction", introduction_prompt),
    ("task", example_prompt),
    ("start", start_prompt),
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt, pipeline_prompts=input_prompts
)


pipeline_prompt.input_variables

['example_q', 'example_a', 'input', 'person']


print(
    pipeline_prompt.format(
        person="Elon Musk",
        example_q="What's your favorite car?",
        example_a="Tesla",
        input="What's your favorite social media site?",
    )
)