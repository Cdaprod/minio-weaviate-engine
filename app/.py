from datetime import datetime
from typing import Callable, Dict

# Common format strings
DATE_FORMAT = "%B %d, %Y"
COMMON_REPORT_INSTRUCTIONS = (
    "The report should be well structured, informative, in depth, and comprehensive, "
    "with facts and numbers if available. Use an unbiased and journalistic tone. "
    "Include all used source URLs at the end of the report as references, ensuring no duplicates. "
    "Cite search results using inline notations. Assume the current date is {date}."
)

def generate_prompt(
    question: str,
    context: str,
    prompt_type: str = "search_queries",
    report_format: str = "apa",
    total_words: int = 1000
) -> str:
    """Generates various types of prompts based on the given parameters."""
    date_str = datetime.now().strftime(DATE_FORMAT)
    if prompt_type == "search_queries":
        return (
            f'Write 3 google search queries to search online that form an objective opinion from the following: "{question}" '
            f'Use the current date if needed: {date_str}.\n'
            'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3"].'
        )
    else:
        report_instructions = COMMON_REPORT_INSTRUCTIONS.format(date=date_str)
        if prompt_type == "custom_report":
            return f'"{context}"\n\n{question}\n{report_instructions}'
        else:
            return (
                f'Information: """{context}"""\n\n'
                f'Using the above information, answer the following query or task: "{question}" in a detailed report -- '
                f"{report_instructions}\n"
                f"You MUST write the report in {report_format} format and aim for a minimum of {total_words} words."
            )

def get_report_by_type(report_type: str) -> Callable:
    """Returns the appropriate report generation function based on the report type."""
    report_type_mapping: Dict[str, Callable] = {
        'search_queries': generate_prompt,  # Example usage, adjust as necessary
        # Add other mappings if needed
    }
    return report_type_mapping.get(report_type, generate_prompt)


    # This function remains largely unchanged, but ensure it is well-documented.
def auto_agent_instructions() -> str:
    return """
        This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific server, defined by its type and role, with each server requiring distinct instructions.
        Agent
        The server is determined by the field of the topic and the specific name of the server that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each server type is associated with a corresponding emoji.

        examples:
        task: "should I invest in apple stocks?"
        response: 
        {
            "server": "💰 Finance Agent",
            "agent_role_prompt: "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends."
        }
        task: "could reselling sneakers become profitable?"
        response: 
        { 
            "server":  "📈 Business Analyst Agent",
            "agent_role_prompt": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
        }
        task: "what are the most interesting sites in Tel Aviv?"
        response:
        {
            "server:  "🌍 Travel Agent",
            "agent_role_prompt": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights."
        }
    """

def generate_summary_prompt(query: str, data: str) -> str:
    """Generates the summary prompt for the given question and text."""
    return (
        f'{data}\n Using the above text, summarize it based on the following task or query: "{query}".\n'
        'If the query cannot be answered using the text, summarize the text in short.\n'
        'Include all factual information such as numbers, stats, quotes, etc., if available.'
    )
