#!/usr/bin/env python3
import re, os, json
B="/Users/alexlamb/Desktop/AE_Exports/Projects/loopworker-site/blog"
tpl=open(os.path.join(B,"photo-editing-apps-small-business.html"),encoding="utf-8").read()
STYLE=re.search(r'<style>.*?</style>', tpl, re.S).group(0)
TAIL=tpl[tpl.index('<section class="author-bio"'):]   # author-bio + footer + script + </body></html>

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

def cta(text):
    return ('    <div class="cta-section">\n'
            f'        <p>{text}</p>\n'
            '        <div class="cta-buttons">\n'
            '            <a href="/sprint.html" class="cta-btn">See the Sprint</a>\n'
            '            <a href="/book.html" class="cta-btn-alt">Book a Call</a>\n'
            '        </div>\n    </div>')

def faq_section(faqs):
    out=['    <h2 class="fade-up">Frequently Asked Questions</h2>']
    for q,a in faqs: out.append(card("FAQ",q,a))
    return "\n".join(out)

def related(items):
    lis="".join(f'        <li><a href="{h}">{t}</a></li>\n' for t,h in items)
    return f'    <h2 class="fade-up">Related Reading</h2>\n    <ul>\n{lis}    </ul>'

def page(p):
    faq_ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faqs"]]}
    art_ld={"@context":"https://schema.org","@type":"Article","headline":p["social"],
        "author":{"@type":"Person","name":"Alex Lamb"},"publisher":{"@type":"Organization","name":"LoopWorker"},
        "datePublished":"2026-06-17","dateModified":"2026-06-17","description":p["desc"],
        "mainEntityOfPage":{"@type":"WebPage","@id":f'https://www.loopworker.com/blog/{p["slug"]}.html'}}
    bc_ld={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://www.loopworker.com/"},
        {"@type":"ListItem","position":2,"name":"Signals","item":"https://www.loopworker.com/blog/"},
        {"@type":"ListItem","position":3,"name":p["h1"],"item":f'https://www.loopworker.com/blog/{p["slug"]}.html'}]}
    head=f'''<!DOCTYPE html>
<html lang="en">
<head>
    <script defer data-domain="loopworker.com" src="https://plausible.io/js/script.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p["seo"]}</title>
    <meta name="description" content="{p["desc"]}">
    <meta name="keywords" content="{p["keywords"]}">
    <meta name="author" content="Alex Lamb">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
    <link rel="canonical" href="https://www.loopworker.com/blog/{p["slug"]}.html">
    <meta property="og:title" content="{p["social"]}">
    <meta property="og:description" content="{p["desc"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.loopworker.com/blog/{p["slug"]}.html">
    <meta property="og:site_name" content="LoopWorker">
    <meta property="article:author" content="Alex Lamb">
    <meta property="article:section" content="{p["section"]}">
    <meta property="article:published_time" content="2026-06-17">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{p["social"]}">
    <meta name="twitter:description" content="{p["desc"]}">
    <script type="application/ld+json">{json.dumps(art_ld)}</script>
    <script type="application/ld+json">{json.dumps(bc_ld)}</script>
    <script type="application/ld+json">{json.dumps(faq_ld)}</script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
{STYLE}
</head>
<body>
{NAV}
<article class="article-container">
    <div class="article-meta fade-up">June 2026 &middot; Alex Lamb &middot; {p["read"]} min read</div>
    <h1 class="article-title fade-up">{p["h1"]}</h1>
    <p class="article-subtitle fade-up">{p["subtitle"]}</p>
{takeaways(p["takeaways"])}

{p["body"]}

{cta(p["cta"])}
{related(p["related"])}
</article>

{TAIL}'''
    open(os.path.join(B,p["slug"]+".html"),"w",encoding="utf-8").write(head)
    print(f'wrote {p["slug"]}.html ({len(head.splitlines())}L)')

