#!/usr/bin/env python3
"""Builds 3 style versions x 3 languages of the Jani Deroja apartments site.
Content is taken from www.unije-jani.com (2016 version); prices now only in EUR.
Run: python3 build.py  ->  v1/, v2/, v3/ each with index.html (EN), hr.html, sl.html
"""
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = {"en": "index.html", "hr": "hr.html", "sl": "sl.html"}
LANG_LABEL = {"en": "EN", "hr": "HR", "sl": "SL"}

T = {
    "en": dict(
        title="Apartments Jani Deroja – Island Unije, Croatia",
        h1="Apartments & rooms Jani Deroja",
        sub="Island Unije, Croatia",
        slogan="Get into the rhythm of the sea!",
        nav=["Apartments", "Prices", "Island", "Gallery", "Contact"],
        welcome="Welcome – it will be our great pleasure to have you as our guest!",
        intro="When you retreat from the noise and stress of city life, you can find your little place of peace on the green island of Unije: clean sea and warm sun on beautiful beaches smelling of salt, rosemary and lavender, with concerts of cicadas and seagulls smoothly accompanied by the sounds of the sea …",
        beach="Our apartments are 100 m from the beach!",
        island_h="Island Unije",
        island="Unije (17 km²) is an oasis of peace – no cars! – with beautiful old village architecture. It lies in the Kvarner Bay.",
        travel_h="Getting here",
        travel=[("Catamaran Rijeka – Mali Lošinj", "https://www.jadrolinija.hr/en/"),
                ("Catamaran Pula – Zadar", "https://www.visitlosinj.hr/katamaran-pula-unije-susak-mali-losinj-ilovik--silba-zadar-v2.aspx"),
                ("Daily boat Unije – Susak – Mali Lošinj", "https://www.jadrolinija.hr/en/")],
        news_h="Events",
        news="Lignjada – a squid-fishing and darts competition with a folk feast – takes place around the weekend of the feast of St. Andrew (30 Nov). Depending on the weather it can be a week earlier or later.",
        apts_h="Apartments",
        apts=[("Apartment 1", "4+1 persons", "Ground floor: 2 double rooms, kitchen, bathroom, corridor, terrace with barbecue, Wi-Fi."),
              ("Apartment 2", "6 persons", "1st floor, entrance at terrace level: 2 triple rooms, kitchen, dining room, bathroom, terrace with barbecue, air conditioning, Wi-Fi."),
              ("Apartment 3", "4 persons", "Attic, one floor above the terrace entrance: 2 rooms (1 single, 1 triple), kitchen, dining room, bathroom, place on the courtyard terrace with barbecue, air conditioning, Wi-Fi."),
              ("Apartment 4", "2 persons", "Separate little house: place on the courtyard terrace with barbecue, air conditioning, Wi-Fi.")],
        pets="Pets are welcome on request (valid vaccination certificate required).",
        prices_h="Prices",
        per_day="per day",
        season="all year (1 Jan – 31 Dec)",
        pet_fee="Pet",
        notes=["Tourist tax is included.",
               "Stays of 3 days or less: +30 %.",
               "A 30 % deposit confirms the reservation."],
        gallery_h="Gallery",
        map_h="Location",
        contact_h="Contact",
        country="Croatia",
        phone_land="+385 51 235 739",
        book="Write to us",
        footer="Apartments Jani Deroja · Unije 31 · 51562 Unije · Croatia",
    ),
    "hr": dict(
        title="Apartmani Jani Deroja – otok Unije",
        h1="Apartmani i sobe Jani Deroja",
        sub="Otok Unije, Hrvatska",
        slogan="Prepustite se ritmu mora!",
        nav=["Apartmani", "Cijene", "Otok", "Galerija", "Kontakt"],
        welcome="Srdačno dobrodošli – bit će nam jako drago ugostiti Vas u našem smještaju!",
        intro="Kada se maknete od buke i stresa gradskog života, možete pronaći svoj kutak mira na zelenim Unijama: čekaju Vas čisto more i toplo sunce na lijepim plažama s mirisom soli, ružmarina i lavande te koncertima cvrčaka i galebova, pomiješanih sa zvucima mora …",
        beach="Naši apartmani su 100 m udaljeni od plaže!",
        island_h="Otok Unije",
        island="Unije (17 km²) su miran otok bez automobila sa sačuvanom starom seoskom arhitekturom. Leži u Kvarnerskom zaljevu.",
        travel_h="Kako doći",
        travel=[("Katamaran Rijeka – Mali Lošinj", "https://www.jadrolinija.hr/"),
                ("Katamaran Pula – Zadar", "https://www.visitlosinj.hr/hr/katamaran-pula-unije-susak-mali-losinj-ilovik--silba-zadar.aspx"),
                ("Svakodnevni brod Unije – Susak – Mali Lošinj", "https://www.jadrolinija.hr/")],
        news_h="Događanja",
        news="Lignjada (natjecanje u lovu na lignje i u pikadu te pučka fešta) održava se za vikend oko blagdana sv. Andrije (30.11.). Ovisno o vremenu datum se pomiče tjedan ranije ili kasnije.",
        apts_h="Apartmani",
        apts=[("Apartman 1", "4+1 osoba", "Prizemlje: 2 dvokrevetne sobe, kuhinja, kupaonica, hodnik, terasa s roštiljem, Wi-Fi."),
              ("Apartman 2", "6 osoba", "1. kat, ulaz u visini terase: 2 trokrevetne sobe, kuhinja, blagovaonica, kupaonica, terasa s roštiljem, klima uređaj, Wi-Fi."),
              ("Apartman 3", "4 osobe", "Potkrovlje, jedan kat iznad ulaza s terase: 2 sobe (1/1 i 1/3), kuhinja, blagovaonica, kupaonica, mjesto na terasi u dvorištu s roštiljem, klima uređaj, Wi-Fi."),
              ("Apartman 4", "2 osobe", "Zaseban objekt: mjesto na terasi u dvorištu s roštiljem, klima uređaj, Wi-Fi.")],
        pets="Kućni ljubimci su dozvoljeni na upit (uz važeći certifikat o cijepljenju).",
        prices_h="Cijene",
        per_day="po danu",
        season="cijela godina (1.1. – 31.12.)",
        pet_fee="Kućni ljubimac",
        notes=["Boravišna pristojba je uključena u cijenu.",
               "Boravak od 3 ili manje dana: +30 %.",
               "Uplata predujma od 30 % potvrđuje rezervaciju."],
        gallery_h="Galerija",
        map_h="Lokacija",
        contact_h="Kontakt",
        country="Hrvatska",
        phone_land="+385 51 235 739",
        book="Pišite nam",
        footer="Apartmani Jani Deroja · Unije 31 · 51562 Unije · Hrvatska",
    ),
    "sl": dict(
        title="Apartmaji Jani Deroja – otok Unije",
        h1="Apartmaji in sobe Jani Deroja",
        sub="Otok Unije, Hrvaška",
        slogan="Prepustite se ritmu morja!",
        nav=["Apartmaji", "Cene", "Otok", "Galerija", "Kontakt"],
        welcome="Prisrčno dobrodošli – v veliko veselje nam bo, če se odločite priti k nam v goste!",
        intro="Ko se umaknete od hrupa in stresa mestnega življenja, lahko najdete svoj košček miru na zelenih Unijah: čakajo Vas čisto morje in toplo sonce na lepih plažah z vonjem po soli, rožmarinu in sivki, kjer se lahko prepustite koncertom škržatov in galebov ob nežni spremljavi zvokov morja …",
        beach="Naši apartmaji so 100 m oddaljeni od plaže!",
        island_h="Otok Unije",
        island="Unije (17 km²) so miren otok brez avtomobilov z ohranjeno staro vaško arhitekturo. Otok leži v Kvarnerskem zalivu.",
        travel_h="Kako do nas",
        travel=[("Katamaran Rijeka – Mali Lošinj", "https://www.jadrolinija.hr/"),
                ("Katamaran Pula – Zadar", "https://www.visitlosinj.hr/si/katamaran-pula-unije-susak-mali-losinj-ilovik--silba-zadar.aspx"),
                ("Vsakodnevna ladja Unije – Susak – Mali Lošinj", "https://www.jadrolinija.hr/")],
        news_h="Dogodki",
        news="Lignjada (tekmovanje v lovu lignjev in pikadu ter veselica) je vsako leto za vikend okoli praznika sv. Andreja (30.11.), odvisno od vremena lahko vikend prej ali kasneje.",
        apts_h="Apartmaji",
        apts=[("Apartma 1", "4+1 oseb", "Pritličje: 2 dvoposteljni sobi, kuhinja, kopalnica, hodnik, terasa z žarom, Wi-Fi."),
              ("Apartma 2", "6 oseb", "1. nadstropje, vhod v višini terase: 2 troposteljni sobi, kuhinja, jedilnica, kopalnica, terasa z žarom, klima naprava, Wi-Fi."),
              ("Apartma 3", "4 osebe", "Podstrešje, nadstropje nad vhodom s terase: 2 sobi (1/1 in 1/3), kuhinja, jedilnica, kopalnica, mesto na terasi na dvorišču z žarom, klima naprava, Wi-Fi."),
              ("Apartma 4", "2 osebi", "Samostojna hiška: mesto na terasi na dvorišču z žarom, klima naprava, Wi-Fi.")],
        pets="Hišni ljubljenčki so dovoljeni na povpraševanje (z veljavnim potrdilom o cepljenju).",
        prices_h="Cene",
        per_day="na dan",
        season="vse leto (1.1. – 31.12.)",
        pet_fee="Hišni ljubljenček",
        notes=["Turistična taksa je vključena v ceno.",
               "Bivanje 3 dni ali manj: +30 %.",
               "Plačilo 30 % avansa velja kot potrditev rezervacije."],
        gallery_h="Galerija",
        map_h="Lokacija",
        contact_h="Kontakt",
        country="Hrvaška",
        phone_land="+386 31 649 157",
        book="Pišite nam",
        footer="Apartmaji Jani Deroja · Unije 31 · 51562 Unije · Hrvaška",
    ),
}

