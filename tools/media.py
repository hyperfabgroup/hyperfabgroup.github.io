"""رسانه‌های واقعی هایپرفب: نمونه‌کارها (از inc-portfolio.php قالب ۲۰٫۰) و ویدیوهای آپارات (از inc-videos.php).
این‌ها عکس و فیلم خود هایپرفب‌اند و زیرنویس منبع آرشیوی نمی‌گیرند."""

WORKS = [
    {'img': 'assets/img/works/flange-steel-2.jpg', 'more': ['flange-steel-3', 'flange-steel-5', 'flange-steel-6'],
     'fa': ('مجموعه‌ی آب‌بند استیل ۳۰۴، تراشکاری CNC و جوش آرگون', 'استیل ۳۰۴ · صنایع فرآیندی',
            'ساخت کامل در هایپرفب: تراشکاری و سوراخ‌کاری دقیق CNC، جوش آرگون قطعات و تست PT جوش برای اطمینان از سلامت اتصال؛ با کنترل ابعادی نهایی مطابق نقشه، برای کاربرد صنعتی تحت فشار.'),
     'en': ('AISI 304 stainless sealing assembly, CNC-turned and TIG-welded', 'AISI 304 stainless · process industry',
            'Made end to end by HyperFab: precision CNC turning and drilling, TIG welding of the parts and a PT test of the welds to confirm joint integrity, with final dimensional inspection to the drawing, for a pressurised industrial application.')},
    {'img': 'assets/img/works/ptfe-part-1.jpg', 'more': ['ptfe-part-4', 'ptfe-part-3'],
     'fa': ('قطعه و واشر تفلون (PTFE) تراشکاری‌شده با CNC', 'تفلون PTFE · صنایع شیمیایی',
            'قطعات و واشرهای تفلونی با تراشکاری دقیق CNC، به‌صورت تیراژی. تلرانس‌ها برای آب‌بندی بدون نشتی در محیط خورنده رعایت شده است.'),
     'en': ('CNC-turned PTFE parts and gaskets', 'PTFE · chemical industry',
            'PTFE parts and gaskets CNC-turned in a production run, with tolerances held for leak-free sealing in corrosive service.')},
    {'img': 'assets/img/works/alu-cone-1.jpg', 'more': [],
     'fa': ('توپی فولادی CK45 تراشکاری‌شده با CNC', 'فولاد CK45 · صنعتی',
            'توپی فولادی با تراشکاری دقیق CNC؛ شیارها و پله‌ها با تلرانس دقیق برای قطعات دوّار و یاتاقان‌بندی.'),
     'en': ('CNC-turned CK45 steel hub', 'CK45 (C45) steel · industrial',
            'A CNC-turned steel hub with grooves and steps held to tight tolerances for rotating and bearing applications.')},
    {'img': 'assets/img/works/spline-shaft-1.jpg', 'more': [],
     'fa': ('شفت فولادی ماشین‌کاری‌شده با هزارخار در دو سر', 'فولاد · مکانیک و خودرو',
            'شفت با هزارخار در هر دو انتها برای انتقال گشتاور بالا؛ ماشین‌کاری دقیق برای درگیری کامل و بدون لقی.'),
     'en': ('Machined steel shaft splined at both ends', 'Steel · mechanical and automotive',
            'A shaft with splines at both ends for high-torque transmission, machined for full, backlash-free engagement.')},
    {'img': 'assets/img/works/steel-bush-1.jpg', 'more': [],
     'fa': ('بوش استیل ۳۰۴ تراشکاری‌شده', 'استیل ۳۰۴ · صنعتی',
            'بوش استیل با پله‌ها و شیارهای دقیق و سطح پرداخت تمیز، برای یاتاقان‌بندی و مواضع نیازمند ابعاد دقیق.'),
     'en': ('Turned AISI 304 stainless steel bushing', 'AISI 304 stainless · industrial',
            'A stainless bushing with precise steps and grooves and a clean finish, for bearing seats and other precision locations.')},
    {'img': 'assets/img/works/misc-parts-1.jpg', 'more': [],
     'fa': ('قطعات دقیق خارج از محور از برنج، استیل و پلیمر', 'برنج، استیل و پلیمر · مکانیزم',
            'مجموعه‌ای از قطعات کوچک و دقیق، از جمله قطعات خارج از محور، از برنج، استیل و پلیمر در یک پروژه، با کنترل ابعادی موشکافانه.'),
     'en': ('Precision off-axis parts in brass, stainless steel and polymer', 'Brass, stainless and polymer · mechanisms',
            'A set of small precision parts, including off-axis parts, in brass, stainless steel and polymer, made in one project with meticulous dimensional inspection.')},
]

