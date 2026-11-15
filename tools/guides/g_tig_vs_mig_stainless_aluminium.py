"""Guide: TIG vs MIG welding for stainless steel and 6000-series aluminium (fa/en)."""

SLUG = 'tig-vs-mig-stainless-aluminium'

FA = {
    'slug': SLUG,
    'title': 'فرق جوش آرگون (TIG) و جوش میگ (MIG) برای استیل و آلومینیوم',
    'desc': 'فرق جوش TIG و MIG در سرعت، ظاهر، اعوجاج و کاربرد؛ نکات جوشکاری استیل ضدزنگ و آلومینیوم ۶۰۶۱ و ۶۰۶۳ و اینکه آزمون VT، PT یا PAUT کجا لازم است.',
    'lead': ('جوش TIG یا همان جوش آرگون، با الکترود تنگستنی و سیم‌جوش جداگانه، جوشی تمیز، دقیق و بدون پاشش می‌دهد و برای ورق نازک، '
             'تجهیزات پزشکی و قطعات ظاهری مناسب‌تر است. جوش MIG سیم‌جوش را پیوسته تغذیه می‌کند، سریع‌تر است و برای درزهای طولانی و سازه‌ای '
             'اقتصادی‌تر. انتخاب نهایی به جنس، ضخامت، ظاهر موردنیاز و آزمون‌های جوش بستگی دارد.'),
    'updated': '2026-11-15',
    'service': 'welding',
    'img': 'assets/img/vz-tig-welding.jpg',
    'sections': [
        {'h': 'فرق جوش TIG و MIG چیست؟',
         'p': [
             'پاسخ کوتاه: TIG کندتر ولی کنترل‌پذیرتر است و جوشی تمیز و یکدست می‌دهد؛ MIG سریع‌تر است و در جوش‌های طولانی و سازه‌ای هزینه‌ی کمتری '
             'دارد. هیچ‌کدام ذاتاً بهتر نیست و روش مناسب را جنس، ضخامت، نوع اتصال و الزامات ظاهری و بهداشتی تعیین می‌کند.',
             'درباره‌ی نام‌ها: در بازار ایران «جوش آرگون» معمولاً به TIG گفته می‌شود و «جوش CO2» به جوشکاری با سیم‌جوش پیوسته، یعنی خانواده‌ی MIG/MAG. '
             'در اصطلاح فنی، MIG با گاز محافظ بی‌اثر (Inert) مثل آرگون کار می‌کند و روش سیمی مناسب آلومینیوم است؛ اگر گاز محافظ فعال (Active) باشد، '
             'مثل CO2 روی فولاد، نام درست آن MAG است. پس «جوش CO2» در اصل MAG است و آلومینیوم با CO2 جوش داده نمی‌شود. TIG هم با آرگون کار می‌کند '
             'و به همین دلیل گاهی به هر دو روش جوشکاری آرگون می‌گویند. املای «جوش‌کاری» و نام‌های «تیگ» و «میگ» هم رایج است.',
         ],
         'table': {
             'head': ['معیار', 'جوش TIG (آرگون)', 'جوش MIG'],
             'rows': [
                 ['سرعت', 'کندتر؛ سیم‌جوش جداگانه با دست اضافه می‌شود', 'سریع‌تر؛ سیم‌جوش پیوسته از مشعل تغذیه می‌شود'],
                 ['ظاهر جوش', 'تمیز و یکدست، بدون پاشش', 'خوب، با کمی پاشش که ممکن است پرداخت بخواهد'],
                 ['ورق نازک یا ضخیم', 'برای ورق نازک، لوله و درزهای حساس مناسب‌تر', 'برای مقاطع ضخیم‌تر و درزهای طولانی اقتصادی‌تر'],
                 ['اعوجاج', 'کنترل دقیق حرارت روی ورق نازک؛ در درز طولانی، سرعت کم حرارت را پخش می‌کند', 'حرکت سریع‌تر در درز طولانی؛ روی ورق نازک بدون تنظیم دقیق، خطر سوراخ‌شدن و تاب'],
                 ['مهارت جوشکار', 'مهارت و هماهنگی دو دست بیشتری می‌خواهد', 'یادگیری ساده‌تر، ولی تنظیم دستگاه تعیین‌کننده است'],
                 ['کاربرد رایج', 'تجهیزات پزشکی و غذایی، لوله‌ی استیل، قطعات ظاهری، پاس ریشه', 'شاسی و فریم، سازه‌های بزرگ، کار تیراژی'],
             ],
         }},
        {'h': 'جوش TIG یا جوش آرگون چیست و کجا به کار می‌رود؟',
         'p': [
             'در جوش TIG (مخفف Tungsten Inert Gas، با نام استاندارد GTAW) قوس بین یک الکترود تنگستنی مصرف‌نشدنی و قطعه برقرار می‌شود و آرگون '
             'حوضچه‌ی مذاب را از هوا محافظت می‌کند. سیم‌جوش یا فیلر (Filler) جداگانه اضافه می‌شود و جوشکار حرارت و مقدار فلز جوش را مستقل کنترل '
             'می‌کند؛ نتیجه جوشی باریک، تمیز و بدون پاشش است.',
             'به همین دلیل TIG برای ورق و لوله‌ی نازک استیل، قطعات ظاهری، پاس ریشه و تجهیزات '
             'پزشکی و غذایی روش رایج است. ضعف آن سرعت است و در درزهای طولانی یا مقاطع ضخیم، ساعت‌کار و هزینه بالا می‌رود.',
         ]},
        {'h': 'جوش MIG چیست و چه فرقی با جوش CO2 دارد؟',
         'p': [
             'در جوش MIG (مخفف Metal Inert Gas، با نام استاندارد GMAW) سیم‌جوش پیوسته از قرقره و از داخل مشعل به حوضچه می‌رسد و هم الکترود است و '
             'هم فلز پرکننده. نرخ رسوب بالاست و درزهای طولانی سریع‌تر و یکنواخت‌تر پر می‌شوند.',
             'فرق MIG با آنچه در بازار «جوش CO2» نامیده می‌شود در گاز محافظ است: بی‌اثر در MIG و فعال در MAG. برای آلومینیوم فقط گاز بی‌اثر مناسب '
             'است و روی استیل ضدزنگ معمولاً مخلوط‌های پایه‌ی آرگون به کار می‌رود. ظاهر جوش MIG، حتی در حالت پالسی (Pulsed)، معمولاً به یکدستی TIG نمی‌رسد. جای اصلی MIG شاسی، فریم، بدنه‌ی دستگاه و سازه‌های بزرگ است، جایی که سرعت و هزینه تعیین‌کننده‌اند.',
         ]},
        {'h': 'جوشکاری استیل ضدزنگ: تغییر رنگ، اسیدشویی و پسیواسیون چیست؟',
         'p': [
             'مقاومت استیل ضدزنگ در برابر خوردگی از لایه‌ی بسیار نازکی از اکسید کروم روی سطح می‌آید. حرارت جوش کنار درز رنگ‌های طلایی تا آبی ایجاد '
             'می‌کند که به آن تغییر رنگ حرارتی (Heat Tint) می‌گویند. هرچه رنگ تیره‌تر باشد، سطح زیر آن از کروم فقیرتر است و زودتر زنگ می‌زند. '
             'برای کم‌کردن آن حرارت ورودی کنترل می‌شود و در لوله و مخزن، پشت درز هم با آرگون محافظت می‌شود (Back Purging).',
             'پس از جوشکاری، تغییر رنگ معمولاً با اسیدشویی (Pickling) یا روش‌های مکانیکی برداشته می‌شود و با پسیواسیون (Passivation) لایه‌ی محافظ '
             'دوباره و یکنواخت شکل می‌گیرد. الزامات آن باید در نقشه یا شرح سفارش بیاید.',
             'در تجهیزات پزشکی، غذایی و بهداشتی، جوش باید صاف، بدون شکاف و حفره و قابل شست‌وشو باشد تا آلودگی در آن جمع نشود؛ برای همین TIG با نفوذ '
             'کامل و پرداخت جوش در این کاربردها رایج است. هایپرفب نمونه‌های زیادی برای صنایع پزشکی و دریایی ساخته است.',
         ]},
        {'h': 'جوشکاری آلومینیوم ۶۰۶۱ و ۶۰۶۳ چه نکاتی دارد؟',
         'p': [
             'سطح آلومینیوم همیشه با لایه‌ی نازک و سختی از اکسید پوشیده است که دمای ذوبش بسیار بالاتر از خود فلز است. اگر این لایه شکسته نشود، اتصال '
             'درست شکل نمی‌گیرد و آخال اکسید در جوش می‌ماند. برای همین جوش TIG آلومینیوم با جریان متناوب (AC) انجام می‌شود: در نیم‌سیکلی که الکترود '
             'مثبت است قوس لایه‌ی اکسید را می‌شکند (اثر تمیزکنندگی) و در نیم‌سیکل دیگر حرارت بیشتری به قطعه می‌رسد و نفوذ ایجاد می‌کند. در MIG '
             'آلومینیوم، سیم‌جوش قطب مثبت است و همین قطبیت اثر تمیزکنندگی را می‌دهد. رطوبت و چربی هم عامل اصلی تخلخل‌اند، پس درز پیش از جوشکاری چربی‌زدایی و برس‌زده می‌شود.',
             'آلیاژهای سری ۶۰۰۰، مثل ۶۰۶۱ و ۶۰۶۳، استحکام خود را تا حد زیادی از عملیات حرارتی می‌گیرند. حرارت جوش این اثر را در ناحیه‌ی متأثر از '
             'حرارت (HAZ) تا حدی از بین می‌برد و این ناحیه از فلز پایه نرم‌تر می‌شود. این نرم‌شدن در TIG و MIG هر دو رخ می‌دهد و باید در طراحی سازه '
             'دیده شود. این آلیاژها بدون سیم‌جوش مناسب مستعد ترک گرم‌اند، پس انتخاب فیلر بخشی از دستورالعمل جوشکاری است.',
         ]},
        {'h': 'بازرسی جوش: کی VT، کی PT و کی PAUT؟',
         'p': [
             'هایپرفب آزمون چشمی (VT)، مایع نافذ (PT)، فراصوتی آرایه‌فازی (PAUT) و آزمون‌های دیگر را به درخواست مشتری انجام می‌دهد. انتخاب آزمون به '
             'نوع عیبی بستگی دارد که نگران آن هستید:',
             'معیار پذیرش هم باید از پیش روشن باشد. برای جوش ذوبی فولاد، از جمله استیل ضدزنگ، سطح کیفی معمولاً طبق ISO 5817 و برای جوش قوسی '
             'آلومینیوم طبق ISO 10042 مشخص می‌شود و صلاحیت پرسنل آزمون غیرمخرب (NDT) معمولاً طبق ISO 9712 خواسته می‌شود. اگر پروژه‌ی شما سطح کیفی خاصی لازم دارد، آن را همراه نقشه اعلام کنید.',
         ],
         'ul': [
             'VT (بازرسی چشمی): پایه‌ی هر بازرسی و برای همه‌ی جوش‌ها؛ شکل و ابعاد جوش، ترک سطحی، بریدگی کناره (Undercut)، پاشش و تغییر رنگ را بررسی می‌کند.',
             'PT (مایع نافذ): ترک‌ها و ناپیوستگی‌های باز به سطح را نشان می‌دهد؛ روش رایج آزمون سطحی برای استیل ضدزنگ و آلومینیوم که معمولاً غیرمغناطیسی‌اند.',
             'PAUT (فراصوتی آرایه‌فازی): عیوب داخلی مثل عدم ذوب، ترک داخلی و حفره را با تصویر مقطع جوش نشان می‌دهد؛ برای جوش‌های نفوذ کامل و اتصال‌های سازه‌ای و باربر.',
         ]},
        {'h': 'قیمت جوشکاری TIG و MIG به چه عواملی بستگی دارد؟',
         'p': [
             'طراحی سازه با کارفرماست و هایپرفب ساخت را بر اساس نقشه‌ی تأییدشده‌ی شما انجام می‌دهد؛ نقشه پیش از شروع از نظر ساخت‌پذیری، ترتیب '
             'جوشکاری و کنترل اعوجاج بررسی و سپس قیمت اعلام می‌شود. عوامل اصلی قیمت:',
             'برای قیمت دقیق، نقشه، جنس، تعداد و آزمون‌های لازم را آماده کنید و با ۰۹۹۶۲۲۳۳۸۹۸ تماس بگیرید.',
         ],
         'ul': [
             'جنس قطعه: استیل ضدزنگ یا آلومینیوم سری ۶۰۰۰',
             'طول و نوع جوش و روش جوشکاری؛ TIG کندتر و MIG سریع‌تر است',
             'ابعاد سازه و فیکسچربندی؛ در سازه‌های بزرگ، مثل شاسی شبکه‌ای که روی چرخ نصب می‌شود و روی ریل حرکت می‌کند، صافی و هم‌راستایی در طول زیاد تعیین‌کننده است',
             'الزامات ظاهری و بهداشتی: پرداخت جوش، محافظت پشت درز و پاک‌سازی تغییر رنگ',
             'آزمون‌های درخواستی: VT، PT، PAUT یا آزمون‌های دیگر',
             'تعداد قطعات و تکرارپذیری کار',
         ]},
    ],
    'faq': [
        ('جوش TIG محکم‌تر است یا MIG؟',
         'هیچ‌کدام ذاتاً محکم‌تر نیست؛ استحکام اتصال به ذوب و نفوذ کامل، فیلر مناسب و نبود عیوبی مثل حفره و عدم ذوب بستگی دارد. '
         'در آلومینیوم سری ۶۰۰۰، نرم‌شدن ناحیه‌ی کنار جوش در هر دو روش استحکام را محدود می‌کند.'),
        ('چرا جوش TIG آلومینیوم با جریان AC انجام می‌شود؟',
         'چون لایه‌ی اکسید سطح آلومینیوم دمای ذوب بسیار بالاتری از خود فلز دارد. در جریان متناوب، نیم‌سیکل الکترود مثبت این لایه را می‌شکند و '
         'نیم‌سیکل دیگر نفوذ می‌دهد؛ بدون این اثر، اکسید در جوش حبس می‌شود.'),
        ('آزمون PT چه عیوبی را نشان می‌دهد؟',
         'آزمون مایع نافذ (PT) ترک‌ها، حفره‌ها و ناپیوستگی‌های باز به سطح را نشان می‌دهد. مایع رنگی به داخل عیب نفوذ می‌کند و پس از تمیزکردن سطح '
         'و زدن آشکارساز (Developer)، محل عیب دیده می‌شود. PT عیوب کاملاً داخلی را نشان نمی‌دهد.'),
        ('چه زمانی آزمون PAUT لازم است؟',
         'وقتی عیوب داخلی، مثل عدم ذوب، ترک داخلی یا حفره، برای ایمنی یا عملکرد قطعه مهم باشد؛ معمولاً در جوش‌های نفوذ کامل و اتصال‌های سازه‌ای '
         'و باربر.'),
    ],
    'related': ['aluminium-extrusion-die-design', 'powder-coating-process-finishes'],
}

