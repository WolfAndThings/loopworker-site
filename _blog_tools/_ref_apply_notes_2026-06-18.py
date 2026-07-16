#!/usr/bin/env python3
import re, os, json
ROOT="/Users/alexlamb/Desktop/AE_Exports/Projects/loopworker-site"
BLOG=f"{ROOT}/blog"
tpl=open(f"{BLOG}/photo-editing-apps-small-business.html",encoding="utf-8").read()
STYLE=re.search(r'<style>.*?</style>', tpl, re.S).group(0)
TAIL=tpl[tpl.index('<section class="author-bio"'):]
NAV='''<nav class="site-nav">
    <a href="/" class="nav-logo">LoopWorker</a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle-checkbox" aria-label="Toggle navigation">
    <label for="nav-toggle" class="nav-toggle-label"><span></span><span></span><span></span></label>
    <div class="nav-links">
        <a href="/sprint.html">Sprints</a>
        <a href="/pricing.html">Pricing</a>
        <a href="/blog/">Signals</a>
        <a href="/book.html" class="nav-cta">Book a Call</a>
    </div>
</nav>'''
def card(num,title,detail):
    return f'    <div class="idea-card fade-up">\n        <div class="idea-num">{num}</div>\n        <div class="idea-title">{title}</div>\n        <div class="idea-detail">{detail}</div>\n    </div>'
def takeaways(items):
    lis="".join(f"<li>{i}</li>" for i in items)
    return ('    <div class="key-takeaways fade-up" style="background:#0d1117;border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:1.5rem 2rem;margin:2rem 0 3rem;">\n'
            '        <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#666;margin-bottom:0.8rem;font-weight:600;">Key Takeaways</div>\n'
            f'        <ul style="margin:0;padding-left:1.2rem;color:#CCC;">{lis}</ul>\n    </div>')
def qa(text):
    return ('    <div class="quick-answer fade-up" style="background:#0d1117;border-left:3px solid #4CAF50;border-radius:6px;padding:1.2rem 1.6rem;margin:0 0 2.5rem;">\n'
            '        <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#4CAF50;margin-bottom:0.5rem;font-weight:700;">Quick Answer</div>\n'
            f'        <p style="margin:0;color:#E8E8E8;">{text}</p>\n    </div>')
def cta(text):
    return ('    <div class="cta-section">\n'
            f'        <p>{text}</p>\n'
            '        <div class="cta-buttons">\n'
            '            <a href="/sprint.html" class="cta-btn">See the Sprint</a>\n'
            '            <a href="/book.html" class="cta-btn-alt">Book a Call</a>\n        </div>\n    </div>')
def faq_section(faqs):
    return "\n".join(['    <h2 class="fade-up">Frequently Asked Questions</h2>']+[card("FAQ",q,a) for q,a in faqs])
def related(items):
    lis="".join(f'        <li><a href="{h}">{t}</a></li>\n' for t,h in items)
    return f'    <h2 class="fade-up">Related Reading</h2>\n    <ul>\n{lis}    </ul>'

