"""Regenerate the static portfolio after editing content.json. Python 3; no packages needed."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
PROJECTS = CONTENT['projects']
E = lambda value: escape(str(value), quote=True)
ARROW = '<span class="arrow" aria-hidden="true">↗</span>'

def head(title, description, prefix=''):
    structured = {'@context':'https://schema.org','@type':'Person','name':CONTENT['name'],'jobTitle':CONTENT['title'],'sameAs':[CONTENT['github'],CONTENT['linkedin']]}
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(description)}"><meta name="theme-color" content="#f5f4ef">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(description)}">
<meta name="twitter:card" content="summary"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css"><link rel="preload" href="{prefix}assets/manrope-600.ttf" as="font" type="font/ttf" crossorigin>
<script type="application/ld+json">{json.dumps(structured)}</script><script src="{prefix}assets/app.js" defer></script></head><body id="top">
<a href="#main" class="skip-link">Skip to content</a>'''

def header(prefix=''):
    home = prefix + 'index.html' if prefix else ''
    return f'''<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="{home}#top" aria-label="Haider Najeeb — home"><span class="monogram">HN</span><span><span class="brand-name">Haider Najeeb</span><span class="brand-role">Computer Vision &amp; ML Engineer</span></span></a>
<nav class="desktop-nav" aria-label="Main navigation"><a href="{home}#work">Selected work</a><a href="{home}#expertise">Expertise</a><a href="{home}#about">About</a><a class="nav-cta" href="{home}#contact">Let’s talk {ARROW}</a></nav>
<details class="mobile-nav"><summary>Menu <span aria-hidden="true">+</span></summary><nav aria-label="Mobile navigation"><a href="{home}#work">Selected work</a><a href="{home}#expertise">Expertise</a><a href="{home}#about">About</a><a href="{home}#contact">Let’s talk ↗</a></nav></details>
</div></header>'''

def footer(prefix=''):
    home = prefix + 'index.html' if prefix else ''
    return f'''<footer class="site-footer"><div class="wrap footer-inner"><span>© 2026 Haider Najeeb · Computer Vision &amp; ML Engineering</span><div class="footer-links"><a href="{E(CONTENT['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{E(CONTENT['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="#top">Back to top ↑</a></div></div></footer>
<dialog class="demo-dialog" id="demo-dialog" aria-labelledby="demo-title"><div class="dialog-top"><h2 id="demo-title">Project demo</h2><button class="dialog-close" data-close-dialog aria-label="Close video">×</button></div><div class="demo-frame"><iframe title="Project demo video player" allow="fullscreen; encrypted-media" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div><div class="dialog-foot"><p>Player not loading? Open the original demo in a new tab.</p><a data-demo-fallback href="https://drive.google.com" target="_blank" rel="noopener noreferrer">Open original demo ↗</a></div></dialog>
</body></html>'''

def demo_link(demo, project_name, cls='text-link'):
    attributes = f' data-embed="{E(demo["embed"])}" data-demo-title="{E(project_name + " · " + demo["label"])}"' if demo.get('embed') else ''
    return f'<a class="{cls}" href="{E(demo["url"])}" target="_blank" rel="noopener noreferrer"{attributes}>{E(demo["label"])} {ARROW}</a>'

def art(project, prefix=''):
    pid = project['id']
    if project.get('image'):
        cloud = ' image-cloud' if pid == 'point-cloud-planning' else ''
        return f'<div class="project-visual{cloud}"><img src="{prefix}assets/{E(project["image"])}" alt="{E(project["alt"])}" loading="lazy" width="1400" height="788"><span class="visual-label">ACTUAL PROJECT OUTPUT</span></div>'
    if pid == 'wedding-engine':
        return '''<div class="project-visual"><div class="pipeline-art"><div class="art-label">ENGINEERING WORKFLOW / SCHEMATIC</div><div class="pipeline-grid"><div class="pipeline-step"><small>01 / INPUT</small>Multi-camera footage</div><div class="pipeline-step"><small>02 / ANALYZE</small>Quality + scene signals</div><div class="pipeline-step"><small>03 / ORGANIZE</small>Selection + sequencing</div><div class="pipeline-step out"><small>04 / OUTPUT</small>Premiere timeline</div></div><div class="runtime"><div class="runtime-header"><span>Measured processing workflow</span><strong>~2.7× faster</strong></div><div class="runtime-row"><span>Before</span><div class="bar-track"><div class="bar"></div></div><span>~4 h</span></div><div class="runtime-row"><span>After</span><div class="bar-track"><div class="bar after"></div></div><span>~90 m</span></div><div class="runtime-note">~2.5 h of footage · CUDA/OpenCV optical flow<br>Benchmark applies to this measured workflow.</div></div></div></div>'''
    if pid == 'image-to-kg':
        return '''<div class="project-visual"><div class="graph-art"><svg viewBox="0 0 490 225" role="img" aria-label="Architecture schematic: documents and media connect through provenance to a knowledge graph and retrieval."><g><line x1="107" y1="45" x2="240" y2="110"/><line x1="380" y1="45" x2="240" y2="110"/><line x1="107" y1="183" x2="240" y2="110"/><line x1="380" y1="183" x2="240" y2="110"/><rect class="node" x="22" y="24" width="145" height="44" rx="3"/><rect class="node" x="327" y="24" width="140" height="44" rx="3"/><rect class="node" x="22" y="161" width="145" height="44" rx="3"/><rect class="node" x="327" y="161" width="140" height="44" rx="3"/><rect class="center" x="174" y="88" width="145" height="49" rx="3"/><text x="94" y="51" text-anchor="middle">DOCUMENTS + OCR</text><text x="397" y="51" text-anchor="middle">IMAGE / VIDEO</text><text x="94" y="188" text-anchor="middle">PROVENANCE</text><text x="397" y="188" text-anchor="middle">RETRIEVE + RERANK</text><text class="center-text" x="247" y="118" text-anchor="middle">KNOWLEDGE GRAPH</text></g></svg></div><span class="visual-label">ARCHITECTURE SCHEMATIC</span></div>'''
    if pid == 'multispectral-calibration':
        return '''<div class="project-visual"><div class="calibration-art"><div class="bands"><div class="band" style="--band:#a6d277">GREEN</div><div class="band" style="--band:#de9a84">RED</div><div class="band" style="--band:#ceac88">RED EDGE</div><div class="band" style="--band:#b2abda">NIR</div></div><div class="process-label">GEOMETRIC + RADIOMETRIC CALIBRATION</div><div class="bits"><span>8-bit</span><i aria-hidden="true">→</i><span>16-bit</span></div></div><span class="visual-label">FOUR-BAND PIPELINE / SCHEMATIC</span></div>'''
    return '''<div class="project-visual"><div class="camera-art"><div class="camera-frame"><svg viewBox="0 0 110 110" role="img" aria-label="Face-recognition pipeline schematic"><ellipse cx="55" cy="40" rx="21" ry="25"/><path d="M17 100 Q19 73 55 73 Q91 73 93 100"/><path d="M45 39 L48 39 M62 39 L65 39 M52 50 L57 50 M47 59 Q55 63 63 59"/></svg></div><div class="camera-steps"><strong>CONTINUOUS VIDEO</strong>Detect + align<br>Recognize + track<br>Access feedback</div></div><span class="visual-label">LIVE-CAMERA WORKFLOW / SCHEMATIC</span></div>'''

def project_card(project):
    featured = ' project-featured' if project['number']=='01' else ''
    skills = ''.join(f'<span>{E(s)}</span>' for s in project['skills'][:4])
    demos = [d for d in project['demos'] if d.get('embed')]
    demo = demo_link(demos[0],project['name']) if demos else ''
    return f'''<article class="project{featured}" id="{E(project['id'])}" data-project-type="{E(project['type'])}">{art(project)}<div class="project-content"><div class="project-kicker"><span>{E(project['category'])}</span><span>{E(project['number'])}</span></div><h3><a href="projects/{E(project['id'])}.html">{E(project['name'])}</a></h3><p class="project-description">{E(project['summary'])}</p><span class="status">{E(project['status'])}</span><div class="project-skills">{skills}</div><div class="project-links"><a class="text-link" href="projects/{E(project['id'])}.html">Read case study {ARROW}</a>{demo}</div></div></article>'''

def more_row(project):
    demo = demo_link(project,project['name']) if project.get('url') else ''
    return f'''<details class="more-row"><summary><strong>{E(project['name'])}</strong><span>{E(project['field'])}</span><span class="expand" aria-hidden="true">+</span></summary><div class="more-body"><span class="more-meta">{E(project['status'])}</span><p>{E(project['body'])}</p><p>{E(project['skills'])}</p>{demo}</div></details>'''

def home():
    return head('Haider Najeeb — Computer Vision & ML Engineer','Selected engineering work in video AI, multimodal retrieval, 3D geometry, and GPU optimization. Case studies, actual project outputs, and demos.')+header()+f'''
<main id="main">
<section class="hero wrap" aria-labelledby="hero-title"><div class="hero-grid"><div><div class="eyebrow"><span class="dot"></span>Computer vision · Machine learning · Applied AI</div><h1 id="hero-title">Computer vision,<br>engineered for<br><span>real work.</span></h1><p class="hero-copy">I’m Haider. I build video-processing pipelines, multimodal knowledge systems, and 3D vision workflows — connecting models to the software people actually use.</p><div class="hero-actions"><a class="btn btn-dark" href="#work">Explore selected work <span class="arrow" aria-hidden="true">↓</span></a><a class="text-link" href="{E(CONTENT['github'])}" target="_blank" rel="noopener noreferrer">GitHub {ARROW}</a></div></div>
<figure class="hero-visual"><div class="visual-topline"><span>SELECTED OUTPUT / 3D POINT CLOUD</span><span class="visual-dot">PCL · A*</span></div><img src="assets/pointcloud.webp" width="1400" height="788" fetchpriority="high" alt="Actual client-project point cloud with structural geometry and path-planning visualization."><figcaption class="visual-caption"><span>Geometry becomes a navigable representation.</span><a href="projects/point-cloud-planning.html" aria-label="Read the point-cloud case study">View case study ↗</a></figcaption></figure></div>
<div class="hero-foot"><span>Pakistan · Working with international clients</span><span>Client systems / Research / Public teaching projects</span></div></section>
<div class="wrap evidence-strip" aria-label="Selected scoped engineering results"><a href="projects/wedding-engine.html"><strong>~2.7×</strong><span>Faster measured video workflow<br>CUDA / OpenCV optical flow</span></a><a href="projects/image-to-kg.html"><strong>76 / 76</strong><span>Targeted macOS compatibility<br>regressions passed</span></a><a href="projects/multispectral-calibration.html"><strong>16-bit</strong><span>Orthomosaic output preservation<br>Multispectral / OpenDroneMap</span></a></div>
<section class="section wrap" id="work" aria-labelledby="work-title"><div class="section-top"><div><div class="eyebrow">01 / SELECTED ENGINEERING WORK</div><h2 id="work-title">The work, in detail.</h2></div><p class="section-intro">Six projects that show how I work: the problem, my contribution, the delivered output, and the engineering behind it.</p></div>
<div class="filter-bar"><div class="filters" role="group" aria-label="Filter projects by discipline"><button class="filter" data-filter="all" aria-pressed="true">All work</button><button class="filter" data-filter="video" aria-pressed="false">Vision &amp; video</button><button class="filter" data-filter="ai" aria-pressed="false">Multimodal AI</button><button class="filter" data-filter="3d" aria-pressed="false">3D &amp; geometry</button></div><span class="filter-count" data-filter-count role="status" aria-live="polite">06 projects / all disciplines</span></div>
<noscript><p class="section-intro">All projects are shown below. Case studies and original demo links work without JavaScript.</p></noscript>
<div class="projects">{''.join(project_card(p) for p in PROJECTS)}</div>
<div class="more-work"><div class="more-heading"><h3>More engineering work.</h3><span>A few additional projects across vision and automation.</span></div>{''.join(more_row(p) for p in CONTENT['additional'])}</div></section>
<section class="section capabilities" id="expertise" aria-labelledby="expertise-title"><div class="wrap"><div class="section-top"><div><div class="eyebrow">02 / CAPABILITIES IN PRACTICE</div><h2 id="expertise-title">Depth where it matters.</h2></div><p class="section-intro">My strongest areas come from building and debugging complete workflows, from image acquisition to useful output.</p></div><div class="cap-grid">
<article class="cap-item"><span class="cap-number">01</span><h3>Vision &amp; video systems</h3><p>Detection, segmentation, tracking, OCR, and temporal logic integrated with real media and application workflows.</p><a href="projects/retail-analytics.html">Retail tracking case study ↗</a></article>
<article class="cap-item"><span class="cap-number">02</span><h3>Performance engineering</h3><p>Profiling, GPU optical flow, and batch inference. Measure the bottleneck, optimize it, and compare the result.</p><a href="projects/wedding-engine.html">CUDA optimization evidence ↗</a></article>
<article class="cap-item"><span class="cap-number">03</span><h3>Multimodal knowledge</h3><p>Document/media ingestion, OCR, provenance, graph integration, and semantic retrieval with reranking.</p><a href="projects/image-to-kg.html">Knowledge-system case study ↗</a></article>
<article class="cap-item"><span class="cap-number">04</span><h3>3D &amp; geometric vision</h3><p>Camera calibration, photogrammetry, point-cloud segmentation, spatial representation, and path planning.</p><a href="projects/point-cloud-planning.html">Point-cloud case study ↗</a></article></div>
<div class="toolbelt" aria-label="Core technologies"><span>Python / C++</span><span>OpenCV / CUDA</span><span>PyTorch / TensorFlow</span><span>YOLO / Tracking</span><span>FFmpeg / Premiere</span><span>PCL / OpenDroneMap</span><span>Neo4j / Retrieval</span></div></div></section>
<section class="section wrap about" id="about" aria-labelledby="about-title"><div class="about-grid"><div><div class="eyebrow">03 / THE ENGINEER BEHIND THE WORK</div><h2 id="about-title">Research roots.<br>Applied engineering.</h2></div><div class="about-text"><p>My first professional work was in aerial imaging and 3D reconstruction. It taught me to look beyond a model’s output and understand the camera, the geometry, and the data behind it.</p><p>At the Institute of Space Technology, I worked on multispectral calibration and C++ integration into OpenDroneMap. Learning radiometry, camera models, and photogrammetry while solving a real research problem shaped how I approach unfamiliar work.</p><p>Since then, I’ve built client video-automation systems, tracking and segmentation workflows, and multimodal knowledge pipelines. I’ve also taught computer vision and robotics through practical projects on Udemy.</p><p>I like the engineering work between a promising model and a useful application: inspecting failure cases, fixing the responsible stage, improving runtime, and making the workflow understandable.</p><div class="about-links"><a class="text-link" href="{E(CONTENT['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn {ARROW}</a><a class="text-link" href="{E(CONTENT['github'])}" target="_blank" rel="noopener noreferrer">Public projects {ARROW}</a></div></div></div>
<div class="timeline" aria-label="Career milestones"><article class="timeline-item"><span class="period">MAR — AUG 2019</span><h3>Burqstream Technologies</h3><p>Computer Vision Research Engineer<br>Drone imagery, calibration, multi-view reconstruction.</p></article><article class="timeline-item"><span class="period">AUG 2019 — JUN 2020</span><h3>Institute of Space Technology</h3><p>Computer Vision R&amp;D<br>Multispectral calibration and OpenDroneMap integration.</p></article><article class="timeline-item"><span class="period">SINCE JUN 2020</span><h3>Udemy instruction</h3><p>Computer vision and robotics<br>Practical applications, teaching, and public repositories.</p></article><article class="timeline-item"><span class="period">SINCE MAR 2023</span><h3>Independent client engineering</h3><p>International remote consulting<br>Video AI, applied CV, automation, and multimodal systems.</p></article></div>
<div class="teaching-note"><p>Teaching has made clear explanations part of my engineering work. The public courses and repositories show both the implementation and how I break a technical problem into understandable steps.</p><a class="text-link" href="https://www.udemy.com/course/computer-vision-2022-masterclass-with-opencv4-and-python/" target="_blank" rel="noopener noreferrer">View CV course {ARROW}</a></div></section>
<section class="contact" id="contact" aria-labelledby="contact-title"><div class="wrap contact-grid"><div><div class="eyebrow">04 / LET’S WORK TOGETHER</div><h2 id="contact-title">Have a vision problem<br>worth solving?</h2><p>Open to applied CV/ML projects and long-term technical collaborations. Let’s discuss the problem, the constraints, and what a useful first delivery would look like.</p></div><div class="contact-actions"><a class="btn btn-dark" href="{E(CONTENT['linkedin'])}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn {ARROW}</a><a class="text-link" href="{E(CONTENT['github'])}" target="_blank" rel="noopener noreferrer">Explore my GitHub {ARROW}</a></div></div></section>
</main>'''+footer()

def case_page(project,index):
    title = project['name'] + ' — Haider Najeeb'
    links = ' '.join(demo_link(d,project['name'],'btn btn-dark' if d.get('embed') else 'btn') for d in project['demos'] if not d['url'].startswith('../projects/'))
    caption = 'Actual project output.' if project.get('image') else 'Technical schematic of the implemented workflow; not a screenshot.'
    gallery = ''
    if project['id']=='point-cloud-planning':
        names = [('pcl-structure.webp','Structural segmentation: ground, pillars, and walls.'),('pcl-traversable.webp','Traversable-area segmentation.'),('pcl-octree.webp','Spatial discretization with octree cells.'),('pointcloud.webp','Path-planning visualization.')]
        gallery = '<section class="case-section" id="outputs"><h2>Actual project outputs</h2><div class="case-gallery">'+''.join(f'<figure><img src="../assets/{fn}" alt="{E(label)}" loading="lazy" width="700" height="440"><figcaption>{E(label)}</figcaption></figure>' for fn,label in names)+'</div></section>'
    next_p = PROJECTS[(index+1)%len(PROJECTS)]
    bullet = lambda items: '<ul>'+''.join(f'<li>{E(i)}</li>' for i in items)+'</ul>'
    sec = lambda name, body: f'<section class="case-section"><h2>{name}</h2>{body}</section>'
    evidence_note = f'<p class="evidence-note">{E(project["evidenceNote"])}</p>' if project.get('evidenceNote') else ''
    actual = ''
    if project['id']=='wedding-engine' and (ROOT/'assets/ppwe-output.webp').exists():
        actual = '<figure class="case-media"><img src="../assets/ppwe-output.webp" alt="Actual frame from the PremierPro Wedding Engine demo." loading="lazy" width="1400" height="788"><figcaption class="media-caption">Actual frame from the linked system demo.</figcaption></figure>'
    return head(title,project['summary'],'../')+header('../')+f'''<main id="main"><section class="case-hero"><div class="wrap"><a class="back-link" href="../index.html#work">← All selected work</a><div class="eyebrow">CASE STUDY {E(project['number'])} / {E(project['category'])}</div><h1>{E(project['headline'])}</h1><p class="case-project-name">{E(project['name'])}</p><span class="status">{E(project['status'])}</span><div class="case-meta">{links}</div></div></section>
<div class="wrap case-main"><article class="case-text"><div class="case-media">{art(project,'../')}<div class="media-caption">{caption}</div></div>
{sec('The problem','<p>'+E(project['problem'])+'</p>')}{sec('My contribution','<p>'+E(project['role'])+'</p>')}{sec('What I delivered',bullet(project['delivered']))}{sec('Engineering decisions',bullet(project['approach']))}{actual}{gallery}{sec('Outcome &amp; scope','<p>'+E(project['result'])+'</p><p class="evidence-note">'+E(project['metricNote'])+'</p>'+evidence_note)}{sec('Skills strengthened','<p>'+E(project['growth'])+'</p>')}
<div class="next-project"><span>Continue exploring</span><a href="{E(next_p['id'])}.html">{E(next_p['name'])} {ARROW}</a></div></article>
<aside class="case-sidebar" aria-label="Project result and technical skills"><div><div class="eyebrow">PROJECT RESULT</div><div class="metric">{E(project['metric'])}</div><div class="metric-label">{E(project['metricLabel'])}</div><p class="metric-note">{E(project['metricNote'])}</p>{('<div class="secondary-metric">'+E(project['secondaryMetric'])+'</div><p class="metric-note">'+E(project['secondaryNote'])+'</p>') if project.get('secondaryMetric') else ''}</div><div class="case-skills">{''.join('<span>'+E(s)+'</span>' for s in project['skills'])}</div></aside></div></main>'''+footer('../')

(ROOT/'index.html').write_text(home(),encoding='utf-8')
(ROOT/'projects').mkdir(exist_ok=True)
for i,project in enumerate(PROJECTS):
    (ROOT/'projects'/f"{project['id']}.html").write_text(case_page(project,i),encoding='utf-8')
(ROOT/'.nojekyll').touch()
print(f'Built index.html and {len(PROJECTS)} case-study pages.')
