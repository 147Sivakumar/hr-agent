
import asyncio
import os

from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load the API key from the .env file
load_dotenv()


async def main():
    # 1) Brain: The model client powers the agent using OpenAI.
    # The API key is read from the environment, not hard-coded.
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from your .env file.")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    try:
        # 2) Agent: Give it a name and a job.
        # The system message tells the agent its role.
        agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant.",
        )

        # 3) Run it: Ask the agent to write a five-line job description.
        # We use await because AutoGen runs asynchronously.
        # Console displays the conversation in the terminal.
        await Console(
            agent.run_stream(
                task=(
                    "Write a job description for a Junior Python Developer "
                    "in exactly 5 lines, using 5 numbered bullet points. "
                    "Do not include a heading or extra text."
                )
            )
        )

        # The agent's answer is the LAST message displayed in the terminal.

    finally:
        # 4) Clean up: Close the model client when the task is complete.
        # This helps prevent the script from hanging.
        await model_client.close()


# Start the program using asyncio.
# In a Jupyter notebook, we would typically use: await main()
if __name__ == "__main__":
    asyncio.run(main())

