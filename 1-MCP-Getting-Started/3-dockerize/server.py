from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0", # only used for SSE transport
    port=8050, # only used for SSE transport (set this to any port)
    stateless_http=True,  # Use stateless HTTP transport
)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    print("Running server with SSE transport")
    mcp.run(transport="sse")
