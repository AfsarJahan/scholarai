# src/json_to_csv.py

import json
import pandas as pd
import os

input_path = "data/dblp.v12.json"
output_path = "data/papers.csv"

def is_valid(paper):
    return (
        paper.get("title") 
        and paper.get("abstract") 
        and isinstance(paper.get("n_citation"), int)
        and len(paper["abstract"].strip()) > 50  # basic filter
    )

def convert_json_to_csv(infile, outfile, limit=100000):
    papers = []

    with open(infile, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            try:
                paper = json.loads(line)
                if is_valid(paper):
                    papers.append({
                        "title": paper["title"],
                        "abstract": paper["abstract"],
                        "year": paper.get("year"),
                        "venue": paper.get("venue", "Unknown"),
                        "citations": paper["n_citation"]
                    })
            except json.JSONDecodeError:
                continue

            if len(papers) >= limit:
                break

    df = pd.DataFrame(papers)
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    df.to_csv(outfile, index=False)
    print(f"✅ Saved {len(df)} papers to {outfile}")

if __name__ == "__main__":
    convert_json_to_csv(input_path, output_path)
