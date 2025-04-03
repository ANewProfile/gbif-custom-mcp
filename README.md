
## How to setup MCP servers to access GBIF dataset from Claude Desktop

We will be setting up two MCP servers

1. A BigQuery MCP server to access GBIF dataset on BigQuery
2. A MCP server to provide context to LLMs (in this case, Claude) how to use the GBIF schema

### BigQuery MCP

1. Clone https://github.com/ANewProfile/gbif-bigquery-mcp
2. Install dependencies and build code locally

```
git clone https://github.com/ANewProfile/gbif-bigquery-mcp
cd gbif-bigquery-mcp
npm install

# Build
npm run build
```

3. Add the following to your Claude desktop configuration fil
`~/Library/Application Support/Claude/claude_desktop_config.json`. Note this is
if you are using Benjie's Google Cloud setup. Obtain the
`gbif_service_account_key.json` file from Benjie. You can also create your own
Google Cloud project and generate a service account key.

```json
{
  "mcpServers": {
    "gbif-bigquery": {
      "command": "node",
      "args": [
        "<path-to-your-gbif-bigquery-mcp-working-directory>/dist/index.js",
        "--project-id",
        "gbif-data-if-i-can-get-it",
        "--key-file",
        "<path-to-benjie-gbif-service-account-key-file>/gbif_service_account_key.json"
      ]
    }
  }
}
```

4. If you start Claude Desktop, you should now be able to enter the following
prompt and see Claude uses the MCP server (it will ask you for permission) to
obtain the dataset schema.

```Can you query GBIF database and get me schema for the occurrence table? It's
called bigquery-public-data.gbif.occurrences```


### Custom MCP server

1. Clone this repo, https://github.com/ANewProfile/gbif-custom-mcp
2. Run the following to update your Claude desktop configuration file

```
uv run mcp install gbif-context.py
```

3. Restart Claude Desktop, you should now be able to choose the GBIF context
MCP server and attach the context.

