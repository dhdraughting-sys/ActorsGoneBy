#!/usr/bin/env python3
"""Builds the static "Actors Gone By" site from actors_data.py.

To add, edit or remove an actor: change actors_data.py, then re-run this
script (`python3 build_actors_site.py`) and re-upload whatever changed to
GitHub — index.html, portfolio.html, and/or the individual page(s) under
actors/. Nothing else needs to change; filters, "coming soon" photo
placeholders and cross-links all update themselves from the data file.
"""
import os
import re
import json

from actors_data import ACTORS, CATEGORY_ORDER

SITE_URL = "https://www.actorsgoneby.co.uk"

BASE = os.path.dirname(os.path.abspath(__file__))
ACTORS_OUT = os.path.join(BASE, "actors")
os.makedirs(ACTORS_OUT, exist_ok=True)
os.makedirs(os.path.join(BASE, "images", "actors"), exist_ok=True)


def _esc(s):
    return (str(s) if s is not None else "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")


def ordered_categories():
    """CATEGORY_ORDER, plus any category used in the data that isn't
    listed there yet — so a new show/franchise just works."""
    seen = list(CATEGORY_ORDER)
    for actor in ACTORS:
        for cat in actor["categories"]:
            if cat not in seen:
                seen.append(cat)
    return seen


def actors_in(category):
    return [a for a in ACTORS if category in a["categories"]]


# ---------------- shared page chrome ----------------

