#!/usr/bin/env python3
"""
Embed scenarios-data.json directly into clinical-guide-enhanced.html
to avoid fetch() issues with file:// URLs.
"""

import json
from pathlib import Path

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    base_dir = Path(__file__).parent
    html_file = base_dir / 'clinical-guide-enhanced.html'
    json_file = base_dir / 'scenarios-data.json'
    output_file = base_dir / 'clinical-guide-enhanced.html'

    print("=== Embedding Scenarios Data ===\n")

    # Read files
    print(f"Reading {html_file}...")
    html = read_file(html_file)

    print(f"Reading {json_file}...")
    scenarios_json = read_file(json_file)

    # Find the fetch call and replace it
    old_code = """        // Load and render all scenarios
        async function loadScenarios() {
            try {
                const response = await fetch('scenarios-data.json');
                const scenarios = await response.json();"""

    new_code = """        // Embedded scenarios data
        const SCENARIOS_DATA = """ + scenarios_json + """;

        // Load and render all scenarios
        async function loadScenarios() {
            try {
                const scenarios = SCENARIOS_DATA;"""

    if old_code not in html:
        print("ERROR: Could not find fetch code to replace!")
        return

    html = html.replace(old_code, new_code)

    # Write output
    print(f"\nWriting to {output_file}...")
    write_file(output_file, html)

    # Stats
    print(f"\nComplete!")
    print(f"  Scenarios data embedded: {len(scenarios_json):,} characters")
    print(f"  File now works without server - open directly in browser")

if __name__ == '__main__':
    main()
