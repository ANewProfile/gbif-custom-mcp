from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-gbif-context")

@mcp.resource("config://app")
def gbif_dataset_info():
    """Necessary resource regarding GBIF dataset"""
    return "Use bigquery-public-data.gbif.occurrences table to fetch observations. Most users will want to filter by occurrencestatus=PRESENT, as there are also observations reporting absences."