STYLE = """
:root{
  --ink:#2c241c; --cream:#f6efe2; --paper:#fffdf8;
  --charcoal:#201a15; --charcoal-2:#2b231c;
  --gold:#c9a24b; --gold-deep:#a7802f; --gold-pale:#e7cf9a;
  --wine:#5c2626; --line:#3a3026; --line-light:#e4d8bd;
  --radius:10px; --maxw:1120px;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'EB Garamond',Georgia,serif;color:var(--cream);background:var(--charcoal);line-height:1.65;font-size:18px;}
img{max-width:100%;display:block;}
a{color:inherit;}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;}
.marquee{font-family:'Bebas Neue',Impact,sans-serif;letter-spacing:.14em;}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px;}

.top-bar{background:#0f0c09;border-bottom:1px solid var(--line);text-align:center;padding:7px 0;}
.top-bar .wrap{font-size:12.5px;letter-spacing:.04em;color:#a89a7c;}
.top-bar a{color:var(--gold-pale);text-decoration:none;font-weight:600;}
.top-bar a:hover{text-decoration:underline;}

header.site-nav{position:sticky;top:0;z-index:50;background:rgba(32,26,21,.92);border-bottom:1px solid var(--line);backdrop-filter:blur(6px);}
.nav-inner{display:flex;align-items:center;justify-content:space-between;padding:16px 24px;max-width:var(--maxw);margin:0 auto;gap:16px;}
.nav-logo{display:flex;align-items:center;gap:12px;text-decoration:none;}
.film-badge{width:42px;height:42px;border-radius:50%;background:radial-gradient(circle at 32% 28%,var(--gold-pale),var(--gold) 65%,var(--gold-deep));display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;box-shadow:0 4px 12px rgba(0,0,0,.4);}
.nav-word{font-size:1.4rem;color:var(--gold-pale);font-weight:700;letter-spacing:.01em;}
nav.links{display:flex;gap:30px;font-size:15px;font-weight:600;}
nav.links a{text-decoration:none;color:#cbbfa8;transition:color .15s;font-family:'EB Garamond',serif;font-size:17px;}
nav.links a:hover,nav.links a.active{color:var(--gold-pale);}

.hero{background:linear-gradient(160deg,#241d17 0%,#201a15 55%,#1a140f 100%);padding:80px 0 68px;border-bottom:1px solid var(--line);text-align:center;position:relative;}
.eyebrow{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--charcoal);background:var(--gold);padding:7px 16px;border-radius:20px;margin-bottom:22px;font-family:'Bebas Neue',sans-serif;}
h1.script-title{font-size:clamp(2.6rem,6vw,4.4rem);line-height:1.05;color:var(--gold-pale);margin-bottom:18px;font-weight:700;}
.hero p.lead{font-size:1.18rem;color:#d9cdb4;max-width:60ch;margin:0 auto 30px;}
.hero-ctas{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
.btn{display:inline-block;padding:13px 28px;border-radius:26px;font-weight:700;text-decoration:none;font-size:15px;transition:transform .15s,box-shadow .15s;border:1.5px solid transparent;cursor:pointer;font-family:'EB Garamond',serif;}
.btn-primary{background:var(--gold);color:var(--charcoal);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(201,162,75,.35);}
.btn-secondary{background:transparent;color:var(--gold-pale);border-color:var(--gold-deep);}
.btn-secondary:hover{transform:translateY(-2px);border-color:var(--gold);}

section{padding:70px 0;}
.section-head{max-width:640px;margin:0 auto 42px;text-align:center;}
.section-head h2{font-size:2rem;color:var(--gold-pale);margin-bottom:14px;font-weight:700;}
.section-head p{color:#cbbfa8;font-size:1.05rem;}

.page-hero{background:linear-gradient(160deg,#241d17 0%,#1a140f 100%);border-bottom:1px solid var(--line);padding:56px 0 48px;text-align:center;}
.page-hero h1{font-size:clamp(2.1rem,4.5vw,2.8rem);color:var(--gold-pale);margin-bottom:12px;}
.page-hero p{color:#cbbfa8;font-size:1.08rem;max-width:640px;margin:0 auto;}

.gallery-filters{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:40px;}
.filter-btn{background:transparent;border:1.5px solid var(--gold-deep);color:var(--gold-pale);font-size:14px;font-weight:700;padding:9px 20px;border-radius:22px;cursor:pointer;transition:background .15s,color .15s;font-family:'EB Garamond',serif;}
.filter-btn:hover{background:rgba(201,162,75,.12);}
.filter-btn.active{background:var(--gold);color:var(--charcoal);border-color:var(--gold);}

.actor-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:24px;}
.actor-card{background:var(--charcoal-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;text-decoration:none;display:block;transition:box-shadow .15s,transform .15s,border-color .15s;}
.actor-card:hover{box-shadow:0 16px 36px rgba(0,0,0,.45);transform:translateY(-3px);border-color:var(--gold-deep);}
.actor-photo{aspect-ratio:3/4;overflow:hidden;background:linear-gradient(150deg,#332a20,#241d17);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;border-bottom:1px solid var(--line);position:relative;}
.actor-photo img{width:100%;height:100%;object-fit:cover;}
.actor-photo .ph-icon{font-size:2rem;opacity:.7;}
.actor-photo .ph-label{font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:#a89a7c;font-weight:600;font-family:'Bebas Neue',sans-serif;}
.actor-body{padding:16px 18px 20px;}
.actor-cat{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);font-family:'Bebas Neue',sans-serif;}
.actor-name{font-size:1.15rem;color:var(--cream);margin:7px 0 4px;font-family:'Playfair Display',serif;}
.actor-years{font-size:.86rem;color:#a89a7c;font-variant-numeric:tabular-nums;}

.bio-page .wrap{max-width:880px;}
.bio-hero{display:grid;grid-template-columns:260px 1fr;gap:40px;align-items:start;padding:56px 0 10px;}
.bio-photo{aspect-ratio:3/4;border-radius:var(--radius);overflow:hidden;background:linear-gradient(150deg,#332a20,#241d17);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;border:1px solid var(--line);}
.bio-photo img{width:100%;height:100%;object-fit:cover;}
.bio-photo .ph-icon{font-size:2.6rem;opacity:.7;}
.bio-photo .ph-label{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:#a89a7c;font-weight:600;text-align:center;padding:0 14px;font-family:'Bebas Neue',sans-serif;}
.bio-name{font-size:clamp(1.9rem,4vw,2.6rem);color:var(--gold-pale);margin-bottom:6px;}
.bio-years{font-size:1.1rem;color:var(--gold);font-variant-numeric:tabular-nums;margin-bottom:16px;font-family:'Bebas Neue',sans-serif;letter-spacing:.04em;}
.bio-known{font-size:1.02rem;color:#d9cdb4;margin-bottom:18px;font-style:italic;}
.bio-facts{display:flex;flex-direction:column;gap:6px;font-size:.92rem;color:#a89a7c;}
.bio-facts b{color:#cbbfa8;font-weight:700;}
.bio-cats{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px;}
.bio-cats a{font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;background:rgba(201,162,75,.12);color:var(--gold-pale);padding:5px 12px;border-radius:14px;text-decoration:none;border:1px solid var(--gold-deep);font-family:'Bebas Neue',sans-serif;}
.bio-cats a:hover{background:rgba(201,162,75,.22);}
.bio-text{padding:36px 0 10px;font-size:1.08rem;color:#e6dcc6;max-width:70ch;}
.bio-text p{margin-bottom:18px;}
.bio-nav{padding:10px 0 60px;}
.bio-nav a{color:var(--gold-pale);text-decoration:none;font-weight:600;font-size:.95rem;}
.bio-nav a:hover{text-decoration:underline;}

.divider{border:none;border-top:1px solid var(--line);margin:0;}

footer{background:#15100c;color:#9c8e73;padding:34px 0;font-size:13px;}
.footer-inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}
.footer-inner .brand{color:var(--gold-pale);font-family:'Playfair Display',serif;font-size:1.15rem;}
.footer-inner .flinks a{color:#9c8e73;text-decoration:none;margin-left:16px;}
.footer-inner .flinks a:hover{color:var(--gold-pale);}
.footer-note{color:#6b6150;font-size:11.5px;margin-top:10px;max-width:760px;line-height:1.6;}

@media(max-width:820px){
  .bio-hero{grid-template-columns:1fr;}
  .bio-photo{max-width:260px;margin:0 auto;}
}
@media(max-width:600px){
  nav.links{display:none;}
  .actor-grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px;}
}

.slideshow{position:relative;max-width:820px;margin:0 auto;background:var(--charcoal-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.45);}
.slideshow-track{position:relative;min-height:400px;}
.slide{position:absolute;inset:0;display:grid;grid-template-columns:190px 1fr;gap:28px;align-items:center;padding:32px;opacity:0;visibility:hidden;transition:opacity .7s ease;}
.slide.active{opacity:1;visibility:visible;position:relative;}
.slide-photo{aspect-ratio:3/4;border-radius:8px;overflow:hidden;background:linear-gradient(150deg,#332a20,#241d17);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;border:1px solid var(--line);}
.slide-photo img{width:100%;height:100%;object-fit:cover;}
.slide-photo .ph-icon{font-size:1.8rem;opacity:.7;}
.slide-photo .ph-label{font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:#a89a7c;font-weight:600;text-align:center;padding:0 10px;font-family:'Bebas Neue',sans-serif;}
.slide-cat{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);font-family:'Bebas Neue',sans-serif;}
.slide-name{font-size:1.6rem;color:var(--gold-pale);margin:6px 0 4px;font-family:'Playfair Display',serif;}
.slide-years{font-size:.95rem;color:#a89a7c;font-variant-numeric:tabular-nums;margin-bottom:10px;}
.slide-known{font-size:.98rem;color:#d9cdb4;font-style:italic;margin-bottom:16px;}
.slide-link{font-size:13px;font-weight:700;color:var(--gold-pale);text-decoration:none;border-bottom:1.5px solid var(--gold-deep);padding-bottom:2px;}
.slide-link:hover{border-color:var(--gold);}
.slide-controls{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:14px 24px;border-top:1px solid var(--line);background:rgba(0,0,0,.15);}
.slide-btn{background:transparent;border:1.5px solid var(--gold-deep);color:var(--gold-pale);width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:17px;line-height:1;flex-shrink:0;transition:background .15s,border-color .15s;}
.slide-btn:hover{background:rgba(201,162,75,.15);border-color:var(--gold);}
.slide-counter{font-size:13px;color:#a89a7c;font-variant-numeric:tabular-nums;white-space:nowrap;}
.slide-progress{flex:1;height:3px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden;}
.slide-progress-bar{height:100%;width:0;background:var(--gold);transition:width linear;}
@media(max-width:600px){
  .slide{grid-template-columns:1fr;text-align:center;padding:24px;}
  .slide-photo{max-width:170px;margin:0 auto;}
  .slideshow-track{min-height:480px;}
}
"""

