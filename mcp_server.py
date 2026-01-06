from mcp.server.fastmcp import FastMCP
from app import get_realtime_info, generate_video_transcription as gene

mcp = FastMCP("this is for real time news ")

@mcp.tool()
async def get_latest_info_mcp(query):
    return get_realtime_info(query=query)


@mcp.tool()
async def gen_video_script_mcp(query):
    news = get_realtime_info(query=query)
    return gene(news)


if __name__ == "__main__":
    mcp.run(transport = "stdio")