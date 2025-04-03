from mcp.server.fastmcp import FastMCP

mcp = FastMCP("gbif-context")

@mcp.resource("gbif://context")
def gbif_dataset_info():
    """Providing context on the GBIF dataset"""

    return """GBIF public dataset consists of the
bigquery-public-data.gbif.occurrences BigQuery table, which captures metadata
on crowd sourced observations. Most users will want to filter by
occurrencestatus=PRESENT, as there are also observations reporting absences.
"""
