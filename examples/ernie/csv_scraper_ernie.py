"""
Basic example of scraping pipeline using CSVScraperGraph from CSV documents
"""
import os
from dotenv import load_dotenv
import pandas as pd
from scrapegraphai.graphs import CSVScraperGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

load_dotenv()

# ************************************************
# Read the CSV file
# ************************************************

FILE_NAME = "inputs/username.csv"
curr_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(curr_dir, FILE_NAME)

text = pd.read_csv(file_path)

# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = { 
    "llm": {
        "model": "ernie/ernie-bot-turbo",
        "ernie_client_id": "<ernie_client_id>",
        "ernie_client_secret": "<ernie_client_secret>",
        "temperature": 0.1
    }
}

# ************************************************
# Create the CSVScraperGraph instance and run it
# ************************************************

csv_scraper_graph = CSVScraperGraph(
    prompt="List me all the last names",
    source=str(text),  # Pass the content of the file, not the file object
    config=graph_config
)

result = csv_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = csv_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Save to json or csv
convert_to_csv(result, "result")
convert_to_json(result, "result")
