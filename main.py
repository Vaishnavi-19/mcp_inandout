import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
print("Environment variables loaded:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

async def main():
    print("Hello from mcp-inandout!")


if __name__ == "__main__":
    asyncio.run(main())
