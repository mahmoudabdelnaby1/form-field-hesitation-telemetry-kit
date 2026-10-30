#!/usr/bin/env python3
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

def aggregate_hesitation(events_json, out_html):
    with open(events_json, "r", encoding="utf-8") as f:
        events = json.load(f)

    field_dwell = defaultdict(list)
    for e in events:
        field = e.get("field_id")
        dwell = float(e.get("dwell_time_ms", 0))
        field_dwell[field].append(dwell)

    results = []
    for field, times in field_dwell.items():
        avg_dwell = sum(times) / len(times)
        results.append({
            "field": field,
            "sample_size": len(times),
            "avg_dwell_sec": round(avg_dwell / 1000, 2),
            "friction_level": "HIGH" if avg_dwell > 8000 else ("MEDIUM" if avg_dwell > 4000 else "LOW")
        })

    results.sort(key=lambda x: x["avg_dwell_sec"], reverse=True)

    rows = "".join([f"<tr><td><code>{r['field']}</code></td><td>{r['avg_dwell_sec']}s</td><td>{r['sample_size']}</td><td>{r['friction_level']}</td></tr>" for r in results])
    html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'><title>Form Hesitation Heatmap</title><style>body{{font-family:sans-serif;padding:2rem;background:#0f172a;color:#fff}}table{{width:100%;border-collapse:collapse}}th,td{{padding:10px;border:1px solid #334155}}th{{background:#0284c7}}</style></head><body><h1>Form Field Hesitation Telemetry Report</h1><table><tr><th>Field Name</th><th>Avg Dwell Time</th><th>Samples</th><th>Friction Rating</th></tr>{rows}</table></body></html>"""
    Path(out_html).parent.mkdir(parents=True, exist_ok=True)
    Path(out_html).write_text(html, encoding="utf-8")
    return results

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--events", required=True)
    p.add_argument("--report", default="reports/hesitation_heatmap.html")
    args = p.parse_args()

    r = aggregate_hesitation(args.events, args.report)
    print(f"Aggregated hesitation for {len(r)} fields -> {args.report}")

if __name__ == "__main__":
    main()
