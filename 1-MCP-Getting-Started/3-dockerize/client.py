from mcp.client.sse import sse_client
from mcp import ClientSession
import asyncio
import nest_asyncio
nest_asyncio.apply()

ENDPOINT = "http://localhost:8050/sse"

async def main():
    async with sse_client(ENDPOINT) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            response = await session.call_tool('add', arguments={'a': 2, 'b': 7})
            print(f"2 + 7 = {response.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
    