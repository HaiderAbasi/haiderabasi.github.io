(() => {
  'use strict';
  const filters = [...document.querySelectorAll('[data-filter]')];
  const projects = [...document.querySelectorAll('[data-project-type]')];
  const count = document.querySelector('[data-filter-count]');
  const labels = { all: 'all disciplines', video: 'vision & video', ai: 'multimodal AI', '3d': '3D & geometry' };
  filters.forEach(button => button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    let visible = 0;
    projects.forEach(project => {
      project.hidden = selected !== 'all' && project.dataset.projectType !== selected;
      if (!project.hidden) visible++;
    });
    filters.forEach(filter => filter.setAttribute('aria-pressed', String(filter === button)));
    if (count) count.textContent = `${String(visible).padStart(2, '0')} projects / ${labels[selected]}`;
  }));

  const dialog = document.querySelector('#demo-dialog');
  const frame = dialog?.querySelector('iframe');
  const title = dialog?.querySelector('#demo-title');
  const fallback = dialog?.querySelector('[data-demo-fallback]');
  let trigger;
  document.querySelectorAll('[data-embed]').forEach(link => link.addEventListener('click', event => {
    if (!dialog || !frame || typeof dialog.showModal !== 'function') return;
    const url = new URL(link.dataset.embed);
    if (url.origin !== 'https://drive.google.com') return;
    event.preventDefault();
    trigger = link;
    const name = link.dataset.demoTitle || link.textContent.trim();
    title.textContent = name;
    frame.title = `${name} — video player`;
    frame.src = url.href;
    fallback.href = link.href;
    dialog.showModal();
    dialog.querySelector('[data-close-dialog]').focus();
  }));
  dialog?.querySelector('[data-close-dialog]').addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog?.addEventListener('close', () => {
    frame?.removeAttribute('src');
    trigger?.focus();
  });
  document.querySelectorAll('.mobile-nav a').forEach(link => link.addEventListener('click', () => {
    document.querySelector('.mobile-nav').removeAttribute('open');
  }));
})();