EN = {
    'slug': SLUG,
    'title': 'TIG vs MIG Welding for Stainless Steel and 6000-Series Aluminium',
    'seo_title': 'TIG vs MIG for Stainless Steel and 6000 Aluminium',
    'desc': 'TIG vs MIG compared on speed, finish, distortion and use, with notes on welding stainless steel and 6061/6063 aluminium and when VT, PT or PAUT applies.',
    'lead': ('TIG welding uses a non-consumable tungsten electrode with filler added separately, giving clean, precise, spatter-free welds that suit '
             'thin sheet, medical equipment and cosmetic parts. MIG feeds wire continuously, so it is faster and cheaper on long structural seams. '
             'The right choice depends on material, thickness, required finish and the weld tests your project specifies.'),
    'updated': '2026-11-15',
    'service': 'welding',
    'img': 'assets/img/vz-tig-welding.jpg',
    'sections': [
        {'h': 'What is the difference between TIG and MIG welding?',
         'p': [
             'The short answer: TIG is slower but more controllable and leaves a clean, even bead; MIG is faster and cheaper on long and structural '
             'welds. Neither is better across the board. Material, thickness, joint type and any cosmetic or hygiene requirements decide which one fits.',
             'A note on names, since Iranian suppliers use Persian trade terms: “argon welding” usually means TIG, while “CO2 welding” means '
             'continuous-wire welding, the MIG/MAG family. Strictly, MIG uses an inert shielding gas such as argon and is the wire process for aluminium; '
             'with an active gas such as CO2 on carbon steel, the correct name is MAG. So “CO2 welding” is really MAG, and aluminium is never welded '
             'under CO2. TIG also runs on argon, which is why both processes sometimes get called argon welding.',
         ],
         'table': {
             'head': ['Criterion', 'TIG (GTAW)', 'MIG (GMAW)'],
             'rows': [
                 ['Speed', 'Slower; filler rod is added by hand', 'Faster; wire feeds continuously through the torch'],
                 ['Appearance', 'Clean, even bead with no spatter', 'Good, with some spatter that may need cleaning up'],
                 ['Thin vs thick material', 'Better on thin sheet, tube and delicate joints', 'More economical on thicker sections and long seams'],
                 ['Distortion', 'Fine heat control on thin sheet, though slow travel spreads heat on long seams', 'Faster travel on long seams; risk of burn-through and warping on thin sheet unless well tuned'],
                 ['Welder skill', 'Demands more skill and two-handed coordination', 'Easier to learn, but machine setup is critical'],
                 ['Typical use', 'Medical and food equipment, stainless tube, cosmetic parts, root passes', 'Chassis and frames, large structures, batch work'],
             ],
         }},
        {'h': 'What is TIG welding and where is it used?',
         'p': [
             'In TIG welding (Tungsten Inert Gas, standardised as GTAW), the arc burns between a non-consumable tungsten electrode and the workpiece while '
             'argon shields the pool from the air. Filler is added separately, so the welder controls heat and deposited metal independently and has '
             'fine command of bead shape and penetration.',
             'The result is a narrow, clean, spatter-free weld, which is why TIG is the default for thin stainless sheet and tube, cosmetic parts, root '
             'passes, and medical and food equipment. Its weakness is speed: on long seams or thick sections labour hours and '
             'cost climb quickly.',
         ]},
        {'h': 'What is MIG welding, and how does it relate to “CO2 welding”?',
         'p': [
             'In MIG welding (Metal Inert Gas, standardised as GMAW), wire feeds continuously from a spool through the torch and serves as both electrode '
             'and filler. Deposition is high, so long seams fill faster and more consistently.',
             'What separates MIG from market “CO2 welding” is the shielding gas: inert for MIG, active for MAG. Aluminium needs inert gas, and stainless '
             'is normally welded with argon-based mixtures. Pulsed MIG reduces spatter and heat input, but the bead rarely looks as even as TIG. MIG '
             'earns its place on chassis, frames, machine bodies and large structures, where speed and cost matter most.',
         ]},
        {'h': 'Welding stainless steel: heat tint, pickling and passivation',
         'p': [
             'Stainless steel resists corrosion thanks to an extremely thin chromium-oxide film. Welding heat leaves straw-to-blue colours beside the '
             'seam, called heat tint. The darker the tint, the more chromium-depleted the surface beneath it and the sooner it rusts. Controlling heat '
             'input helps, and on tube and vessels the back of the joint is purged with argon (back purging).',
             'After welding, heat tint is usually removed by pickling or mechanical means, and the surface is passivated so the protective film reforms '
             'evenly. The details depend on the grade, service environment and project specification, so they belong on the drawing or order. Tools and '
             'brushes reserved for stainless matter too, so no carbon-steel particles are left on the surface.',
             'In medical, food and sanitary equipment, welds must be smooth, free of crevices and pores, and easy to clean so contamination has nowhere '
             'to collect; full-penetration TIG with dressed beads is the norm. HyperFab has built many units for the medical and marine industries.',
         ]},
        {'h': 'Welding 6061 and 6063 aluminium: what to watch for',
         'p': [
             'Aluminium is always covered by a thin, tough oxide skin that melts at a far higher temperature than the metal underneath. If it is not '
             'broken up, the joint does not fuse properly and oxide gets trapped in the weld. That is why aluminium is TIG welded on alternating current '
             '(AC): during the electrode-positive half-cycle the arc scours away the oxide (cleaning action), and during the other half more heat goes '
             'into the work for penetration. In MIG the wire runs electrode-positive, which gives the same cleaning action. Degreasing and brushing the '
             'joint just before welding also matter, because moisture and grease are the main causes of porosity.',
             'The 6000-series alloys, such as 6061 and 6063, owe much of their strength to heat treatment. Welding heat partly undoes it in the '
             'heat-affected zone (HAZ), leaving that band softer than the parent metal. This happens with both TIG and MIG and must be allowed for in '
             'the structural design. These alloys are also prone to hot cracking without a suitable '
             'filler, so filler selection is part of the welding procedure.',
         ]},
        {'h': 'Weld inspection: when to use VT, PT or PAUT',
         'p': [
             'HyperFab carries out visual testing (VT), liquid penetrant testing (PT), phased-array ultrasonic testing (PAUT) and other tests on request. '
             'Which one you need depends on the defect you are worried about:',
             'Agree acceptance criteria up front too. For fusion welds in steel, including stainless, quality levels are typically specified per ISO 5817, '
             'and for arc welds in aluminium per ISO 10042; NDT personnel qualification is commonly requested per ISO 9712. If your project calls for a '
             'particular standard or quality level, state it with the drawings.',
         ],
         'ul': [
             'VT (visual testing): the baseline for every weld; checks weld shape and size, surface cracks, undercut, spatter and heat tint.',
             'PT (liquid penetrant): reveals surface-breaking cracks and discontinuities; the usual surface method for stainless steel and aluminium, which are generally non-magnetic.',
             'PAUT (phased-array ultrasonics): finds internal defects such as lack of fusion, internal cracks and porosity, with a cross-sectional image of the weld; used on full-penetration and load-bearing structural joints.',
         ]},
        {'h': 'What drives the cost of TIG and MIG welding?',
         'p': [
             'Structural design is the client’s, and HyperFab fabricates to your approved drawings. The drawings are first checked for manufacturability, '
             'welding sequence and distortion control, and then quoted. The main cost drivers are:',
             'For an exact quote, have your drawings, material, quantity and required tests ready and call 09962233898.',
         ],
         'ul': [
             'Material: stainless steel or 6000-series aluminium',
             'Weld length and type, and the process; TIG is slower, MIG faster',
             'Structure size and fixturing; on large frames, such as a framed chassis mounted on wheels that runs on rails, flatness and alignment over long lengths drive the effort',
             'Cosmetic and hygiene requirements: weld dressing, back purging and heat-tint removal',
             'Requested tests: VT, PT, PAUT or others',
             'Quantity and how repeatable the work is',
         ]},
    ],
    'faq': [
        ('Which is stronger, TIG or MIG?',
         'Neither is inherently stronger; joint strength comes from full fusion and penetration, the right filler, and freedom from defects such as '
         'porosity and lack of fusion. On 6000-series aluminium, HAZ softening limits strength whichever process is used.'),
        ('Why does aluminium need AC TIG?',
         'Aluminium’s oxide skin melts at a far higher temperature than the metal itself. On alternating current, the electrode-positive half-cycle '
         'breaks up that oxide and the other half delivers heat and penetration; without this cleaning action, oxide is trapped in the weld.'),
        ('What does PT detect?',
         'Liquid penetrant testing (PT) reveals cracks, pores and other discontinuities open to the surface. A dyed liquid seeps into the flaw and, once '
         'the surface is cleaned and developer applied, the indication shows. It cannot find fully internal defects; those need ultrasonic testing.'),
        ('When is PAUT needed?',
         'When internal defects such as lack of fusion, internal cracks or porosity matter for safety or function, typically in full-penetration and '
         'load-bearing structural welds.'),
    ],
    'related': ['aluminium-extrusion-die-design', 'powder-coating-process-finishes'],
}

GUIDE = {'fa': FA, 'en': EN}
