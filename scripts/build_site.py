"""Generate the survey's static paper explorer from the Markdown collections."""

import argparse
import hashlib
import html
import json
import re
import shutil
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/LuckyGirl-XU/Awesome-Agent-Dynamic-Graphs"
SITE_URL = "https://luckygirl-xu.github.io/Awesome-Agent-Dynamic-Graphs/"


def normalize(text):
    return re.sub(r"[^\w]", "", unicodedata.normalize("NFKC", text)).casefold()


def read_catalog(root=ROOT):
    sections = json.loads((root / "site/sections.json").read_text())
    records = {}
    topics = {}
    for section_id, section in sections.items():
        by_label = {topic["label"]: topic["id"] for topic in section["topics"]}
        for item in section["topics"]:
            topics[section_id + ":" + item["id"]] = {"label": item["label"], "section": section_id}
        path = root / "papers" / (section_id + ".md")
        topic_id = None
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if line.startswith("### "):
                label = line[4:].strip()
                if label not in by_label:
                    raise ValueError(f"Unknown topic: {path}:{number}: {label}")
                topic_id = section_id + ":" + by_label[label]
            if not line.startswith("| ") or line.startswith(("| Paper |", "| ---")):
                continue
            match = re.fullmatch(r"\|\s*\[(.+)\]\((https?://.+)\)\s*\|\s*(\d{4})\s*\|", line)
            if not match or not topic_id:
                raise ValueError(f"Invalid paper entry: {path}:{number}")
            title, url, year = match.groups()
            title, year = html.unescape(title), int(year)
            key = (normalize(title), year)
            if key not in records:
                records[key] = {"id": hashlib.sha256((key[0] + str(year)).encode()).hexdigest()[:12],
                                "title": title, "year": year, "sections": [], "topics": [],
                                "urls": [], "sources": [], "title_variants": []}
            paper = records[key]
            for field, value in (("sections", section_id), ("topics", topic_id), ("urls", url), ("title_variants", title)):
                if value not in paper[field]:
                    paper[field].append(value)
            paper["sources"].append({"path": str(path.relative_to(root)), "line": number})
    return {"sections": sections, "topics": topics,
            "papers": sorted(records.values(), key=lambda p: (-p["year"], p["title"].casefold())),
            "source_entries": sum(len(p["sources"]) for p in records.values())}


def escape(value):
    return html.escape(str(value), quote=True)


def cards(data):
    result = []
    for paper in data["papers"]:
        topic_buttons = "".join(f'<button class="topic-tag" type="button" data-topic="{key}">{escape(data["topics"][key]["label"])}</button>' for key in paper["topics"])
        sections = " · ".join(data["sections"][key]["label"] for key in paper["sections"])
        links = "".join(f'<a class="resource-link" href="{escape(url)}" target="_blank" rel="noopener noreferrer">{"Paper" if i == 0 else "Alternative source"} ↗</a>' for i, url in enumerate(paper["urls"]))
        source = paper["sources"][0]
        result.append(f'''<article class="paper-card" data-paper-id="{paper['id']}">
          <div class="paper-meta"><span>{paper['year']}</span><span>{escape(sections)}</span></div>
          <h3><a href="{escape(paper['urls'][0])}" target="_blank" rel="noopener noreferrer">{escape(paper['title'])}</a></h3>
          <div class="paper-topics">{topic_buttons}</div>
          <div class="paper-actions">{links}<a class="source-link" href="{REPOSITORY}/blob/main/{source['path']}#L{source['line']}" target="_blank" rel="noopener noreferrer">In full paper list ↗</a></div>
        </article>''')
    return "\n".join(result)


def section_cards(data):
    result = []
    descriptions = {
        "agent-evolution": "How memories, tools, skills, workflows, and agent relationships evolve.",
        "graph-infrastructure": "Graph learning methods that support persistent agent-state evolution.",
        "evaluation-governance": "Temporal protocols, privacy, safety, rollback, and audit.",
        "benchmarks": "Evaluation resources for memory, tools, web, software, and safety.",
    }
    for index, (key, section) in enumerate(data["sections"].items(), 1):
        count = sum(key in paper["sections"] for paper in data["papers"])
        result.append(f'''<article class="collection-card">
          <div class="collection-meta"><span>0{index}</span><span>{count} paper records · {len(section['topics'])} topics</span></div>
          <a class="collection-figure" href="./{escape(section['figure'])}" target="_blank" rel="noopener noreferrer" aria-label="Open {escape(section['title'])} diagram"><img src="./{escape(section['figure'])}" alt="Diagram for {escape(section['title'])}" loading="lazy"></a>
          <h3><a href="?section={key}#paper-explorer">{escape(section['label'])}</a></h3>
          <p>{escape(descriptions[key])}</p>
          <div class="collection-actions"><a class="text-link" href="?section={key}#paper-explorer">Explore papers →</a><a href="{REPOSITORY}/blob/main/papers/{key}.md">Full paper list ↗</a></div>
        </article>''')
    return "\n".join(result)


def build(output, root=ROOT):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    data = read_catalog(root)
    source = (root / "site/index.html").read_text()
    replacements = {
        "PAPER_COUNT": str(len(data["papers"])), "TOPIC_COUNT": str(len(data["topics"])),
        "PAPER_CARDS": cards(data), "SECTION_CARDS": section_cards(data),
        "YEAR_OPTIONS": "".join(f'<option value="{year}">{year}</option>' for year in sorted({p["year"] for p in data["papers"]}, reverse=True)),
        "SECTION_OPTIONS": "".join(f'<option value="{key}">{escape(section["label"])}</option>' for key, section in data["sections"].items()),
        "TOPIC_OPTIONS": "".join(f'<option value="{key}" data-section="{topic["section"]}">{escape(data["sections"][topic["section"]]["label"])} / {escape(topic["label"])}</option>' for key, topic in data["topics"].items()),
        "CATALOG_JSON": json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
    }
    for key, value in replacements.items():
        source = source.replace("{{" + key + "}}", value)
    for name in ("app.js", "styles.css", "favicon.svg"):
        asset = root / "site" / name
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
        source = source.replace(f'"./{name}"', f'"./{name}?v={digest}"')
        shutil.copyfile(asset, output / name)
    if re.search(r"{{[A-Z_]+}}", source):
        raise ValueError("Unresolved template placeholder")
    (output / "index.html").write_text(source)
    (output / "papers.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    (output / ".nojekyll").touch()
    shutil.copytree(root / "figs", output / "figs", dirs_exist_ok=True)
    (output / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE_URL}</loc></url></urlset>\n')
    print(f"Built {len(data['papers'])} paper records from {data['source_entries']} entries across {len(data['topics'])} topics")
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    build(parser.parse_args().output)