NAV_ITEMS = [("/index.html", "Home"), ("/portfolio.html", "Portfolio")]


def top_bar_html():
    return """
<div class="top-bar">
  <div class="wrap">Sponsored by <a href="https://www.clearlineweb.co.uk" target="_blank" rel="noopener">Clearline Web</a></div>
</div>
"""


def nav_html(active, depth=0):
    prefix = "../" * depth
    links = "\n      ".join(
        '<a href="{}{}"{}>{}</a>'.format(
            prefix, href.lstrip("/"), ' class="active"' if href == active else "", label
        )
        for href, label in NAV_ITEMS
    )
    return f"""
<header class="site-nav">
  <div class="nav-inner">
    <a href="{prefix}index.html" class="nav-logo">
      <div class="film-badge">&#127909;</div>
      <span class="nav-word marquee">Actors Gone By</span>
    </a>
    <nav class="links">
      {links}
    </nav>
  </div>
</header>
"""


def footer_html(depth=0):
    prefix = "../" * depth
    return f"""
<footer>
  <div class="wrap footer-inner">
    <div class="brand marquee">Actors Gone By</div>
    <div class="flinks"><a href="{prefix}index.html">Home</a><a href="{prefix}portfolio.html">Portfolio</a></div>
  </div>
  <div class="wrap footer-note">
    A fan-made tribute site remembering actors and actresses of British stage and screen who have
    passed away. Biographical summaries are written for this site from publicly available
    information. This is an unofficial, non-commercial project with no affiliation to any studio,
    broadcaster, estate or rights holder; photographs are used only where the specific image is
    confirmed public domain or openly (e.g. Creative Commons) licensed, with source credited under
    the photo.
  </div>
</footer>
"""


