"""راهنماها (مقاله‌های آموزشی) سایت.

هر راهنما یک فایل tools/guides/g_<نام>.py است که متغیر GUIDE را با دو کلید 'fa' و 'en'
تعریف می‌کند؛ این بسته همه‌ی آن فایل‌ها را خودکار بارگذاری می‌کند. قالب داده در README.md آمده است.
اگر هیچ فایلی نباشد، فهرست خالی است و build.py صفحه‌ی راهنماها و آیتم منو را نمی‌سازد.
"""
import glob
import importlib
import os

LANGS = ('fa', 'en')


def load():
    """همه‌ی GUIDE های g_*.py به ترتیب نام فایل: [(نام ماژول، GUIDE)]"""
    out = []
    here = os.path.dirname(os.path.abspath(__file__))
    for path in sorted(glob.glob(os.path.join(here, 'g_*.py'))):
        name = os.path.splitext(os.path.basename(path))[0]
        mod = importlib.import_module(f'{__name__}.{name}')
        guide = getattr(mod, 'GUIDE', None)
        if not isinstance(guide, dict) or not all(isinstance(guide.get(k), dict) for k in LANGS):
            raise ValueError(f'tools/guides/{name}.py: GUIDE must be a dict with "fa" and "en" dicts')
        out.append((name, guide))
    return out
