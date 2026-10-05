"""A practical three-method guide; authored copy is shared by HTML/Markdown."""
import html
import json
from locked_ai_locales import COPY
from keep_awake_locales import COPY as UI_COPY
from lid_article_locales import LANGUAGES

UPDATED = '2026-10-05'
SLUG = 'mac-locked-ai-running'
PATHS = {locale: '/guide/' + ('' if locale == 'en' else locale + '/') + SLUG + '/' for locale, _ in LANGUAGES}
IDS = ['lock', 'execution', 'diagnose', 'verify', 'pika', 'faq', 'sources']
CODES = {2: ['pmset -g assertions', 'pmset -g log | tail -n 60'], 3: ['while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done']}
SOURCES = '<ul><li><a href="https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac">Apple · Sleep and wake settings</a></li><li><a href="https://learn.chatgpt.com/docs/codex/cli">OpenAI · Codex CLI</a></li><li><a href="https://learn.chatgpt.com/docs/cloud">OpenAI · Codex Cloud</a></li><li><a href="https://code.claude.com/docs/en/remote-control">Anthropic · Claude Code Remote Control</a></li></ul>'


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
        if i == 1:
            content += '<p><a href="https://learn.chatgpt.com/docs/codex/cli">Codex CLI</a> · <a href="https://learn.chatgpt.com/docs/cloud">Codex Cloud</a> · <a href="https://code.claude.com/docs/en/remote-control">Claude Code Remote Control</a></p>'
        if i == 4:
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
<link rel="icon" href="/assets/favicon.svg"><link rel="stylesheet" href="/install/install.css"><link rel="stylesheet" href="/guide/guide.css"><link rel="stylesheet" href="/guide/article.css?v=20261005-reference"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><div class="shell"><header><a class="brand" href="{home}">no-sleep-pika</a><div class="article-languages"><details><summary>🌐 {dict(LANGUAGES)[locale]}</summary><div>{language_links}</div></details></div></header>
<main id="main"><p class="eyebrow">MAC GUIDE · <time datetime="{UPDATED}">{UPDATED}</time></p><h1>{e(t['title'])}</h1><p class="intro">{e(t['intro'])}</p><nav class="contents">{toc}</nav><div class="guide-layout"><article>{''.join(sections)}</article><aside class="notice"><img class="article-pika" src="/assets/pika-working.png" width="140" height="140" alt=""><p>{e(t['disclosure'])}</p><a class="article-cta" href="{download}">{e(t['download'])}</a><a href="{previous}">{e(UI_COPY[locale]['title'])} →</a><a href="{url}index.md">Markdown</a></aside></div></main><footer><a href="{home}">pika</a><a href="{repo}">GitHub</a></footer></div></body></html>'''


def build(out, base, repo, release):
    assert set(COPY) == set(PATHS)
    for locale, path in PATHS.items():
        assert len(COPY[locale]['headings']) == len(COPY[locale]['paragraphs']) == len(IDS)
        dest = out / path.strip('/')
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'index.html').write_text(render(locale, base, repo, release), encoding='utf-8')
    return [base + path for path in PATHS.values()]
