#!/usr/bin/env python3
import re, os
from urllib.parse import quote
BLOG="/Users/alexlamb/Desktop/AE_Exports/Projects/loopworker-site/blog"
DISQUS="loopworker"  # <-- Disqus shortname; confirm/create at disqus.com then this works site-wide

slugs=["photo-editing-apps-small-business","instagram-hashtag-strategy-2026",
 "content-creation-packages-small-business","free-ai-prompts-for-small-business",
 "restaurant-seasonal-marketing","how-to-hire-content-marketer","time-to-value","retention-cohorts"]

BTN="display:inline-block;padding:0.5rem 1rem;border:1px solid rgba(255,255,255,0.18);border-radius:6px;background:transparent;color:#DDD;font-size:0.85rem;font-weight:600;text-decoration:none;cursor:pointer;font-family:inherit;"

def block(url, title):
    t=quote(title); u=quote(url)
    return f'''<section class="engagement" style="max-width:720px;margin:0 auto;padding:2.5rem 24px;border-top:1px solid rgba(255,255,255,0.06);">
    <div style="display:flex;align-items:center;gap:0.7rem;flex-wrap:wrap;margin-bottom:1.6rem;">
        <span style="color:#999;font-size:0.95rem;">Was this helpful?</span>
        <button onclick="lwReact('yes')" style="{BTN}">Yes</button>
        <button onclick="lwReact('no')" style="{BTN}">Could be better</button>
        <span id="lw-eng-msg" style="color:#4CAF50;font-size:0.9rem;"></span>
    </div>
    <div style="display:flex;align-items:center;gap:0.7rem;flex-wrap:wrap;">
        <span style="color:#999;font-size:0.95rem;">Share</span>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={u}" target="_blank" rel="noopener" style="{BTN}" onclick="if(window.plausible)plausible('Share',{{props:{{net:'linkedin'}}}})">LinkedIn</a>
        <a href="https://twitter.com/intent/tweet?url={u}&text={t}" target="_blank" rel="noopener" style="{BTN}" onclick="if(window.plausible)plausible('Share',{{props:{{net:'x'}}}})">X</a>
        <button onclick="lwCopy(this)" style="{BTN}">Copy link</button>
    </div>
    <h2 style="margin-top:3rem;">Comments</h2>
    <p style="color:#999;">No agenda, just talk. Add your take or a question.</p>
    <div id="disqus_thread"></div>
    <button id="lw-load-comments" onclick="lwLoadComments()" style="{BTN}">Load comments</button>
    <noscript>Enable JavaScript to view the comments.</noscript>
</section>
<script>
function lwReact(v){{if(window.plausible)plausible('Helpful',{{props:{{value:v}}}});var m=document.getElementById('lw-eng-msg');if(m)m.textContent='thanks for the feedback';}}
function lwCopy(b){{navigator.clipboard.writeText(location.href);b.textContent='copied';}}
function lwLoadComments(){{var b=document.getElementById('lw-load-comments');if(b)b.style.display='none';window.disqus_config=function(){{this.page.url=location.href;this.page.identifier=location.pathname;}};var d=document.createElement('script');d.src='https://{DISQUS}.disqus.com/embed.js';d.setAttribute('data-timestamp',+new Date());document.body.appendChild(d);if(window.plausible)plausible('LoadComments');}}
</script>
'''

for slug in slugs:
    p=os.path.join(BLOG,slug+".html"); h=open(p,encoding="utf-8").read()
    if 'class="engagement"' in h: print(f"{slug}: already has engagement"); continue
    m=re.search(r'(<meta property="og:title" content=")([^"]*)(")', h)
    title=m.group(2) if m else "LoopWorker Signals"
    url=f"https://www.loopworker.com/blog/{slug}.html"
    blk=block(url,title)
    i=h.find('<section class="author-bio"')
    if i==-1: i=h.find('<footer')
    h=h[:i]+blk+"\n"+h[i:]
    open(p,"w",encoding="utf-8").write(h)
    print(f"{slug}: engagement injected (title='{title[:40]}...')")
print("DONE")
