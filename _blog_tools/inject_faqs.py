#!/usr/bin/env python3
import re, os, json
BLOG="/Users/alexlamb/Desktop/AE_Exports/Projects/loopworker-site/blog"

def card(q,a):
    return f'    <div class="idea-card fade-up">\n        <div class="idea-num">FAQ</div>\n        <div class="idea-title">{q}</div>\n        <div class="idea-detail">{a}</div>\n    </div>'
def section(faqs):
    return "\n".join(['    <h2 class="fade-up">Frequently Asked Questions</h2>']+[card(q,a) for q,a in faqs])

FAQS={
 "photo-editing-apps-small-business":[
   ("What is the best free photo editor for small business?","Lightroom Mobile (free tier) is the best all-around free editor, handling roughly 90% of small business needs. Pair it with Snapseed for selective edits, Canva for graphics, and Pixlr or Photopea for browser-based, Photoshop-style work."),
   ("Do I need to buy Photoshop?","No. For nearly all small business work a Photoshop subscription is overkill. Free browser editors like Pixlr and Photopea handle compositing, retouching, and background removal at no cost."),
   ("What is the 5-step edit every photo needs?","Crop and straighten, fix exposure, adjust white balance, lift shadows and tame highlights, then add a touch of contrast and sharpening. It takes 60 to 90 seconds per photo."),
 ],
 "free-ai-prompts-for-small-business":[
   ("Do these AI prompts work with ChatGPT and Claude?","Yes. Every prompt is model-agnostic. Paste it into ChatGPT, Claude, Gemini, or any chat AI, replace the bracketed details, and run it."),
   ("How do I get better results from AI prompts?","Be specific. Fill every bracket with real details (your product, audience, tone), give an example if you have one, and tell the AI what good looks like. Vague input is the main cause of generic output."),
   ("Are these prompts really free?","Yes. All 100 are free to copy and use. No signup, no course, and no paid tool required."),
   ("What can small businesses use AI prompts for?","Social captions, email marketing, blog outlines, product descriptions, ad copy, brand strategy, customer service replies, and content planning. The 100 here are grouped into those eight categories."),
 ],
 "restaurant-seasonal-marketing":[
   ("How far ahead should a restaurant plan promotions?","Outline the full year, then lock seasonal campaigns 4 to 6 weeks out: build the promo 4 to 6 weeks before, shoot content 2 to 3 weeks before, and start posting about 2 weeks before the date."),
   ("What should a restaurant marketing calendar include?","Key dates and holidays, local events, seasonal menu changes, your own milestones like anniversaries and openings, plus the social posts, emails, and offers that support each one."),
   ("What promotions fill slow nights?","Target the slow window directly: a weekday happy hour, a themed night such as Taco Tuesday or family night with kids eating free, or a limited seasonal special that gives people a reason to come in on a quiet day."),
   ("Do restaurant marketing calendars actually work?","Yes. Restaurants that run a structured calendar typically see higher engagement and steadier covers, because promotions are planned, photographed, and posted on time instead of improvised."),
 ],
}

for slug,faqs in FAQS.items():
    p=os.path.join(BLOG,slug+".html"); h=open(p,encoding="utf-8").read()
    rep=[]
    # 1) insert visible FAQ section before Related Reading (else before </article>)
    if 'Frequently Asked Questions</h2>' in h:
        rep.append("visible-FAQ already present")
    else:
        sec=section(faqs)+"\n\n"
        m=re.search(r'\s*<h2[^>]*>Related Reading</h2>', h)
        if m:
            h=h[:m.start()]+"\n"+sec+h[m.start():].lstrip("\n"); rep.append("FAQ before Related Reading")
        else:
            i=h.rfind("</article>")
            h=h[:i]+sec+h[i:]; rep.append("FAQ before </article>")
    # 2) replace FAQPage schema mainEntity with real Qs
    me=json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs])
    new_h, n = re.subn(r'("@type":\s*"FAQPage",\s*"mainEntity":\s*)\[[^\]]*\]',
                       lambda mm: mm.group(1)+me, h, flags=re.S)
    if n: h=new_h; rep.append(f"schema replaced x{n}")
    else: rep.append("schema NOT FOUND")
    open(p,"w",encoding="utf-8").write(h)
    print(f"{slug}: "+" | ".join(rep))
print("DONE")
