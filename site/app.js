(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('catalog-data').textContent);
  const form = document.getElementById('filters');
  const search = document.getElementById('search');
  const year = document.getElementById('year');
  const section = document.getElementById('section');
  const topic = document.getElementById('topic');
  const sort = document.getElementById('sort');
  const list = document.getElementById('paper-list');
  const count = document.getElementById('results-count');
  const empty = document.getElementById('empty-state');
  const more = document.getElementById('load-more');
  const cards = new Map([...list.children].map(card => [card.dataset.paperId, card]));
  const index = new Map(data.papers.map(p => [p.id, [p.title, ...p.title_variants, ...p.topics.map(id => data.topics[id].label), ...p.sections.map(id => data.sections[id].label)].join(' ').normalize('NFKC').toLowerCase()]));
  const pageSize = 25;
  let limit = pageSize;

  function syncTopics() {
    for (const option of topic.options) {
      const excluded = Boolean(section.value && option.dataset.section && option.dataset.section !== section.value);
      option.hidden = excluded;
      option.disabled = excluded;
    }
    if (topic.selectedOptions[0]?.disabled) topic.value = '';
  }

  function readURL() {
    const params = new URLSearchParams(location.search);
    search.value = params.get('q') || '';
    for (const [control, key] of [[year, 'year'], [section, 'section'], [topic, 'topic'], [sort, 'sort']]) {
      const value = params.get(key) || (key === 'sort' ? 'newest' : '');
      control.value = [...control.options].some(option => option.value === value) ? value : (key === 'sort' ? 'newest' : '');
    }
    syncTopics();
  }

  function render(updateURL = true) {
    syncTopics();
    const terms = search.value.trim().normalize('NFKC').toLowerCase().split(/\s+/).filter(Boolean);
    const papers = data.papers.filter(p => (!year.value || String(p.year) === year.value) && (!section.value || p.sections.includes(section.value)) && (!topic.value || p.topics.includes(topic.value)) && terms.every(term => index.get(p.id).includes(term)));
    papers.sort((a, b) => sort.value === 'title' ? a.title.localeCompare(b.title) : (sort.value === 'oldest' ? a.year - b.year : b.year - a.year) || a.title.localeCompare(b.title));
    for (const card of cards.values()) card.hidden = true;
    const fragment = document.createDocumentFragment();
    papers.slice(0, limit).forEach(paper => { const card = cards.get(paper.id); card.hidden = false; fragment.append(card); });
    list.append(fragment);
    const visible = Math.min(limit, papers.length);
    count.textContent = papers.length ? `Showing ${visible} of ${papers.length} paper records` : '0 matching papers';
    empty.hidden = papers.length !== 0;
    more.hidden = visible >= papers.length;
    more.textContent = `Show more papers (${papers.length - visible} remaining)`;
    if (updateURL) {
      const params = new URLSearchParams();
      for (const [key, value] of Object.entries({q: search.value.trim(), year: year.value, section: section.value, topic: topic.value, sort: sort.value === 'newest' ? '' : sort.value})) if (value) params.set(key, value);
      history.replaceState(null, '', location.pathname + (params.size ? '?' + params.toString() : '') + location.hash);
    }
  }

  function reset() {
    search.value = ''; year.value = ''; section.value = ''; topic.value = ''; sort.value = 'newest'; limit = pageSize; render();
  }
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', () => { limit = pageSize; render(); });
  form.addEventListener('reset', event => { event.preventDefault(); reset(); });
  sort.addEventListener('change', () => { limit = pageSize; render(); });
  more.addEventListener('click', () => { limit += pageSize; render(); });
  document.getElementById('empty-reset').addEventListener('click', reset);
  list.addEventListener('click', event => {
    const tag = event.target.closest('button[data-topic]');
    if (!tag) return;
    section.value = data.topics[tag.dataset.topic].section;
    syncTopics(); topic.value = tag.dataset.topic; limit = pageSize; render();
  });
  window.addEventListener('popstate', () => { readURL(); limit = pageSize; render(false); });
  readURL(); render(false);
})();
