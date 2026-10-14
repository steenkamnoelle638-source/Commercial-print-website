import os, html
C = dict(NAME="Jou Pa Se Naam", PHONE="+27 00 000 0000", TEL="+27000000000", WA="27000000000",
         EMAIL="sales@jou-domein.co.za", DOMAIN="https://jou-domein.co.za", GA="", FORM="https://formspree.io/f/JOU_ID")
P = [
("calendars","Calendars","Corporate Stationery & Gifts","Desk, wall and shipping-size calendars for corporate gifting.",[("Formats","Desk tent, wall, poster, shipping size"),("Paper","Gloss or matt art, board backing"),("Finishing","Wire-O binding, UV spot, hanging eyelets"),("Branding","Full-colour, client logo on every page")]),
("diaries","Diaries","Corporate Stationery & Gifts","Executive diaries and notebooks that carry your brand all year.",[("Sizes","A4, A5, pocket"),("Covers","Genuine leather, PU leather, hardcover canvas"),("Branding","Blind debossing, gold or silver foil, full-colour print"),("Inner pages","80gsm cream or white, ribbon markers, gilt edges")]),
("books","Books","High-Volume Publishing","Book printing for publishers, authors and organisations.",[("Binding","Perfect bound, hardcover, case bound, saddle stitch"),("Runs","Short to high-volume"),("Covers","Matt or gloss lamination, spot UV"),("Delivery","Single drop or split to several addresses")]),
("yearbooks","Yearbooks","High-Volume Publishing","Yearbooks for schools and universities, delivered on schedule.",[("Binding","Hardcover, case bound, perfect bound"),("Pages","Full-colour throughout"),("Personalising","Class, name or house inserts"),("Delivery","Straight to the school or to each campus")]),
("retail-tabloids","Retail Tabloids","High-Volume Publishing","Large retail catalogue and promotional tabloid runs.",[("Runs","High-volume weekly or seasonal"),("Formats","Tabloid, broadsheet, inserts"),("Stock","Newsprint and light-weight coated"),("Distribution","Direct to branches and distribution points")]),
("newspapers","Newspapers","High-Volume Publishing","Community and corporate newspapers printed in bulk.",[("Formats","Tabloid and broadsheet"),("Runs","Community to regional"),("Stock","Newsprint"),("Distribution","Scheduled delivery by route")]),
("labels","Labels","Packaging & Logistics","Roll and sheet labels for brands and manufacturers.",[("Types","Roll labels, sheet labels, die-cut shapes"),("Materials","Paper, gloss, matt, waterproof film"),("Finishing","Varnish, foil, lamination"),("Use","Food, retail, e-commerce, industrial")]),
("packaging","Packaging","Packaging & Logistics","Custom cartons and boxes made to your product.",[("Types","Folding cartons, rigid boxes, shippers"),("Board","Cardboard and corrugated"),("Finishing","Die-cut, foil, emboss, spot UV"),("Use","Retail and e-commerce")]),
("distribution","Distribution","Packaging & Logistics","One partner for print and delivery to branches, depots and ports.",[("Local","Delivery to branches across South Africa"),("Africa","Cross-border to neighbouring countries"),("International","Export shipping by arrangement"),("Process","One account manager from proof to delivery")]),
]
GAL = [("Calendars","calendar"),("Diaries","diary"),("Yearbooks","yearbook"),("Retail tabloids","tabloid"),("Labels","label"),("Packaging","packaging"),("Books","book"),("Newspapers","newspaper"),("Distribution","delivery")]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Instrument+Sans:wght@400;600&display=swap" rel="stylesheet">'
def head(title, desc, path):
    ga = f'<script async src="https://www.googletagmanager.com/gtag/js?id={C["GA"]}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{C["GA"]}")</script>' if C["GA"] else ""
    return f'''<!doctype html><html lang="en-ZA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{C["DOMAIN"]}{path}"><link rel="alternate" hreflang="en-za" href="{C["DOMAIN"]}{path}"><link rel="alternate" hreflang="x-default" href="{C["DOMAIN"]}{path}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 10 10%27><rect width=%275%27 height=%275%27 fill=%27%2300a3d9%27/><rect x=%275%27 width=%275%27 height=%275%27 fill=%27%23e5007d%27/><rect y=%275%27 width=%275%27 height=%275%27 fill=%27%23ffd400%27/><rect x=%275%27 y=%275%27 width=%275%27 height=%275%27 fill=%27%2312151c%27/></svg>">
{FONTS}<link rel="stylesheet" href="/style.css">{ga}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"{C["NAME"]} - Novus Print","url":"{C["DOMAIN"]}","telephone":"{C["TEL"]}","email":"{C["EMAIL"]}","description":"Commercial print account management and distribution through Novus Print."}}</script>
</head><body>'''
HEADER = f'''<header class="top"><a class="brand" href="/"><span class="sw"><i></i><i></i><i></i><i></i></span><span>{C["NAME"]}<small>Print Account Manager at Novus Print</small></span></a>
<nav><a href="/#products">Products</a><a href="/gallery.html">Gallery</a><a href="/#quote">Request a quote</a><a class="call" href="tel:{C["TEL"]}">{C["PHONE"]}</a></nav></header>'''
FOOT = f'''<footer><p><strong>{C["NAME"]}</strong>, Print Account Manager at Novus Print.<br>{C["PHONE"]} · <a href="mailto:{C["EMAIL"]}">{C["EMAIL"]}</a></p><p class="fine">Novus Print is a trademark of its owner. This site is run by a Novus Print representative.</p></footer>
<div class="bar"><a href="tel:{C["TEL"]}">Call now</a><a class="wa" href="https://wa.me/{C["WA"]}">WhatsApp</a></div><script src="/app.js" defer></script></body></html>'''
def form(sel=""):
    return f'''<section class="quote" id="quote"><div><h2>Request a tailored print and distribution quote</h2><p>Tell me what you need and I will call you back with an accurate quote. Prefer to chat? <a href="https://wa.me/{C["WA"]}">Message me on WhatsApp</a> or <a href="tel:{C["TEL"]}">call {C["PHONE"]}</a>.</p></div>
<form action="{C["FORM"]}" method="POST"><label>Your name and company<input name="name" required autocomplete="name"></label><label>Phone or email<input name="contact" required></label>
<label>Product<input name="product" value="{sel}" placeholder="e.g. Diaries"></label><label>Estimated quantity<input type="number" name="quantity" min="1" placeholder="e.g. 5000"></label>
<label>Size, binding, finishing and delivery<textarea name="specs" rows="4" placeholder="Include where it must be delivered"></textarea></label><button>Request my quote</button></form></section>'''
def gal(n=None):
    items = GAL[:n] if n else GAL
    f = "".join(f'<figure><img src="/images/gallery/{s}.jpg" alt="{t} printed by Novus Print" loading="lazy" width="600" height="450" onerror="this.remove()"><figcaption>{t}</figcaption></figure>' for t,s in items)
    return f'<div class="gal">{f}</div>'
