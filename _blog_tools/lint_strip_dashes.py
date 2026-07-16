#!/usr/bin/env python3
import re, os
ROOT="/Users/alexlamb/Desktop/AE_Exports/Projects/loopworker-site"
files=[f"{ROOT}/blog/{s}.html" for s in [
 "photo-editing-apps-small-business","instagram-hashtag-strategy-2026",
 "content-creation-packages-small-business","free-ai-prompts-for-small-business",
 "restaurant-seasonal-marketing","how-to-hire-content-marketer","time-to-value","retention-cohorts"]]
files+=[f"{ROOT}/glossary/time-to-value.html", f"{ROOT}/glossary/retention-cohort.html"]

def strip(h):
    # prompt-number labels: "#1 — Title" / "#1 &mdash; Title" -> "#1: Title"
    h=re.sub(r'(#\d+)\s*(?:—|&mdash;)\s*', r'\1: ', h)
    # spaced em dash / mdash entity -> comma
    h=h.replace(' &mdash; ', ', ').replace('&mdash;', ', ')
    h=h.replace(' — ', ', ').replace(' —', ',').replace('— ', ', ').replace('—', ', ')
    # en dash used as separator (keep numeric ranges like 3–5 -> 3-5)
    h=re.sub(r'(\d)\s*–\s*(\d)', r'\1-\2', h)
    h=h.replace(' – ', ', ').replace('–', '-')
    # tidy artifacts
    h=h.replace(' ,', ',').replace(',,', ',').replace(',  ', ', ')
    h=re.sub(r',\s*,', ',', h)
    return h

for p in files:
    if not os.path.exists(p): print("SKIP missing",p); continue
    h=open(p,encoding="utf-8").read()
    before=h.count('—')+h.count('&mdash;')+h.count('–')
    h2=strip(h)
    after=h2.count('—')+h2.count('&mdash;')+h2.count('–')
    open(p,"w",encoding="utf-8").write(h2)
    print(f"{os.path.basename(p)}: dashes {before} -> {after}")
print("DONE")
