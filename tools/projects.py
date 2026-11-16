"""پروژه‌های واقعی هایپرفب (case study): صفحه‌های /portfolio/<slug>/ و /en/portfolio/<slug>/

هر پروژه یک ردیف {'fa': {...}, 'en': {...}} است. کلیدهای هر زبان:
  slug        نشانی صفحه، در دو زبان یکسان (حروف کوچک لاتین و عدد با -)
  title       تیتر H1
  seo_title   (اختیاری) عنوان کوتاه‌تر برای <title>
  desc        توضیح متا (فارسی ≤۱۵۵، انگلیسی ≤۱۶۰ نویسه) و متن کارت پروژه
  lead        پاسخ کوتاه زیر هیرو
  date        تاریخ انتشار صفحه YYYY-MM-DD (lastmod در sitemap)
  img         پوستر/عکس اصلی پروژه (کارت نمونه‌کارها، og:image، هیرو)
  services    کلید خدمت‌های مرتبط: کلید صفحه‌ی خدمت (tubelaser، welding، …)، کلید خدمت آنلاین
              (laser-metal، bending، …) یا services / industrial
  sections    [{'h': 'تیتر', 'p': [...], 'ul': [...] اختیاری, 'video': vid('شناسه', زبان) اختیاری}]
  cta         {'h': ..., 'p': ...}؛ دکمه‌ها تماس و بله‌ی پروژه‌های صنعتی‌اند
  related_guides  (اختیاری) slug راهنماهای مرتبط
ویدیوها در tools/media.py (REAL_VIDEOS) تعریف می‌شوند؛ نام و توضیح و تاریخشان از همان‌جا می‌آید.
عدد و مشخصاتی که از مشتری یا کار نداریم (اندازه، تعداد، نام مشتری) نوشته نمی‌شود.
"""
from media import vid

SLUG = 'mechanism-frame-st37'
SERVICES = ['tubelaser', 'laser-metal', 'bending', 'welding']
GUIDES = ['tube-laser-frame-design', 'tig-vs-mig-stainless-aluminium']
IMG = 'assets/img/works/work-frame-welding.jpg'

