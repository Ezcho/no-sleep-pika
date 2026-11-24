"""Parallel AI worktree guide; reviewed copy shared by HTML and Markdown."""
import html
import json
from worktree_article_locales import COPY
from keep_awake_locales import COPY as UI_COPY
from lid_article_locales import LANGUAGES

UPDATED = '2026-11-24'
SLUG = 'parallel-ai-agents-git-worktree'
PATHS = {locale: '/guide/' + ('' if locale == 'en' else locale + '/') + SLUG + '/' for locale, _ in LANGUAGES}
IDS = ['problem', 'prepare', 'worktrees', 'assign', 'review', 'pika', 'sources']
CODES = {1: ['git status --short'], 2: ['git worktree add -b ai-ui ../project-ai-ui HEAD\ngit worktree add -b ai-tests ../project-ai-tests HEAD'], 4: ['git status --short\ngit diff\ngit diff --cached']}
SOURCES = '<ul><li><a href="https://git-scm.com/docs/git-worktree">Git · git-worktree</a></li><li><a href="https://git-scm.com/docs/git-status">Git · git-status</a></li><li><a href="https://git-scm.com/docs/git-diff">Git · git-diff</a></li></ul>'



def render(locale, base, repo, release):
    t = {**UI_COPY[locale], **COPY[locale]}
    e = html.escape
    url = base + PATHS[locale]
    home = '/' if locale == 'en' else '/' + locale + '/'
    previous = '/guide/' + ('' if locale == 'en' else locale + '/') + 'keep-mac-awake/'
    install = '/install/ko/' if locale == 'ko' else '/install/'
    download = f'{repo}/releases/download/{release}/pika-{release[1:]}.pkg'
    alternate = ''.join(f'<link rel="alternate" hreflang="{lang}" href="{base}{path}">' for lang, path in PATHS.items())
    language_links = ''.join(f'<a href="{PATHS[lang]}" lang="{lang}">{e(name)}</a>' for lang, name in LANGUAGES)
    sections = []
    for i, (heading, paragraphs) in enumerate(zip(t['headings'], t['paragraphs'])):
        content = ''.join(f'<p>{e(p)}</p>' for p in paragraphs)
        content += ''.join(f'<pre dir="ltr"><code>{e(code)}</code></pre>' for code in CODES.get(i, []))
        if i == 0:
            content += '<ol class="worktree-flow">' + ''.join(f'<li><span>{j}</span> {e(label)}</li>' for j, label in enumerate(t['flow'], 1)) + '</ol>'
        if i == 5:
            content += f'<p><a class="article-cta" href="{download}">{e(t["download"])}</a> · <a href="{install}">{e(t["install"])}</a></p>'
        if i == 6:
            sections.append(f'<details class="article-reference" id="{IDS[i]}"><summary>{e(heading)}</summary>{content}{SOURCES}</details>')
            continue
        sections.append(f'<section id="{IDS[i]}"><h2>{e(heading)}</h2>{content}</section>')
    schema = {'@context':'https://schema.org','@graph':[
        {'@type':'Article','headline':t['title'],'description':t['intro'],'url':url,'mainEntityOfPage':url,'inLanguage':locale,'datePublished':UPDATED,'dateModified':UPDATED,'image':base+'/assets/pika-session-guide.webp','author':{'@type':'Organization','name':'no-sleep-pika','url':base+'/'},'publisher':{'@type':'Organization','name':'no-sleep-pika','url':base+'/'}},
        {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'pika','item':base+home},{'@type':'ListItem','position':2,'name':t['title'],'item':url}]}]}
    toc = ''.join(f'<a href="#{key}">{e(title)}</a>' for key,title in zip(IDS,t['headings']))
    return f'''<!doctype html>
<html lang="{locale}" dir="{'rtl' if locale == 'ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t['title'])} | no-sleep-pika</title><meta name="description" content="{e(t['intro'])}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{url}">{alternate}<link rel="alternate" hreflang="x-default" href="{base}{PATHS['en']}">
<meta property="og:type" content="article"><meta property="og:title" content="{e(t['title'])}"><meta property="og:description" content="{e(t['intro'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}/assets/pika-session-guide.webp"><meta property="article:published_time" content="{UPDATED}"><meta property="article:modified_time" content="{UPDATED}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg"><link rel="stylesheet" href="/install/install.css"><link rel="stylesheet" href="/guide/guide.css"><link rel="stylesheet" href="/guide/article.css?v=20261005-reference"><style>.worktree-flow{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;padding:0;list-style:none;margin:24px 0}}.worktree-flow li{{padding:16px 12px;border:1px solid currentColor;border-radius:12px;font-size:.9rem;line-height:1.5}}.worktree-flow span{{display:block;font-weight:700;font-size:1.4rem;margin-bottom:8px}}@media(max-width:650px){{.worktree-flow{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}</style><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><div class="shell"><header><a class="brand" href="{home}">no-sleep-pika</a><div class="article-languages"><details><summary>🌐 {dict(LANGUAGES)[locale]}</summary><div>{language_links}</div></details></div></header>
<main id="main"><p class="eyebrow">MAC GUIDE · <time datetime="{UPDATED}">{UPDATED}</time></p><h1>{e(t['title'])}</h1><p class="intro">{e(t['intro'])}</p><nav class="contents">{toc}</nav><div class="guide-layout"><article>{''.join(sections)}</article><aside class="notice"><img class="article-pika" src="/assets/pika-working.png" width="140" height="140" alt=""><p>{e(t['disclosure'])}</p><a href="{previous}">{e(UI_COPY[locale]['title'])} →</a><a href="{url}index.md">Markdown</a></aside></div></main><footer><a href="{home}">pika</a><a href="{repo}">GitHub</a></footer></div></body></html>'''


def build(out, base, repo, release):
    assert set(COPY) == set(PATHS)
    for locale, path in PATHS.items():
        assert len(COPY[locale]['headings']) == len(COPY[locale]['paragraphs']) == len(IDS)
        dest = out / path.strip('/')
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'index.html').write_text(render(locale, base, repo, release), encoding='utf-8')
    return [base + path for path in PATHS.values()]
