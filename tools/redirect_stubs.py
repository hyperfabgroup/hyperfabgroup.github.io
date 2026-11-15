"""صفحه‌های جابه‌جایی سایت قدیمی hyperfab-ir.github.io به hyperfabgroup.github.io.

سایت قدیمی دیگر محتوا ندارد: هر صفحه‌اش بازدیدکننده و گوگل را بی‌درنگ به همان مسیر در سایت تازه می‌فرستد
(meta refresh صفر ثانیه + canonical + جاوااسکریپت). گوگل این را جابه‌جایی دائمی حساب می‌کند.

اجرا (یک بار، هر وقت صفحه‌ی تازه‌ای به سایت اضافه شد):
    python3 tools/redirect_stubs.py <خروجی>
خروجی را در ریپوی hyperfab-ir.github.io جای همه‌ی فایل‌ها بگذارید و پوش کنید.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, OLD_SITE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERIFY = '<meta name="google-site-verification" content="fU2lqYzDNWrzfksv2M-7JnUH_YPVxpO9Hlq-vi2N9NU">'


def pages():
    out = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if not x.startswith('.') and x not in ('tools', 'assets')]
        if 'index.html' in files:
            rel = os.path.relpath(d, ROOT)
            out.append('/' if rel == '.' else '/' + rel.replace(os.sep, '/') + '/')
    return sorted(out)


def stub(path):
    new = SITE + path
    lang = 'en' if path.startswith('/en/') else 'fa'
    text = 'This page has moved to' if lang == 'en' else 'این صفحه منتقل شد به'
    u = html.escape(new)
    return f'''<!DOCTYPE html>
<html lang="{lang}"{' dir="rtl"' if lang == 'fa' else ''}>
<head>
<meta charset="utf-8">
<title>HyperFab — {u}</title>
<link rel="canonical" href="{u}">
<meta http-equiv="refresh" content="0; url={u}">
{VERIFY if path == '/' else ''}
<script>location.replace({new!r} + location.search + location.hash);</script>
</head>
<body>
<p>{text} <a href="{u}">{u}</a></p>
</body>
</html>
'''


def main(out):
    paths = pages()
    for p in paths:
        d = os.path.join(out, p.strip('/'))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(stub(p))
    with open(os.path.join(out, '404.html'), 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html lang="fa" dir="rtl"><head><meta charset="utf-8"><title>HyperFab</title>
<meta name="robots" content="noindex">
<script>location.replace({SITE!r} + location.pathname + location.search + location.hash);</script>
</head><body><p>سایت به <a href="{SITE}/">{SITE}</a> منتقل شده است.</p></body></html>
''')
    with open(os.path.join(out, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(f'# این سایت به {SITE} منتقل شده است.\nUser-agent: *\nAllow: /\n\nSitemap: {OLD_SITE}/sitemap.xml\n')
    # نقشه‌ی نشانی‌های قدیمی تا خزنده‌ها زودتر جابه‌جایی‌ها را ببینند
    urls = ''.join(f'  <url><loc>{OLD_SITE}{p}</loc></url>\n' for p in paths)
    with open(os.path.join(out, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    with open(os.path.join(out, 'llms.txt'), 'w', encoding='utf-8') as f:
        f.write(f'# HyperFab (هایپرفب)\n\n> This site has moved to {SITE}/ — see {SITE}/llms.txt\n')
    open(os.path.join(out, '.nojekyll'), 'w').close()
    with open(os.path.join(out, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(f'# hyperfab-ir.github.io\n\nاین سایت به {SITE} منتقل شده است. '
                f'صفحه‌ها با `tools/redirect_stubs.py` در ریپوی hyperfabgroup.github.io ساخته می‌شوند.\n')
    print(f'{len(paths)} redirect pages -> {out}')


if __name__ == '__main__':
    main(sys.argv[1])
