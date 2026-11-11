# Contributing

Contributions are welcome through issues and pull requests.

## Add a Paper

1. Choose a relevant collection in `papers/` and its existing topic heading.
2. Include the full title, original paper URL, and publication year. Prefer DOI, arXiv, or official proceedings links.
3. Use the existing `Paper | Year` table format. Keep the survey taxonomy intact and avoid duplicate rows within one topic.
4. Cross-list papers when they are relevant to more than one section. Explain the connection when suggesting a new topic.

The collections include both graph-based agent methods and related foundations. Placement reflects the organizing perspective of the survey.

## Preview the Website

Paper data are generated from the Markdown collections. Update the collections rather than editing generated files.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. Layout and filters live in `site/`; the section structure is defined in `site/sections.json`. GitHub Actions rebuilds the site after source changes on `main`.

## Report a Correction

Include the affected entry and a supporting source or replacement URL. General questions can be sent to [Yuanyuan Xu](mailto:yuanyuan.xu@unsw.edu.au) or [Yin Chen](mailto:yin.chen@student.uts.edu.au).
