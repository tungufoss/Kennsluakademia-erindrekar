"""Build sky-standalone.html: one self-contained file (offline-safe icons).

Usage:  python make-standalone.py [qmd-name-without-ext]   (default: sky)
Needs internet once to download Font Awesome 6.7.2.
"""
import base64, re, subprocess, sys, urllib.request

name = sys.argv[1] if len(sys.argv) > 1 else "sky"
out = f"{name}-standalone.html"
subprocess.run(["quarto", "render", f"{name}.qmd", "-M", "embed-resources:true", "--output", out], check=True)

base = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2"
get = lambda u: urllib.request.urlopen(u).read()
css = get(f"{base}/css/all.min.css").decode()
css = re.sub(r',\s*url\(\.\./webfonts/[^)]*\.ttf\)[^;}]*', '', css)  # drop ttf fallbacks
def inline(m):
    data = base64.b64encode(get(f"{base}/webfonts/{m.group(1)}.woff2")).decode()
    return f"url(data:font/woff2;base64,{data})"
css = re.sub(r'url\(\.\./webfonts/([\w-]+)\.woff2\)', inline, css)

html = open(out, encoding="utf-8").read()
# Quarto embeds FA fonts with an invalid mime type ("octet-stream; charset=...") that browsers reject
html = re.sub(r"@font-face\{[^}]*application/octet-stream; charset=utf-8;base64,[^}]*\}", "", html)
k = re.search(r"</head>\s*<body[^>]*class=", html).start()  # real </head>, not one inside an inlined script
html = html[:k] + f"<style>{css}</style>" + html[k:]
open(out, "w", encoding="utf-8").write(html)
print("wrote", out, f"{len(html)/1e6:.1f} MB")
