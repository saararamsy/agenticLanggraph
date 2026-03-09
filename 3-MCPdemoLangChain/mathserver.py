from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int):
    """Add two numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int):
    """Multiply two numbers
    """
    return a*b

#The transport = "stdio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls
# will run in the command prompt and will get in there itself, helpful to test out things locally
if __name__== "__main__":
    mcp.run(transport = "stdio")
    