import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI()


async def main():
    project_root = Path(__file__).resolve().parent

    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [
                    str(project_root / "server" / "math_server.py")
                ],
            },
            "weather": {
                "transport": "sse",
                "command": sys.executable,
                "args": [
                    str(project_root / "server" / "weather_server.py")
                ],
            },
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    #result = await agent.ainvoke({"messages": "What is 2 + 2?"})
    result = await agent.ainvoke(
        {"messages": "What is the weather in San Francisco?"}
    )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())