# ============ REBUILD INSTAGRAM POST (anti-hashtag pivot) ============
ig={"slug":"instagram-hashtag-strategy-2026","section":"Distribution","read":9,
 "seo":"Instagram Hashtag Strategy 2026: Why We Stopped Using Them (and What Works Now) | LoopWorker",
 "social":"Instagram Hashtag Strategy 2026: Why We Stopped Using Them (and What Works Now)",
 "h1":"Instagram Hashtag Strategy 2026: Why We Stopped Using Them",
 "desc":"Hashtags barely affect Instagram reach in 2026. Why we stopped using them, what actually drives discovery now (keyword captions, Reels, saves and shares), and the 3-5 tag rule if you still want them.",
 "keywords":"instagram hashtag strategy 2026, do hashtags still work, instagram reach 2026, instagram seo, how many hashtags instagram, instagram discovery, what replaced hashtags",
 "subtitle":"Instagram quietly stopped rewarding hashtags. We dropped them and reach went up, not down. Here is what actually drives discovery in 2026, and the only hashtag rule still worth keeping.",
 "qa":"Hashtags barely move reach on Instagram in 2026. What drives discovery now is keyword-rich captions (Instagram SEO), Reels, and saves, shares, and sends. If you still use tags, keep it to 3-5 descriptive ones in the caption.",
 "takeaways":["Hashtags are now a weak ranking signal, not a reach engine","Instagram SEO: keywords in captions and alt text","Reels are how strangers actually find you","Saves, shares, and sends beat likes","The 3-5 tag rule, if you use them at all"],
 "body":"\n".join([
   '    <p class="fade-up">For years the advice was the same: stack 30 hashtags and pray. That era is over. Instagram now works like a search and recommendation engine, and hashtags are a minor signal inside it. We stopped using big hashtag sets across the accounts we run and reach held or climbed. Here is where the reach actually comes from now.</p>',
   '    <h2 class="fade-up">What Actually Changed</h2>',
   '    <p>Instagram shifted from a follower-feed to a recommendation engine. Most reach on a good post now comes from non-followers served by the algorithm and by search, not from people browsing a hashtag. The platform reads your caption, your on-screen text, your audio, and how people respond, then decides who else should see it. Thirty hashtags do not help that decision. They can even read as spam.</p>',
   '    <h2 class="fade-up">Instagram SEO: The New Hashtags</h2>',
   '    <p>People search Instagram like Google now. Your job is to tell Instagram what your post is about in plain words.</p>',
   card("Write keyword-rich captions","Say what the post is, for whom, in the first line.","\"Easy weeknight ramen for busy parents\" beats \"vibes.\" The words in your caption are now the index Instagram searches against."),
   card("Fill in alt text","Add descriptive alt text on every post (Advanced settings).","It is a direct, literal description of the image for search and accessibility. Almost nobody does it, which is exactly why it helps."),
   card("Name your niche out loud","Use the plain terms your buyer would type.","If you are a \"bookkeeper for creative agencies,\" say that. Instagram matches searches to accounts that state what they are."),
   cta("Instagram SEO only works if you know the words your buyers actually use. That is a market-intelligence question, not a guess. A LoopWorker Sprint pulls the exact language your category searches and responds to, so your captions land. Start with a Surface scan."),
   '    <h2 class="fade-up">Reels Are the Discovery Engine</h2>',
   '    <p>If you want strangers to find you, Reels are the lever, not tags. A strong hook in the first second, on-screen keywords, and a reason to watch to the end will out-reach any hashtag set. Post Reels consistently and let the caption do the SEO work.</p>',
   '    <h2 class="fade-up">The Signals That Actually Rank You</h2>',
   card("Sends and shares","The strongest signal in 2026.","A post people DM to a friend tells Instagram it is worth spreading. Make content worth sending, not just liking."),
   card("Saves","Close second.","Saves say \"useful enough to come back to.\" Guides, lists, and how-tos earn them."),
   card("Watch time and replays","For Reels, completion is everything.","Short, tight, loopable. The first second decides the next thousand views."),
   card("Profile visits and follows","Proof the post made someone want more.","A clear hook plus a clear niche turns a view into a follow."),
   '    <h2 class="fade-up">If You Still Want to Use Hashtags</h2>',
   '    <p>Fine. Use 3 to 5 specific, descriptive hashtags in the caption, matched to the actual content. Skip the giant generic tags (#love, #instagood) and skip the 30-tag blocks. That is the entire modern hashtag strategy. Shadowban panic is mostly myth; irrelevant spammy tags are the real risk.</p>',
   '    <h2 class="fade-up">What We Do Instead</h2>',
   '    <p>We spend the time we used to spend building hashtag sets on two things: finding the exact words our audience searches, and making content worth saving and sending. That is the whole game now. Hashtags were a proxy for "help the algorithm understand and spread this." Captions, Reels, and engagement signals do that job better.</p>',
 ]),
 "cta":"Reach follows relevance, and relevance follows language. A LoopWorker Sprint reads what your category actually searches and shares, so your content gets found without gaming tags. Start with a Surface scan.",
 "faqs":[
   ("Do hashtags still work on Instagram in 2026?","Barely. Hashtags are now a weak signal rather than a reach engine. Discovery comes mostly from keyword-rich captions, Reels, and engagement signals like saves, shares, and sends. A few relevant tags do no harm, but they are not a strategy."),
   ("How many hashtags should I use on Instagram?","If you use them at all, 3 to 5 specific, descriptive hashtags in the caption is plenty. Large 20 to 30 tag blocks and generic mega-tags can read as spam and do little for reach."),
   ("What replaced hashtags for Instagram reach?","Instagram SEO. The platform reads your caption text, alt text, on-screen text, and audio to decide who sees your post, and it rewards saves, shares, sends, and watch time. Plain, keyword-rich captions and strong Reels now do what hashtags used to."),
   ("Do hashtags cause shadowbans?","Mostly a myth. The real risk is using irrelevant or spammy tags, or recycling the exact same large block on every post. Relevant tags in small numbers are safe; they are just not very powerful anymore."),
 ],
 "related":[("What category positioning actually means in 2026","/blog/what-category-positioning-means.html"),
            ("Buyer language pulls: read what your category is saying","/blog/buyer-language-pulls.html"),
            ("100 free AI prompts for small business","/blog/free-ai-prompts-for-small-business.html"),
            ("How to grow Instagram followers organically","/blog/how-to-grow-instagram-followers-organically.html")],
}
faq_ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in ig["faqs"]]}
art_ld={"@context":"https://schema.org","@type":"Article","headline":ig["social"],"author":{"@type":"Person","name":"Alex Lamb"},"publisher":{"@type":"Organization","name":"LoopWorker"},"datePublished":"2026-06-18","dateModified":"2026-06-18","description":ig["desc"],"mainEntityOfPage":{"@type":"WebPage","@id":f'https://www.loopworker.com/blog/{ig["slug"]}.html'}}
bc_ld={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.loopworker.com/"},{"@type":"ListItem","position":2,"name":"Signals","item":"https://www.loopworker.com/blog/"},{"@type":"ListItem","position":3,"name":ig["h1"],"item":f'https://www.loopworker.com/blog/{ig["slug"]}.html'}]}
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
    <script defer data-domain="loopworker.com" src="https://plausible.io/js/script.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ig["seo"]}</title>
    <meta name="description" content="{ig["desc"]}">
    <meta name="keywords" content="{ig["keywords"]}">
    <meta name="author" content="Alex Lamb">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
    <link rel="canonical" href="https://www.loopworker.com/blog/{ig["slug"]}.html">
    <meta property="og:title" content="{ig["social"]}">
    <meta property="og:description" content="{ig["desc"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.loopworker.com/blog/{ig["slug"]}.html">
    <meta property="og:site_name" content="LoopWorker">
    <meta property="article:author" content="Alex Lamb">
    <meta property="article:section" content="{ig["section"]}">
    <meta property="article:published_time" content="2026-06-18">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{ig["social"]}">
    <meta name="twitter:description" content="{ig["desc"]}">
    <script type="application/ld+json">{json.dumps(art_ld)}</script>
    <script type="application/ld+json">{json.dumps(bc_ld)}</script>
    <script type="application/ld+json">{json.dumps(faq_ld)}</script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
{STYLE}
</head>
<body>
{NAV}
<article class="article-container">
    <div class="article-meta fade-up">June 2026 &middot; Alex Lamb &middot; {ig["read"]} min read</div>
    <h1 class="article-title fade-up">{ig["h1"]}</h1>
    <p class="article-subtitle fade-up">{ig["subtitle"]}</p>
{qa(ig["qa"])}
{takeaways(ig["takeaways"])}

{ig["body"]}

{faq_section(ig["faqs"])}

{cta(ig["cta"])}
{related(ig["related"])}
</article>

{TAIL}'''
open(f'{BLOG}/{ig["slug"]}.html',"w",encoding="utf-8").write(html)
print(f'rebuilt instagram-hashtag-strategy-2026.html ({len(html.splitlines())}L)')

# ============ QUICK-ANSWER into the other 7 ============
QA={
 "photo-editing-apps-small-business":"You don't need to pay for Photoshop. Free editors like Lightroom Mobile, Snapseed, Canva, and Pixlr handle around 90% of small business photo work, and the only paid pick worth considering is a $3 object remover.",
 "content-creation-packages-small-business":"Content packages run from about $500 to $10,000 a month. Price mostly reflects volume, video, and whether strategy and posting are included, not quality, so match the tier to the outcome you need rather than the sticker.",
 "free-ai-prompts-for-small-business":"Generic prompts get generic results. The fix is specific, structured prompts; the 100 below are written to do real marketing, sales, and ops work and paste straight into ChatGPT or Claude.",
 "restaurant-seasonal-marketing":"Slow nights are usually a planning problem, not a food problem. A month-by-month promotional calendar built around seasons, local events, and your own milestones gives customers a reason to show up all year.",
 "how-to-hire-content-marketer":"A content writer produces words; a content marketer owns strategy, distribution, and the result. Hire for judgment and measurement, screen with work samples tied to a number, and run a 30-day paid trial before committing.",
 "time-to-value":"Time to value is the gap between signup and a customer's first real win. Customers who reach it within about 14 days retain at 80% or more, while those who miss 30 days retain at only 35 to 50%, so shortening it is the highest-leverage retention move.",
 "retention-cohorts":"A retention cohort groups customers by when they joined and tracks who stays. The shape of the curve, declining, flattening, or smiling, tells you whether you have product-market fit or a leaky bucket.",
}
for slug,ans in QA.items():
    p=f"{BLOG}/{slug}.html"; h=open(p,encoding="utf-8").read()
    if 'class="quick-answer"' in h: print(f"  {slug}: QA already present"); continue
    block=qa(ans)
    # insert after article-subtitle paragraph if present, else after first <p> following h1
    m=re.search(r'<p class="article-subtitle[^"]*">.*?</p>', h, re.S)
    if m:
        h=h[:m.end()]+"\n"+block+h[m.end():]
    else:
        m2=re.search(r'(<h1[^>]*>.*?</h1>)', h, re.S)
        h=h[:m2.end()]+"\n"+block+h[m2.end():]
    open(p,"w",encoding="utf-8").write(h)
    print(f"  {slug}: QA inserted ({'subtitle' if m else 'h1'} anchor)")

# ============ FIX PHOTO POST stale schema ============
pp=f"{BLOG}/photo-editing-apps-small-business.html"; h=open(pp,encoding="utf-8").read()
h=h.replace('"description": "12 photo editing apps compared for small business use in 2026.",',
            '"description": "The best free photo editors for small business in 2026, ranked by the job they do best, plus the 5-step edit every photo needs.",')
h=h.replace('"name": "Best Photo Editing Apps for Small Business (2026)", "item"',
            '"name": "Best Free Photo Editor for Small Business (2026)", "item"')
h=h.replace('"name": "Best Photo Editing Apps for Small Business: Free and Paid (2026)",',
            '"name": "Best Free Photo Editor for Small Business: 7 Tools That Beat Paying for Photoshop (2026)",')
# replace weak FAQ mainEntity with real Qs
new_faq='''"mainEntity": [
        { "@type": "Question", "name": "What is the best free photo editor for small business?", "acceptedAnswer": { "@type": "Answer", "text": "Lightroom Mobile (free tier) is the best all-around free editor for small business, handling roughly 90% of needs. Pair it with Snapseed for selective edits, Canva for graphics, and Pixlr or Photopea for browser-based, Photoshop-style work." } },
        { "@type": "Question", "name": "Do I need to buy Photoshop?", "acceptedAnswer": { "@type": "Answer", "text": "No. For nearly all small business work a Photoshop subscription is overkill. Free browser editors like Pixlr and Photopea handle compositing, retouching, and background removal at no cost." } },
        { "@type": "Question", "name": "What is the 5-step edit every photo needs?", "acceptedAnswer": { "@type": "Answer", "text": "Crop and straighten, fix exposure, adjust white balance, lift shadows and tame highlights, then add a touch of contrast and sharpening. It takes 60 to 90 seconds per photo." } }
    ]'''
h=re.sub(r'"mainEntity": \[\s*\{\s*"@type": "Question",\s*"name": "The 5-Step Edit Checklist".*?\}\s*\]', new_faq, h, flags=re.S)
open(pp,"w",encoding="utf-8").write(h)
print("  photo schema cleaned")

# ============ FIX index instagram card ============
idx=f"{BLOG}/index.html"; h=open(idx,encoding="utf-8").read()
h=h.replace("<h2>Instagram Hashtag Strategy 2026: Why 5 Tags Beat 30</h2>",
            "<h2>Instagram Hashtag Strategy 2026: Why We Stopped Using Them</h2>")
h=h.replace("<p>Instagram changed the rules. Precise beats plentiful. The research method plus 200 tags by industry.</p>",
            "<p>Hashtags barely move reach now. What actually drives discovery in 2026: keyword captions, Reels, and saves.</p>")
open(idx,"w",encoding="utf-8").write(h)
print("  index instagram card updated")
print("DONE")
