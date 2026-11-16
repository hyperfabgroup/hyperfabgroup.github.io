"""Guide: tube laser vs saw, drill and punch; designing self-locating tab-and-slot box-section frames (fa/en)."""

SLUG = 'tube-laser-frame-design'

FA = {
    'slug': SLUG,
    'title': 'برش لیزر پروفیل یا اره، دریل و پانچ؟ طراحی فریم قوطی با اتصال زبانه و شیار',
    'seo_title': 'برش لیزر پروفیل یا اره و دریل؟ فریم زبانه و شیار',
    'short': 'برش لیزر پروفیل و فریم زبانه و شیار',
    'desc': 'فرق برش لیزر پروفیل با اره، دریل و پانچ در ساخت فریم قوطی؛ اتصال زبانه و شیار، نکات طراحی، برش دهان‌ماهی و فارسی‌بر، و مسیر جوش و رنگ تا فریم آماده.',
    'lead': ('برش لیزر پروفیل، برش به طول، سوراخ‌ها و فرم سرِ اتصال را در یک مرحله می‌زند؛ '
             'اره و دریل همین کار را در چند مرحله انجام می‌دهند و پانچ برای هر الگوی سوراخ قالب می‌خواهد. '
             'در فریم قوطی، اتصال زبانه و شیار قطعات را پیش از جوش در جای درست نگه می‌دارد و جوشکاری را سریع‌تر و تکرارپذیرتر می‌کند.'),
    'updated': '2026-11-15',
    'service': 'tubelaser',
    'img': 'assets/img/vz-tube-laser.jpg',
    'img_alt': 'هد لیزر در حال برش پروفیل فولادی با جرقه؛ تصویر آرشیوی (ساخته‌شده با هوش مصنوعی)',
    'keywords': ('برش لیزر پروفیل, برش لیزر قوطی, اتصال زبانه و شیار, فریم زبانه و شیار, ساخت فریم قوطی, '
                 'برش دهان ماهی لوله, برش فارسی بر قوطی, لیزر تیوب, برش لیزر یا اره و دریل, هایپرفب'),
    'sections': [
        {'h': 'برش لیزر پروفیل یا اره، دریل و پانچ: کدام برای فریم قوطی بهتر است؟',
         'p': [
             'پاسخ کوتاه: برای قطعه‌ی پروفیلی که چند سوراخ، شیار یا سرِ فرم‌دار دارد و باید در فریم دقیق جا بیفتد، '
             'برش لیزر پروفیل (Tube Laser Cutting)، که در بازار «لیزر تیوب» هم گفته می‌شود، معمولاً انتخاب بهتری است. '
             'همه‌ی برش‌ها با یک برنامه و بدون باز و بسته کردن دوباره‌ی قطعه زده می‌شوند و جای همه از یک مبنا، یعنی سرِ قطعه، می‌آید. '
             'اره و دریل برای برش صاف با سوراخ کم هنوز کافی‌اند و پانچ برای الگوی سوراخ ثابت در تیراژ خیلی بالا ساخته شده است.',
         ],
         'table': {'head': ['معیار', 'برش لیزر پروفیل', 'اره و دریل', 'پانچ پروفیل'],
                   'rows': [
                       ['تعداد مراحل', 'برش به طول، سوراخ و شیار در یک مرحله', 'برش، خط‌کشی و سوراخکاری در چند مرحله', 'برش به طول جدا، سپس یک یا چند ضرب پرس'],
                       ['ابزار و قالب', 'بدون قالب؛ شکل از روی نقشه برنامه‌ریزی می‌شود', 'ابزار عمومی؛ سوراخ فرم‌دار ابزار مخصوص می‌خواهد', 'قالب مخصوص برای هر الگوی سوراخ'],
                       ['جای سوراخ نسبت به سرِ قطعه', 'دقیق و از یک مبنا', 'وابسته به خط‌کشی و دقت اپراتور', 'پس از تنظیم قالب، ثابت و تکرارپذیر'],
                       ['کیفیت لبه', 'لبه‌ی تمیز با کار تکمیلی کم', 'معمولاً پلیسه‌گیری و سنگ‌کاری می‌خواهد', 'بسته به جنس و قالب، ممکن است پلیسه‌گیری بخواهد'],
                       ['تغییر طرح', 'اصلاح نقشه و برنامه', 'شابلون یا روش اندازه‌گیری تازه', 'اصلاح قالب یا ساخت قالب تازه'],
                       ['مناسب برای', 'قطعات پرجزئیات و فریم‌ها، از نمونه تا تیراژ', 'کار تکی با برش صاف و سوراخ کم', 'تیراژ خیلی بالا با چند سوراخ ساده و تکراری'],
                   ]}},
        {'h': 'فریم قوطی به روش سنتی چطور ساخته می‌شود و خطا از کجا وارد می‌شود؟',
         'p': [
             'در روش رایج، شاخه‌ی قوطی با اره به طول بریده می‌شود، جای سوراخ‌ها با متر و گونیا خط‌کشی و سنبه‌نشان می‌شود، '
             'سوراخ‌ها با دریل زده می‌شوند و سرها با سنگ پلیسه‌گیری می‌شوند. هر قطعه چند بار بسته و باز و از نو اندازه‌گیری می‌شود.',
             'خطا دقیقاً در همین جابه‌جایی‌ها وارد می‌شود: خطای کوچک متر و خط‌کشی، لقی گیره در هر مرحله و تفاوت دست اپراتورها. '
             'این خطاها روی هم جمع می‌شوند و سرِ مونتاژ به شکل گونیا نبودن قاب، فاصله‌ی ناهمسان سوراخ‌ها یا درز باز دیده می‌شوند؛ نتیجه، اصلاح با سنگ و پرکردن فاصله با جوش است.',
             'برای مهار این خطاها معمولاً فیکسچر یا شابلون جوش (Jig) ساخته می‌شود که خودش هزینه‌ی ساخت دارد و با هر تغییر طرح باید اصلاح شود؛ '
             'در تیراژ کم، این هزینه سهم بزرگی از قیمت فریم است.',
         ]},
        {'h': 'اتصال زبانه و شیار (Tab and Slot) چیست و چرا جوشکاری فریم را سریع‌تر می‌کند؟',
         'p': [
             'در اتصال زبانه و شیار، روی سرِ یک عضو فریم زبانه‌ای برش می‌خورد و روی عضو مقابل شیاری هم‌اندازه‌ی آن. '
             'وقتی زبانه در شیار می‌نشیند، جای عضو در طول، عرض و زاویه مشخص می‌شود؛ قطعات خودشان جای خود را پیدا می‌کنند و به همین دلیل '
             'به این فریم‌ها خودمکان‌یاب (Self-locating) هم می‌گویند.',
             'به‌جای اندازه‌گیری و نگه‌داشتن هر قطعه با گیره، قطعات در هم جا می‌روند و خال‌جوش زده می‌شوند. '
             'نیاز به فیکسچر کم می‌شود و چون جای قطعات را هندسه‌ی برش تعیین می‌کند، نه دست اپراتور، فریم‌های یک سری شبیه هم از کار درمی‌آیند.',
             'یک نکته را نباید فراموش کرد: زبانه و شیار ابزار جاگذاری است، نه جایگزین جوش. استحکام فریم از جوش و طراحی سازه می‌آید '
             'و زبانه فقط کمک می‌کند جوش در جای درست زده شود.',
         ]},
        {'h': 'نکات طراحی فریم زبانه و شیار برای برش لیزر قوطی',
         'p': [
             'این نکات را از ابتدا در نقشه رعایت کنید؛ هایپرفب هم نقشه را پیش از برش از نظر امکان اجرا بررسی می‌کند.',
         ],
         'ul': [
             'لقی مناسب: در زبانه و شیار کمی لقی بگذارید تا قطعات بدون ضربه جا بروند؛ اما شیار خیلی گشاد دیگر قطعه را مکان‌یابی نمی‌کند.',
             'دوری از شعاع گوشه: گوشه‌ی قوطی گرد است و شیار یا سوراخی که روی این شعاع بیفتد شکلش عوض می‌شود. لبه‌ی شیارها و سوراخ‌ها را روی بخش تخت وجه نگه دارید.',
             'درز جوش قوطی و لوله: قوطی و لوله‌ی درزدار در داخل یک خط جوش دارند. اگر زبانه یا شیاری نباید روی درز بیفتد، در نقشه بنویسید.',
             'طول زبانه و ضخامت دیواره: طول زبانه را با ضخامت دیواره‌ی عضو مقابل هماهنگ کنید و مشخص کنید سرِ زبانه باید هم‌سطح بماند یا برای جوش کمی بیرون بزند.',
             'جلوگیری از جهت اشتباه: جایی که ممکن است، عوارض را متقارن بگذارید تا جهت قطعه اهمیتی نداشته باشد؛ وگرنه یک زبانه یا شیار را متفاوت طراحی کنید تا قطعه در جهت اشتباه جا نرود.',
             'شماره‌گذاری قطعات: در فریم‌های چندعضوی، شماره‌ی هر قطعه را در نقشه بدهید. علامت‌گذاری لیزری شماره روی قطعه، بسته به مقطع، به درخواست شما بررسی می‌شود.',
         ]},
        {'h': 'برش دهان‌ماهی (زین‌اسبی) و برش فارسی‌بر در اتصال لوله و قوطی',
         'p': [
             'وقتی لوله‌ای به بدنه‌ی لوله‌ی دیگر جوش می‌شود، سرِ آن باید به شکل لوله‌ی مقابل فرم بگیرد. به این فرم برش دهان‌ماهی (زین‌اسبی) (Coping یا Fish-mouth) می‌گویند. '
             'به‌جای تقریب زدن با شابلون کاغذی و سنگ، برش لیزر فرم را از روی هندسه‌ی واقعی دو لوله برنامه‌ریزی می‌کند '
             'تا دو لوله بی‌فاصله روی هم بنشینند و جوش یکنواخت‌تر شود. برش دهان‌ماهی روی لوله‌های جدار ضخیم پس از بررسی نقشه تأیید می‌شود.',
             'برش فارسی‌بر (که «فارسی بر» هم نوشته می‌شود؛ Mitre Cut) سرِ مایل قوطی یا پروفیل برای گوشه‌ی قاب است. اگر دو عضو با برش فارسی‌بر دقیق به هم برسند، '
             'گوشه بدون فاصله بسته می‌شود و گونیا بودن قاب کمتر به مهارت جوشکار وابسته است. زاویه‌ی قابل‌اجرا به مقطع بستگی دارد. '
             'قطعات ورقی کنار فریم، مثل لچکی و صفحه‌ی پایه، را می‌توان جداگانه از راه برش لیزر ورق در hyperfab.ir آنلاین سفارش داد.',
         ]},
        {'h': 'چه وقت پانچ یا اره هنوز انتخاب درستی است؟',
         'p': [
             'برش لیزر همیشه ارزان‌ترین راه نیست. اگر قطعه فقط چند سوراخ ساده و تکراری دارد، طرح نهایی شده و تیراژ خیلی بالاست، '
             '<a href="{home}punching/">پانچ لوله و پروفیل</a> پس از ساخت قالب می‌تواند اقتصادی‌تر باشد، چون هزینه‌ی قالب روی کل تیراژ سرشکن می‌شود. '
             'هایپرفب پانچ را هم انجام می‌دهد و بر اساس هندسه و تیراژ، روش مناسب را پیشنهاد می‌کند.',
             'اره هم برای برش صاف چند شاخه با یکی دو سوراخ کافی است. اما هرچه تعداد سوراخ‌ها، شیارها و سرهای فرم‌دار بیشتر شود و فریم به دقت ابعادی بیشتری نیاز داشته باشد، مزیت برش لیزر بیشتر می‌شود.',
         ]},
        {'h': 'از قطعه‌ی بریده تا فریم آماده: جوش، رنگ و عوامل مؤثر بر قیمت',
         'p': [
             'در هایپرفب می‌توانید پس از برش لیزر، جوشکاری TIG و MIG فریم‌های استیل ضدزنگ و آلومینیوم سری ۶۰۰۰ '
             'را بر اساس نقشه‌ی تأییدشده‌ی خودتان و سپس رنگ کوره‌ای (پودری) را در سفارش تیراژی بسپارید؛ '
             'در این حالت همان طرفی که زبانه و شیار را بریده، مسئول جوش و ابعاد نهایی فریم هم هست. '
             'فریم‌های آهنی (فولاد St37) را هم هایپرفب با جوش آرگون TIG جوشکاری می‌کند؛ نمونه‌اش <a href="{home}portfolio/mechanism-frame-st37/">فریم مکانیزمی از قوطی و ورق St37</a> است. '
             'اگر ترجیح می‌دهید، قطعات بریده‌شده را هم می‌توانید آماده‌ی مونتاژ تحویل بگیرید تا جوشکار خودتان آن‌ها را جوش بدهد.',
             'قیمت برش لیزر پروفیل پیش از دیدن نقشه قابل اعلام نیست و از ترکیب این عوامل به دست می‌آید:',
             'برای قیمت دقیق، فایل STEP یا نقشه‌ی فریم را همراه با مقطع، جنس و تعداد در پیام‌رسان بله بفرستید یا با کارشناس پروژه‌های صنعتی هایپرفب '
             'به شماره‌ی ۰۹۹۶۲۲۳۳۸۹۸ تماس بگیرید.',
         ],
         'ul': [
             'مقطع: قوطی مربع و مستطیل، لوله‌ی گرد، نبشی، ناودانی یا مقاطع خاص.',
             'جنس: آهن، استیل یا آلومینیوم.',
             'تعداد برش‌ها، سوراخ‌ها، شیارها و سرهای فرم‌دار هر قطعه.',
             'تیراژ: نمونه، تیراژ اولیه‌ی کوچک یا سفارش تیراژی.',
             'تأمین متریال توسط شما یا هایپرفب.',
             'کارهای بعدی مثل جوش فریم استیل، آهن (St37) یا آلومینیوم، رنگ کوره‌ای یا آندایز.',
         ]},
    ],
    'faq': [
        ('فریم زبانه و شیار به‌اندازه‌ی کافی محکم است یا زبانه فقط برای جاگذاری است؟',
         'زبانه و شیار ابزار جاگذاری است و قطعات را پیش از جوش در جای درست نگه می‌دارد. '
         'استحکام فریم از جوش و طراحی سازه می‌آید، نه از خود زبانه؛ پس فریم باید مثل هر سازه‌ی جوشی دیگر جوش و کنترل شود.'),
        ('برای برش لیزر قطعات فریم حتماً فایل سه‌بعدی لازم است؟',
         'نه، اما بهترین ورودی است. فایل STEP یا IGES رابطه‌ی زبانه‌ها و شیارها را دقیق نشان می‌دهد. '
         'اگر ندارید، نقشه‌ی دوبعدی، DXF یا PDF هم پذیرفته می‌شود، به شرطی که مقطع و ابعادش روشن نوشته شده باشد.'),
        ('جوش و رنگ فریم را هم انجام می‌دهید؟',
         'بله. پس از برش لیزر، هایپرفب فریم‌های استیل ضدزنگ و آلومینیوم سری ۶۰۰۰ را با جوش TIG و MIG و فریم‌های آهنی (فولاد St37) را با جوش TIG، بر اساس نقشه‌ی شما جوشکاری می‌کند و سپس رنگ کوره‌ای را در سفارش تیراژی انجام می‌دهد. '
         'اگر ترجیح می‌دهید، قطعات بریده‌شده را هم می‌توانید آماده‌ی جوش تحویل بگیرید.'),
        ('برای تیراژ من برش لیزر ارزان‌تر است یا اره و دریل؟',
         'به تعداد سوراخ‌ها، شیارها و سرهای فرم‌دار هر قطعه و به تیراژ بستگی دارد. قطعه‌ی پرجزئیات معمولاً با لیزر و برش صاف با یکی دو سوراخ با اره و دریل به‌صرفه‌تر است. '
         'نقشه را بفرستید یا با ۰۹۹۶۲۲۳۳۸۹۸ تماس بگیرید تا روش مناسب پیشنهاد شود.'),
    ],
    'related': ['punching-cost-sheet-tube-pe-pipe', 'tig-vs-mig-stainless-aluminium'],
}

