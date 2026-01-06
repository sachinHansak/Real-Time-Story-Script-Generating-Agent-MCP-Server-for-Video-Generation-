

***

# Realtime News/Information MCP Server on Any Topic

This repository contains a simple Model Context Protocol (MCP) server that exposes tools for fetching realtime news information and generating video-ready scripts from that news.

The server is built on top of `FastMCP` and is intended to be used as an MCP-compatible tool provider (for example from an MCP-enabled client or IDE).

## Features

- **Realtime news lookup**: Query for the latest information about any topic using `get_latest_info_mcp`.
- **Video script generation**: Generate a video-friendly transcription or script based on the retrieved news via `gen_video_script_mcp`.
- **MCP-compatible server**: Runs as an MCP server over `stdio`, ready to be integrated into MCP-aware clients.[1]

## Project Structure

Key files in this repository:

- `mcp_server.py`: Defines and runs the MCP server using `FastMCP` and exposes two tools:
  - `get_latest_info_mcp(query)`: Returns realtime information by delegating to `app.get_realtime_info`.
  - `gen_video_script_mcp(query)`: Fetches realtime news and passes it to `app.generate_video_transcription` to create a script.
- `app.py` (expected, not included here): Should implement:
  - `get_realtime_info(query: str) -> Any`
  - `generate_video_transcription(text: str) -> Any`  
- Git hook samples (`pre-push.sample`, `pre-applypatch.sample`, `push-to-checkout.sample`, `update.sample`): Standard Git hook templates provided by Git, not specific to this project’s logic.

## Requirements

Make sure you have:

- Python 3.9+ (recommended)  
- Project dependencies installed, including:
  - `mcp` / `mcp.server.fastmcp`
  - Any dependencies required by your `app.py` implementation

Example (adjust to match your actual package names):

```bash
pip install mcp
```

If you maintain a `requirements.txt`, install with:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Implement the app functions

Create an `app.py` with at least the following functions:

```python
def get_realtime_info(query: str):
    # Fetch latest info (e.g., from news APIs or search)
    ...

def generate_video_transcription(text: str):
    # Turn the news text into a video script/transcription
    ...
```

`mcp_server.py` imports these functions and wires them into MCP tools.

### 2. Run the MCP server

From the repository root:

```bash
python mcp_server.py
```

The server will run using `stdio` transport:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
``` 

so it can be launched by MCP-aware clients as a subprocess.

### 3. Available tools

Once connected from an MCP client, you can call:

- `get_latest_info_mcp`
  - **Input**: `query: string`  
  - **Description**: Returns realtime information for the given query via `get_realtime_info`.

- `gen_video_script_mcp`
  - **Input**: `query: string`  
  - **Description**: Uses `get_realtime_info` to fetch news, then passes the result into `generate_video_transcription` to create a script.

## Development

- Clone the repository and create a virtual environment.
- Install dependencies as described above.
- Modify `app.py` to point to your preferred news/search APIs and your video script generation logic.
- Optionally configure Git hooks using the provided `*.sample` files if you want pre-push or update checks.