VIDEOS = [
    ('poq88kr', 'tekeyab', ('تکه‌یاب: خرید تکه‌ی کوچک متریال صنعتی', 'قیمت تکه‌ی متریال را بدون تلفن پشت تلفن بگیرید.'),
     ('Tekeyab: buying small pieces of industrial material', 'Get a price for a piece of material without calling around.')),
    ('dne9rlc', 'multicolor-1', ('پرینت سه‌بعدی چندرنگ، قسمت ۱', 'هر بار که رنگ عوض می‌شود، داخل پرینتر چه می‌گذرد؟'),
     ('Multi-colour 3D printing, part 1', 'What happens inside the printer at every colour change?')),
    ('ghz7235', 'multicolor-2', ('پرینت سه‌بعدی چندرنگ، قسمت ۲', 'چرا پرینت رنگی این‌قدر پرتی دارد؟'),
     ('Multi-colour 3D printing, part 2', 'Why does colour 3D printing waste so much material?')),
    ('rbthfo9', 'gripper', ('گریپر پرینت سه‌بعدی: از یک عکس در گوشی تا قطعه‌ی واقعی', 'یک لینک از میکرورلد و چند روز بعد، گریپر در دست.'),
     ('3D-printed gripper: from a photo on a phone to a real part', 'One link to a model online, and a few days later the gripper is in hand.')),
    ('efnzfq6', 'order-guide', ('آموزش سفارش پرینت سه‌بعدی', 'سفارش از سایت هایپرفب در سه قدم.'),
     ('How to order a 3D print', 'Ordering on the HyperFab website in three steps.')),
    ('gqyd926', 'dragon', ('اژدهای مفصلی یک‌تکه با پرینت سه‌بعدی', 'مفصل‌های تودرتو، یک‌تکه از پرینتر.'),
     ('One-piece 3D-printed articulated dragon', 'Interlocking joints, printed in one piece.')),
    ('kxxl13o', 'print-price', ('زمان، یعنی قیمت پرینت سه‌بعدی', 'چرا زمان چاپ قیمت پرینت سه‌بعدی را تعیین می‌کند.'),
     ('Time is price in 3D printing', 'Why print time sets the price of a 3D print.')),
    ('knzjkwm', 'dino-battle', ('نبرد دایناسورهای مفصلی پرینت‌شده', 'سه دایناسور مفصلی رو در روی هم؛ کدام برنده است؟'),
     ('Battle of 3D-printed articulated dinosaurs', 'Three articulated printed dinosaurs face off. Which one wins?')),
]


def video_url(code):
    return 'https://www.aparat.com/v/' + code


def video_embed(code):
    return 'https://www.aparat.com/video/video/embed/videohash/' + code + '/vt/frame'