os.makedirs("public/products", exist_ok=True); os.makedirs("public/images/gallery", exist_ok=True)
w = lambda p,s: open("public/"+p,"w").write(s)
groups = {}
for p in P: groups.setdefault(p[2],[]).append(p)
cards = "".join(f'<div class="grp"><h3>{g}</h3>' + "".join(f'<a class="pc" href="/products/{s}.html"><b>{t}</b><span>{d}</span></a>' for s,t,_,d,_ in ps) + '</div>' for g,ps in groups.items())
idx = head("Commercial Printing & Distribution | Novus Print Account Manager", "High-volume commercial printing through Novus Print with nationwide and international distribution. Get a direct quote from a dedicated account manager.", "/") + HEADER + f'''
<main><section class="hero"><div><h1>Print runs managed by one person, delivered to every branch.</h1>
<p>Calendars, diaries, books, tabloids, labels and packaging printed at Novus Print. You deal with {C["NAME"]} directly, from first quote to final delivery.</p>
<p class="cta"><a class="btn" href="#quote">Request a quote</a><a class="btn alt" href="https://wa.me/{C["WA"]}">Chat on WhatsApp</a></p></div>
<div class="reg" aria-hidden="true"><i class="c"></i><i class="m"></i><i class="y"></i><i class="k"></i></div></section>
<section class="band"><div><h2>One account manager. Not a call centre.</h2></div><ul><li><b>Direct line</b>Your quote comes from a person who knows your job.</li><li><b>Print and delivery</b>Finished work goes straight to your branches, depots or ports.</li><li><b>Quoted to your spec</b>Every job is priced for your quantity, stock and finishing.</li></ul></section>
<section id="products"><h2>What I print</h2>{cards}</section>
<section><h2>Recent work</h2>{gal(6)}<p><a href="/gallery.html">See the full gallery</a></p></section>{form()}</main>''' + FOOT
w("index.html", idx)
for s,t,g,d,specs in P:
    li = "".join(f"<li><b>{a}</b>{b}</li>" for a,b in specs)
    pg = head(f"{t} Printing South Africa | Novus Print Account Manager", f"{d} High-volume runs through Novus Print with delivery across South Africa and abroad. Request a direct quote.", f"/products/{s}.html") + HEADER + f'''<main><section class="ph"><p class="crumb"><a href="/">Home</a> / {g}</p><h1>{t} printing and distribution</h1><p>{d} Available in high volume with local and international delivery.</p></section>
<section><h2>Specifications and finishes</h2><ul class="spec">{li}</ul><p>Not sure what you need? Send what you have and I will advise on stock, size and finishing.</p></section>
<section><h2>Examples</h2>{gal(3)}</section>{form(t)}</main>''' + FOOT
    w(f"products/{s}.html", pg)