def page(title, description, active, body_content, depth=0, extra_head="", canonical=None):
    prefix = "../" * depth
    canonical_path = active.lstrip("/") if canonical is None else canonical
    if canonical_path == "index.html":
        canonical_path = ""
    canonical_url = f"{SITE_URL}/{canonical_path}" if canonical_path else f"{SITE_URL}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_esc(title)} | Actors Gone By</title>
<meta name="description" content="{_esc(description)}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Actors Gone By">
<meta property="og:title" content="{_esc(title)} | Actors Gone By">
<meta property="og:description" content="{_esc(description)}">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>{STYLE}</style>
{extra_head}
</head>
<body>
{top_bar_html()}
{nav_html(active, depth)}
{body_content}
{footer_html(depth)}
</body>
</html>
"""


# ---------------- Portfolio grid (shared by Home teaser + Portfolio page) ----------------

def photo_block(actor, css_class="actor-photo"):
    if actor["photo"]:
        return f'<div class="{css_class}"><img src="images/actors/{actor["photo"]}" alt="{_esc(actor["name"])}" loading="lazy"></div>'
    return (
        f'<div class="{css_class}"><span class="ph-icon">&#127909;</span>'
        f'<span class="ph-label">Photo coming soon</span></div>'
    )


def actor_card(actor, depth=0):
    prefix = "../" * depth if depth else ""
    href = f'{prefix}actors/{actor["slug"]}.html' if depth == 0 else f'{actor["slug"]}.html'
    cat = actor["categories"][0]
    photo_html = photo_block(actor).replace('images/actors/', f'{prefix}images/actors/' if depth == 0 else f'../images/actors/')
    return f"""
    <a class="actor-card" href="{href}">
      {photo_html}
      <div class="actor-body">
        <div class="actor-cat">{_esc(cat)}</div>
        <div class="actor-name">{_esc(actor["name"])}</div>
        <div class="actor-years">{_esc(actor["years"])}</div>
      </div>
    </a>"""


def portfolio_section(categories):
    filter_btns = '\n      '.join(
        f'<button class="filter-btn{" active" if i == 0 else ""}" data-filter="{"All" if i == 0 else c}">{"All" if i == 0 else c}</button>'
        for i, c in enumerate(["All"] + categories)
    )
    cards = "\n".join(
        f'<div class="grid-item" data-cats=\'{json.dumps(a["categories"])}\'>{actor_card(a)}</div>'
        for a in ACTORS
    )
    return f"""
