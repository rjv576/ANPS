import json

''' JSON Exporter Module - This module provides functionality to export scan results to a JSON file.'''
def export_to_json(data: list, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
