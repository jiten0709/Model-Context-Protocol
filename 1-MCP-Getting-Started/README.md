# Getting Started with MCP

## To run the MCP server

- create a virtual environment

  ```bash
    uv venv
  ```

- install dependencies

  ```bash
    uv pip install -r requirements.txt
  ```

- run the server

  ```bash
    mcp dev server.py
  ```

  OR

  ```bash
    uv run server.py
  ```

- then in mcp inspector, update the below fields

  ```bash
    command: uv
    arguments: run --with mcp mcp run server.py
  ```

# refernce

- https://github.com/daveebbelaar/ai-cookbook/blob/main/mcp/crash-course