PRICES = [85, 85, 80, 55]          # EUR/day, apartments 1-4
PET_FEE = 10                       # EUR/day
APT_IMG = ["apt002.jpg", "apt004.jpg", "apt006.jpg", "apt008.jpg"]
EMAIL = "unije.jani@gmail.com"
PHONES = [("Jani", "+385 98 329 561"), ("Milena (HR)", "+385 98 329 561"), ("Milena (SL)", "+385 99 838 9248")]
MAP = "https://www.openstreetmap.org/export/embed.html?bbox=14.2394%2C44.6336%2C14.2554%2C44.6416&layer=mapnik&marker=44.6376%2C14.2474"
MAP_LINK = "https://www.openstreetmap.org/?mlat=44.6376&mlon=14.2474#map=16/44.6376/14.2474"

# (file, hr, en, sl) – captions from the original photo gallery
GALLERY = [
    ("unije_image001", "plaža Za smokve", "Za smokve beach", "plaža Za smokve"),
    ("unije_image003", "selo Unije", "Unije village", "vas Unije"),
    ("unije_image005", "plaža Centrala", "Centrala beach", "plaža Centrala"),
    ("unije_image007_20160920_185737", "ribolov u sumrak", "Fishing at sunset", "ribolov ob sončnem zahodu"),
    ("unije_20160805_201504", "na dočeku broda", "Expecting a ferry", "v pričakovanju ladje"),
    ("unije_20160822_195846", "zalazak sunca", "Sunset", "sončni zahod"),
    ("unije_20160917_124645", "val", "Wave", "val"),
    ("unije_20161011_073717", "galeb u zoru", "Seagull at sunrise", "galeb ob zori"),
    ("unije2_20160714_125450", "Janijeva plaža", "Jani's beach", "Janijeva plaža"),
    ("unije2_20160914_115939", "ribarska barka Za smokve", "Fishing boat at Za smokve", "ribiška barka Za smokve"),
    ("unije2_20160917_124220", "šetnica ispod maslina", "Olive tree path", "pot ob oljkah"),
    ("unije2_20160917_125744", "uvalica Drestitena", "Drestitena bay", "zaliv Drestitena"),
    ("unije2_20160917_131228", "šetnica uz more", "Seaside path", "pot ob morju"),
    ("unije2_20160917_140947", "selo Unije", "Unije village", "vas Unije"),
    ("unije2_20160917_141129", "Janijeva plaža", "Jani's beach", "Janijeva plaža"),
    ("unije2_20160919_190231", "šetnica uz more", "Seaside path", "pot ob morju"),
    ("unije2_20160919_191113", "plaža Centrala", "Centrala beach", "plaža Centrala"),
]
CAP = {"hr": 1, "en": 2, "sl": 3}