w("gallery.html", head("Print Gallery | Novus Print Account Manager","Examples of calendars, diaries, yearbooks, tabloids, labels and packaging printed through Novus Print.","/gallery.html") + HEADER + f'<main><section class="ph"><h1>Gallery</h1><p>A selection of work printed at Novus Print. Click an image to enlarge.</p></section><section>{gal()}</section>{form()}</main>' + FOOT)
urls = ["/","/gallery.html"]+[f"/products/{p[0]}.html" for p in P]
w("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{C['DOMAIN']}{u}</loc></url>" for u in urls)+"</urlset>")
w("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {C['DOMAIN']}/sitemap.xml\n")
w("style.css",''':root{--paper:#fbfaf6;--ink:#12151c;--mute:#566;--c:#00a3d9;--m:#e5007d;--y:#ffd400;--line:#dcd9cf;--bg:var(--paper);--tx:var(--ink)}
@media(prefers-color-scheme:dark){:root{--bg:#12151c;--tx:#f3f1ea;--mute:#a9adb8;--line:#2b303b}}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--tx);font:17px/1.6 "Instrument Sans",system-ui,sans-serif;padding-bottom:64px}
h1,h2,h3,.brand{font-family:"Bricolage Grotesque",system-ui,sans-serif}h1{font-size:clamp(2.2rem,6vw,4.2rem);line-height:1.02;margin:0 0 1rem;font-weight:800;letter-spacing:-.02em}h2{font-size:clamp(1.5rem,3vw,2.2rem);margin:0 0 1rem;font-weight:800}
a{color:inherit}section,.top,footer{max-width:1100px;margin:0 auto;padding:3rem 1.25rem}p{max-width:62ch}
.top{display:flex;flex-wrap:wrap;gap:1rem;justify-content:space-between;align-items:center;padding-block:1rem}.top nav{display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center}.top nav a{text-decoration:none;font-weight:600}
.brand{display:flex;gap:.7rem;align-items:center;text-decoration:none;font-weight:800;line-height:1.1}.brand small{display:block;font:400 .78rem "Instrument Sans";color:var(--mute)}
.sw{display:grid;grid-template-columns:1fr 1fr;width:30px;height:30px}.sw i:nth-child(1){background:var(--c)}.sw i:nth-child(2){background:var(--m)}.sw i:nth-child(3){background:var(--y)}.sw i:nth-child(4){background:#12151c}
.call{background:var(--tx);color:var(--bg);padding:.4rem .9rem;border-radius:99px}
.hero{display:grid;grid-template-columns:1.3fr 1fr;gap:2rem;align-items:center;padding-block:3rem 4rem}
.reg{display:grid;grid-template-columns:1fr 1fr;aspect-ratio:1;max-width:380px;justify-self:center;width:100%;gap:0}.reg i{display:block;mix-blend-mode:multiply}.c{background:var(--c)}.m{background:var(--m)}.y{background:var(--y)}.k{background:#12151c}
.reg{position:relative}.reg::after{content:"";position:absolute;inset:25%;border:3px solid var(--bg);border-radius:50%;box-shadow:0 0 0 3px var(--tx)}
.btn{display:inline-block;background:var(--m);color:#fff;padding:.8rem 1.4rem;border-radius:4px;font-weight:600;text-decoration:none;border:2px solid var(--m);cursor:pointer;font:600 1rem "Instrument Sans"}.btn.alt{background:none;color:var(--tx);border-color:var(--tx)}.cta{display:flex;gap:.8rem;flex-wrap:wrap}
.btn:hover,button:hover{filter:brightness(1.1)}a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{outline:3px solid var(--c);outline-offset:2px}
.band{display:grid;grid-template-columns:1fr 2fr;gap:2rem;border-block:2px solid var(--tx)}.band ul{list-style:none;padding:0;margin:0;display:grid;gap:1rem}.band b,.spec b{display:block}
.grp{margin-bottom:2rem}.grp h3{margin:0 0 .6rem;border-bottom:2px solid var(--tx);padding-bottom:.3rem}.grp{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}.grp h3{grid-column:1/-1}
.pc{text-decoration:none;border:1px solid var(--line);padding:1rem;border-radius:6px;display:block;border-left:6px solid var(--c)}.grp:nth-of-type(2) .pc{border-left-color:var(--m)}.grp:nth-of-type(3) .pc{border-left-color:var(--y)}.pc b{font-family:"Bricolage Grotesque";font-size:1.2rem;display:block}.pc span{color:var(--mute);font-size:.95rem}.pc:hover{border-color:var(--tx)}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem}.gal figure{margin:0;aspect-ratio:4/3;background:linear-gradient(135deg,var(--c),var(--m),var(--y));position:relative;overflow:hidden;border-radius:6px;cursor:zoom-in}.gal img{width:100%;height:100%;object-fit:cover;display:block;position:absolute;inset:0}.gal figcaption{position:absolute;left:0;bottom:0;background:var(--bg);color:var(--tx);padding:.3rem .7rem;font-weight:600;font-size:.9rem}
.spec{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}.spec li{border-top:3px solid var(--tx);padding-top:.5rem}.crumb{color:var(--mute);font-size:.9rem}.ph{padding-bottom:1rem}
.quote{display:grid;grid-template-columns:1fr 1fr;gap:2rem;background:var(--tx);color:var(--bg);max-width:none;border-radius:0}.quote>*{max-width:520px}.quote>div{justify-self:end}.quote a{color:var(--y)}
form{display:grid;gap:.8rem}label{display:grid;gap:.25rem;font-weight:600;font-size:.92rem}input,textarea{font:inherit;padding:.6rem;border:2px solid var(--line);border-radius:4px;background:var(--bg);color:var(--tx)}form button{justify-self:start}
footer{border-top:1px solid var(--line)}.fine{font-size:.8rem;color:var(--mute)}
.bar{position:fixed;left:0;right:0;bottom:0;display:flex;z-index:9}.bar a{flex:1;text-align:center;padding:.9rem;font-weight:700;text-decoration:none;background:var(--tx);color:var(--bg)}.bar .wa{background:#25d366;color:#052}
.lb{position:fixed;inset:0;background:#000d;display:grid;place-items:center;z-index:20;cursor:zoom-out}.lb img{max-width:92vw;max-height:88vh}
@media(min-width:900px){.bar{left:auto;right:1.2rem;bottom:1.2rem;width:auto}.bar a:first-child{display:none}.bar a{border-radius:99px;padding:.8rem 1.3rem}body{padding-bottom:0}}
@media(max-width:800px){.hero,.band,.quote{grid-template-columns:1fr}.quote>div{justify-self:start}.reg{max-width:200px}}''')
w("app.js",'document.querySelectorAll(".gal img").forEach(i=>i.addEventListener("click",()=>{const d=document.createElement("div");d.className="lb";d.innerHTML=`<img src="${i.src}" alt="${i.alt}">`;d.onclick=()=>d.remove();document.body.append(d)}));')
open(".gitlab-ci.yml","w").write('pages:\n  stage: deploy\n  image: python:3.12-alpine\n  script:\n    - python build.py\n  pages: true\n  artifacts:\n    paths:\n      - public\n  rules:\n    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH\n')