# ---------------- POST 1 ----------------
p1={"slug":"how-to-hire-content-marketer","section":"Marketing","read":11,
 "seo":"How to Hire a Content Marketer Who Grows Pipeline, Not Just Writes Posts (2026) | LoopWorker",
 "social":"How to Hire a Content Marketer Who Grows Pipeline, Not Just Writes Posts",
 "h1":"How to Hire a Content Marketer Who Grows Pipeline, Not Just Writes Posts",
 "desc":"Most businesses hire a writer and call it a content marketer. They are not the same job. How to scope the role, screen for growth skills, what to pay in 2026, and the questions that filter 90% of applicants.",
 "keywords":"how to hire content marketer, hire a content marketer, content marketer vs content writer, content marketing salary, freelance content marketer, content marketer interview questions",
 "subtitle":"Most businesses hire a writer and call it a content marketer. The two are not the same job — and confusing them costs a quarter of pipeline. Here's how to scope the role, where to find the right person, and the interview questions that separate writers from marketers.",
 "takeaways":["Writer vs. content marketer: the costly confusion","In-house vs. freelance vs. agency, and when each wins","The 4 questions that filter 90% of applicants","What to pay in 2026","The 30-day paid trial that proves it"],
 "body":"\n".join([
   '    <p class="fade-up">A content writer turns a brief into words. A content marketer decides what to write, who it is for, where it goes, and whether it moved a number. One is a production role. The other is a growth role. If you hire the first while expecting the second, you get a tidy blog and a flat pipeline.</p>',
   '    <h2 class="fade-up">Writer vs. Content Marketer</h2>',
   '    <p>A writer spends 80-90% of the day writing. A content marketer spends most of the day on research, strategy, distribution, and measurement — and writes (or briefs writers) with the time that is left. Decide which problem you have before you post a job. If you already know what to publish and just need volume, hire a writer. If you need someone to figure out what wins and own the result, hire a marketer.</p>',
   card("The difference in one line","Writer answers \"can you write this?\" Marketer answers \"what should we publish, and did it work?\"","A writer is judged on output quality. A marketer is judged on leads, signups, pipeline, or whatever number the content is supposed to move. Pay for the judgment, not just the prose."),
   '    <h2 class="fade-up">Decide What You Actually Need</h2>',
   card("In-house","Best when content is core to growth and you want context to compound.","Highest cost and slowest to hire, but they learn your category, product, and customers deeply. Worth it once content is a primary channel."),
   card("Freelance / fractional","Best when you need senior strategy without a full-time salary.","Fast to start, flexible, often more experienced than what you could hire full-time on the same budget. The right first move for most small businesses."),
   card("Agency","Best when you need a whole stack (strategy + writing + design + distribution) at once.","More expensive per output, less embedded, but turnkey. Good when you have budget and no internal owner."),
   cta("Before you hire anyone, know what your category actually rewards. Most content hires spend month one guessing. A LoopWorker Sprint hands your new marketer the evidence — the language, the angles, the gaps — so they start from a map, not a hunch. Start with a Surface scan."),
   '    <h2 class="fade-up">The 4 Questions That Filter 90%</h2>',
   card("1","\"Walk me through a piece you made and the number it moved.\"","Writers describe the piece. Marketers describe the goal, the result, and what they changed when it underperformed. If there is no number, there is no marketing."),
   card("2","\"How would you decide what we publish next quarter?\"","Listen for a method — audience research, search demand, sales-call mining, competitive gaps. \"I'd brainstorm topics\" is a writer answer."),
   card("3","\"What have you killed, and why?\"","Good marketers cut formats and channels that did not work. Someone who has never stopped doing something has never been measuring."),
   card("4","\"How do you work with sales and product?\"","Content that grows pipeline is wired to the rest of the business. A marketer who has never talked to sales will write content nobody can sell against."),
   '    <h2 class="fade-up">What to Pay in 2026</h2>',
   '    <p>Rough US ranges. Freelance/fractional content marketers run roughly $50-150/hr or $2,000-6,000/mo for a defined scope. In-house salaries cluster around $55,000-85,000, higher in major markets or for senior strategists. Agencies run $2,000-10,000+/mo depending on volume and how much strategy is included. Pay more for judgment and measurement; pay less for pure production you can direct yourself.</p>',
   '    <h2 class="fade-up">The 30-Day Test</h2>',
   '    <p>Do not hire on a portfolio alone. Give the top candidate a small paid trial: a real brief, access to one channel, and a single metric to move. In 30 days a marketer will show you a plan, a published piece, and a read on what happened. A writer will show you a published piece. That gap is the entire hire.</p>',
 ]),
 "cta":"Hiring is step two. Step one is knowing what your market actually wants to hear — so whoever you hire is not guessing on your payroll. A LoopWorker Sprint gives you that read in days. Start with a Surface scan.",
 "faqs":[
   ("What is the difference between a content writer and a content marketer?","A content writer produces the words. A content marketer decides strategy, audience, distribution, and measurement, then writes or briefs writers. A writer is judged on output; a marketer is judged on the business result the content drives."),
   ("How much does a content marketer cost in 2026?","Freelance and fractional content marketers typically run $50-150/hr or $2,000-6,000/mo for a defined scope. In-house salaries cluster around $55,000-85,000. Agencies range from $2,000 to $10,000+ per month depending on volume and strategy."),
   ("Should I hire freelance or in-house?","Start freelance or fractional if content is not yet your primary growth channel — you get senior strategy without a full-time salary. Move in-house once content is core and you want category context to compound over time."),
   ("How do I know if a content marketer is good?","Ask for a piece they made and the number it moved, how they would decide what to publish, what they have killed, and how they work with sales and product. Then run a 30-day paid trial with one real metric to move."),
 ],
 "related":[("What category positioning actually means in 2026","/blog/what-category-positioning-means.html"),
            ("Buyer language pulls: read what your category is saying","/blog/buyer-language-pulls.html"),
            ("Content creation packages: what you actually pay","/blog/content-creation-packages-small-business.html"),
            ("How much does social media management cost?","/blog/how-much-does-social-media-management-cost.html")],
}