IMG = "../images/"


# ---------- shared building blocks ----------

def lang_switch(cur):
    return "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if l == cur else ""} hreflang="{l}">{LANG_LABEL[l]}</a>'
        for l, f in LANGS.items())


def nav(t):
    ids = ["apartments", "prices", "island", "gallery", "contact"]
    return "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(ids, t["nav"]))


def apartments(t, cls="apt"):
    return "".join(
        f'<article class="{cls}"><img src="{IMG}{img}" alt="{name}" loading="lazy">'
        f'<div><h3>{name} <small>{cap}</small></h3><p>{desc}</p></div></article>'
        for (name, cap, desc), img in zip(t["apts"], APT_IMG))


def price_table(t):
    rows = "".join(f'<tr><td>{a[0]} <small>({a[1]})</small></td><td>{p} €</td></tr>'
                   for a, p in zip(t["apts"], PRICES))
    rows += f'<tr><td>{t["pet_fee"]}</td><td>{PET_FEE} €</td></tr>'
    notes = "".join(f"<li>{n}</li>" for n in t["notes"])
    return (f'<table class="prices"><caption>EUR {t["per_day"]} · {t["season"]}</caption>{rows}</table>'
            f'<ul class="notes">{notes}</ul>')


def gallery(lang):
    i = CAP[lang]
    return "".join(
        f'<figure><a href="{IMG}{g[0]}.jpg"><img src="{IMG}{g[0]}.jpg" alt="{g[i]}" loading="lazy"></a>'
        f'<figcaption>{g[i]}</figcaption></figure>' for g in GALLERY)


