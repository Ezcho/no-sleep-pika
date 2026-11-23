/* Keep installation help visible before Gatekeeper permits pika to launch. */
(() => {
  'use strict';
  if (!document.querySelectorAll || !document.createElement) return;
  const ko = document.documentElement.lang === 'ko';
  const copy = ko ? {
    title: '설치가 막히면 이렇게 해주세요',
    intro: '다운로드한 PKG를 먼저 한 번 여세요. 설치 후 앱이 차단되면 응용 프로그램의 pika를 먼저 여세요.',
    steps: ['시스템 설정 → 개인정보 보호 및 보안', '아래쪽 보안 영역에서 방금 연 pika 파일 확인', '출처를 신뢰하면 ‘그래도 열기’ → macOS 인증 → ‘열기’'],
    note: '개발자를 확인하거나 앱을 검증할 수 없다는 경고에만 해당합니다. 현재 빌드는 Developer ID 서명·공증이 없습니다.',
    danger: '손상 경고는 파일을 다시 받은 뒤 확인하세요. 악성 소프트웨어·인증 취소 경고는 우회하지 마세요.',
    link: '단계별 설치 안내 ↗', close: '알겠어요'
  } : {
    title: 'If macOS blocks installation',
    intro: 'Try opening the downloaded PKG once. If the app is blocked after installation, first open pika in Applications.',
    steps: ['System Settings → Privacy & Security', 'Scroll to Security and find the pika file you just opened', 'If you trust its source: Open Anyway → authenticate if asked → Open'],
    note: 'For unidentified-developer or unverifiable-app warnings only. This build is not Developer ID signed or notarized.',
    danger: 'For a damaged file, download a fresh copy and check again. Do not override malware or revoked-authorization warnings.',
    link: 'Step-by-step installation guide ↗', close: 'Got it'
  };
  let dialog;
  function show() {
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.setAttribute('aria-labelledby', 'pika-install-help-title');
      dialog.style.cssText = 'max-width:420px;width:calc(100% - 48px);box-sizing:border-box;padding:24px;border:1px solid #ccd5c5;border-radius:14px;background:#fafbf8;color:#30392c;font:14px/1.6 system-ui;box-shadow:0 12px 50px #0003';
      const heading = document.createElement('h2'); heading.id = 'pika-install-help-title'; heading.textContent = copy.title;
      heading.style.cssText = 'margin:0 0 12px;font-size:20px;line-height:1.4'; dialog.appendChild(heading);
      const text = value => {const p = document.createElement('p');p.textContent=value;dialog.appendChild(p);};
      text(copy.intro);
      const list = document.createElement('ol');
      for (const step of copy.steps) {const li=document.createElement('li');li.textContent=step;li.style.marginBottom='8px';list.appendChild(li);}
      dialog.appendChild(list);text(copy.note);text(copy.danger);
      const guide = document.createElement('a'); guide.href = ko ? '/install/ko/#gatekeeper' : '/install/#gatekeeper';
      guide.target = '_blank';guide.rel = 'noopener';guide.textContent = copy.link;dialog.appendChild(guide);
      const close = document.createElement('button');close.type='button';close.textContent=copy.close;close.autofocus=true;
      close.style.cssText='display:block;margin-top:18px;padding:8px 18px;font:inherit;border:1px solid #a9b79f;border-radius:8px;background:white;cursor:pointer';
      close.addEventListener('click',()=>dialog.close());dialog.appendChild(close);document.body.appendChild(dialog);
    }
    if (typeof dialog.showModal === 'function' && !dialog.open) dialog.showModal();
  }
  for (const link of document.querySelectorAll('a[href]')) {
    let url; try {url = new URL(link.href, location.href);} catch (_) {continue;}
    if (url.protocol !== 'https:' || url.hostname !== 'github.com' ||
        !/^\/Ezcho\/(?:no-sleep-pika|always-awake-mac)\/releases\/download\/[^/]+\/pika-[0-9.]+\.pkg$/.test(url.pathname)) continue;
    link.addEventListener('click', event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      // Keep this page and its instructions available while the attachment opens.
      link.target = '_blank';link.rel = 'noopener';show();
    });
  }
})();

/* Public release-asset totals, not visits or unique people. No tracking cookies. */
(() => {
  'use strict';
  const node = document.getElementById('download-count');
  if (!node) return;
  const api = 'https://api.github.com/repos/Ezcho/no-sleep-pika';
  const cacheKey = 'pika-downloads-v1';
  const valid = value => value && Number.isSafeInteger(value.total) && value.total >= 0 &&
    Number.isFinite(Date.parse(value.updatedAt));
  const render = value => {
    if (!valid(value)) return;
    node.textContent = `${new Intl.NumberFormat(document.documentElement.lang).format(value.total)} ${node.dataset.label}`;
    node.dataset.updatedAt = value.updatedAt;
    node.title = `GitHub · ${new Intl.DateTimeFormat(document.documentElement.lang, { dateStyle: 'medium', timeStyle: 'short' }).format(new Date(value.updatedAt))}`;
  };
  let cached;
  try { cached = JSON.parse(localStorage.getItem(cacheKey)); } catch (_) { /* Optional cache. */ }
  if (valid(cached)) render(cached);
  if (valid(cached) && Date.now() - Date.parse(cached.updatedAt) >= 0 &&
      Date.now() - Date.parse(cached.updatedAt) < 3600000) return;

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);
  async function pages(endpoint) {
    const all = [];
    for (let page = 1; page <= 100; page++) {
      const response = await fetch(`${api}/${endpoint}?per_page=100&page=${page}`, {
        signal: controller.signal, headers: { Accept: 'application/vnd.github+json' }, credentials: 'omit'
      });
      if (!response.ok) throw new Error('GitHub unavailable');
      const batch = await response.json();
      if (!Array.isArray(batch)) throw new Error('Invalid response');
      all.push(...batch);
      if (batch.length < 100) return all;
    }
    throw new Error('Incomplete total');
  }
  (async () => {
    try {
      const releases = await pages('releases');
      const assets = new Map();
      for (const release of releases) {
        if (release.draft) continue;
        if (!Number.isSafeInteger(release.id)) throw new Error('Invalid release');
        for (const asset of await pages(`releases/${release.id}/assets`)) {
          if (!/\.(dmg|zip|pkg)$/i.test(asset.name) || /uninstall/i.test(asset.name)) continue;
          if (!Number.isSafeInteger(asset.download_count) || asset.download_count < 0) throw new Error('Invalid count');
          assets.set(asset.id, asset.download_count);
        }
      }
      const total = [...assets.values()].reduce((sum, count) => sum + count, 0);
      const value = { total, updatedAt: new Date().toISOString() };
      if (!valid(value)) throw new Error('Invalid total');
      render(value);
      try { localStorage.setItem(cacheKey, JSON.stringify(value)); } catch (_) { /* Optional cache. */ }
    } catch (_) {
      // Keep the server-rendered snapshot (or cached total), never invent zero.
    } finally { clearTimeout(timeout); }
  })();
})();