MECHANISM_FRAME = {
    'fa': {
        'slug': SLUG,
        'title': 'طراحی و ساخت فریم مکانیزم از قوطی و ورق St37',
        'seo_title': 'فریم مکانیزم از قوطی و ورق St37؛ از طراحی تا جوش',
        'card': 'فریم مکانیزم از قوطی و ورق St37',
        'desc': 'فریم یک مکانیزم از قوطی و ورق St37، از طراحی تا جوش در هایپرفب: برش لیزر قوطی، برش لیزر و خم ورق، جوش آرگون TIG و مهره‌پرچ؛ با ویدیوی واقعی هر مرحله.',
        'lead': ('هایپرفب فریم سبک و کم‌هزینه‌ی یک مکانیزم را از طراحی تا جوش نهایی خودش انجام داد: '
                 'قوطی فولادی St37 با <b>برش لیزر قوطی</b> آماده شد، ورق‌ها با <b>برش لیزر</b> بریده و <b>خم</b> شدند، '
                 'قطعات با <b>جوش آرگون TIG</b> به هم متصل شدند و برای بستن اجزا روی ورق نازک، <b>مهره‌پرچ</b> نصب شد. '
                 'ویدیوهای این صفحه از همین کار در کارگاه هایپرفب گرفته شده‌اند.'),
        'date': '2026-11-16', 'img': IMG, 'img_alt': 'فریم St37 از قوطی و ورق خم‌شده در حال جوش آرگون در کارگاه هایپرفب',
        'services': SERVICES, 'related_guides': GUIDES,
        'sections': [
            {'h': 'سفارش: فریمی سبک و کم‌هزینه برای یک مکانیزم',
             'p': ['این فریم برای مکانیزم یکی از مشتریان هایپرفب طراحی و ساخته شد؛ سازه‌ای که اجزای مکانیزم روی آن بسته می‌شوند. '
                   'هدف طراحی این بود که فریم در عین استحکام کافی، سبک و کم‌هزینه باشد.',
                   'در چنین کاری، انتخاب پروفیل، ضخامت ورق و روش اتصال از همان ابتدا قیمت تمام‌شده را تعیین می‌کند. '
                   'به همین دلیل هایپرفب کار را از طراحی شروع کرد، نه از برش.']},
            {'h': 'طراحی فریم در هایپرفب',
             'p': ['هایپرفب فریم را از دو جزء طراحی کرد: <b>قوطی فولادی St37</b> برای اسکلت فریم '
                   'و <b>ورق St37</b> که با برش لیزر و خم‌کاری به قطعات ورقی فریم تبدیل می‌شود. '
                   'وقتی برش با لیزر انجام می‌شود، سوراخ‌ها و محل اتصال‌ها را می‌توان از همان ابتدا در طراحی دید تا بعد از ساخت، سوراخکاری و اصلاح دستی کمتر لازم شود.',
                   'یک تصمیم مهم طراحی، استفاده از ورق نازک بود. ورق نازک‌تر هم وزن فریم را پایین می‌آورد و هم هزینه‌ی متریال و برش را؛ '
                   'اما برای پیچ، رزوه‌ی کافی ندارد. راه‌حل این مشکل مهره‌پرچ بود که پایین‌تر توضیح داده شده است.']},
            {'h': 'برش لیزر قوطی فولادی St37',
             'p': ['قطعات اسکلت از قوطی St37 با دستگاه لیزر لوله بریده شدند. در برش لیزر قوطی، طول قطعه، سوراخ‌ها و فرم سرِ قوطی '
                   'برای جفت شدن با قطعه‌ی کناری، همه در یک مرحله و مستقیم از روی فایل طراحی بریده می‌شوند. '
                   'نتیجه، قطعاتی است که دقیق کنار هم می‌نشینند و جوشکار مجبور نیست درزها را با سنگ و سوهان جفت کند.'],
             'video': vid('tube-laser', 'fa')},
            {'h': 'برش لیزر و خم ورق در کارگاه‌های هایپرفب',
             'p': ['قطعات ورقی فریم از ورق St37 در کارگاه‌های هایپرفب با لیزر بریده و سپس خم شدند. '
                   'برش لیزر، شکل گسترده‌ی قطعه را با همه‌ی سوراخ‌ها و شیارها یک‌جا درمی‌آورد و خم‌کاری آن را به فرم نهایی درمی‌آورد.',
                   'لبه‌های خم‌شده به ورق نازک سفتی می‌دهند؛ برای همین با ورقی نازک‌تر هم می‌شود به صفحه‌ای رسید که زیر بار تاب برندارد. '
                   'این همان جایی است که طراحی و ساخت به هم گره می‌خورند: ورق نازک فقط وقتی جواب می‌دهد که خم‌ها درست طراحی شده باشند.']},
            {'h': 'جوش آرگون TIG فریم St37',
             'p': ['در مرحله‌ی بعد، قطعات قوطی که با لیزر بریده شده بودند به ورق‌های برش‌خورده و خم‌شده جوش داده شدند. '
                   'این کار با <b>جوش آرگون (TIG)</b> انجام شد: حرارت در این روش متمرکز و قابل کنترل است، '
                   'روی ورق نازک کمتر باعث سوراخ شدن و تاب برداشتن می‌شود و جوشی تمیز می‌دهد که به سنگ‌زنی زیادی نیاز ندارد.',
                   'قطعاتی که با لیزر بریده می‌شوند درست روی هم می‌نشینند؛ این، مونتاژ و جوشکاری را ساده‌تر و رسیدن به ابعاد نقشه را آسان‌تر می‌کند.'],
             'video': vid('frame-welding', 'fa')},
            {'h': 'مهره‌پرچ روی ورق نازک: رزوه‌ی محکم بدون ورق ضخیم',
             'p': ['ورق نازک برای سبک و ارزان ماندن فریم انتخاب شده بود، اما آن‌قدر ضخامت ندارد که بشود در آن رزوه‌ی قابل اعتماد زد؛ '
                   'رزوه‌ای که فقط یکی دو دنده در ورق دارد، با چند بار باز و بسته کردن پیچ از بین می‌رود. راه‌حل، <b>مهره‌پرچ</b> بود.',
                   'مهره‌پرچ از یک طرف ورق در سوراخ گذاشته می‌شود و ابزار پرچ، بدنه‌اش را پشت ورق جمع می‌کند تا محکم در جای خود قفل شود. '
                   'در این پروژه مهره‌پرچ‌ها با <b>ابزار پرچ بادی</b> نصب شدند که کار را سریع و یکنواخت می‌کند. مزیت‌های این روش:'],
             'ul': ['رزوه‌ی کامل و محکم برای پیچ، بدون نیاز به ورق ضخیم‌تر',
                    'نصب از یک طرف ورق، بدون دسترسی به پشت کار',
                    'بدون جوش و بدون حرارت روی ورق نازک، پس بدون تاب برداشتن',
                    'وزن و هزینه‌ی کمتر نسبت به ورق ضخیم'],
             'video': vid('rivet-nut', 'fa')},
            {'h': 'نتیجه: یک گروه، از طراحی تا فریم آماده',
             'p': ['حاصل کار، فریمی سبک از قوطی و ورق St37 بود که اجزای مکانیزم با پیچ روی آن بسته می‌شوند. '
                   'اما نکته‌ی مهم‌تر این پروژه، روش کار است: طراحی، برش لیزر قوطی، برش لیزر و خم ورق، جوشکاری و نصب مهره‌پرچ '
                   'همه در هایپرفب انجام شد و یک گروه مسئول کل کار بود.',
                   'وقتی طراح و سازنده یکی باشند، تصمیم‌هایی مثل نازک کردن ورق یا انتخاب مهره‌پرچ با توجه به امکانات ساخت گرفته می‌شوند '
                   'و هزینه‌ی تمام‌شده پایین می‌آید. اگر برای دستگاه یا مکانیزم خود به فریم و سازه‌ی فلزی نیاز دارید، '
                   'نقشه یا حتی ایده‌ی اولیه را برای هایپرفب بفرستید.']},
        ],
        'cta': {'h': 'فریم یا سازه‌ی فلزی لازم دارید؟',
                'p': 'نقشه، طرح اولیه یا عکس نمونه را بفرستید یا تماس بگیرید. کارشناس پروژه‌های صنعتی هایپرفب تلفنی و در بله پاسخ‌گوی شماست.'},
    },
    'en': {
        'slug': SLUG,
        'title': 'Mechanism Frame in St37: From Design to Welding',
        'card': 'Mechanism frame in St37 box section and sheet',
        'desc': 'A mechanism frame in St37 box section and sheet, designed and built by HyperFab: tube laser cutting, sheet cutting and bending, TIG welding and rivet nuts.',
        'lead': ('HyperFab took a light, low-cost mechanism frame from design to final weld in house: '
                 'St37 steel box section was cut on a <b>tube laser</b>, the sheet parts were <b>laser cut</b> and <b>bent</b>, '
                 'everything was joined by <b>TIG welding</b>, and <b>rivet nuts</b> were fitted so parts could be screwed to the thin sheet. '
                 'The videos on this page were filmed on this job in HyperFab’s workshop.'),
        'date': '2026-11-16', 'img': IMG, 'img_alt': 'An St37 frame of box section and bent sheet being TIG welded in HyperFab’s workshop',
        'services': SERVICES, 'related_guides': GUIDES,
        'sections': [
            {'h': 'The brief: a light, low-cost frame for a mechanism',
             'p': ['This frame was designed and made for a HyperFab customer’s mechanism: a structure the mechanism’s parts are mounted on. '
                   'The aim of the design was a frame that is strong enough for the job but light and inexpensive.',
                   'On a job like this, the choice of section, sheet thickness and joining method sets the final cost from day one. '
                   'So HyperFab started with the design, not with the cutting.']},
            {'h': 'Designed by HyperFab',
             'p': ['HyperFab designed the frame around two elements: <b>St37 steel box section</b> for the skeleton, '
                   'and <b>St37 sheet</b>, laser cut and bent into the frame’s sheet parts. '
                   'With laser cutting, holes and joint positions can be settled in the design from the start, so less drilling and hand fitting is needed after fabrication.',
                   'One key design decision was to use thin sheet. Thinner sheet cuts both the weight of the frame and the cost of material and cutting, '
                   'but it is too thin to hold a usable thread. Rivet nuts solved that, as explained below.']},
            {'h': 'Tube laser cutting the St37 box section',
             'p': ['The skeleton parts were cut from St37 box section on a tube laser. Tube laser cutting produces the length, the holes and the end profile '
                   'that mates with the neighbouring part in a single operation, straight from the design file. '
                   'The result is parts that fit together accurately, so the welder does not have to grind and file joints to make them meet.'],
             'video': vid('tube-laser', 'en')},
            {'h': 'Sheet laser cutting and bending in HyperFab’s workshops',
             'p': ['The frame’s sheet parts were laser cut from St37 sheet in HyperFab’s workshops and then bent. '
                   'Laser cutting produces the flat pattern with every hole and slot in one go, and bending brings it to its final shape.',
                   'Bent flanges stiffen thin sheet, which is why a thinner gauge can still give a plate that does not flex under load. '
                   'This is where design and fabrication meet: thin sheet only works when the bends are designed for it.']},
            {'h': 'TIG welding the St37 frame',
             'p': ['Next, the laser-cut box-section parts were welded to the cut and bent sheet. '
                   'This was done by <b>TIG welding</b>, whose heat is concentrated and easy to control: it is less likely to burn through or distort thin sheet, '
                   'and it leaves a clean weld that needs little grinding.',
                   'Laser-cut parts fit together properly, which makes assembly and welding simpler and the drawing dimensions easier to hold.'],
             'video': vid('frame-welding', 'en')},
            {'h': 'Rivet nuts in thin sheet: strong threads without thick sheet',
             'p': ['Thin sheet kept the frame light and affordable, but it is too thin to hold a reliable thread: '
                   'a thread with only a turn or two of engagement strips after the screw has been in and out a few times. The answer was <b>rivet nuts</b>.',
                   'A rivet nut goes into a hole from one side of the sheet, and the setting tool collapses its body behind the sheet so it locks firmly in place. '
                   'On this job the rivet nuts were set with a <b>pneumatic rivet-nut tool</b>, which makes the work fast and consistent. The benefits:'],
             'ul': ['A full, strong thread for screws without moving to thicker sheet',
                    'Fitted from one side, with no access needed behind the part',
                    'No welding and no heat on the thin sheet, so no distortion',
                    'Less weight and cost than thicker sheet'],
             'video': vid('rivet-nut', 'en')},
            {'h': 'The result: one team from design to finished frame',
             'p': ['The result was a light frame in St37 box section and sheet, with the mechanism’s parts screwed to it. '
                   'The more important point is how it was made: the design, tube laser cutting, sheet laser cutting and bending, welding and rivet nuts '
                   'were all done by HyperFab, with one team responsible for the whole job.',
                   'When the designer and the fabricator are the same team, decisions such as thinning the sheet or choosing rivet nuts are made with the workshop in mind, '
                   'and the final cost comes down. If your machine or mechanism needs a frame or a steel structure, send HyperFab a drawing or even an early idea.']},
        ],
        'cta': {'h': 'Need a frame or a steel structure?',
                'p': 'Send a drawing, a sketch or a photo of a sample, or give us a call. HyperFab’s industrial projects specialist answers by phone and on Bale.'},
    },
}