def travel(t):
    return "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in t["travel"])


def contact(t):
    phones = "".join(f'<li>{n}: <a href="tel:{p.replace(" ", "")}">{p}</a></li>' for n, p in PHONES)
    phones += f'<li>Tel.: <a href="tel:{t["phone_land"].replace(" ", "")}">{t["phone_land"]}</a></li>'
    return (f'<address><strong>Jani &amp; Milena Deroja</strong><br>Unije 31<br>51562 Unije<br>{t["country"]}</address>'
            f'<ul class="phones">{phones}<li><a href="mailto:{EMAIL}?subject=Apartmani%20Deroja">{EMAIL}</a></li></ul>')


def mapframe(t):
    return (f'<iframe class="map" title="{t["map_h"]}" src="{MAP}" loading="lazy"></iframe>'
            f'<p class="maplink"><a href="{MAP_LINK}" target="_blank" rel="noopener">OpenStreetMap ↗</a></p>')


def head(t, lang, css, fonts=""):
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{f}">' for l, f in LANGS.items())
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["h1"]} – {t["sub"]}. {t["beach"]}">
<link rel="icon" href="{IMG}icon.png">{alts}{fonts}
<style>{css}</style></head>"""


# ---------- version 1: "Adriatic" – clean, white, sea blue, full-screen hero ----------

CSS1 = """
:root{--sea:#0b6e99;--ink:#1d2a33;--mute:#5d6b75;--bg:#fff;--soft:#f2f7fa}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--sea)}img{max-width:100%;display:block}
header{position:sticky;top:0;z-index:9;background:#fffffff0;backdrop-filter:blur(6px);border-bottom:1px solid #e3ebf0}
.bar{max-width:1100px;margin:auto;display:flex;gap:1rem;align-items:center;justify-content:space-between;padding:.6rem 1rem;flex-wrap:wrap}
.brand{font-weight:700;text-decoration:none;color:var(--ink)}
nav a,.lang a{text-decoration:none;color:var(--mute);margin-left:1rem;font-size:.95rem}
.lang a[aria-current]{color:var(--sea);font-weight:700}
.hero{min-height:78vh;display:grid;place-items:center;text-align:center;color:#fff;
 background:linear-gradient(#0003,#0006),url(../images/hero.jpg) center/cover}
.hero h1{font-size:clamp(2rem,6vw,3.6rem);margin:.2em;line-height:1.1}
.hero p{font-size:1.25rem;margin:.3em}
.btn{display:inline-block;margin-top:1.2rem;background:#fff;color:var(--sea);padding:.7rem 1.4rem;border-radius:99px;text-decoration:none;font-weight:600}
section{max-width:1100px;margin:auto;padding:4rem 1rem}
h2{font-size:2rem;margin:0 0 1.2rem;color:var(--sea)}
.lead{font-size:1.15rem;max-width:760px}
.badge{display:inline-block;background:var(--soft);color:var(--sea);font-weight:600;padding:.4rem .9rem;border-radius:8px}
.apts{display:grid;gap:1.5rem}
.apt img{width:100%}
.apt{background:var(--soft);border-radius:12px;overflow:hidden}
.apt div{padding:1rem 1.25rem}.apt h3{margin:0}.apt small{color:var(--mute);font-weight:400}
.apt p{margin:.3rem 0 0}
.pets{margin-top:1.5rem;color:#a00000}
.prices{border-collapse:collapse;width:100%;max-width:520px}
.prices caption{text-align:left;color:var(--mute);padding-bottom:.5rem}
.prices td{padding:.6rem 0;border-bottom:1px solid #e3ebf0}.prices td:last-child{text-align:right;font-weight:700}
.notes{color:var(--mute);padding-left:1.1rem}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:.8rem}
.gal figure{margin:0}.gal img{aspect-ratio:16/9;object-fit:cover;border-radius:8px;width:100%}
.gal figcaption{font-size:.85rem;color:var(--mute);padding:.3rem 0}
.map{width:100%;height:340px;border:0;border-radius:12px}.maplink{font-size:.85rem}
.phones{list-style:none;padding:0}address{font-style:normal;margin-bottom:1rem}
footer{background:var(--ink);color:#cfd8de;text-align:center;padding:2rem 1rem;font-size:.9rem}
.soft{background:var(--soft);max-width:none}.soft>div{max-width:1100px;margin:auto}
@media(max-width:700px){nav{display:none}}
"""


def v1(lang):
    t = T[lang]
    return head(t, lang, CSS1) + f"""<body>
<header><div class="bar"><a class="brand" href="#">Jani Deroja · Unije</a><nav>{nav(t)}</nav><span class="lang">{lang_switch(lang)}</span></div></header>
<div class="hero"><div><p>{t["slogan"]}</p><h1>{t["h1"]}</h1><p>{t["sub"]}</p><a class="btn" href="#contact">{t["book"]}</a></div></div>
<section><p class="lead"><strong>{t["welcome"]}</strong></p><p class="lead">{t["intro"]}</p><p class="badge">{t["beach"]}</p></section>
<section id="apartments"><h2>{t["apts_h"]}</h2><div class="apts">{apartments(t)}</div><p class="pets">{t["pets"]}</p></section>
<div class="soft" id="prices"><section><h2>{t["prices_h"]}</h2>{price_table(t)}</section></div>
<section id="island"><div class="cols">
<div><h2>{t["island_h"]}</h2><p>{t["island"]}</p><h3>{t["travel_h"]}</h3><ul>{travel(t)}</ul><h3>{t["news_h"]}</h3><p>{t["news"]}</p></div>
<div><h2>{t["map_h"]}</h2>{mapframe(t)}</div></div></section>
<section id="gallery"><h2>{t["gallery_h"]}</h2><div class="gal">{gallery(lang)}</div></section>
<div class="soft" id="contact"><section><h2>{t["contact_h"]}</h2>{contact(t)}</section></div>
<footer>{t["footer"]}</footer>
</body></html>"""


# ---------- version 2: "Kamen" – warm Mediterranean, serif, stone & terracotta ----------

FONTS2 = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">'
CSS2 = """
:root{--terra:#b4532a;--olive:#5f6b3a;--ink:#3a2f28;--bg:#faf6ef;--card:#fff}
*{box-sizing:border-box}body{margin:0;font:17px/1.7 Lato,sans-serif;color:var(--ink);background:var(--bg)}
h1,h2,h3{font-family:"Cormorant Garamond",Georgia,serif;font-weight:700;line-height:1.15}
a{color:var(--terra)}img{max-width:100%;display:block}
.top{text-align:center;padding:1.2rem 1rem .4rem}
.lang a{margin:0 .4rem;text-decoration:none;color:var(--ink);font-size:.85rem;letter-spacing:.1em}
.lang a[aria-current]{border-bottom:2px solid var(--terra)}
.mast{text-align:center;padding:1rem 1rem 2rem}
.mast h1{font-size:clamp(2.2rem,6vw,4rem);margin:.1em 0}
.mast em{font-family:"Cormorant Garamond",serif;font-size:1.4rem;color:var(--terra)}
nav{text-align:center;border-top:1px solid #e4dccd;border-bottom:1px solid #e4dccd;padding:.6rem}
nav a{margin:0 .8rem;text-decoration:none;color:var(--ink);text-transform:uppercase;font-size:.8rem;letter-spacing:.15em}
.heroimg{max-width:1200px;margin:2rem auto;padding:0 1rem}.heroimg img{border-radius:4px;width:100%;aspect-ratio:21/9;object-fit:cover}
main{max-width:860px;margin:auto;padding:0 1.2rem}
section{padding:2.5rem 0;border-bottom:1px solid #e4dccd}
h2{font-size:2.4rem;margin:0 0 1rem;text-align:center}
h2::after{content:"";display:block;width:50px;height:2px;background:var(--terra);margin:.6rem auto 0}
.intro{text-align:center;font-size:1.1rem}
.beach{font-family:"Cormorant Garamond",serif;font-size:1.7rem;text-align:center;color:var(--olive);margin:1rem 0 0}
.apt img{width:100%}
.apt{background:var(--card);margin:0 0 1.5rem;box-shadow:0 1px 3px #0001}
.apt div{padding:1rem 1.4rem}.apt h3{font-size:1.7rem;margin:0}.apt small{font-family:Lato;font-size:.9rem;color:var(--olive)}
.apt p{margin:.3rem 0 0}
.pets{text-align:center;font-style:italic}
.prices{margin:auto;border-collapse:collapse;min-width:min(100%,460px);background:var(--card)}
.prices caption{padding:.5rem;font-style:italic}
.prices td{padding:.7rem 1.2rem;border-bottom:1px dotted #d6c9b4}.prices td:last-child{text-align:right;font-weight:700;color:var(--terra)}
.notes{max-width:460px;margin:1rem auto;font-size:.95rem}
.gal{columns:3 220px;column-gap:.8rem}
.gal figure{margin:0 0 .8rem;break-inside:avoid;background:var(--card);padding:.4rem}
.gal figcaption{font-family:"Cormorant Garamond",serif;font-size:1.05rem;text-align:center;padding:.3rem}
.map{width:100%;height:320px;border:0}.maplink{font-size:.85rem;text-align:center}
#contact{text-align:center}.phones{list-style:none;padding:0}address{font-style:normal;margin-bottom:1rem}
footer{text-align:center;padding:2.5rem 1rem;font-size:.85rem;color:#8a7d70}
"""


def v2(lang):
    t = T[lang]
    return head(t, lang, CSS2, FONTS2) + f"""<body>
<div class="top lang">{lang_switch(lang)}</div>
<div class="mast"><em>{t["slogan"]}</em><h1>{t["h1"]}</h1><div>{t["sub"]}</div></div>
<nav>{nav(t)}</nav>
<div class="heroimg"><img src="{IMG}hero.jpg" alt="{t["sub"]}"></div>
<main>
<section><p class="intro"><strong>{t["welcome"]}</strong></p><p class="intro">{t["intro"]}</p><p class="beach">{t["beach"]}</p></section>
<section id="apartments"><h2>{t["apts_h"]}</h2>{apartments(t)}<p class="pets">{t["pets"]}</p></section>
<section id="prices"><h2>{t["prices_h"]}</h2>{price_table(t)}</section>
<section id="island"><h2>{t["island_h"]}</h2><p>{t["island"]}</p>
<h3>{t["travel_h"]}</h3><ul>{travel(t)}</ul><h3>{t["news_h"]}</h3><p>{t["news"]}</p>{mapframe(t)}</section>
<section id="gallery"><h2>{t["gallery_h"]}</h2><div class="gal">{gallery(lang)}</div></section>
<section id="contact"><h2>{t["contact_h"]}</h2>{contact(t)}</section>
</main><footer>{t["footer"]}</footer>
</body></html>"""


# ---------- version 3: "Compact" – dark navy sidebar, everything on one screen-friendly page ----------

CSS3 = """
:root{--navy:#0f2638;--accent:#f2b43c;--ink:#1b1b1b;--mute:#666;--bg:#fff;--line:#e6e6e6}
*{box-sizing:border-box}body{margin:0;font:16px/1.55 "Helvetica Neue",Arial,sans-serif;color:var(--ink);background:var(--bg)}
a{color:inherit}img{max-width:100%;display:block}
.wrap{display:grid;grid-template-columns:300px 1fr;min-height:100vh}
aside{background:var(--navy);color:#e9eef2;padding:2rem 1.5rem;position:sticky;top:0;height:100vh;overflow:auto}
aside h1{font-size:1.6rem;margin:.2rem 0;line-height:1.2}
aside .sub{color:var(--accent);font-weight:700;margin:0 0 1.5rem}
aside nav a{display:block;padding:.35rem 0;text-decoration:none;border-bottom:1px solid #ffffff1a}
aside nav a:hover{color:var(--accent)}
aside .lang{margin:1.5rem 0}aside .lang a{margin-right:.6rem;text-decoration:none;padding:.2rem .5rem;border:1px solid #ffffff40;border-radius:4px;font-size:.8rem}
aside .lang a[aria-current]{background:var(--accent);color:var(--navy);border-color:var(--accent)}
aside .phones{list-style:none;padding:0;font-size:.9rem}aside address{font-style:normal;font-size:.9rem;margin-bottom:.6rem}
main{padding:0 0 3rem}
.hero{height:42vh;min-height:260px;background:url(../images/hero.jpg) center/cover;display:flex;align-items:flex-end}
.hero p{margin:0;background:var(--navy);color:#fff;padding:.6rem 1.2rem;font-weight:700}
section{padding:2.5rem 2rem;border-bottom:1px solid var(--line);max-width:1000px}
h2{font-size:.85rem;text-transform:uppercase;letter-spacing:.2em;color:var(--mute);margin:0 0 1.2rem}
.beach{display:inline-block;background:var(--accent);color:var(--navy);font-weight:700;padding:.3rem .7rem}
.apts{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:1.2rem}
.apt{border:1px solid var(--line)}.apt div{padding:.8rem 1rem}.apt h3{margin:0;font-size:1.1rem}
.apt small{color:var(--mute);font-weight:400}.apt p{margin:.3rem 0 0;font-size:.95rem}
.pets{font-size:.95rem;color:var(--mute)}
.split{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem}
.prices{border-collapse:collapse;width:100%}.prices caption{text-align:left;font-size:.85rem;color:var(--mute);padding-bottom:.4rem}
.prices td{padding:.45rem 0;border-bottom:1px solid var(--line)}.prices td:last-child{text-align:right;font-weight:700}
.notes{font-size:.9rem;color:var(--mute);padding-left:1rem}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:4px}
.gal figure{margin:0;position:relative}.gal img{aspect-ratio:1;object-fit:cover;width:100%}
.gal figcaption{position:absolute;bottom:0;left:0;right:0;background:#0f2638cc;color:#fff;font-size:.75rem;padding:.2rem .4rem;opacity:0;transition:.2s}
.gal figure:hover figcaption{opacity:1}
.map{width:100%;height:280px;border:0}.maplink{font-size:.8rem}
footer{padding:1.5rem 2rem;font-size:.8rem;color:var(--mute)}
@media(max-width:820px){.wrap{display:block}aside{position:static;height:auto}aside nav{display:none}.apts{grid-template-columns:1fr}section{padding:2rem 1rem}}
"""


def v3(lang):
    t = T[lang]
    return head(t, lang, CSS3) + f"""<body><div class="wrap">
<aside><h1>{t["h1"]}</h1><p class="sub">{t["sub"]}</p><nav>{nav(t)}</nav>
<div class="lang">{lang_switch(lang)}</div><div id="contact">{contact(t)}</div></aside>
<main>
<div class="hero"><p>{t["slogan"]}</p></div>
<section><p><strong>{t["welcome"]}</strong> {t["intro"]}</p><p class="beach">{t["beach"]}</p></section>
<section id="apartments"><h2>{t["apts_h"]}</h2><div class="apts">{apartments(t)}</div><p class="pets">{t["pets"]}</p></section>
<section id="prices" class="split"><div><h2>{t["prices_h"]}</h2>{price_table(t)}</div>
<div id="island"><h2>{t["island_h"]}</h2><p>{t["island"]}</p><p><strong>{t["travel_h"]}</strong></p><ul>{travel(t)}</ul>
<p><strong>{t["news_h"]}:</strong> {t["news"]}</p></div></section>
<section id="gallery"><h2>{t["gallery_h"]}</h2><div class="gal">{gallery(lang)}</div></section>
<section><h2>{t["map_h"]}</h2>{mapframe(t)}</section>
<footer>{t["footer"]}</footer>
</main></div></body></html>"""


INDEX = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jani Deroja – website drafts</title><style>body{font:17px/1.6 system-ui,sans-serif;max-width:640px;margin:3rem auto;padding:0 1rem}
a{display:block;padding:1rem;margin:.6rem 0;border:1px solid #ddd;border-radius:8px;text-decoration:none;color:#0b6e99}</style></head>
<body><h1>Apartments Jani Deroja – 3 design drafts</h1>
<a href="v1/index.html"><b>Version 1 – Adriatic</b><br><small>clean, white &amp; sea blue, full-screen beach photo</small></a>
<a href="v2/index.html"><b>Version 2 – Kamen (stone)</b><br><small>warm Mediterranean, serif type, terracotta &amp; olive</small></a>
<a href="v3/index.html"><b>Version 3 – Compact</b><br><small>navy sidebar with contact always visible, dense one-pager</small></a>
</body></html>"""

if __name__ == "__main__":
    for name, fn in [("v1", v1), ("v2", v2), ("v3", v3)]:
        d = ROOT / name
        d.mkdir(exist_ok=True)
        for lang, fname in LANGS.items():
            (d / fname).write_text(fn(lang), encoding="utf-8")
    (ROOT / "index.html").write_text(INDEX, encoding="utf-8")
    print("built v1, v2, v3")