# ---------------------------------------------------------------- ویدیوهای واقعی کارگاه
# فیلم‌های خود هایپرفب که روی همین سایت میزبانی می‌شوند (assets/media/). از اینجا ساخته می‌شوند:
#   - نوار «کار واقعی» صفحه‌ی اصلی (home=True، به همین ترتیب)
#   - ویدیوهای صفحه‌ی پروژه (tools/projects.py با vid('شناسه', زبان))؛ VideoObject فقط آنجا ساخته می‌شود
#   - بلوک «پروژه‌ی واقعی» صفحه‌ی خدمت service (اولین ویدیوی هر خدمت که project دارد)
# برای ویدیوی تازه (مثلاً نورد رزوه یا فرز فلنج استیل): mp4 را در assets/media/ و پوستر jpg هم‌اندازه را
# در assets/img/works/ بگذارید و یک ردیف اینجا اضافه کنید. upload_date روز فیلم‌برداری است (YYYY-MM-DD)،
# duration به قالب ISO 8601 (PT51S). focus نقطه‌ی برش تصویر در کارت‌های مربعی نوار صفحه‌ی اصلی است.
REAL_VIDEOS = [
    {'id': 'tube-laser', 'src': 'assets/media/work-tube-laser.mp4', 'poster': 'assets/img/works/work-tube-laser.jpg',
     'w': 540, 'h': 960, 'upload_date': '2024-07-14', 'duration': 'PT51S',
     'project': 'mechanism-frame-st37', 'service': 'tubelaser', 'home': True, 'focus': '50% 40%',
     'fa': {'caption': 'برش لیزر قوطی فولادی برای فریم یک مکانیزم · تیر ۱۴۰۳',
            'name': 'برش لیزر قوطی فولادی St37 برای فریم یک مکانیزم',
            'desc': 'برش لیزر قوطی فولادی St37 با دستگاه لیزر لوله در هایپرفب؛ قطعات اسکلت فریم مکانیزمی که طراحی‌اش هم کار خود هایپرفب است.'},
     'en': {'caption': 'Tube laser cutting steel box section for a mechanism frame · Jul 2024',
            'name': 'Tube laser cutting St37 steel box section for a mechanism frame',
            'desc': 'Laser cutting St37 steel box section on a tube laser at HyperFab: the skeleton parts of a mechanism frame that HyperFab also designed.'}},
    {'id': 'frame-welding', 'src': 'assets/media/work-frame-welding.mp4', 'poster': 'assets/img/works/work-frame-welding.jpg',
     'w': 1280, 'h': 720, 'upload_date': '2024-10-09', 'duration': 'PT8S',
     'project': 'mechanism-frame-st37', 'service': 'welding', 'home': True, 'focus': '50% 50%',
     'fa': {'caption': 'جوش آرگون TIG فریم St37؛ قوطی لیزرشده و ورق خم‌شده · مهر ۱۴۰۳',
            'name': 'جوش آرگون TIG فریم St37',
            'desc': 'جوشکاری آرگون TIG قطعات قوطی برش‌خورده با لیزر به ورق برش‌خورده و خم‌شده؛ فریم St37 ساخت کارگاه هایپرفب.'},
     'en': {'caption': 'TIG welding the St37 frame: laser-cut tube and bent sheet · Oct 2024',
            'name': 'TIG welding an St37 steel frame',
            'desc': 'TIG welding laser-cut box-section parts to laser-cut, bent sheet: an St37 frame made in HyperFab’s workshop.'}},
    {'id': 'rivet-nut', 'src': 'assets/media/work-rivet-nut.mp4', 'poster': 'assets/img/works/work-rivet-nut.jpg',
     'w': 540, 'h': 960, 'upload_date': '2024-10-09', 'duration': 'PT13S',
     'project': 'mechanism-frame-st37', 'service': None, 'home': True, 'focus': '50% 35%',
     'fa': {'caption': 'نصب مهره‌پرچ با ابزار بادی روی ورق نازک همان فریم · مهر ۱۴۰۳',
            'name': 'نصب مهره‌پرچ با ابزار بادی روی ورق نازک',
            'desc': 'نصب مهره‌پرچ با ابزار پرچ بادی روی ورق نازک فریم St37 در هایپرفب، تا پیچ‌ها رزوه‌ی کامل و محکم داشته باشند.'},
     'en': {'caption': 'Fitting rivet nuts in the frame’s thin sheet with a pneumatic tool · Oct 2024',
            'name': 'Fitting rivet nuts in thin sheet with a pneumatic tool',
            'desc': 'Installing rivet nuts with a pneumatic rivet-nut tool in the thin sheet of an St37 frame at HyperFab, so the screws get full, strong threads.'}},
    {'id': 'flange-milling', 'src': 'assets/media/work-flange-milling.mp4', 'poster': 'assets/img/works/work-flange-milling.jpg',
     'w': 540, 'h': 960, 'upload_date': '2023-11-30', 'duration': 'PT29S',
     'project': None, 'service': 'turning', 'home': True, 'focus': '50% 45%',
     'fa': {'caption': 'فرزکاری چهارپهلوی داخل یک فلنج استیل · آذر ۱۴۰۲',
            'name': 'فرزکاری چهارپهلوی داخل فلنج استیل',
            'desc': 'فلنج استیلی که داخلش باید چهارپهلو می‌شد، روی دستگاه فرز در هایپرفب ماشین‌کاری می‌شود؛ فرزکاری استیل از کارهای دشوار ماشین‌کاری است. قطعه برای مشتری ساخته شده است.'},
     'en': {'caption': 'Milling a square bore inside a stainless flange · Nov 2023',
            'name': 'Milling a square bore in a stainless steel flange',
            'desc': 'A stainless flange whose bore had to be square, machined on a milling machine at HyperFab; milling stainless is among the hardest machining jobs. Made for a customer.'}},
]

REAL_BY_ID = {v['id']: v for v in REAL_VIDEOS}


def vid(vid_id, lang):
    """ویدیوی واقعی برای بخش صفحه‌ی پروژه: {'id','src','poster','w','h','name','desc','upload_date','duration'}"""
    v = REAL_BY_ID[vid_id]
    return {'id': v['id'], 'src': v['src'], 'poster': v['poster'], 'w': v['w'], 'h': v['h'],
            'upload_date': v['upload_date'], 'duration': v['duration'],
            'name': v[lang]['name'], 'desc': v[lang]['desc']}
