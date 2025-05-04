import json
import sys

def verify_spark(path):
    with open(path, 'r') as f:
        spark = json.load(f)
    result = {
        "name": spark.get("name", "Unnamed"),
        "codex_reference": "Present" if "codex_reference" in spark else "Missing",
        "lineage": "Present" if "lineage" in spark else "Missing",
        "scroll_binding": spark.get("codex_reference", {}).get("bound_by", "Missing"),
        "status": "COMPLIANT" if "codex_reference" in spark and "lineage" in spark else "NONCOMPLIANT"
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    verify_spark(sys.argv[1])