<section id="portfolio">
  <div class="wrap">
    <div class="gallery-filters">
      {filter_btns}
    </div>
    <div class="actor-grid" id="actor-grid">
      {cards}
    </div>
  </div>
</section>

<script>
(function(){{
  var btns = document.querySelectorAll('.filter-btn');
  var items = document.querySelectorAll('#actor-grid .grid-item');
  btns.forEach(function(btn){{
    btn.addEventListener('click', function(){{
      btns.forEach(function(b){{ b.classList.remove('active'); }});
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      items.forEach(function(item){{
        var cats = JSON.parse(item.getAttribute('data-cats'));
        item.style.display = (f === 'All' || cats.indexOf(f) !== -1) ? '' : 'none';
      }});
    }});
  }});
}})();
</script>
"""


# ---------------- Home ----------------

def slide_block(actor, index):
    photo_html = photo_block(actor, css_class="slide-photo")
    cat = actor["categories"][0]
    return f"""
      <div class="slide{' active' if index == 0 else ''}" data-index="{index}">
        {photo_html}
        <div>
          <div class="slide-cat">{_esc(cat)}</div>
          <div class="slide-name">{_esc(actor["name"])}</div>
          <div class="slide-years">{_esc(actor["years"])}</div>
          <div class="slide-known">{_esc(actor["known_for"])}</div>
          <a class="slide-link" href="actors/{actor["slug"]}.html">View biography &rarr;</a>
        </div>
      </div>"""


def build_home(categories):
    slides = "\n".join(slide_block(a, i) for i, a in enumerate(ACTORS))
    body = f"""
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">A Tribute Site</span>
    <h1 class="script-title">Actors Gone By</h1>
    <p class="lead">Remembering the faces and voices of British stage and screen —
    from Steptoe and Son to the Carry On films, Oliver! and beyond — actors and
    actresses no longer with us, but never forgotten.</p>
    <div class="hero-ctas">
      <a href="portfolio.html" class="btn btn-primary">Browse the Portfolio</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{len(ACTORS)} Faces Remembered</span>
      <h2>Every star, one at a time</h2>
      <p>A rolling slideshow of everyone featured on the site — or use the full Portfolio to browse and filter by show or film.</p>
    </div>
    <div class="slideshow" id="home-slideshow">
      <div class="slideshow-track" id="slideshow-track">
        {slides}
      </div>
      <div class="slide-controls">
        <button class="slide-btn" id="slide-prev" aria-label="Previous actor">&#8249;</button>
        <div class="slide-progress"><div class="slide-progress-bar" id="slide-progress-bar"></div></div>
        <span class="slide-counter"><span id="slide-current">1</span> / {len(ACTORS)}</span>
        <button class="slide-btn" id="slide-next" aria-label="Next actor">&#8250;</button>
      </div>
    </div>
    <div style="text-align:center;margin-top:40px;">
      <a href="portfolio.html" class="btn btn-secondary">See the Full Portfolio</a>
    </div>
  </div>
</section>