# تازه‌ترین پروژه اول
PROJECTS = [MECHANISM_FRAME]

# برچسب‌های صفحه‌ی پروژه، فهرست پروژه‌ها و نوار «کار واقعی»
PROJECT_LABELS = {
    'fa': {'real_video': 'ویدیوی واقعی از پروژه‌های هایپرفب', 'services_h': 'خدمت‌های به‌کاررفته در این پروژه',
           'guides_h': 'راهنماهای مرتبط', 'published': 'انتشار', 'all_work': 'همه‌ی نمونه‌کارها',
           'projects_kicker': 'PROJECTS', 'projects_title': 'پروژه‌های واقعی، مرحله به مرحله',
           'projects_sub': 'داستان کامل کارهایی که هایپرفب از طراحی تا ساخت انجام داده است، با ویدیوی واقعی هر مرحله.',
           'read': 'داستان کامل پروژه',
           'strip_kicker': 'REAL WORK', 'strip_title': 'کار واقعی، از پروژه‌های هایپرفب',
           'strip_sub': 'ویدیوهای واقعی از قطعاتی که هایپرفب برای مشتریانش طراحی کرده، ساخته یا ساختشان را پیش برده است.', 'strip_btn': 'داستان کامل پروژه‌ی فریم مکانیزم',
           'svc_kicker': 'REAL PROJECT', 'svc_title': 'پروژه‌ی واقعی: ', 'svc_btn': 'داستان کامل این پروژه'},
    'en': {'real_video': 'Real footage from HyperFab projects', 'services_h': 'Services used on this project',
           'guides_h': 'Related guides', 'published': 'Published', 'all_work': 'All work',
           'projects_kicker': 'PROJECTS', 'projects_title': 'Real projects, step by step',
           'projects_sub': 'The full story of jobs HyperFab took from design to fabrication, with real footage of each step.',
           'read': 'Read the full project',
           'strip_kicker': 'REAL WORK', 'strip_title': 'Real work from HyperFab projects',
           'strip_sub': 'Real footage of parts HyperFab designed, made or saw through production for its customers.', 'strip_btn': 'The full mechanism-frame project',
           'svc_kicker': 'REAL PROJECT', 'svc_title': 'Real project: ', 'svc_btn': 'See the full project'},
}