EN = {
    'slug': SLUG,
    'title': 'Tube Laser vs Saw, Drill and Punch: Designing Self-Locating Box-Section Frames',
    'seo_title': 'Tube Laser vs Saw & Drill: Tab-and-Slot Frames',
    'short': 'Tube laser vs saw & drill for frames',
    'desc': 'Tube laser cutting vs sawing, drilling and punching for box-section frames: tab-and-slot design rules, coped and mitred joints, then welding and coating.',
    'lead': ('A tube laser cuts the length, holes, slots and joint ends of a profile in one programmed setup. '
             'Sawing and drilling get there in several steps with marking out and re-clamping, and punching needs a die for every hole pattern. '
             'In box-section frames, tab-and-slot joints locate each member before welding, so frames weld faster and come out consistent.'),
    'updated': '2026-11-15',
    'service': 'tubelaser',
    'img': 'assets/img/vz-tube-laser.jpg',
    'img_alt': 'Laser head cutting a steel profile with sparks; stock image (AI-generated)',
    'keywords': ('tube laser cutting, tube laser vs saw and drill, tab and slot frame, self-locating weld frame, '
                 'box section frame design, coped pipe joint, fish-mouth cut, mitre cut, HyperFab'),
    'sections': [
        {'h': 'Tube laser, saw and drill, or punching: which suits a box-section frame?',
         'p': [
             'The short answer: for a profile part with several holes, slots or shaped ends that has to fit accurately into a frame, '
             'tube laser cutting is usually the better choice. Every feature is cut from one program without re-clamping, '
             'so all of them are positioned from the same datum, the end of the part. '
             'Sawing and drilling still do the job for straight cuts with few holes, and punching is built for a fixed hole pattern at very high volume.',
         ],
         'table': {'head': ['Criterion', 'Tube laser cutting', 'Saw and drill', 'Profile punching'],
                   'rows': [
                       ['Setups', 'Cut to length, holes and slots in one setup', 'Cutting, marking out and drilling in several steps', 'Separate cut to length, then one or more press strokes'],
                       ['Tooling', 'No die; shapes are programmed from the drawing', 'General tools; shaped holes need special tooling', 'A dedicated die for each hole pattern'],
                       ['Hole position relative to the ends', 'Accurate, from a single datum', 'Depends on marking out and operator skill', 'Fixed and repeatable once the die is set'],
                       ['Edge quality', 'Clean edge with little finishing', 'Usually needs deburring and grinding', 'May need deburring, depending on material and die'],
                       ['Design changes', 'Update the drawing and program', 'New template or measuring routine', 'Modify the die or build a new one'],
                       ['Best for', 'Feature-rich parts and frames, from sample to batch', 'One-offs with straight cuts and few holes', 'Very high volumes with a few simple, repeated holes'],
                   ]}},
        {'h': 'How is a box-section frame made conventionally, and where do errors creep in?',
         'p': [
             'The usual route: the tube is sawn to length, hole positions are measured and marked with a tape and square, centre-punched and drilled, '
             'and the ends are deburred with a grinder. Each part is clamped, unclamped and measured again several times.',
             'That handling is exactly where errors get in: small tape and marking errors, clamp play at each step, and differences between operators. '
             'They add up and show at assembly as an out-of-square frame, mismatched hole spacing or open gaps, which means grinding to fit and filling gaps with weld.',
             'To control this, shops usually build a welding jig, which has its own build cost and must be reworked whenever the design changes; '
             'on a small run, the jig can be a large share of the frame price.',
         ]},
        {'h': 'What is a tab-and-slot frame, and why does it weld faster?',
         'p': [
             'In a tab-and-slot joint, a tab is cut on the end of one frame member and a matching slot in the member it meets. '
             'When the tab drops into the slot, the member is located in length, width and angle: the parts find their own position, which is why these are called self-locating frames.',
             'Instead of measuring and clamping each part, the welder slots the members together and tacks them. '
             'Fixturing is reduced, and because the cut geometry, not the operator, sets where each part sits, frames in a batch come out alike.',
             'One point matters: tab and slot is a locating aid, not a replacement for the weld. The frame’s strength comes from the welds and the structural design; '
             'the tab only makes sure the weld goes in the right place.',
         ]},
        {'h': 'Design rules for tab-and-slot box-section frames',
         'p': [
             'Build these into the drawing from the start; HyperFab also reviews the drawing for manufacturability before cutting.',
         ],
         'ul': [
             'Fit clearance: leave a little clearance in tabs and slots so parts go together without hammering, but not so much that the slot stops locating.',
             'Keep off the corner radii: box section has rounded corners, and a slot or hole that runs onto the radius changes shape. Keep feature edges on the flat part of the face.',
             'Weld seam: welded tube and pipe carry a weld seam on the inside. If a tab or slot must not land on the seam, say so on the drawing.',
             'Tab length and wall: match tab length to the wall of the mating member, and state whether the tab should finish flush or stand slightly proud for welding.',
             'Wrong-way assembly: where you can, make features symmetric so orientation does not matter; otherwise make one tab or slot different so the part cannot go in backwards.',
             'Part numbering: on multi-member frames, give every part a number on the drawing. Laser-marking the number on the part can be considered on request, depending on the section.',
         ]},
        {'h': 'Coped (fish-mouth) and mitred joints in pipe and box section',
         'p': [
             'When one pipe is welded onto the side of another, its end has to be shaped to the mating pipe. This is called a coped, fish-mouth or saddle cut. '
             'Instead of approximating it with a paper template and a grinder, a tube laser programs the cope from the real geometry of both pipes, so they sit together without gaps and weld more evenly. On thick-wall pipe, coping is confirmed after reviewing the drawing.',
             'A mitre cut is an angled end on box section or profile for a frame corner. When two members meet on accurate mitres, the corner closes without a gap '
             'and squareness depends less on the welder’s skill. The achievable angle depends on the section. '
             'Sheet parts that go with the frame, such as gussets and base plates, can be ordered separately online through sheet metal laser cutting on hyperfab.ir.',
         ]},
        {'h': 'When do punching or sawing still make sense?',
         'p': [
             'Laser cutting is not always the cheapest route. If a part has only a few simple, repeated holes, the design is frozen and the volume is very high, '
             '<a href="{home}punching/">tube and profile punching</a> can be more economical once the die is made, because the die cost is spread across the whole run. '
             'HyperFab does punching too, and recommends the process that suits the geometry and quantity.',
             'A saw is also fine for straight cuts on a few lengths with a hole or two. But the more holes, slots and shaped ends a part carries, and the tighter the frame has to be, the stronger the case for the laser.',
         ]},
        {'h': 'From cut parts to a finished frame: welding, coating and what drives the price',
         'p': [
             'After laser cutting, HyperFab can also carry out TIG and MIG welding of stainless steel '
             'and 6000-series aluminium frames to your approved design, followed by powder coating for batch orders; '
             'whoever cut the tabs and slots is then also responsible for the welding and final frame dimensions. '
             'HyperFab also TIG welds mild-steel (St37) frames; one example is a <a href="{home}portfolio/mechanism-frame-st37/">mechanism frame made from St37 box section and sheet</a>. '
             'If you prefer, the parts can still be delivered cut and ready to assemble for your own welder.',
             'A tube laser price cannot be given before the drawing is seen; it comes from a combination of these factors:',
             'For an exact quote, send the STEP file or frame drawing with the section, material and quantity on Bale, or call HyperFab’s industrial projects specialist on 09962233898 (+98 996 223 3898).',
         ],
         'ul': [
             'Section: square and rectangular tube, round pipe, angle, channel or special sections.',
             'Material: mild steel, stainless steel or aluminium.',
             'The number of cuts, holes, slots and shaped ends on each part.',
             'Quantity: sample, small first run or batch order.',
             'Whether you or HyperFab supply the material.',
             'Follow-on work such as welding a stainless, St37 steel or aluminium frame, powder coating or anodizing.',
         ]},
    ],
    'faq': [
        ('Is a tab-and-slot frame strong enough, or is the tab only a locating aid?',
         'It is a locating aid: tabs and slots hold the members in the right place before welding. '
         'The strength comes from the welds and the structural design, not from the tabs, so the frame should be welded and checked like any other welded structure.'),
        ('Do I need a 3D file?',
         'No, but it is the best input. A STEP or IGES model shows exactly how the tabs and slots relate. '
         'Without one, a 2D drawing, DXF or PDF is accepted, as long as the section and its dimensions are clearly stated.'),
        ('Can you weld and paint the frame too?',
         'Yes. After laser cutting, HyperFab TIG and MIG welds stainless steel and 6000-series aluminium frames and TIG welds mild-steel (St37) frames to your drawing, followed by powder coating for batch orders. '
         'If you prefer, cut parts can also be delivered ready for welding.'),
        ('Which is cheaper for my quantity: laser or saw and drill?',
         'It depends on how many holes, slots and shaped ends each part has, and on the quantity. Feature-rich parts usually favour the laser; a straight cut with a hole or two may favour the saw and drill. '
         'Send the drawing or call 09962233898 and HyperFab will recommend the right route.'),
    ],
    'related': ['punching-cost-sheet-tube-pe-pipe', 'tig-vs-mig-stainless-aluminium'],
}

GUIDE = {'fa': FA, 'en': EN}