# ---------------- POST 2 ----------------
p2={"slug":"time-to-value","section":"Growth Metrics","read":10,
 "seo":"Time to Value: The SaaS Metric That Decides Who Churns (2026 Guide) | LoopWorker",
 "social":"Time to Value: The SaaS Metric That Decides Who Churns",
 "h1":"Time to Value: The Metric That Decides Who Churns",
 "desc":"Customers who reach first value in 14 days retain at 80%+. Those who do not hit it in 30 days retain at 35-50%. How to measure time to value, what good looks like in 2026, and five ways to shorten it.",
 "keywords":"time to value, time to value SaaS, TTV, time to first value, reduce time to value, activation metric, onboarding metric, time to value benchmark",
 "subtitle":"Customers rarely churn because the product is bad. They churn because they never hit the moment it pays off. Reach first value inside 14 days and retention runs 80%+; miss 30 days and it falls to 35-50%. Here's how to measure time to value, what good looks like, and how to compress it.",
 "takeaways":["Time to value, defined (and the two moments that matter)","Why TTV decides retention more than features do","How to instrument and measure it","2026 benchmarks","Five levers to shorten it"],
 "body":"\n".join([
   '    <p class="fade-up">Time to value (TTV) is the gap between a customer first touching your product and the moment they feel it pay off. It is the most honest leading indicator you have: if people are not reaching value fast, no feature, discount, or email cadence will save the retention number downstream.</p>',
   '    <h2 class="fade-up">What Time to Value Actually Means</h2>',
   '    <p>There are two moments, and teams confuse them constantly.</p>',
   card("Time to first value","The first real win — the \"oh, this works\" moment.","A sent campaign, a first report, a first booking. This is the one that prevents early churn. Optimize it ruthlessly."),
   card("Time to full value","When the product is woven into the workflow and switching would hurt.","Slower, deeper, and tied to expansion and referrals. You earn it after first value, not instead of it."),
   '    <h2 class="fade-up">Why TTV Decides Retention</h2>',
   '    <p>The numbers are blunt. Across SaaS benchmarks, customers who reach first value within about 14 days retain at roughly 80% or higher at month 12. Customers who do not hit first value inside the first 30 days retain at 35-50%. The first two weeks are not onboarding housekeeping — they are where most of your churn is decided.</p>',
   cta("Slow time to value is often a positioning problem, not a product problem — you attracted buyers the product was never built to help. A LoopWorker Sprint reads which buyers actually activate and what language pulled them in, so you acquire more of the ones who stick. Start with a Surface scan."),
   '    <h2 class="fade-up">How to Measure It</h2>',
   card("1. Define the value event","Name the single action that equals \"first value\" for your product.","Be specific and observable — \"published first post,\" not \"engaged.\" If you cannot name it, you cannot shorten it."),
   card("2. Instrument it","Track the timestamp from signup to that event.","Most product analytics tools (and a spreadsheet, at first) can do this. The point is a number, not a vibe."),
   card("3. Cohort it","Group by signup week and watch TTV trend.","One blended average hides the story. Cohorts show whether changes you ship actually move the curve. (See our guide on retention cohorts.)"),
   '    <h2 class="fade-up">2026 Benchmarks</h2>',
   '    <p>For most self-serve SaaS, a healthy time to first value is 1-3 days; many users now expect it within a day or two of signing up. Complex or sales-led products run longer, but the principle holds: every day between signup and first value is a day the customer can quit. Measure against your own trend first, the industry second.</p>',
   '    <h2 class="fade-up">Five Levers to Shorten It</h2>',
   card("1","Delete setup steps","Every required field, integration, or config before first value is a place to lose people. Cut what is not load-bearing."),
   card("2","Guide, do not tour","Replace passive product tours with a guided path to the one value event. Show, prompt, get them to do it."),
   card("3","Pre-fill and template","Start users with sample data, templates, or a done example so value appears before work does."),
   card("4","Nudge to the milestone","Trigger email/in-app nudges aimed only at the value event — not generic \"tips.\""),
   card("5","Concierge the high-value","For bigger accounts, a human who gets them to first value fast pays for itself in retention."),
 ]),
 "cta":"The fastest way to shorten time to value is to stop attracting the wrong customer. A LoopWorker Sprint shows you which buyers actually activate and the language that pulls them — so retention starts at acquisition. Start with a Surface scan.",
 "faqs":[
   ("What is a good time to value?","For most self-serve SaaS, a healthy time to first value is 1-3 days, and many users expect it within a day or two of signup. Sales-led or complex products run longer. Measure against your own trend first and industry benchmarks second."),
   ("How do you measure time to value?","Define a single observable value event (the customer's first real win), track the time from signup to that event, and analyze it by signup cohort rather than as one blended average so you can see whether changes actually move it."),
   ("What is the difference between time to value and onboarding?","Onboarding is the process; time to value is the outcome. Good onboarding exists only to shorten time to value. You can have a polished onboarding flow and still have slow TTV if it does not drive users to their first real win."),
   ("How does time to value affect churn?","Strongly. Customers who reach first value within roughly 14 days tend to retain at 80%+ at one year, while those who miss it in the first 30 days retain at only 35-50%. Most early churn is decided in the first two weeks."),
 ],
 "related":[("Retention cohorts: how to read the curve that predicts churn","/blog/retention-cohorts.html"),
            ("The 6-month visibility cycle","/blog/visibility-cycle.html"),
            ("What category positioning actually means in 2026","/blog/what-category-positioning-means.html"),
            ("How to read a pricing band","/blog/how-to-read-a-pricing-band.html")],
}

