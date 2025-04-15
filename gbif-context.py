from mcp.server.fastmcp import FastMCP

mcp = FastMCP("gbif-context")

@mcp.resource("gbif://context")
def gbif_dataset_info():
    """Providing context on the GBIF dataset"""

    return """GBIF public dataset consists of the
bigquery-public-data.gbif.occurrences BigQuery table (also called the
occurrences table), which captures metadata on crowd sourced observations. Most
users will want to filter by occurrencestatus=PRESENT, as there are also
observations reporting absences.

The column names in the GBIF occurrences table follow the Darwin Core standard,
described by https://dwc.tdwg.org/terms/.

Specifically, the columns "kingdom", "phylum", "class", "order", "family",
"genus", and "species" refer to terms in a taxonomy hierarchy, with "kingdom"
on top and "species" on the bottom. Any Python, Javascript, or other
programming language software to use the table should use hierarchical data
structures to represent these values, rather than individual variables for each
term.

The number of occurrences (e.g. rows in the table) should not be confused with
the number of individuals - or sums from the "individualcount" column.

BigQuery does not support TIMESTAMP_SUB. To get a year range, use "EXTRACT(YEAR
FROM eventdate)" to limit to certain years.

Sometimes a useful analysis is to breakdown observations by latitude and then
group by month of the year, and then year. A plot supporting this analysis
would plot month and year on the x-axis, and latitude on the y-axis, and use
heatmap bars on top of the x-axis to show observation counts at corresponding
latitude and time.
"""
