from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
try:
    load_dotenv(".env")
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
    stateless_http=True,
)

# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Run the server
if __name__ == "__main__":
    transport = os.getenv('TRANSPORT', 'stdio')
    if transport == 'stdio':
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == 'sse':
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == 'streamable-http':
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")
    