# ---------------- POST 3 ----------------
p3={"slug":"retention-cohorts","section":"Growth Metrics","read":10,
 "seo":"Retention Cohorts: How to Read the Curve That Predicts Churn (2026) | LoopWorker",
 "social":"Retention Cohorts: How to Read the Curve That Predicts Churn",
 "h1":"Retention Cohorts: How to Read the Curve That Predicts Churn",
 "desc":"Your blended retention rate hides your best and worst months. How to build retention cohorts, read the curve (declining, flattening, smiling), and turn the shape into growth.",
 "keywords":"retention cohorts, cohort retention analysis, retention curve, cohort analysis, customer retention, acquisition cohort, behavioral cohort, retention curve smile",
 "subtitle":"Your blended retention rate hides both your best month and your worst. Cohorts pull them apart — and the shape of the curve, whether it declines, flattens, or smiles, tells you whether you have a growth engine or a leaky bucket. Here's how to build them and what each shape means.",
 "takeaways":["What a retention cohort is","Why one blended number lies","The three curve shapes and what each means","Acquisition vs. behavioral vs. predictive cohorts","How to build one and act on it"],
 "body":"\n".join([
   '    <p class="fade-up">A cohort is a group of customers who share a starting point — signed up the same week, made a first purchase the same month — tracked over time. Retention cohort analysis watches what percentage of each group is still active in week 1, 4, 12, and beyond. It is the difference between knowing your retention and understanding it.</p>',
   '    <h2 class="fade-up">Why Blended Retention Lies</h2>',
   '    <p>A single company-wide retention number averages every cohort together. A great recent month can hide a collapsing older one, or a fixed onboarding flow can be masked by months of churn that came before it. Cohorts separate the signal: you see exactly which start-month is bleeding and whether the changes you shipped actually helped the people who joined after them.</p>',
   card("The tell","If your blended retention is \"fine\" but growth is stalling, you have a cohort problem.","Some group is leaking and the average is covering for it. Split the data and the leak shows up immediately."),
   '    <h2 class="fade-up">The Three Curve Shapes</h2>',
   card("Declining","The curve falls and keeps falling toward zero.","No retention floor. Each cohort eventually leaves. This is a product-market fit problem, not a marketing problem — fix it before spending on acquisition."),
   card("Flattening","The curve drops, then levels off at a stable floor.","You have a core that stays. The flatter and higher the floor, the healthier the business. Now the job is widening that core."),
   card("Smiling","The curve dips, flattens, then ticks back up.","Net revenue or usage expands within cohorts over time — expansion, resurrection, or referrals. The strongest signal there is. Find what causes it and pour fuel on it."),
   cta("A retention curve tells you something is working — it rarely tells you who. The cohort that stays is your real market. A LoopWorker Sprint reads that segment's language and proof, so you acquire more of the customers who already love you. Start with a Surface scan."),
   '    <h2 class="fade-up">Three Types of Cohort</h2>',
   card("Acquisition cohorts","Group by when customers joined.","Show what happened over time — which signup periods retained and which did not."),
   card("Behavioral cohorts","Group by an action customers took.","Explain why it happened — e.g. users who used Feature X in week 1 retain far better. This is where you find your activation lever."),
   card("Predictive cohorts","Group by likelihood to behave a certain way.","Let you act before the curve turns — intervene with at-risk groups while there is still time."),
   '    <h2 class="fade-up">How to Build One</h2>',
   '    <p>Pick a start event (signup, first purchase, first payment). Pick a retention event (active, logged in, purchased again). Pick an interval (day, week, or month, matched to your usage rhythm). Then plot the percentage of each start cohort still doing the retention event at each interval. Read down a column to compare cohorts; read across a row to see a single cohort decay. Most analytics tools build this in minutes; a spreadsheet works to start.</p>',
   '    <h2 class="fade-up">Turn the Shape Into Growth</h2>',
   '    <p>Find the behavioral cohort that flattens or smiles — the segment, feature, or first-week action tied to staying — and engineer more of it. Guide new users to that action faster (that is your time-to-value lever), and acquire more of the people who match the cohort that already retains. Retention is not one number to defend; it is a map of who your business is actually for.</p>',
 ]),
 "cta":"The cohort that retains is telling you who your real market is. A LoopWorker Sprint turns that signal into language and positioning that pulls more of them — so growth compounds instead of leaking. Start with a Surface scan.",
 "faqs":[
   ("What is a retention cohort?","A retention cohort is a group of customers who share a starting point — such as signing up in the same week — tracked over time to see what percentage stay active. It reveals retention patterns that a single blended number hides."),
   ("What does a good retention curve look like?","A healthy curve drops at first, then flattens at a stable floor, meaning you have a core of customers who stay. The strongest curves \"smile\" — they flatten and then tick upward as cohorts expand through usage, referrals, or resurrection."),
   ("What is the difference between acquisition and behavioral cohorts?","Acquisition cohorts group customers by when they joined and show what happened over time. Behavioral cohorts group them by an action they took and explain why retention differs — surfacing the activation lever that makes customers stay."),
   ("How do I build a cohort analysis?","Pick a start event (signup or first purchase), a retention event (active or repeat purchase), and an interval (day, week, or month). Plot the percentage of each start cohort still active at each interval. Most product analytics tools build this automatically; a spreadsheet works to start."),
 ],
 "related":[("Time to value: the metric that decides who churns","/blog/time-to-value.html"),
            ("The 6-month visibility cycle","/blog/visibility-cycle.html"),
            ("What category positioning actually means in 2026","/blog/what-category-positioning-means.html"),
            ("Buyer language pulls","/blog/buyer-language-pulls.html")],
}

for p in (p1,p2,p3): page(p)
print("DONE")