<script>
(function(){{
  var track = document.getElementById('slideshow-track');
  if (!track) return;
  var slides = track.querySelectorAll('.slide');
  var counter = document.getElementById('slide-current');
  var bar = document.getElementById('slide-progress-bar');
  var box = document.getElementById('home-slideshow');
  var i = 0, total = slides.length, timer = null, DURATION = 4500;

  function show(n){{
    slides[i].classList.remove('active');
    i = (n + total) % total;
    slides[i].classList.add('active');
    counter.textContent = (i + 1);
    restartProgress();
  }}
  function next(){{ show(i + 1); }}
  function prev(){{ show(i - 1); }}
  function restartProgress(){{
    bar.style.transition = 'none';
    bar.style.width = '0%';
    requestAnimationFrame(function(){{
      requestAnimationFrame(function(){{
        bar.style.transition = 'width ' + DURATION + 'ms linear';
        bar.style.width = '100%';
      }});
    }});
  }}
  function start(){{
    stop();
    restartProgress();
    timer = setInterval(next, DURATION);
  }}
  function stop(){{
    if (timer) clearInterval(timer);
    timer = null;
  }}

  document.getElementById('slide-next').addEventListener('click', function(){{ next(); start(); }});
  document.getElementById('slide-prev').addEventListener('click', function(){{ prev(); start(); }});
  box.addEventListener('mouseenter', stop);
  box.addEventListener('mouseleave', start);
  box.addEventListener('focusin', stop);
  box.addEventListener('focusout', start);

  if (total > 1) start(); else bar.style.width = '0%';
}})();
</script>
"""
    return page(
        "Home",
        "Actors Gone By — a tribute site remembering British actors and actresses of stage and screen who have passed away, from Steptoe and Son to the Carry On films and Oliver!.",
        "/index.html",
        body,
    )


# ---------------- Portfolio ----------------

def build_portfolio(categories):
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">The Full Roster</span>
    <h1>Portfolio</h1>
    <p>Filter by show or film, or browse everyone. Tap a face for their full biography.</p>
  </div>
</section>
{portfolio_section(categories)}
"""
    return page(
        "Portfolio",
        "Browse every actor and actress featured on Actors Gone By, filterable by show and film.",
        "/portfolio.html",
        body,
    )


# ---------------- Individual biography pages ----------------

def build_bio_page(actor):
    paragraphs = "".join(f"<p>{_esc(p.strip())}</p>" for p in actor["bio"].split("\n\n") if p.strip())
    cats_html = "".join(
        f'<a href="../portfolio.html">{_esc(c)}</a>' for c in actor["categories"]
    )
    photo_html = photo_block(actor, css_class="bio-photo").replace('images/actors/', '../images/actors/')
    body = f"""
<div class="bio-page">
  <div class="wrap">
    <div class="bio-hero">
      {photo_html}
      <div>
        <h1 class="bio-name">{_esc(actor["name"])}</h1>
        <div class="bio-years marquee">{_esc(actor["years"])}</div>
        <div class="bio-known">Known for: {_esc(actor["known_for"])}</div>
        <div class="bio-facts">
          <div><b>Born</b> {_esc(actor["born"])}</div>
          <div><b>Died</b> {_esc(actor["died"])}</div>
        </div>
        <div class="bio-cats">{cats_html}</div>
      </div>
    </div>
    <hr class="divider">
    <div class="bio-text">
      {paragraphs}
    </div>
    <div class="bio-nav">
      <a href="../portfolio.html">&larr; Back to the full Portfolio</a>
    </div>
  </div>
</div>
"""
    return page(
        actor["name"],
        f'{actor["name"]} ({actor["years"]}) — {actor["known_for"]}. Biography on Actors Gone By.',
        "/portfolio.html",
        body,
        depth=1,
        canonical=f'actors/{actor["slug"]}.html',
    )


# ---------------- write everything ----------------

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content))


def main():
    categories = ordered_categories()
    write("index.html", build_home(categories))
    write("portfolio.html", build_portfolio(categories))
    for actor in ACTORS:
        write(os.path.join("actors", f'{actor["slug"]}.html'), build_bio_page(actor))

    # Minimal sitemap/robots, same pattern as the flower site.
    urls = ["", "portfolio.html"] + [f'actors/{a["slug"]}.html' for a in ACTORS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>\n" for u in urls)
    sitemap += "</urlset>\n"
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"\n{len(ACTORS)} actors across {len(categories)} categories.")


if __name__ == "__main__":
    main()
