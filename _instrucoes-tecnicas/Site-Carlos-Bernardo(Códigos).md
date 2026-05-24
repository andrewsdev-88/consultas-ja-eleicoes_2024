<!-- Carlos Bernardo - Home i18n Multi-Language -->
<!DOCTYPE html><html class="dark" lang="pt-BR"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                "surface-container-highest": "#353533",
                "primary": "#ffb68d",
                "on-error": "#690005",
                "background": "#131312",
                "on-primary-fixed-variant": "#6c3919",
                "on-secondary": "#412d00",
                "tertiary-fixed": "#d7e8c5",
                "surface-container-high": "#2a2a29",
                "surface-bright": "#3a3938",
                "on-tertiary-fixed": "#121f09",
                "inverse-surface": "#e5e2e0",
                "glass-stroke": "rgba(255, 255, 255, 0.08)",
                "tertiary-fixed-dim": "#bbccaa",
                "surface-container-low": "#1c1c1a",
                "primary-container": "#c3815b",
                "on-secondary-fixed": "#261900",
                "secondary": "#e4c285",
                "surface-container": "#20201e",
                "tertiary-container": "#869677",
                "secondary-fixed": "#ffdea4",
                "tertiary": "#bbccaa",
                "surface-tint": "#ffb68d",
                "canvas-light": "#F5F0EB",
                "on-tertiary": "#27341d",
                "surface-variant": "#353533",
                "inverse-primary": "#89502e",
                "inverse-on-surface": "#31302f",
                "on-surface-variant": "#d7c2b8",
                "secondary-fixed-dim": "#e4c285",
                "secondary-container": "#5d4514",
                "outline": "#9f8d84",
                "on-primary-container": "#481d01",
                "on-secondary-fixed-variant": "#5a4312",
                "on-primary": "#512405",
                "error-container": "#93000a",
                "on-surface": "#e5e2e0",
                "glass-fill": "rgba(15, 15, 14, 0.6)",
                "on-secondary-container": "#d5b478",
                "primary-fixed": "#ffdbc9",
                "on-tertiary-fixed-variant": "#3d4b31",
                "surface": "#131312",
                "primary-fixed-dim": "#ffb68d",
                "on-tertiary-container": "#202d16",
                "outline-variant": "#52443c",
                "error": "#ffb4ab",
                "on-error-container": "#ffdad6",
                "surface-container-lowest": "#0e0e0d",
                "surface-dim": "#131312",
                "on-primary-fixed": "#331200",
                "on-background": "#e5e2e0"
            },
            "borderRadius": {
                "DEFAULT": "0.125rem",
                "lg": "0.25rem",
                "xl": "0.5rem",
                "full": "0.75rem"
            },
            "spacing": {
                "container-max": "1440px",
                "margin-mobile": "20px",
                "margin-desktop": "80px",
                "gutter": "24px",
                "unit": "8px",
                "section-gap": "160px"
            },
            "fontFamily": {
                "button-text": ["Inter"],
                "label-caps": ["Inter"],
                "headline-xl": ["Playfair Display"],
                "headline-xl-mobile": ["Playfair Display"],
                "display-lg-mobile": ["Playfair Display"],
                "body-md": ["Inter"],
                "display-lg": ["Playfair Display"],
                "headline-md": ["Playfair Display"],
                "body-lg": ["Inter"],
                "quote": ["Playfair Display"]
            },
            "fontSize": {
                "button-text": ["14px", {"lineHeight": "1.0", "letterSpacing": "0.05em", "fontWeight": "500"}],
                "label-caps": ["12px", {"lineHeight": "1.0", "letterSpacing": "0.1em", "fontWeight": "600"}],
                "headline-xl": ["48px", {"lineHeight": "1.2", "fontWeight": "400"}],
                "headline-xl-mobile": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}],
                "display-lg-mobile": ["44px", {"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                "body-md": ["16px", {"lineHeight": "1.6", "fontWeight": "400"}],
                "display-lg": ["72px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "400"}],
                "headline-md": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}],
                "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
                "quote": ["24px", {"lineHeight": "1.5", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; }
        body { background-color: #131312; color: #e5e2e0; }
        .glass { background: rgba(15, 15, 14, 0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
        .interactive { transition: all 500ms cubic-bezier(0.23, 1, 0.32, 1); }
        @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
        .animate-scroll { display: flex; width: max-content; animation: scroll 60s linear infinite; }
        .reveal { transition: all 1200ms cubic-bezier(0.23, 1, 0.32, 1); }
        
        @keyframes hero-entrance {
            0% { transform: scale(1.05); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        .animate-hero-entrance {
            animation: hero-entrance 2400ms cubic-bezier(0.23, 1, 0.32, 1) forwards;
        }
        .hero-overlay {
            background: linear-gradient(to left, rgba(19, 19, 18, 0.2) 20%, rgba(19, 19, 18, 0.7) 45%, #131312 75%);
        }
        @media (max-width: 1024px) {
            .hero-overlay {
                background: linear-gradient(to top, #131312 40%, rgba(19, 19, 18, 0.3) 100%);
            }
        }
        .highlight-ring {
            padding: 2px;
            background: linear-gradient(45deg, #ffb68d 0%, #e4c285 100%);
            border-radius: 50%;
        }
        /* Ensure CJK fonts don't break line heights */
        [lang="zh-CN"] {
            line-height: 1.4;
        }
    </style>
</head>
<body class="font-body-md text-on-surface selection:bg-primary/30 overflow-x-hidden">
<header class="fixed top-0 w-full z-50 bg-glass-fill backdrop-blur-md border-b border-glass-stroke interactive">
<div class="flex justify-between items-center h-20 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="font-headline-md text-headline-md font-bold text-on-surface tracking-tighter" data-i18n="nav-name"></div>
<nav class="hidden lg:flex gap-gutter items-center">
<a class="font-button-text text-button-text text-primary border-b border-primary pb-1 interactive" data-i18n="nav-home" href="#"></a>
<a class="font-button-text text-button-text text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="nav-trajectory" href="#"></a>
<a class="font-button-text text-button-text text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="nav-projects" href="#"></a>
<a class="font-button-text text-button-text text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="nav-university" href="#"></a>
<a class="font-button-text text-button-text text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="nav-contact" href="#"></a>
</nav>
<div class="flex items-center gap-6">
<!-- Language Switcher -->
<div class="flex items-center gap-2 font-button-text text-[12px] tracking-[0.1em] text-on-surface-variant">
<button class="hover:text-primary interactive opacity-50 px-1" id="btn-pt-BR" onclick="switchLang('pt-BR')">PT</button>
<span class="opacity-30">|</span>
<button class="hover:text-primary interactive opacity-50 px-1" id="btn-es-419" onclick="switchLang('es-419')">ES</button>
<span class="opacity-30">|</span>
<button class="hover:text-primary interactive opacity-50 px-1" id="btn-en" onclick="switchLang('en')">EN</button>
<span class="opacity-30">|</span>
<button class="hover:text-primary interactive opacity-50 px-1" id="btn-zh-CN" onclick="switchLang('zh-CN')">ZH</button>
</div>
<button class="bg-primary text-on-primary px-6 py-2.5 font-button-text text-button-text hover:brightness-110 active:scale-95 interactive uppercase tracking-wider" data-i18n="btn-connect"></button>
</div>
</div>
</header>
<main class="pt-20">
<!-- Hero Section -->
<section class="relative min-h-[95vh] flex flex-col items-start justify-center overflow-hidden bg-background">
<div class="absolute right-0 top-0 w-full h-full z-10 overflow-hidden">
<div class="relative w-full h-full animate-hero-entrance">
<img alt="Carlos Bernardo" class="w-full h-full object-cover object-[center_center] lg:object-[right_center] contrast-[1.05] brightness-90" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBdAC7KfsbUq0odKx9C7VjjOfFJsDnw37tOyag4PDUyXUMATIvmX51gqNns7XWS3Xi69MrINlWbEp4Ss3Sp0FDgg28TG74mBIikKSBDOVwETr9qxp6njHzaBq-K6DULScEBgNYYFp2We3DAJZgJEc0qsigNGqnTEAL-ziTRP1oFxO5zOYJKiwsP4jbbIhAKy4MfT1YwGEUMZTgFWf_2kiz57B65SOMroiBEe6T13BYAB-7FuTmmXiLEHItJ8vtcn2GM2Dt8p_Qi5eOk">
<div class="absolute inset-0 hero-overlay"></div>
<div class="absolute inset-0 bg-primary/5 mix-blend-overlay"></div>
</div>
</div>
<div class="w-full lg:w-1/2 z-20 px-margin-mobile md:px-margin-desktop py-20 lg:py-0 text-left flex flex-col items-start">
<div class="max-w-2xl reveal opacity-0 translate-y-12" style="transition-delay: 600ms">
<div class="w-20 h-[1px] bg-primary mb-10"></div>
<div class="relative">
<h1 class="font-display-lg text-display-lg-mobile md:text-display-lg mb-8 leading-tight drop-shadow-2xl" data-i18n="hero-title"></h1>
</div>
<p class="font-body-lg text-body-lg text-on-surface-variant mb-16 max-w-lg" data-i18n="hero-subtitle"></p>
<!-- Highlights Ticker -->
<div class="w-full mb-16 overflow-hidden max-w-xl">
<div class="relative flex overflow-hidden group">
<div class="animate-scroll flex gap-10 items-center">
<div class="flex flex-col items-center gap-3 shrink-0 group/highlight">
<div class="highlight-ring p-[2px] w-16 h-16 interactive group-hover/highlight:scale-105">
<div class="w-full h-full rounded-full border-2 border-background overflow-hidden bg-surface-container">
<img alt="Technology" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDWkg4vTWDuT9lDZgBnzwzyicy6_5oTv_oknch313oERexLByEZjh8YMjSA_voSpB3fF8xchSX6YH_YXLFnrtEbaqfJVDs6OnR3nvylK8opLuxM2vGfM6jOqTdPIlGQiK0O2PNAkkS8bAok0LUGOr0MNinDIy5GSll9xl-fhC5FmjUer7toUzDl-LIC1smMs6a7hYOsd3vrxJ_WiQ212Nzqe2UdYFH7Sr2kPacgKuUS9Fka0kaF9f5yDuQZyEEeMWQPH4x4ARn1_4ED">
</div>
</div>
<span class="font-label-caps text-[9px] text-on-surface-variant uppercase tracking-[0.15em]" data-i18n="label-tech"></span>
</div>
<div class="flex flex-col items-center gap-3 shrink-0 group/highlight">
<div class="highlight-ring p-[2px] w-16 h-16 interactive group-hover/highlight:scale-105">
<div class="w-full h-full rounded-full border-2 border-background overflow-hidden bg-surface-container">
<img alt="Agribusiness" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDqeCTItR7V75vdQcqGt-RO52deEjdq2sIGgSO_DpWi0DJPruW2n58RVyig3reOS3dX17UCh8Y5KrxqTu5VcBZ29JDXm751S2VKgglNrq6UFFvTPSQumZ3Ru5LkMap7cYaHVFDdpCQjvHnqoa3b27WxtxhX-k8Oaa604-P1dLUNP725V_PFCH2dArbfWVLvnpLoph3L-NI9vI_9kgS2a-WZZNs8z0uSepXXmj7dr03Jkd675TFOqoOxTOvX-IW0t_hucPqtAHvvcDTN">
</div>
</div>
<span class="font-label-caps text-[9px] text-on-surface-variant uppercase tracking-[0.15em]" data-i18n="label-agro"></span>
</div>
<div class="flex flex-col items-center gap-3 shrink-0 group/highlight">
<div class="highlight-ring p-[2px] w-16 h-16 interactive group-hover/highlight:scale-105">
<div class="w-full h-full rounded-full border-2 border-background overflow-hidden bg-surface-container">
<img alt="Education" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuApvbcn0hdChjoiyT3AkT_GQ6Whpy14pLcSV3p03X9q2RfzV_mpHuYWxRLhyV37R03UNSLEOSexVTOR-V-ZYCcvTtFtL0dHG5J7HGeh3KlexUgEljGcORypdojWgFREkRrS8voN4YDk1aRsnHxADc6rClfXrhw58zsR75-eqVtRfTV7EpXCZB7KikXUGkw3K3j8IyLxyBTBh4vVmU5TWIRtq1Nt_3VMMMa1btQzV6KHph5J5u8nsWXCjiaywEPPJaDRHP5VhalKWCH3">
</div>
</div>
<span class="font-label-caps text-[9px] text-on-surface-variant uppercase tracking-[0.15em]" data-i18n="label-edu"></span>
</div>
<div class="flex flex-col items-center gap-3 shrink-0 group/highlight">
<div class="highlight-ring p-[2px] w-16 h-16 interactive group-hover/highlight:scale-105">
<div class="w-full h-full rounded-full border-2 border-background overflow-hidden bg-surface-container">
<img alt="Health" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA5yJQ8EcEftI1mcsrGnCyU5fZxXs2gLTg04TrQphI1pQrsJMEpbBQLQpiCS7GJAuTdcNAGjS7xrnb0ZdERSyo6aNZPmLCu_8_jXcNN8neWmntJZd4kOt4k_YwWrHLrKgQNkdcgKatZWVukNWB7zMbTO6QZtzQifzrk2v4kdOs_WSW_NL-8wRfaJmtDN0L17IOq_PmaAMEmsO7l4S7Ms0nARcnZKS9-_H0zYv1AnCRbCRfMRBjJdlOWyAkZbwwgjsUnJT6NVkANklj3">
</div>
</div>
<span class="font-label-caps text-[9px] text-on-surface-variant uppercase tracking-[0.15em]" data-i18n="label-health"></span>
</div>
<div class="flex flex-col items-center gap-3 shrink-0 group/highlight">
<div class="highlight-ring p-[2px] w-16 h-16 interactive group-hover/highlight:scale-105">
<div class="w-full h-full rounded-full border-2 border-background overflow-hidden bg-surface-container">
<img alt="Infrastructure" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDthZzJdjUaCjJxYnAlaWFa05lCE06RTKAwgqF7P43LFCRLU0gX1mDJHlCxgczQz9fK0oQOe8V-FJFNPkuSnNc7rqNoq59pnL2smcKg-GJWwUB6RyoO-szfV56wb0nUit99sHoDNfHnWx9ow-2kwIaKxSXvlUnX6E4KShbBYzzNQN5SVcRtVshzzNxQE61Qwmz58WClTplOzI44cO-7hNr2a2rWVLnYn41Xd6VcaIutYnDYD5olJU3kxtrYxSt9IYQBDtS1j_sJ6oob">
</div>
</div>
<span class="font-label-caps text-[9px] text-on-surface-variant uppercase tracking-[0.15em]" data-i18n="label-infra"></span>
</div>
</div>
</div>
</div>
</div>
<!-- Hero Stats -->
<div class="flex flex-wrap gap-8">
<div class="flex flex-col">
<span class="font-display-lg text-headline-md md:text-headline-xl text-primary mb-1">484</span>
<span class="font-label-caps text-[10px] text-on-surface-variant max-w-[120px] leading-tight" data-i18n="stat-families"></span>
</div>
<div class="flex flex-col">
<span class="font-display-lg text-headline-md md:text-headline-xl text-primary mb-1">+5k</span>
<span class="font-label-caps text-[10px] text-on-surface-variant max-w-[120px] leading-tight" data-i18n="stat-students"></span>
</div>
<div class="flex flex-col">
<span class="font-display-lg text-headline-md md:text-headline-xl text-primary mb-1">40k</span>
<span class="font-label-caps text-[10px] text-on-surface-variant max-w-[120px] leading-tight" data-i18n="stat-health"></span>
</div>
</div>
</div>
</section>
<!-- Trajectory Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter">
<div class="md:col-span-4 reveal opacity-0 translate-y-12">
<div class="sticky top-32">
<span class="font-label-caps text-label-caps text-primary block mb-6 tracking-[0.2em]" data-i18n="traj-label"></span>
<h2 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl mb-10" data-i18n="traj-title"></h2>
<div class="w-16 h-[1px] bg-primary mb-10"></div>
<p class="font-body-lg text-body-lg text-on-surface-variant leading-relaxed" data-i18n="traj-p"></p>
</div>
</div>
<div class="md:col-span-7 md:col-start-6 space-y-32">
<div class="relative pl-12 border-l border-glass-stroke reveal opacity-0 translate-y-12" style="transition-delay: 100ms">
<div class="absolute -left-[4px] top-2 w-2 h-2 bg-primary rotate-45"></div>
<span class="font-label-caps text-label-caps text-on-surface-variant mb-4 block opacity-50" data-i18n="traj-1-label"></span>
<h3 class="font-headline-md text-headline-md mb-6 italic text-on-surface" data-i18n="traj-1-title"></h3>
<p class="text-on-surface-variant body-lg leading-relaxed" data-i18n="traj-1-p"></p>
</div>
<div class="relative pl-12 border-l border-glass-stroke reveal opacity-0 translate-y-12" style="transition-delay: 200ms">
<div class="absolute -left-[4px] top-2 w-2 h-2 bg-primary rotate-45"></div>
<span class="font-label-caps text-label-caps text-on-surface-variant mb-4 block opacity-50" data-i18n="traj-2-label"></span>
<h3 class="font-headline-md text-headline-md mb-6 italic text-on-surface" data-i18n="traj-2-title"></h3>
<p class="text-on-surface-variant body-lg leading-relaxed" data-i18n="traj-2-p"></p>
</div>
<div class="relative pl-12 border-l border-glass-stroke reveal opacity-0 translate-y-12" style="transition-delay: 300ms">
<div class="absolute -left-[4px] top-2 w-2 h-2 bg-primary rotate-45"></div>
<span class="font-label-caps text-label-caps text-on-surface-variant mb-4 block opacity-50" data-i18n="traj-3-label"></span>
<h3 class="font-headline-md text-headline-md mb-6 italic text-on-surface" data-i18n="traj-3-title"></h3>
<p class="text-on-surface-variant body-lg leading-relaxed" data-i18n="traj-3-p"></p>
</div>
</div>
</div>
</section>
<!-- Impact Metrics Section -->
<section class="bg-surface-container-lowest py-section-gap relative overflow-hidden">
<div class="absolute top-0 right-0 w-1/3 h-full bg-primary/5 blur-[120px] rounded-full pointer-events-none"></div>
<div class="px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto relative z-10">
<div class="mb-20 reveal opacity-0 translate-y-12">
<span class="font-label-caps text-label-caps text-primary block mb-4 tracking-widest" data-i18n="metrics-label"></span>
<h2 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-on-surface" data-i18n="metrics-title"></h2>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
<div class="group glass p-10 reveal opacity-0 translate-y-12 interactive hover:bg-surface-container-high" style="transition-delay: 100ms">
<div class="font-display-lg text-headline-xl text-primary mb-4">484</div>
<div class="font-label-caps text-label-caps text-on-surface mb-6 tracking-widest" data-i18n="metric-1-label"></div>
<p class="text-on-surface-variant text-sm leading-relaxed" data-i18n="metric-1-p"></p>
</div>
<div class="group glass p-10 reveal opacity-0 translate-y-12 interactive hover:bg-surface-container-high" style="transition-delay: 200ms">
<div class="font-display-lg text-headline-xl text-primary mb-4">+5.000</div>
<div class="font-label-caps text-label-caps text-on-surface mb-6 tracking-widest" data-i18n="metric-2-label"></div>
<p class="text-on-surface-variant text-sm leading-relaxed" data-i18n="metric-2-p"></p>
</div>
<div class="group glass p-10 reveal opacity-0 translate-y-12 interactive hover:bg-surface-container-high" style="transition-delay: 300ms">
<div class="font-display-lg text-headline-xl text-primary mb-4">40k</div>
<div class="font-label-caps text-label-caps text-on-surface mb-6 tracking-widest" data-i18n="metric-3-label"></div>
<p class="text-on-surface-variant text-sm leading-relaxed" data-i18n="metric-3-p"></p>
</div>
</div>
</div>
</section>
<!-- Visual Signature Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop overflow-hidden">
<div class="max-w-container-max mx-auto">
<div class="flex flex-col md:flex-row items-center gap-16">
<div class="w-full md:w-1/2 reveal opacity-0 -translate-x-12">
<div class="relative group">
<img class="w-full aspect-[4/5] md:aspect-[16/10] object-cover grayscale brightness-50 transition-all duration-700 group-hover:grayscale-0 group-hover:brightness-100" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD-58scgnQUaWnBIaykiq1CMqwXTKLw1rTRUh8vKBbjhFlk92kJdjC_djOSAn3sytHbLXnGm0gmo67681SI0ifYLIxfA_DT6VbSINxGrrHEVlu0a1x4SAsh57OP1I_p8wKJ4mG9l-c6mwAAKbMOzXYZr8EacZO26LHvWmzjc8gWbWIqZvFjoOnX_jmFn5r6mgA52yljKj7YqHmGfqKCSMGIZZSjder2ks3R-d1NmydSBHSBIlSz37ORClZDux_DNC3e0fTVbR5N94gR">
<div class="absolute inset-0 border border-primary/20 m-4 pointer-events-none"></div>
</div>
</div>
<div class="w-full md:w-1/2 reveal opacity-0 translate-x-12">
<span class="material-symbols-outlined text-primary text-5xl mb-8 opacity-40">format_quote</span>
<h2 class="font-quote text-headline-md italic mb-12 text-on-surface leading-snug" data-i18n="quote"></h2>
<div class="flex items-center gap-6">
<span class="font-label-caps text-label-caps tracking-widest text-primary" data-i18n="sig-name"></span>
<div class="h-[1px] flex-grow bg-glass-stroke"></div>
</div>
</div>
</div>
</div>
</section>
</main>
<footer class="bg-surface-container-lowest border-t border-glass-stroke w-full py-20 mt-20">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto items-start">
<div class="flex flex-col gap-10">
<div>
<div class="font-headline-md text-headline-md text-on-surface mb-2" data-i18n="nav-name"></div>
<p class="font-body-md text-body-md text-on-surface-variant max-w-xs opacity-60" data-i18n="footer-tagline"></p>
</div>
<div class="flex flex-col gap-4">
<span class="font-label-caps text-label-caps text-primary tracking-[0.2em]" data-i18n="footer-follow"></span>
<div class="flex gap-8">
<a class="text-on-surface hover:text-primary transition-colors duration-300 interactive" href="#"><span class="material-symbols-outlined">public</span></a>
<a class="text-on-surface hover:text-primary transition-colors duration-300 interactive" href="#"><span class="material-symbols-outlined">mail</span></a>
<a class="text-on-surface hover:text-primary transition-colors duration-300 interactive" href="#"><span class="material-symbols-outlined">share</span></a>
</div>
</div>
</div>
<div class="grid grid-cols-2 gap-x-20 gap-y-6 md:justify-self-end">
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="link-privacy" href="#"></a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="link-terms" href="#"></a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="link-institutional" href="#"></a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="link-press" href="#"></a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" href="#">LinkedIn</a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors duration-300 interactive" data-i18n="link-edu-exec" href="#"></a>
</div>
</div>
</footer>
<script id="i18n-data" type="application/json">
{
    "pt-BR": {
        "nav-name": "Carlos Bernardo",
        "nav-home": "Home",
        "nav-trajectory": "Trajetória",
        "nav-projects": "Projetos",
        "nav-university": "Universidad",
        "nav-contact": "Contato",
        "btn-connect": "Conectar",
        "hero-title": "Nasceu no Carajá.<br/>Construiu um estado.",
        "hero-subtitle": "Empreendedor, educador e criador de oportunidades reais no Mato Grosso do Sul.",
        "label-tech": "Tecnologia",
        "label-agro": "Agronegócio",
        "label-edu": "Educação",
        "label-health": "Saúde",
        "label-infra": "Infraestrutura",
        "stat-families": "FAMÍLIAS COM EMPREGO DIRETO",
        "stat-students": "ALUNOS NA UNIVERSIDAD",
        "stat-health": "ATENDIMENTOS ANUAIS",
        "traj-label": "TRAJETÓRIA",
        "traj-title": "A convicção de quem conhece a escassez.",
        "traj-p": "Carlos Bernardo não herdou caminho pronto. Cada empresa que fundou, cada família que empregou, cada aluno que formou — veio do mesmo lugar: da convicção de quem conheceu a escassez e decidiu que outros não precisam vivê-la.",
        "traj-1-label": "AS ORIGENS",
        "traj-1-title": "Ubiratã e o Trabalho Braçal",
        "traj-1-p": "O início forjado na disciplina do trabalho físico. A base de caráter que sustentaria grandes empreendimentos futuros nasceu no Carajá, entre desafios que moldaram a visão de mundo de um realizador.",
        "traj-2-label": "EMPREENDEDORISMO",
        "traj-2-title": "Primeiros Negócios e Monarca Group",
        "traj-2-p": "A transição do esforço para a estratégia. A fundação do Monarca Group marcou a consolidação de uma visão empresarial focada em solidez e impacto regional.",
        "traj-3-label": "EDUCAÇÃO",
        "traj-3-title": "Universidad Interamericana",
        "traj-3-p": "A crença de que o conhecimento é a única ferramenta capaz de romper ciclos de pobreza. Milhares de jovens encontraram o caminho para a dignidade profissional.",
        "metrics-label": "MÉTRICAS DE IMPACTO",
        "metrics-title": "A prova real do compromisso.",
        "metric-1-label": "FAMÍLIAS SUSTENTADAS",
        "metric-1-p": "Empregos diretos gerados através das operações do Monarca Group e instituições coligadas.",
        "metric-2-label": "ALUNOS ATIVOS",
        "metric-2-p": "Estudantes em formação na Universidad Interamericana, preparando a próxima geração.",
        "metric-3-label": "ATENDIMENTOS SAÚDE",
        "metric-3-p": "Procedimentos de saúde realizados anualmente sem custo para a população.",
        "quote": "\"O progresso não é um acidente geográfico. É uma decisão tomada por quem não tem medo de erguer as mangas.\"",
        "sig-name": "CARLOS BERNARDO",
        "footer-tagline": "© 2024 Carlos Bernardo. Excelência em Liderança.",
        "footer-follow": "SIGA A TRAJETÓRIA",
        "link-privacy": "Política de Privacidade",
        "link-terms": "Termos de Serviço",
        "link-institutional": "Institucional",
        "link-press": "Press Kit",
        "link-edu-exec": "Educação Executiva"
    },
    "es-419": {
        "nav-home": "Inicio",
        "nav-trajectory": "Trayectoria",
        "nav-projects": "Proyectos",
        "nav-university": "Universidad",
        "nav-contact": "Contacto",
        "btn-connect": "Conectar",
        "hero-title": "Nació en Carajá.<br/>Construyó un estado.",
        "hero-subtitle": "Emprendedor, educador y creador de oportunidades reales en Mato Grosso del Sur.",
        "label-tech": "Tecnología",
        "label-agro": "Agronegocios",
        "label-edu": "Educación",
        "label-health": "Salud",
        "label-infra": "Infraestructura",
        "stat-families": "FAMILIAS CON EMPLEO DIRECTO",
        "stat-students": "ALUMNOS EN LA UNIVERSIDAD",
        "stat-health": "ATENCIONES ANUALES",
        "traj-label": "TRAYECTORIA",
        "traj-title": "La convicción de quien conoce la escasez.",
        "traj-p": "Carlos Bernardo no heredó un camino hecho. Cada empresa que fundó, cada familia que empleó, cada alumno que formó — vino del mismo lugar: de la convicción de quien conoció la escasez y decidió que otros no necesitan vivirla.",
        "traj-1-label": "LOS ORÍGENES",
        "traj-1-title": "Ubiratã y el Trabajo Manual",
        "traj-1-p": "El inicio forjado en la disciplina del trabajo físico. La base del carácter que sostendría grandes emprendimientos futuros nació en Carajá, entre desafíos que moldearon la visión del mundo de un realizador.",
        "traj-2-label": "EMPRENDIMIENTO",
        "traj-2-title": "Primeros Negocios y Grupo Monarca",
        "traj-2-p": "La transición del esfuerzo a la estrategia. La fundación del Grupo Monarca marcó la consolidación de una visión empresarial enfocada en la solidez y el impacto regional.",
        "traj-3-label": "EDUCACIÓN",
        "traj-3-title": "Universidad Interamericana",
        "traj-3-p": "La creencia de que el conocimiento es la única herramienta capaz de romper ciclos de pobreza. Miles de jóvenes encontraron el camino hacia la dignidad profesional.",
        "metrics-label": "MÉTRICAS DE IMPACTO",
        "metrics-title": "La prueba real del compromiso.",
        "metric-1-label": "FAMILIAS SUSTENTADAS",
        "metric-1-p": "Empleos directos generados a través de las operaciones del Grupo Monarca e instituciones afiliadas.",
        "metric-2-label": "ALUMNOS ACTIVOS",
        "metric-2-p": "Estudiantes en formación en la Universidad Interamericana, preparando a la próxima generación.",
        "metric-3-label": "ATENCIONES DE SALUD",
        "metric-3-p": "Procedimientos de salud realizados anualmente sin costo para la población.",
        "quote": "\"El progreso no es un accidente geográfico. Es una decisión tomada por quien no tiene miedo de remangarse las mangas.\"",
        "sig-name": "CARLOS BERNARDO",
        "footer-tagline": "© 2024 Carlos Bernardo. Excelencia en Liderazgo.",
        "footer-follow": "SIGA LA TRAYECTORIA",
        "link-privacy": "Política de Privacidad",
        "link-terms": "Términos de Servicio",
        "link-institutional": "Institucional",
        "link-press": "Press Kit",
        "link-edu-exec": "Educación Ejecutiva"
    },
    "en": {
        "nav-name": "Carlos Bernardo",
        "nav-home": "Home",
        "nav-trajectory": "Trajectory",
        "nav-projects": "Projects",
        "nav-university": "University",
        "nav-contact": "Contact",
        "btn-connect": "Connect",
        "hero-title": "Born in Carajá.<br/>Built a state.",
        "hero-subtitle": "Entrepreneur, educator and creator of real opportunities in Mato Grosso do Sul.",
        "label-tech": "Technology",
        "label-agro": "Agribusiness",
        "label-edu": "Education",
        "label-health": "Health",
        "label-infra": "Infrastructure",
        "stat-families": "FAMILIES WITH DIRECT EMPLOYMENT",
        "stat-students": "STUDENTS AT THE UNIVERSITY",
        "stat-health": "ANNUAL CONSULTATIONS",
        "traj-label": "TRAJECTORY",
        "traj-title": "The conviction of one who knows scarcity.",
        "traj-p": "Carlos Bernardo did not inherit a ready-made path. Every company he founded, every family he employed, every student he trained — came from the same place: the conviction of one who knew scarcity and decided that others do not need to live it.",
        "traj-1-label": "ORIGINS",
        "traj-1-title": "Ubiratã and Physical Labor",
        "traj-1-p": "A beginning forged in the discipline of physical work. The foundation of character that would sustain great future enterprises was born in Carajá, amid challenges that shaped a doer's worldview.",
        "traj-2-label": "ENTREPRENEURSHIP",
        "traj-2-title": "First Businesses and Monarca Group",
        "traj-2-p": "The transition from effort to strategy. The foundation of Monarca Group marked the consolidation of a business vision focused on solidity and regional impact.",
        "traj-3-label": "EDUCATION",
        "traj-3-title": "Universidad Interamericana",
        "traj-3-p": "The belief that knowledge is the only tool capable of breaking cycles of poverty. Thousands of young people found the path to professional dignity.",
        "metrics-label": "IMPACT METRICS",
        "metrics-title": "Real proof of commitment.",
        "metric-1-label": "SUSTAINED FAMILIES",
        "metric-1-p": "Direct jobs generated through the operations of Monarca Group and affiliated institutions.",
        "metric-2-label": "ACTIVE STUDENTS",
        "metric-2-p": "Students in training at Universidad Interamericana, preparing the next generation.",
        "metric-3-label": "HEALTHCARE VISITS",
        "metric-3-p": "Health procedures performed annually at no cost to the population.",
        "quote": "\"Progress is not a geographical accident. It is a decision made by those who are not afraid to roll up their sleeves.\"",
        "sig-name": "CARLOS BERNARDO",
        "footer-tagline": "© 2024 Carlos Bernardo. Leadership Excellence.",
        "footer-follow": "FOLLOW THE TRAJECTORY",
        "link-privacy": "Privacy Policy",
        "link-terms": "Terms of Service",
        "link-institutional": "Institutional",
        "link-press": "Press Kit",
        "link-edu-exec": "Executive Education"
    },
    "zh-CN": {
        "nav-name": "卡洛斯·贝尔纳多",
        "nav-home": "首页",
        "nav-trajectory": "个人历程",
        "nav-projects": "项目",
        "nav-university": "大学",
        "nav-contact": "联系我们",
        "btn-connect": "联系",
        "hero-title": "生于卡拉雅。<br/>建设了一个州。",
        "hero-subtitle": "南马托格罗索州的企业家、教育家和真实机会的创造者。",
        "label-tech": "科技",
        "label-agro": "农业综合企业",
        "label-edu": "教育",
        "label-health": "医疗健康",
        "label-infra": "基础设施",
        "stat-families": "直接就业家庭",
        "stat-students": "在校大学生",
        "stat-health": "年度诊疗次数",
        "traj-label": "个人历程",
        "traj-title": "来自对匮乏深刻理解的信念。",
        "traj-p": "卡洛斯·贝尔纳多并没有继承现成的道路。他创建的每一家公司、雇佣的每一个家庭、培养的每一个学生——都源于同一个地方：一个经历过匮乏并决定让其他人不再经历匮乏的人的信念。",
        "traj-1-label": "起源",
        "traj-1-title": "乌比拉唐与体力劳动",
        "traj-1-p": "在体力劳动的磨练中铸就的开端。支撑未来伟大事业的性格基础诞生于卡拉雅，诞生在塑造了一位实干家世界观的挑战之中。",
        "traj-2-label": "创业历程",
        "traj-2-title": "初创业务与 Monarca 集团",
        "traj-2-p": "从努力到策略的转变。Monarca 集团的成立标志着专注于稳固性和地区影响力的商业愿景的巩固。",
        "traj-3-label": "教育事业",
        "traj-3-title": "美洲际大学",
        "traj-3-p": "坚信知识是唯一能够打破贫困循环的工具。成千上万的年轻人在这里找到了通往职业尊严的道路。",
        "metrics-label": "影响指标",
        "metrics-title": "承诺的真实证明。",
        "metric-1-label": "获助家庭",
        "metric-1-p": "通过 Monarca 集团及附属机构的运营创造的直接就业岗位。",
        "metric-2-label": "在校学生",
        "metric-2-p": "在美洲际大学接受培训的学生，正在为下一代做准备。",
        "metric-3-label": "医疗服务",
        "metric-3-p": "每年为民众免费进行的医疗程序。",
        "quote": "“进步不是地理上的偶然。它是那些不畏惧卷起袖子干活的人做出的决定。”",
        "sig-name": "卡洛斯·贝尔纳多",
        "footer-tagline": "© 2024 卡洛斯·贝尔纳多。卓越领导力。",
        "footer-follow": "关注发展历程",
        "link-privacy": "隐私政策",
        "link-terms": "服务条款",
        "link-institutional": "机构信息",
        "link-press": "新闻资料包",
        "link-edu-exec": "高管教育"
    }
}
</script>
<script>
    const i18nData = JSON.parse(document.getElementById('i18n-data').textContent);
    const defaultLang = 'pt-BR';
    let currentLang = defaultLang;

    function switchLang(lang) {
        currentLang = lang;
        const strings = i18nData[lang] || i18nData[defaultLang];
        const fallbacks = i18nData[defaultLang];
        
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            // Reactive update with fallback logic
            const content = strings[key] || fallbacks[key] || "";
            if (el.innerHTML !== content) {
                el.innerHTML = content;
            }
        });

        // Update switcher UI
        const langs = ['pt-BR', 'es-419', 'en', 'zh-CN'];
        langs.forEach(l => {
            const btn = document.getElementById(`btn-${l}`);
            if (btn) {
                if (l === lang) {
                    btn.classList.replace('opacity-50', 'opacity-100');
                    btn.classList.add('font-bold');
                } else {
                    btn.classList.replace('opacity-100', 'opacity-50');
                    btn.classList.remove('font-bold');
                }
            }
        });
        
        document.documentElement.setAttribute('lang', lang);
    }

    // Initialize with default
    window.addEventListener('DOMContentLoaded', () => {
        switchLang(defaultLang);
        
        // Animation Observers
        const observerOptions = { threshold: 0.15, rootMargin: '0px 0px -50px 0px' };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('opacity-100', 'translate-y-0', 'translate-x-0');
                    entry.target.classList.remove('opacity-0', 'translate-y-12', '-translate-x-12', 'translate-x-12');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    });

    // Simple Parallax
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const heroImg = document.querySelector('section .animate-hero-entrance img');
        if(heroImg && window.innerWidth > 1024) {
            heroImg.style.transform = `translateY(${scrolled * 0.15}px)`;
        }
    });
</script>
</body></html>

<!-- Carlos Bernardo - Projetos i18n Multi-Language -->
<!DOCTYPE html><html class="dark" lang="pt-BR"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Carlos Bernardo | Projetos &amp; Portfólio</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Playfair+Display:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "on-background": "#e5e2e0",
                    "primary-fixed-dim": "#ffb68d",
                    "on-primary-container": "#481d01",
                    "surface-container-low": "#1c1c1a",
                    "on-surface": "#e5e2e0",
                    "glass-stroke": "rgba(255, 255, 255, 0.08)",
                    "secondary-fixed-dim": "#e4c285",
                    "on-primary": "#512405",
                    "on-secondary-container": "#d5b478",
                    "primary": "#ffb68d",
                    "tertiary-fixed": "#d7e8c5",
                    "on-secondary-fixed": "#261900",
                    "primary-container": "#c3815b",
                    "surface-bright": "#3a3938",
                    "on-error-container": "#ffdad6",
                    "primary-fixed": "#ffdbc9",
                    "on-secondary-fixed-variant": "#5a4312",
                    "outline-variant": "#52443c",
                    "tertiary-fixed-dim": "#bbccaa",
                    "secondary": "#e4c285",
                    "surface-dim": "#131312",
                    "tertiary": "#bbccaa",
                    "error": "#ffb4ab",
                    "on-surface-variant": "#d7c2b8",
                    "on-tertiary-container": "#202d16",
                    "on-tertiary": "#27341d",
                    "error-container": "#93000a",
                    "inverse-primary": "#89502e",
                    "secondary-container": "#5d4514",
                    "surface-container-lowest": "#0e0e0d",
                    "on-secondary": "#412d00",
                    "glass-fill": "rgba(15, 15, 14, 0.6)",
                    "inverse-on-surface": "#31302f",
                    "tertiary-container": "#869677",
                    "surface-variant": "#353533",
                    "on-tertiary-fixed-variant": "#3d4b31",
                    "surface-tint": "#ffb68d",
                    "surface-container-highest": "#353533",
                    "canvas-light": "#F5F0EB",
                    "surface-container-high": "#2a2a29",
                    "outline": "#9f8d84",
                    "on-tertiary-fixed": "#121f09",
                    "on-primary-fixed-variant": "#6c3919",
                    "surface-container": "#20201e",
                    "inverse-surface": "#e5e2e0",
                    "on-error": "#690005",
                    "background": "#131312",
                    "surface": "#131312",
                    "secondary-fixed": "#ffdea4",
                    "on-primary-fixed": "#331200"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "margin-mobile": "20px",
                    "margin-desktop": "80px",
                    "gutter": "24px",
                    "container-max": "1440px",
                    "unit": "8px"
            },
            "fontFamily": {
                    "button-text": ["Inter"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "label-caps": ["Inter"],
                    "headline-xl": ["Playfair Display"],
                    "headline-md": ["Playfair Display"],
                    "display-lg-mobile": ["Playfair Display"],
                    "display-lg": ["Playfair Display"],
                    "headline-xl-mobile": ["Playfair Display"]
            },
            "fontSize": {
                    "button-text": ["14px", {"lineHeight": "1.0", "letterSpacing": "0.05em", "fontWeight": "500"}],
                    "body-md": ["16px", {"lineHeight": "1.6", "fontWeight": "400"}],
                    "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
                    "label-caps": ["12px", {"lineHeight": "1.0", "letterSpacing": "0.1em", "fontWeight": "600"}],
                    "headline-xl": ["48px", {"lineHeight": "1.2", "fontWeight": "400"}],
                    "headline-md": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}],
                    "display-lg-mobile": ["44px", {"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                    "display-lg": ["72px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "400"}],
                    "headline-xl-mobile": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            background-color: #0F0F0E;
            color: #e5e2e0;
            overflow-x: hidden;
        }
        .ease-out-quint {
            transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1);
        }
        .glass-card {
            background: rgba(15, 15, 14, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .reveal-stagger {
            opacity: 0;
            transform: translateY(20px);
        }
        /* Language handling transitions */
        [data-i18n] {
            transition: opacity 0.3s ease;
        }
        .lang-switching [data-i18n] {
            opacity: 0;
        }
    </style>
</head>
<body class="font-body-md selection:bg-primary-container selection:text-white">
<!-- TopNavBar -->
<header class="fixed top-0 w-full z-50 bg-glass-fill backdrop-blur-md border-b border-glass-stroke">
<div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop h-20 max-w-container-max mx-auto">
<a class="font-headline-md text-headline-md text-primary tracking-tight" href="#">Carlos Bernardo</a>
<nav class="hidden md:flex gap-10 items-center">
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-trajectory" href="#">Trajetória</a>
<a class="font-label-caps text-label-caps text-primary font-bold border-b-2 border-primary pb-1" data-i18n="nav-projects" href="#">Projetos</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-university" href="#">Universidade</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-contact" href="#">Contato</a>
</nav>
<div class="flex items-center gap-4">
<div class="flex items-center gap-2 font-label-caps text-[10px] tracking-widest text-on-surface-variant">
<button class="hover:text-primary transition-colors cursor-pointer px-1 lang-btn" data-lang="pt-BR" onclick="setLanguage('pt-BR')">PT</button>
<span>|</span>
<button class="hover:text-primary transition-colors cursor-pointer px-1 lang-btn" data-lang="es-419" onclick="setLanguage('es-419')">ES</button>
<span>|</span>
<button class="hover:text-primary transition-colors cursor-pointer px-1 lang-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
<span>|</span>
<button class="hover:text-primary transition-colors cursor-pointer px-1 lang-btn" data-lang="zh-CN" onclick="setLanguage('zh-CN')">ZH</button>
</div>
</div>
</div>
</header>
<main class="pt-20">
<!-- Hero Section -->
<section class="relative min-h-[90vh] flex flex-col justify-center px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto py-20">
<div class="grid grid-cols-1 lg:grid-cols-12 gap-gutter items-center">
<div class="lg:col-span-7 z-10">
<span class="font-label-caps text-label-caps text-secondary mb-6 block uppercase tracking-widest" data-i18n="hero-label">Liderança Visionária</span>
<h1 class="font-display-lg text-display-lg-mobile md:text-display-lg mb-8 text-on-background leading-tight">
<span data-i18n="hero-title-1">Transformando Paisagens através da</span> <span class="text-primary italic" data-i18n="hero-title-accent">Estratégia</span> <span data-i18n="hero-title-2">e Inovação.</span>
</h1>
<p class="font-body-lg text-body-lg max-w-xl text-on-surface-variant mb-12 min-h-[5rem]" data-i18n="hero-description">
                    Liderando o Grupo Monarca com compromisso com o agronegócio sustentável e investimentos em tecnologia de ponta que redefinem o impacto econômico regional.
                </p>
<div class="flex flex-wrap gap-6">
<button class="bg-primary text-on-primary font-button-text text-button-text px-10 py-5 hover:bg-primary-fixed-dim transition-all duration-300 active:scale-95 ease-out-quint" data-i18n="btn-view-projects">
                        VER PROJETOS
                    </button>
<button class="glass-card text-primary font-button-text text-button-text px-10 py-5 border border-primary hover:bg-primary/10 transition-all duration-300 active:scale-95 ease-out-quint" data-i18n="btn-philosophy">
                        FILOSOFIA DE INVESTIMENTO
                    </button>
</div>
</div>
<div class="lg:col-span-5 relative mt-12 lg:mt-0">
<div class="aspect-[4/5] overflow-hidden border border-glass-stroke relative group">
<img alt="Agribusiness Sunset" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" src="https://lh3.googleusercontent.com/aida/ADBb0uiZqooTY340asCEOzN0oYlFm7LNTFQSbbUSUE3loK-6F6FSDG-1d3SoBxmaTPiH_xpU5duB6c0D-N4W8wYUrOCdekUPZYUJ_sdjoT1TYdOOc6hzkInIW0_ZIKfKBHKZvJhfrtc4-PWXtAfLRmF3HzNGNXeqhwz8cvlLdzmQAwJPNoNY2NLu1zCziyt3jg441BMJbbD9m-4XPrMEC7qL2UvUw1aInBq3Oif0vgtkmUpe68utzTWF2OmqcHHl">
<div class="absolute inset-0 bg-gradient-to-t from-background/80 to-transparent"></div>
</div>
</div>
</div>
</section>
<!-- Impact Metrics -->
<section class="py-32 bg-surface-container-lowest border-y border-glass-stroke">
<div class="px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="grid grid-cols-1 md:grid-cols-3 gap-16 md:gap-gutter text-center md:text-left">
<div class="reveal-stagger">
<span class="block font-display-lg text-display-lg text-primary mb-2">484</span>
<span class="font-label-caps text-label-caps text-secondary uppercase" data-i18n="stat-families-label">Famílias Impactadas</span>
<p class="mt-4 text-on-surface-variant font-body-md text-body-md" data-i18n="stat-families-desc">Transformação socioeconômica através das iniciativas do Grupo Monarca.</p>
</div>
<div class="reveal-stagger" style="transition-delay: 100ms;">
<span class="block font-display-lg text-display-lg text-primary mb-2">12k+</span>
<span class="font-label-caps text-label-caps text-secondary uppercase" data-i18n="stat-hectares-label">Hectares Gerenciados</span>
<p class="mt-4 text-on-surface-variant font-body-md text-body-md" data-i18n="stat-hectares-desc">Agricultura de precisão e gestão sustentável da terra através das fronteiras.</p>
</div>
<div class="reveal-stagger" style="transition-delay: 200ms;">
<span class="block font-display-lg text-display-lg text-primary mb-2">15</span>
<span class="font-label-caps text-label-caps text-secondary uppercase" data-i18n="stat-ventures-label">Empreendimentos Tech</span>
<p class="mt-4 text-on-surface-variant font-body-md text-body-md" data-i18n="stat-ventures-desc">Investimentos estratégicos em fintech e engenharia agrotech.</p>
</div>
</div>
</div>
</section>
<!-- Project Grid -->
<section class="py-40 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="flex flex-col md:flex-row justify-between items-end mb-24 gap-8">
<div class="max-w-2xl">
<span class="font-label-caps text-label-caps text-primary mb-4 block" data-i18n="portfolio-label">PORTFÓLIO</span>
<h2 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl" data-i18n="portfolio-title">Projetos Estratégicos &amp; Investimentos Globais</h2>
</div>
<div class="flex gap-4">
<button class="w-12 h-12 flex items-center justify-center glass-card hover:border-primary transition-all duration-300">
<span class="material-symbols-outlined text-primary">arrow_back</span>
</button>
<button class="w-12 h-12 flex items-center justify-center glass-card hover:border-primary transition-all duration-300">
<span class="material-symbols-outlined text-primary">arrow_forward</span>
</button>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter">
<!-- Project Card 1 -->
<div class="group cursor-pointer">
<div class="relative overflow-hidden mb-8 border border-glass-stroke group-hover:border-primary transition-all duration-500 aspect-[16/10]">
<img alt="Tech Hardware" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida/ADBb0ug15HhzeDg2W9VTsGVaC2aQLfcajmwuYKVt9_VqoxWJ-Tzjm0wKa1-LcZB2shfSDlWfyNqyv4lgyFK-YbhgGfkWlcZvQDKlCfa2thr6KmVhpsuiRALR7HqHH0M0T3EN2jiJA6XSfk4GrZg_A_wHPpqNtq7LaG7dn69E-SRlYieWQaiGNA_q9nl51eGkUCofFTz6JPQ1Y2vGNGdyYVw4NE-Y2Ia-Et2H2xOWy_PmlsawDwJAk9rMh3ZASYyF">
<div class="absolute top-6 right-6 px-4 py-1 glass-card border border-primary/40">
<span class="font-label-caps text-label-caps text-primary" data-i18n="project-tag-tech">INVESTIMENTO TECH</span>
</div>
</div>
<div class="px-2">
<h3 class="font-headline-md text-headline-md mb-4 group-hover:text-primary transition-colors">Quantum Ventures Lab</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2 min-h-[3rem]" data-i18n="project-1-desc">Explorando as fronteiras da engenharia de semicondutores e infraestrutura fintech de próxima geração.</p>
<div class="mt-6 flex items-center gap-2 text-primary group-hover:gap-4 transition-all">
<span class="font-label-caps text-label-caps" data-i18n="link-explore">EXPLORAR PROJETO</span>
<span class="material-symbols-outlined text-[16px]">arrow_right_alt</span>
</div>
</div>
</div>
<!-- Project Card 2 -->
<div class="group cursor-pointer mt-12 md:mt-24">
<div class="relative overflow-hidden mb-8 border border-glass-stroke group-hover:border-primary transition-all duration-500 aspect-[16/10]">
<div class="absolute inset-0 bg-secondary/10 z-10 group-hover:opacity-0 transition-opacity"></div>
<img alt="Monarca Fields" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida/ADBb0uiZqooTY340asCEOzN0oYlFm7LNTFQSbbUSUE3loK-6F6FSDG-1d3SoBxmaTPiH_xpU5duB6c0D-N4W8wYUrOCdekUPZYUJ_sdjoT1TYdOOc6hzkInIW0_ZIKfKBHKZvJhfrtc4-PWXtAfLRmF3HzNGNXeqhwz8cvlLdzmQAwJPNoNY2NLu1zCziyt3jg441BMJbbD9m-4XPrMEC7qL2UvUw1aInBq3Oif0vgtkmUpe68utzTWF2OmqcHHl">
<div class="absolute top-6 right-6 px-4 py-1 glass-card border border-primary/40">
<span class="font-label-caps text-label-caps text-primary" data-i18n="project-tag-monarca">GRUPO MONARCA</span>
</div>
</div>
<div class="px-2">
<h3 class="font-headline-md text-headline-md mb-4 group-hover:text-primary transition-colors">Monarca Agribusiness Hub</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2 min-h-[3rem]" data-i18n="project-2-desc">Liderando a indústria em agricultura de precisão e comércio sustentável de commodities na América Latina.</p>
<div class="mt-6 flex items-center gap-2 text-primary group-hover:gap-4 transition-all">
<span class="font-label-caps text-label-caps" data-i18n="link-explore">EXPLORAR PROJETO</span>
<span class="material-symbols-outlined text-[16px]">arrow_right_alt</span>
</div>
</div>
</div>
</div>
</section>
<!-- Editorial Quote -->
<section class="py-40 relative">
<div class="absolute inset-0 flex items-center justify-center overflow-hidden pointer-events-none opacity-5">
<span class="font-headline-xl text-[400px] leading-none text-primary whitespace-nowrap" data-i18n="quote-bg">VISIONÁRIO</span>
</div>
<div class="px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto text-center relative z-10">
<blockquote class="font-headline-xl text-headline-xl-mobile md:text-headline-xl italic max-w-4xl mx-auto mb-12 min-h-[12rem] flex items-center justify-center">
<span data-i18n="quote-text">"O sucesso empresarial não é medido pelo lucro, mas pelo legado de inovação e pelas vidas transformadas em cada projeto."</span>
</blockquote>
<cite class="font-label-caps text-label-caps text-secondary not-italic tracking-widest">— CARLOS BERNARDO</cite>
</div>
</section>
</main>
<!-- Footer -->
<footer class="w-full py-20 bg-surface-container-lowest border-t border-glass-stroke">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="flex flex-col justify-between">
<div>
<h2 class="font-headline-xl text-headline-xl text-primary opacity-20 mb-8">Carlos Bernardo</h2>
<p class="font-body-md text-body-md text-on-surface-variant max-w-sm" data-i18n="footer-desc">
                    Liderança Empresarial de Alto Nível e Educação. Definindo o futuro da indústria regional e do comércio global.
                </p>
</div>
<div class="mt-12">
<p class="font-body-md text-body-md text-on-surface-variant">© 2024 Carlos Bernardo. <span data-i18n="footer-rights">Todos os direitos reservados.</span></p>
</div>
</div>
<div class="flex flex-col md:items-end justify-between mt-16 md:mt-0">
<div class="grid grid-cols-2 gap-12 md:text-right">
<div class="flex flex-col gap-4">
<span class="font-label-caps text-label-caps text-secondary" data-i18n="footer-sitemap">MAPA DO SITE</span>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="nav-trajectory" href="#">Trajetória</a>
<a class="font-label-caps text-label-caps text-primary" data-i18n="nav-projects" href="#">Projetos</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="nav-university" href="#">Universidade</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="nav-contact" href="#">Contato</a>
</div>
<div class="flex flex-col gap-4">
<span class="font-label-caps text-label-caps text-secondary" data-i18n="footer-legal">LEGAL</span>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="legal-privacy" href="#">Política de Privacidade</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="legal-terms" href="#">Termos de Serviço</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" data-i18n="legal-press" href="#">Kit de Imprensa</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors" href="#">LinkedIn</a>
</div>
</div>
<div class="mt-20 flex gap-6">
<div class="w-10 h-10 glass-card flex items-center justify-center hover:text-primary transition-colors cursor-pointer">
<span class="material-symbols-outlined">share</span>
</div>
<div class="w-10 h-10 glass-card flex items-center justify-center hover:text-primary transition-colors cursor-pointer">
<span class="material-symbols-outlined">language</span>
</div>
<div class="w-10 h-10 glass-card flex items-center justify-center hover:text-primary transition-colors cursor-pointer">
<span class="material-symbols-outlined">mail</span>
</div>
</div>
</div>
</div>
</footer>
<script>
    const translations = {
        'pt-BR': {
            'nav-trajectory': 'Trajetória',
            'nav-projects': 'Projetos',
            'nav-university': 'Universidade',
            'nav-contact': 'Contato',
            'hero-label': 'Liderança Visionária',
            'hero-title-1': 'Transformando Paisagens através da',
            'hero-title-accent': 'Estratégia',
            'hero-title-2': 'e Inovação.',
            'hero-description': 'Liderando o Grupo Monarca com compromisso com o agronegócio sustentável e investimentos em tecnologia de ponta que redefinem o impacto econômico regional.',
            'btn-view-projects': 'VER PROJETOS',
            'btn-philosophy': 'FILOSOFIA DE INVESTIMENTO',
            'stat-families-label': 'Famílias Impactadas',
            'stat-families-desc': 'Transformação socioeconômica através das iniciativas do Grupo Monarca.',
            'stat-hectares-label': 'Hectares Gerenciados',
            'stat-hectares-desc': 'Agricultura de precisão e gestão sustentável da terra através das fronteiras.',
            'stat-ventures-label': 'Empreendimentos Tech',
            'stat-ventures-desc': 'Investimentos estratégicos em fintech e engenharia agrotech.',
            'portfolio-label': 'PORTFÓLIO',
            'portfolio-title': 'Projetos Estratégicos & Investimentos Globais',
            'project-tag-tech': 'INVESTIMENTO TECH',
            'project-tag-monarca': 'GRUPO MONARCA',
            'project-1-desc': 'Explorando as fronteiras da engenharia de semicondutores e infraestrutura fintech de próxima geração.',
            'project-2-desc': 'Liderando a indústria em agricultura de precisão e comércio sustentável de commodities na América Latina.',
            'link-explore': 'EXPLORAR PROJETO',
            'quote-bg': 'VISIONÁRIO',
            'quote-text': '"O sucesso empresarial não é medido pelo lucro, mas pelo legado de inovação e pelas vidas transformadas em cada projeto."',
            'footer-desc': 'Liderança Empresarial de Alto Nível e Educação. Definindo o futuro da indústria regional e do comércio global.',
            'footer-rights': 'Todos os direitos reservados.',
            'footer-sitemap': 'MAPA DO SITE',
            'footer-legal': 'LEGAL',
            'legal-privacy': 'Política de Privacidade',
            'legal-terms': 'Termos de Serviço',
            'legal-press': 'Kit de Imprensa'
        },
        'es-419': {
            'nav-trajectory': 'Trayectoria',
            'nav-projects': 'Proyectos',
            'nav-university': 'Universidad',
            'nav-contact': 'Contacto',
            'hero-label': 'Liderazgo Visionario',
            'hero-title-1': 'Transformando Paisajes a través de la',
            'hero-title-accent': 'Estrategia',
            'hero-title-2': 'y la Innovación.',
            'hero-description': 'Liderando el Grupo Monarca con un compromiso con el agronegocio sostenible e inversiones tecnológicas de vanguardia que redefinen el impacto económico regional.',
            'btn-view-projects': 'VER PROYECTOS',
            'btn-philosophy': 'FILOSOFÍA DE INVERSIÓN',
            'stat-families-label': 'Familias Impactadas',
            'stat-families-desc': 'Transformación socioeconómica a través de las iniciativas del Grupo Monarca.',
            'stat-hectares-label': 'Hectáreas Gestionadas',
            'stat-hectares-desc': 'Agricultura de precisión y gestión sostenible de la tierra a través de las fronteras.',
            'stat-ventures-label': 'Emprendimientos Tech',
            'stat-ventures-desc': 'Inversiones estratégicas en fintech e ingeniería agrotech.',
            'portfolio-label': 'PORTAFOLIO',
            'portfolio-title': 'Proyectos Estratégicos e Inversiones Globales',
            'project-tag-tech': 'INVERSIÓN TECH',
            'project-tag-monarca': 'GRUPO MONARCA',
            'project-1-desc': 'Explorando las fronteras de la ingeniería de semiconductores e infraestructura fintech de próxima generación.',
            'project-2-desc': 'Liderando la industria en agricultura de precisión y comercio sostenible de materias primas en América Latina.',
            'link-explore': 'EXPLORAR PROYECTO',
            'quote-bg': 'VISIONARIO',
            'quote-text': '"El éxito empresarial no se mide por las ganancias, sino por el legado de innovación y las vidas transformadas en cada proyecto."',
            'footer-desc': 'Liderazgo Empresarial de Alto Nivel y Educación. Definiendo el futuro de la industria regional y el comercio global.',
            'footer-rights': 'Todos los derechos reservados.',
            'footer-sitemap': 'MAPA DEL SITIO',
            'footer-legal': 'LEGAL',
            'legal-privacy': 'Política de Privacidad',
            'legal-terms': 'Términos de Servicio',
            'legal-press': 'Kit de Prensa'
        },
        'en': {
            'nav-trajectory': 'Trajectory',
            'nav-projects': 'Projects',
            'nav-university': 'University',
            'nav-contact': 'Contact',
            'hero-label': 'Visionary Leadership',
            'hero-title-1': 'Transforming Landscapes through',
            'hero-title-accent': 'Strategy',
            'hero-title-2': 'and Innovation.',
            'hero-description': 'Leading the Monarca Group with a commitment to sustainable agribusiness and forward-thinking technology investments that redefine regional economic impact.',
            'btn-view-projects': 'VIEW PROJECTS',
            'btn-philosophy': 'INVESTMENT PHILOSOPHY',
            'stat-families-label': 'Families Impacted',
            'stat-families-desc': 'Socio-economic transformation through Monarca Group initiatives.',
            'stat-hectares-label': 'Hectares Managed',
            'stat-hectares-desc': 'Precision agriculture and sustainable land stewardship across borders.',
            'stat-ventures-label': 'Tech Ventures',
            'stat-ventures-desc': 'Strategic investments in fintech and agrotech engineering.',
            'portfolio-label': 'PORTFOLIO',
            'portfolio-title': 'Strategic Projects & Global Ventures',
            'project-tag-tech': 'TECH INVESTMENT',
            'project-tag-monarca': 'MONARCA GROUP',
            'project-1-desc': 'Exploring the frontiers of semiconductor engineering and next-generation fintech infrastructure.',
            'project-2-desc': 'Leading the industry in precision agriculture and sustainable commodity trading across Latin America.',
            'link-explore': 'EXPLORE PROJECT',
            'quote-bg': 'VISIONARY',
            'quote-text': '"Business success is not measured by profit, but by the legacy of innovation and the lives transformed in every project."',
            'footer-desc': 'High-end Business Leadership & Education. Defining the future of regional industry and global commerce.',
            'footer-rights': 'All rights reserved.',
            'footer-sitemap': 'SITEMAP',
            'footer-legal': 'LEGAL',
            'legal-privacy': 'Privacy Policy',
            'legal-terms': 'Terms of Service',
            'legal-press': 'Press Kit'
        },
        'zh-CN': {
            'nav-trajectory': '发展历程',
            'nav-projects': '项目案例',
            'nav-university': '学术合作',
            'nav-contact': '联系我们',
            'hero-label': '远见领导力',
            'hero-title-1': '通过',
            'hero-title-accent': '战略',
            'hero-title-2': '与创新重塑格局。',
            'hero-description': '领导 Monarca 集团，致力于可持续农业综合企业和前瞻性技术投资，重新定义地区经济影响。',
            'btn-view-projects': '查看项目',
            'btn-philosophy': '投资理念',
            'stat-families-label': '影响家庭',
            'stat-families-desc': '通过 Monarca 集团的倡议实现社会经济转型。',
            'stat-hectares-label': '管理公顷',
            'stat-hectares-desc': '跨越国界的精准农业和可持续土地管理。',
            'stat-ventures-label': '科技创投',
            'stat-ventures-desc': '在金融科技和农业科技工程领域的战略投资。',
            'portfolio-label': '项目作品集',
            'portfolio-title': '战略项目与全球投资',
            'project-tag-tech': '科技投资',
            'project-tag-monarca': 'MONARCA 集团',
            'project-1-desc': '探索半导体工程和下一代金融科技基础设施的前沿。',
            'project-2-desc': '在拉丁美洲的精准农业和可持续大宗商品贸易领域处于行业领先地位。',
            'link-explore': '探索项目',
            'quote-bg': '远见者',
            'quote-text': '“商业成功不应以利润来衡量，而应以创新的遗产和每个项目中被改变的生活来衡量。”',
            'footer-desc': '高端商业领导力与教育。定义区域工业和全球商业的未来。',
            'footer-rights': '版权所有。',
            'footer-sitemap': '网站地图',
            'footer-legal': '法律信息',
            'legal-privacy': '隐私政策',
            'legal-terms': '服务条款',
            'legal-press': '新闻资料'
        }
    };

    function setLanguage(lang) {
        document.documentElement.lang = lang;
        document.body.classList.add('lang-switching');

        // Update active state in nav
        document.querySelectorAll('.lang-btn').forEach(btn => {
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('text-primary');
                btn.classList.remove('text-on-surface-variant');
            } else {
                btn.classList.remove('text-primary');
                btn.classList.add('text-on-surface-variant');
            }
        });

        setTimeout(() => {
            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang] && translations[lang][key]) {
                    el.innerText = translations[lang][key];
                }
            });
            document.body.classList.remove('lang-switching');
        }, 300);
    }

    // Initialize with PT-BR
    document.addEventListener('DOMContentLoaded', () => {
        setLanguage('pt-BR');
        
        // Simple Intersection Observer for staggered entrance
        const observerOptions = {
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    entry.target.style.transition = 'all 0.8s cubic-bezier(0.23, 1, 0.32, 1)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.reveal-stagger').forEach(el => observer.observe(el));
    });
</script>
</body></html>

<!-- Carlos Bernardo - Contato i18n Multi-Language -->
<!DOCTYPE html><html class="dark" lang="pt-BR"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Contact &amp; Institutional Relations | Carlos Bernardo</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Playfair+Display:wght@400;700&amp;family=Noto+Sans+SC:wght@400;500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<style>
        body {
            background-color: #131312;
            color: #e5e2e0;
            overflow-x: hidden;
        }
        .ease-out-quint {
            transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1);
        }
        .glass-panel {
            background: rgba(15, 15, 14, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .stagger-item {
            opacity: 0;
            transform: translateY(20px);
        }
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #ffb68d !important;
            box-shadow: none !important;
        }
        /* Chinese Language Specific Adjustments */
        [lang="zh-CN"] .font-body-md, 
        [lang="zh-CN"] .font-body-lg,
        [lang="zh-CN"] .font-label-caps {
            font-family: 'Noto Sans SC', 'Inter', sans-serif;
            letter-spacing: 0.02em;
        }
    </style>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "on-background": "#e5e2e0",
                    "primary-fixed-dim": "#ffb68d",
                    "on-primary-container": "#481d01",
                    "surface-container-low": "#1c1c1a",
                    "on-surface": "#e5e2e0",
                    "glass-stroke": "rgba(255, 255, 255, 0.08)",
                    "secondary-fixed-dim": "#e4c285",
                    "on-primary": "#512405",
                    "on-secondary-container": "#d5b478",
                    "primary": "#ffb68d",
                    "tertiary-fixed": "#d7e8c5",
                    "on-secondary-fixed": "#261900",
                    "primary-container": "#c3815b",
                    "surface-bright": "#3a3938",
                    "on-error-container": "#ffdad6",
                    "primary-fixed": "#ffdbc9",
                    "on-secondary-fixed-variant": "#5a4312",
                    "outline-variant": "#52443c",
                    "tertiary-fixed-dim": "#bbccaa",
                    "secondary": "#e4c285",
                    "surface-dim": "#131312",
                    "tertiary": "#bbccaa",
                    "error": "#ffb4ab",
                    "on-surface-variant": "#d7c2b8",
                    "on-tertiary-container": "#202d16",
                    "on-tertiary": "#27341d",
                    "error-container": "#93000a",
                    "inverse-primary": "#89502e",
                    "secondary-container": "#5d4514",
                    "surface-container-lowest": "#0e0e0d",
                    "on-secondary": "#412d00",
                    "glass-fill": "rgba(15, 15, 14, 0.6)",
                    "inverse-on-surface": "#31302f",
                    "tertiary-container": "#869677",
                    "surface-variant": "#353533",
                    "on-tertiary-fixed-variant": "#3d4b31",
                    "surface-tint": "#ffb68d",
                    "surface-container-highest": "#353533",
                    "canvas-light": "#F5F0EB",
                    "surface-container-high": "#2a2a29",
                    "outline": "#9f8d84",
                    "on-tertiary-fixed": "#121f09",
                    "on-primary-fixed-variant": "#6c3919",
                    "surface-container": "#20201e",
                    "inverse-surface": "#e5e2e0",
                    "on-error": "#690005",
                    "background": "#131312",
                    "surface": "#131312",
                    "secondary-fixed": "#ffdea4",
                    "on-primary-fixed": "#331200"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "margin-mobile": "20px",
                    "margin-desktop": "80px",
                    "gutter": "24px",
                    "container-max": "1440px",
                    "unit": "8px"
            },
            "fontFamily": {
                    "button-text": ["Inter"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "label-caps": ["Inter"],
                    "headline-xl": ["Playfair Display"],
                    "headline-md": ["Playfair Display"],
                    "display-lg": ["Playfair Display"]
            },
            "fontSize": {
                    "button-text": ["14px", {"lineHeight": "1.0", "letterSpacing": "0.05em", "fontWeight": "500"}],
                    "body-md": ["16px", {"lineHeight": "1.6", "fontWeight": "400"}],
                    "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
                    "label-caps": ["12px", {"lineHeight": "1.0", "letterSpacing": "0.1em", "fontWeight": "600"}],
                    "headline-xl": ["48px", {"lineHeight": "1.2", "fontWeight": "400"}],
                    "headline-md": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}],
                    "display-lg": ["72px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
</head>
<body class="bg-background text-on-background selection:bg-primary selection:text-on-primary">
<!-- Top Navigation Bar -->
<nav class="fixed top-0 w-full z-50 bg-glass-fill backdrop-blur-md border-b border-glass-stroke">
<div class="flex justify-between items-center w-full px-margin-desktop h-20 max-w-container-max mx-auto">
<a class="font-headline-md text-headline-md text-primary tracking-tight" data-i18n="nav-logo" href="/">Carlos Bernardo</a>
<div class="hidden md:flex gap-10 items-center">
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-trajectory" href="#">Trajectory</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-projects" href="#">Projects</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300" data-i18n="nav-universidad" href="#">Universidad</a>
<a class="font-label-caps text-label-caps text-primary font-bold border-b-2 border-primary pb-1" data-i18n="nav-contact" href="#">Contact</a>
</div>
<div class="flex items-center gap-4">
<div class="flex items-center gap-2">
<button class="font-label-caps text-label-caps hover:text-primary transition-colors duration-300 text-primary" onclick="setLanguage('pt-BR')">PT</button>
<span class="text-glass-stroke opacity-30">|</span>
<button class="font-label-caps text-label-caps hover:text-primary transition-colors duration-300 text-on-surface-variant" onclick="setLanguage('es-419')">ES</button>
<span class="text-glass-stroke opacity-30">|</span>
<button class="font-label-caps text-label-caps hover:text-primary transition-colors duration-300 text-on-surface-variant" onclick="setLanguage('en')">EN</button>
<span class="text-glass-stroke opacity-30">|</span>
<button class="font-label-caps text-label-caps hover:text-primary transition-colors duration-300 text-on-surface-variant" onclick="setLanguage('zh-CN')">ZH</button>
</div>
</div>
</div>
</nav>
<!-- Main Content Shell -->
<main class="pt-40 pb-20 px-margin-desktop max-w-container-max mx-auto min-h-screen">
<!-- Header Section -->
<header class="mb-24 stagger-item" id="header">
<p class="font-label-caps text-label-caps text-primary mb-4" data-i18n="header-tag">INSTITUTIONAL RELATIONS</p>
<h1 class="font-display-lg text-display-lg mb-6 leading-tight max-w-4xl" id="main-headline">
<span data-i18n="headline-primary">Conexões que geram impacto.</span><br>
<span class="italic text-on-surface-variant font-headline-xl" data-i18n="headline-secondary">Relaciones que impulsan el cambio.</span>
</h1>
<div class="w-24 h-px bg-primary opacity-50"></div>
</header>
<section class="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
<!-- Information Column -->
<div class="lg:col-span-5 space-y-20 stagger-item">
<!-- Contact Details -->
<div class="space-y-8">
<div class="space-y-2">
<span class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="label-location">Localização</span>
<p class="font-body-lg text-body-lg" data-i18n="content-address">Av. da Liberdade, 110. 1250-146 Lisboa, Portugal.</p>
</div>
<div class="space-y-2">
<span class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="label-coordination">Coordenação</span>
<p class="font-body-lg text-body-lg">relations@carlosbernardo.edu</p>
</div>
<div class="flex gap-6 pt-4">
<a class="w-12 h-12 rounded-full border border-glass-stroke flex items-center justify-center hover:bg-primary hover:text-on-primary transition-all duration-300" href="#">
<span class="material-symbols-outlined text-xl">share</span>
</a>
<a class="w-12 h-12 rounded-full border border-glass-stroke flex items-center justify-center hover:bg-primary hover:text-on-primary transition-all duration-300" href="#">
<span class="material-symbols-outlined text-xl">language</span>
</a>
</div>
</div>
<!-- High-End Background Context (Image) -->
<div class="relative h-[400px] overflow-hidden rounded-lg group">
<img alt="Conference Room" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" data-alt="A sophisticated, high-end corporate boardroom at dusk. The room features a long, polished dark walnut table reflecting minimalist architectural lighting. Floor-to-ceiling windows reveal a blurred urban skyline in deep blues. The interior lighting is warm and copper-toned, creating a luxurious and authoritative atmosphere suitable for international relations and business leadership discussions. The visual style is cinematic and editorial." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAiHV25x5Fw4hpdbskcVcDWC9-8zW2hJbI6Qc3ufFt9WefbdpxeDaJd-myo2hf5G4smKrkKZh00lTvnBRQO7B_pK8AROlhkT-OhZmyQ4EIwin_hsPj0oCC_WE8UZaa2LqTYBC5lkABOiNs_sKN7VkUP1Kp3t9i11PZDZMIZf5xiXxRBsCOGFG-9NkvPyktSN6DetGztrGDgdMs_WbuR_oyWYcC9NMlmw55ErrpWIfWRI6UYaQetbxnz13IoqmEjU5by34JiPfYZN3ng">
<div class="absolute inset-0 bg-gradient-to-t from-background/80 to-transparent"></div>
<div class="absolute bottom-6 left-6">
<p class="font-label-caps text-label-caps text-on-surface" data-i18n="image-caption">CENTRO DE OPERAÇÕES</p>
</div>
</div>
</div>
<!-- Form Column -->
<div class="lg:col-span-7 stagger-item">
<div class="glass-panel p-10 md:p-16 rounded-lg relative overflow-hidden">
<!-- Decorative subtle gradient -->
<div class="absolute -top-24 -right-24 w-64 h-64 bg-primary/5 rounded-full blur-[100px]"></div>
<form class="space-y-12 relative z-10" id="contact-form">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter">
<div class="space-y-2">
<label class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="form-label-name">Nome</label>
<input class="w-full bg-transparent border-0 border-b border-glass-stroke py-4 font-body-md text-body-md text-on-surface placeholder:opacity-20 transition-all focus:border-primary" data-i18n-placeholder="form-placeholder-name" placeholder="John Doe" type="text">
</div>
<div class="space-y-2">
<label class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="form-label-email">Email</label>
<input class="w-full bg-transparent border-0 border-b border-glass-stroke py-4 font-body-md text-body-md text-on-surface placeholder:opacity-20 transition-all focus:border-primary" data-i18n-placeholder="form-placeholder-email" placeholder="email@domain.com" type="email">
</div>
</div>
<div class="space-y-2">
<label class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="form-label-subject">Assunto</label>
<select class="w-full bg-transparent border-0 border-b border-glass-stroke py-4 font-body-md text-body-md text-on-surface appearance-none focus:border-primary">
<option class="bg-surface-container" data-i18n="subject-opt1">Institutional Relations</option>
<option class="bg-surface-container" data-i18n="subject-opt2">Education Programs</option>
<option class="bg-surface-container" data-i18n="subject-opt3">Partnerships</option>
<option class="bg-surface-container" data-i18n="subject-opt4">Press Inquiry</option>
</select>
</div>
<div class="space-y-2">
<label class="font-label-caps text-label-caps text-on-surface-variant uppercase" data-i18n="form-label-message">Mensagem</label>
<textarea class="w-full bg-transparent border-0 border-b border-glass-stroke py-4 font-body-md text-body-md text-on-surface placeholder:opacity-20 transition-all focus:border-primary resize-none" data-i18n-placeholder="form-placeholder-message" placeholder="Sua mensagem..." rows="4"></textarea>
</div>
<div class="pt-6">
<button class="group flex items-center gap-4 bg-primary text-on-primary px-10 py-5 rounded-full font-button-text text-button-text transition-all duration-300 hover:bg-primary-fixed-dim hover:gap-6 active:scale-95 ease-out-quint" type="submit">
<span data-i18n="form-submit">ENVIAR MENSAGEM</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</div>
</form>
</div>
</div>
</section>
</main>
<!-- Footer -->
<footer class="w-full py-20 border-t border-glass-stroke bg-surface-container-lowest">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter px-margin-desktop max-w-container-max mx-auto">
<div class="space-y-8">
<div class="font-headline-xl text-headline-xl text-primary opacity-20">Carlos Bernardo</div>
<p class="font-body-md text-body-md text-on-surface-variant max-w-xs" data-i18n="footer-copyright">
                    © 2024 Carlos Bernardo. All rights reserved. High-end Business Leadership &amp; Education.
                </p>
</div>
<div class="flex flex-col md:items-end justify-between">
<div class="flex gap-8 mb-10">
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="footer-privacy" href="#">Privacy Policy</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="footer-terms" href="#">Terms of Service</a>
<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="footer-press" href="#">Press Kit</a>
<a class="font-label-caps text-label-caps text-primary" href="#">LinkedIn</a>
</div>
<div class="text-on-surface-variant font-label-caps text-[10px] tracking-widest opacity-40">
                    POWERED BY CORTEX DESIGN SYSTEMS
                </div>
</div>
</div>
</footer>
<script>
        const i18n = {
            'pt-BR': {
                'nav-logo': 'Carlos Bernardo',
                'nav-trajectory': 'Trajetória',
                'nav-projects': 'Projetos',
                'nav-universidad': 'Universidade',
                'nav-contact': 'Contato',
                'header-tag': 'RELAÇÕES INSTITUCIONAIS',
                'headline-primary': 'Conexões que geram impacto.',
                'headline-secondary': 'Parcerias que transformam o futuro.',
                'label-location': 'Localização',
                'content-address': 'Av. da Liberdade, 110. 1250-146 Lisboa, Portugal.',
                'label-coordination': 'Coordenação',
                'image-caption': 'CENTRO DE OPERAÇÕES',
                'form-label-name': 'Nome',
                'form-placeholder-name': 'Seu nome completo',
                'form-label-email': 'E-mail',
                'form-placeholder-email': 'email@exemplo.com',
                'form-label-subject': 'Assunto',
                'subject-opt1': 'Relações Institucionais',
                'subject-opt2': 'Programas Educacionais',
                'subject-opt3': 'Parcerias',
                'subject-opt4': 'Assessoria de Imprensa',
                'form-label-message': 'Mensagem',
                'form-placeholder-message': 'Como podemos ajudar?',
                'form-submit': 'ENVIAR MENSAGEM',
                'footer-copyright': '© 2024 Carlos Bernardo. Todos os direitos reservados. Liderança e Educação de Alto Nível.',
                'footer-privacy': 'Política de Privacidade',
                'footer-terms': 'Termos de Serviço',
                'footer-press': 'Press Kit'
            },
            'es-419': {
                'nav-logo': 'Carlos Bernardo',
                'nav-trajectory': 'Trayectoria',
                'nav-projects': 'Proyectos',
                'nav-universidad': 'Universidad',
                'nav-contact': 'Contacto',
                'header-tag': 'RELACIONES INSTITUCIONALES',
                'headline-primary': 'Conexiones que generan impacto.',
                'headline-secondary': 'Relaciones que impulsan el cambio.',
                'label-location': 'Ubicación',
                'content-address': 'Av. da Liberdade, 110. 1250-146 Lisboa, Portugal.',
                'label-coordination': 'Coordinación',
                'image-caption': 'CENTRO DE OPERACIONES',
                'form-label-name': 'Nombre',
                'form-placeholder-name': 'Su nombre completo',
                'form-label-email': 'Correo electrónico',
                'form-placeholder-email': 'correo@ejemplo.com',
                'form-label-subject': 'Asunto',
                'subject-opt1': 'Relaciones Institucionales',
                'subject-opt2': 'Programas Educativos',
                'subject-opt3': 'Alianzas',
                'subject-opt4': 'Prensa',
                'form-label-message': 'Mensaje',
                'form-placeholder-message': '¿En qué podemos ayudarle?',
                'form-submit': 'ENVIAR MENSAJE',
                'footer-copyright': '© 2024 Carlos Bernardo. Todos los derechos reservados. Liderazgo y Educación de Alto Nivel.',
                'footer-privacy': 'Política de Privacidad',
                'footer-terms': 'Términos de Servicio',
                'footer-press': 'Sala de Prensa'
            },
            'en': {
                'nav-logo': 'Carlos Bernardo',
                'nav-trajectory': 'Trajectory',
                'nav-projects': 'Projects',
                'nav-universidad': 'University',
                'nav-contact': 'Contact',
                'header-tag': 'INSTITUTIONAL RELATIONS',
                'headline-primary': 'Connections that drive impact.',
                'headline-secondary': 'Relationships that fuel change.',
                'label-location': 'Location',
                'content-address': 'Av. da Liberdade, 110. 1250-146 Lisbon, Portugal.',
                'label-coordination': 'Coordination',
                'image-caption': 'OPERATIONS CENTER',
                'form-label-name': 'Name',
                'form-placeholder-name': 'Your full name',
                'form-label-email': 'Email',
                'form-placeholder-email': 'email@example.com',
                'form-label-subject': 'Subject',
                'subject-opt1': 'Institutional Relations',
                'subject-opt2': 'Educational Programs',
                'subject-opt3': 'Partnerships',
                'subject-opt4': 'Press Inquiry',
                'form-label-message': 'Message',
                'form-placeholder-message': 'How can we help you?',
                'form-submit': 'SEND MESSAGE',
                'footer-copyright': '© 2024 Carlos Bernardo. All rights reserved. High-end Business Leadership & Education.',
                'footer-privacy': 'Privacy Policy',
                'footer-terms': 'Terms of Service',
                'footer-press': 'Press Kit'
            },
            'zh-CN': {
                'nav-logo': '卡洛斯·贝尔纳多',
                'nav-trajectory': '职业轨迹',
                'nav-projects': '重点项目',
                'nav-universidad': '大学教育',
                'nav-contact': '联系我们',
                'header-tag': '机构关系',
                'headline-primary': '产生影响力的连接。',
                'headline-secondary': '驱动变革的伙伴关系。',
                'label-location': '办公地点',
                'content-address': '葡萄牙里斯本 Av. da Liberdade, 110, 1250-146。',
                'label-coordination': '协调部门',
                'image-caption': '运营中心',
                'form-label-name': '姓名',
                'form-placeholder-name': '您的全名',
                'form-label-email': '电子邮箱',
                'form-placeholder-email': 'email@example.com',
                'form-label-subject': '咨询主题',
                'subject-opt1': '机构关系',
                'subject-opt2': '教育项目',
                'subject-opt3': '合作伙伴',
                'subject-opt4': '媒体查询',
                'form-label-message': '留言内容',
                'form-placeholder-message': '我们能为您提供什么帮助？',
                'form-submit': '发送消息',
                'footer-copyright': '© 2024 Carlos Bernardo. 版权所有。高端商业领导力与教育。',
                'footer-privacy': '隐私政策',
                'footer-terms': '服务条款',
                'footer-press': '新闻资料'
            }
        };

        function setLanguage(lang) {
            document.documentElement.lang = lang;
            const dictionary = i18n[lang] || i18n['pt-BR'];

            // Update text content
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dictionary[key]) el.textContent = dictionary[key];
            });

            // Update placeholders
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (dictionary[key]) el.placeholder = dictionary[key];
            });

            // Update active state in selector
            document.querySelectorAll('nav button').forEach(btn => {
                if (btn.textContent.trim() === lang.split('-')[0].toUpperCase()) {
                    btn.classList.add('text-primary');
                    btn.classList.remove('text-on-surface-variant');
                } else {
                    btn.classList.remove('text-primary');
                    btn.classList.add('text-on-surface-variant');
                }
            });
        }

        document.addEventListener('DOMContentLoaded', () => {
            const items = document.querySelectorAll('.stagger-item');
            items.forEach((item, index) => {
                setTimeout(() => {
                    item.style.transition = 'all 0.8s cubic-bezier(0.23, 1, 0.32, 1)';
                    item.style.opacity = '1';
                    item.style.transform = 'translateY(0)';
                }, 100 + (index * 150));
            });

            const header = document.getElementById('header');
            header.style.opacity = '0';
            header.style.transform = 'translateY(40px)';
            
            setTimeout(() => {
                header.style.transition = 'all 1.2s cubic-bezier(0.23, 1, 0.32, 1)';
                header.style.opacity = '1';
                header.style.transform = 'translateY(0)';
            }, 50);

            // Initialize default language
            setLanguage('pt-BR');
        });
    </script>
</body></html>

<!-- Carlos Bernardo - Universidad i18n Multi-Language -->
<!DOCTYPE html><html class="dark" lang="pt-BR"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Universidad Interamericana | Carlos Bernardo</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Playfair+Display:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "on-background": "#e5e2e0",
                        "primary-fixed-dim": "#ffb68d",
                        "on-primary-container": "#481d01",
                        "surface-container-low": "#1c1c1a",
                        "on-surface": "#e5e2e0",
                        "glass-stroke": "rgba(255, 255, 255, 0.08)",
                        "secondary-fixed-dim": "#e4c285",
                        "on-primary": "#512405",
                        "on-secondary-container": "#d5b478",
                        "primary": "#ffb68d",
                        "tertiary-fixed": "#d7e8c5",
                        "on-secondary-fixed": "#261900",
                        "primary-container": "#c3815b",
                        "surface-bright": "#3a3938",
                        "on-error-container": "#ffdad6",
                        "primary-fixed": "#ffdbc9",
                        "on-secondary-fixed-variant": "#5a4312",
                        "outline-variant": "#52443c",
                        "tertiary-fixed-dim": "#bbccaa",
                        "secondary": "#e4c285",
                        "surface-dim": "#131312",
                        "tertiary": "#bbccaa",
                        "error": "#ffb4ab",
                        "on-surface-variant": "#d7c2b8",
                        "on-tertiary-container": "#202d16",
                        "on-tertiary": "#27341d",
                        "error-container": "#93000a",
                        "inverse-primary": "#89502e",
                        "secondary-container": "#5d4514",
                        "surface-container-lowest": "#0e0e0d",
                        "on-secondary": "#412d00",
                        "glass-fill": "rgba(15, 15, 14, 0.6)",
                        "inverse-on-surface": "#31302f",
                        "tertiary-container": "#869677",
                        "surface-variant": "#353533",
                        "on-tertiary-fixed-variant": "#3d4b31",
                        "surface-tint": "#ffb68d",
                        "surface-container-highest": "#353533",
                        "canvas-light": "#F5F0EB",
                        "surface-container-high": "#2a2a29",
                        "outline": "#9f8d84",
                        "on-tertiary-fixed": "#121f09",
                        "on-primary-fixed-variant": "#6c3919",
                        "surface-container": "#20201e",
                        "inverse-surface": "#e5e2e0",
                        "on-error": "#690005",
                        "background": "#131312",
                        "surface": "#131312",
                        "secondary-fixed": "#ffdea4",
                        "on-primary-fixed": "#331200"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "margin-mobile": "20px",
                        "margin-desktop": "80px",
                        "gutter": "24px",
                        "container-max": "1440px",
                        "unit": "8px"
                    },
                    "fontFamily": {
                        "button-text": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "label-caps": ["Inter"],
                        "headline-xl": ["Playfair Display"],
                        "headline-md": ["Playfair Display"],
                        "display-lg-mobile": ["Playfair Display"],
                        "display-lg": ["Playfair Display"],
                        "headline-xl-mobile": ["Playfair Display"]
                    },
                    "fontSize": {
                        "button-text": ["14px", { "lineHeight": "1.0", "letterSpacing": "0.05em", "fontWeight": "500" }],
                        "body-md": ["16px", { "lineHeight": "1.6", "fontWeight": "400" }],
                        "body-lg": ["18px", { "lineHeight": "1.6", "fontWeight": "400" }],
                        "label-caps": ["12px", { "lineHeight": "1.0", "letterSpacing": "0.1em", "fontWeight": "600" }],
                        "headline-xl": ["48px", { "lineHeight": "1.2", "fontWeight": "400" }],
                        "headline-md": ["32px", { "lineHeight": "1.3", "fontWeight": "400" }],
                        "display-lg-mobile": ["44px", { "lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "400" }],
                        "display-lg": ["72px", { "lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "400" }],
                        "headline-xl-mobile": ["32px", { "lineHeight": "1.3", "fontWeight": "400" }]
                    }
                },
            },
        }
    </script>
<style>
        body {
            background-color: #131312;
            color: #e5e2e0;
            overflow-x: hidden;
        }
        .ease-out-quint {
            transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1);
        }
        .staggered-entrance {
            opacity: 0;
            transform: translateY(20px);
            animation: fadeIn 0.8s cubic-bezier(0.23, 1, 0.32, 1) forwards;
        }
        @keyframes fadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .glass-panel {
            background: rgba(15, 15, 14, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .image-reveal {
            clip-path: inset(0 100% 0 0);
            animation: reveal 1.5s cubic-bezier(0.23, 1, 0.32, 1) forwards;
        }
        @keyframes reveal {
            to { clip-path: inset(0 0 0 0); }
        }
        /* Custom ZH character rendering adjustments */
        [lang="zh-CN"] .font-headline-xl,
        [lang="zh-CN"] .font-display-lg,
        [lang="zh-CN"] .font-headline-md {
            letter-spacing: 0.02em;
            line-height: 1.4;
        }
    </style>
</head>
<body class="font-body-md text-body-md selection:bg-primary-container selection:text-on-primary-container">
<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-glass-fill backdrop-blur-md border-b border-glass-stroke">
<div class="flex justify-between items-center w-full px-margin-desktop h-20 max-w-container-max mx-auto">
<div class="font-headline-md text-headline-md text-primary tracking-tight">Carlos Bernardo</div>
<div class="hidden md:flex gap-gutter items-center">
<a class="text-on-surface-variant hover:text-primary transition-colors duration-300 font-label-caps text-label-caps" data-i18n="nav_trajectory" href="#">TRAJETÓRIA</a>
<a class="text-on-surface-variant hover:text-primary transition-colors duration-300 font-label-caps text-label-caps" data-i18n="nav_projects" href="#">PROJETOS</a>
<a class="text-primary font-bold border-b-2 border-primary pb-1 font-label-caps text-label-caps" data-i18n="nav_university" href="#">UNIVERSIDADE</a>
<a class="text-on-surface-variant hover:text-primary transition-colors duration-300 font-label-caps text-label-caps" data-i18n="nav_contact" href="#">CONTATO</a>
</div>
<div class="flex items-center gap-2">
<div class="flex gap-2 font-label-caps text-[10px] text-on-surface-variant">
<button class="hover:text-primary transition-colors cursor-pointer px-1 border-r border-glass-stroke" onclick="setLanguage('pt-BR')">PT</button>
<button class="hover:text-primary transition-colors cursor-pointer px-1 border-r border-glass-stroke" onclick="setLanguage('es-419')">ES</button>
<button class="hover:text-primary transition-colors cursor-pointer px-1 border-r border-glass-stroke" onclick="setLanguage('en')">EN</button>
<button class="hover:text-primary transition-colors cursor-pointer px-1" onclick="setLanguage('zh-CN')">ZH</button>
</div>
</div>
</div>
</nav>
<main class="pt-20">
<!-- Hero Section -->
<section class="relative h-[90vh] flex items-center overflow-hidden">
<div class="absolute inset-0 z-0">
<img alt="Institutional Hero" class="w-full h-full object-cover opacity-60 transition-transform duration-1000 ease-out" src="https://lh3.googleusercontent.com/aida/ADBb0uhatsZXAAF2ZTmWPKYaqZXbv2rxeB4yC-s0nD7uklfNj8TgnbzFt0D6lvPubc8qIB6s0mS2F40khlS2cLlLYIstYsEEUwG35a-72qOm7Iee4TxgGUO2bi0B6ihHZ-YmUMpCPlFpluEJKNl60EMSA6SP4UvholrZIX3pYXw4vmE6J5dbuRESin70Qs2dhfstiEJ6e14oYmbNm-vCbRn4VNi9rdi70K4wZEe05Bya2oL287lWygZt4M_tREvw">
<div class="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent"></div>
</div>
<div class="relative z-10 w-full px-margin-desktop max-w-container-max mx-auto staggered-entrance" style="animation-delay: 200ms;">
<span class="font-label-caps text-label-caps text-primary mb-4 block" data-i18n="hero_tag">VISÃO INSTITUCIONAL</span>
<h1 class="font-display-lg text-display-lg max-w-4xl mb-8 leading-none" data-i18n="hero_title">O Futuro da Educação é <span class="italic text-secondary">Sem Fronteiras.</span></h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl" data-i18n="hero_desc">A Universidad Interamericana destaca-se como um farol de educação superior de alta qualidade, transformando vidas em toda a região através da liderança visionária de Carlos Bernardo.</p>
</div>
</section>
<!-- Mission & Values -->
<section class="py-32 px-margin-desktop max-w-container-max mx-auto">
<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter">
<div class="md:col-span-8 glass-panel p-12 rounded-lg staggered-entrance" style="animation-delay: 300ms;">
<span class="material-symbols-outlined text-primary mb-6" style="font-size: 40px;">school</span>
<h2 class="font-headline-xl text-headline-xl mb-6" data-i18n="mission_title">Nossa Missão</h2>
<p class="font-body-lg text-body-lg text-on-surface-variant" data-i18n="mission_text">Democratizar o acesso ao ensino de elite, fundindo o rigor acadêmico tradicional com as necessidades dinâmicas da força de trabalho moderna. Focamos na formação de líderes que compreendem tanto o impacto local quanto a estratégia global.</p>
</div>
<div class="md:col-span-4 glass-panel p-12 rounded-lg flex flex-col justify-center items-center text-center staggered-entrance" style="animation-delay: 400ms;">
<div class="font-display-lg text-display-lg text-primary mb-2">5000+</div>
<div class="font-label-caps text-label-caps tracking-widest text-secondary" data-i18n="stats_label">ESTUDANTES ATIVOS</div>
<div class="mt-4 text-on-surface-variant" data-i18n="stats_desc">Construindo uma comunidade acadêmica em toda a América do Sul.</div>
</div>
<div class="md:col-span-4 aspect-square overflow-hidden rounded-lg staggered-entrance" style="animation-delay: 500ms;">
<img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCh2BndreYp4H7dqOP8jVbZgj59g24nvkxxzzBrWnJNpndq5IMIyu2RzmwB28kXzd5MejzNotmmk70uAwNfz6MoTRF1QKOtcanECI71ZhF_I-F_xxNso1TdAKeD1AigHCUAKmqto2ncsGanGPhwG4Rs1UyY6Ns9epCff7eRTjkhxXf1MBNYisu5EJoCqbhH7SosVclr6RMNQOUTqsc9_BFuCf-5L-i-YeIyoN_BTisAM4FYOgu_vjA1Y6aPHkXuLWZU-hoBi60XEmCo">
</div>
<div class="md:col-span-8 glass-panel p-12 rounded-lg staggered-entrance" style="animation-delay: 600ms;">
<h3 class="font-headline-md text-headline-md mb-4 text-secondary" data-i18n="values_title">Excelência Acessível</h3>
<p class="font-body-md text-body-md text-on-surface-variant mb-8" data-i18n="values_desc">Acreditamos que barreiras financeiras ou geográficas nunca devem sufocar o potencial. Nossa infraestrutura é projetada para fomentar a inovação, de laboratórios de ponta a espaços sociais colaborativos.</p>
<div class="grid grid-cols-2 gap-8">
<div>
<div class="font-label-caps text-label-caps text-primary mb-2" data-i18n="sub_infra_label">INFRAESTRUTURA</div>
<div class="text-on-surface" data-i18n="sub_infra_text">Campi digitais integrados e excelência física.</div>
</div>
<div>
<div class="font-label-caps text-label-caps text-primary mb-2" data-i18n="sub_curriculum_label">CURRÍCULO</div>
<div class="text-on-surface" data-i18n="sub_curriculum_text">Programas bilíngues focados em agilidade profissional.</div>
</div>
</div>
</div>
</div>
</section>
<!-- Founder's Word -->
<section class="bg-surface-container-lowest py-32">
<div class="px-margin-desktop max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-2 gap-24 items-center">
<div class="staggered-entrance" style="animation-delay: 700ms;">
<div class="relative">
<img class="rounded-lg shadow-2xl grayscale hover:grayscale-0 transition-all duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBzAAfQ3g3hTVTHFWgfNMtxI5yE_aATFvUEwNIiclijPogsUOjOt3f5lTIrQLOQVWHabHCm_qxfTRn3YC7Ng0D1jeD3ol5T73Dwjxy1gvNbzETDrtsaCFfqv9VfTW5mJxsi_gUMCU-2x1jceM_0_DEI1VG_b4nwEACW6AdHa0oq76WZ5MlG3TgFjs_9uCS9Wexy8AmtgjEM0cwqzPEyglSXysCSTmKmzJA9PetOfCLoMnW2n_GlQZntBWlXsfOsHdiuJtov-TejxmvL">
<div class="absolute -bottom-8 -right-8 glass-panel p-8 rounded-lg max-w-xs">
<p class="font-headline-md text-headline-md italic leading-tight text-primary" data-i18n="founder_quote">"A educação é a ferramenta mais poderosa para a soberania regional."</p>
</div>
</div>
</div>
<div class="staggered-entrance" style="animation-delay: 850ms;">
<span class="font-label-caps text-label-caps text-secondary mb-4 block" data-i18n="founder_tag">PALAVRA DO FUNDADOR</span>
<h2 class="font-headline-xl text-headline-xl mb-8">Carlos Bernardo</h2>
<div class="space-y-6 text-on-surface-variant font-body-lg">
<p data-i18n="founder_p1">Durante décadas, meu compromisso tem sido encurtar a distância entre o sonho e a realidade. Na Universidad Interamericana, não ensinamos apenas teoria; cultivamos a resiliência e a visão necessárias para liderar em um mundo complexo.</p>
<p data-i18n="founder_p2">Nosso legado não é medido pelos edifícios que construímos, mas pelo impacto que nossos graduados têm em suas famílias e nações. Estamos construindo um legado de liberdade intelectual e dignidade profissional.</p>
</div>
<div class="mt-12 flex gap-6">
<button class="bg-primary text-on-primary font-button-text text-button-text px-8 py-4 rounded-lg hover:bg-primary-container transition-colors duration-300" data-i18n="btn_manifesto">Ler Manifesto Completo</button>
<button class="border border-glass-stroke glass-fill text-on-surface font-button-text text-button-text px-8 py-4 rounded-lg hover:bg-surface-variant transition-colors duration-300" data-i18n="btn_trajectory">Ver Trajetória</button>
</div>
</div>
</div>
</section>
<!-- Infrastructure Showcase -->
<section class="py-32 px-margin-desktop max-w-container-max mx-auto">
<div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
<div class="max-w-xl">
<h2 class="font-display-lg text-display-lg-mobile md:text-display-lg mb-4" data-i18n="infra_title">Um Espaço para a <span class="text-primary italic">Inovação.</span></h2>
<p class="text-on-surface-variant" data-i18n="infra_desc">Arquitetura que inspira. Cada canto do nosso campus é projetado para facilitar a troca, o foco e a busca pela excelência.</p>
</div>
<div class="flex gap-4">
<button class="p-4 rounded-full border border-glass-stroke hover:bg-primary hover:text-on-primary transition-all duration-300">
<span class="material-symbols-outlined">arrow_back</span>
</button>
<button class="p-4 rounded-full border border-glass-stroke hover:bg-primary hover:text-on-primary transition-all duration-300">
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
<div class="group relative overflow-hidden rounded-lg aspect-[4/5] staggered-entrance" style="animation-delay: 900ms;">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDapekeWcZ9R2Oq2mhaVNxivhyMohcMpd_6WyZhOhU5dTRvXnwLjiE6YD9zFnihazzZwCFZr4HyhBPeDrIO4xLD_0zUS2wgQcViBznOS9Mlv6uwbsCN_UmMhdScpKHcVeTsBa1DUg-3SVDCHKXmqXEXtH8_rdDKNQzsW-kfsF9HlNqVmkrHIRd1qN_VlLbIVh3vqx7ds5YYD6GFHvU7MvvpgAa8dL17d8UBwBdHcEdUv0X_Mc486lmSzJi0CVuwLApYKZBK-xu67Q9N">
<div class="absolute inset-0 bg-gradient-to-t from-background to-transparent opacity-60"></div>
<div class="absolute bottom-8 left-8">
<div class="font-label-caps text-label-caps text-primary mb-2" data-i18n="card_hub_label">CENTRO DE CONHECIMENTO</div>
<div class="font-headline-md text-headline-md" data-i18n="card_hub_title">Biblioteca Central</div>
</div>
</div>
<div class="group relative overflow-hidden rounded-lg aspect-[4/5] staggered-entrance" style="animation-delay: 1000ms;">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuB_gobdc0BCTLa5va2GNhR6Cp-VLDqNj2xQWRI1RvJofIhkVMCcFNzytOGZ3v_hQevvttTPFklFmSx9Z2FXD6ANnBj4C1GraBV6BlLTv2bZVHFL_fLFcOSSennK-gMvRFwpbOx-zivwx6DaxHsGXFXxZ_VOZE2aAOZvoouAAsjF7TPvs-EQQmyzx10mGFHDYOtIlsvFgZP53eIXx6q2PwzLulbM-DYbVDCS_dVzHW8Zu4nmEjdH0aKHzEaYpcDG0WJtLu7MoiJ1FNDl">
<div class="absolute inset-0 bg-gradient-to-t from-background to-transparent opacity-60"></div>
<div class="absolute bottom-8 left-8">
<div class="font-label-caps text-label-caps text-primary mb-2" data-i18n="card_science_label">PROGRESSO CIENTÍFICO</div>
<div class="font-headline-md text-headline-md" data-i18n="card_science_title">Laboratórios de Pesquisa</div>
</div>
</div>
<div class="group relative overflow-hidden rounded-lg aspect-[4/5] staggered-entrance" style="animation-delay: 1100ms;">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD2WTkZyKLrco3Xi1t5x6VeFwWupWYWTLmImocciRwC-HNVj7oAALLPF6CA1n5GxaI1PmimNcswa4YtC9S3Yycpy6YnhH86njr0hW-HqaO9-T94A28MtVlv0niVI4AA4eQ20CZhPzamf3hy37FC-lpcKalj388gTvkTl6IwOQwxWg4t-m603LkTtTGU3MwjN0b0IpmsP8rDqu0w11iDQ80RcNxqndmqPuEUA5IlopfR_qWXmbLgJB3DmWClAeWYcSFrGb62Tb63M3st">
<div class="absolute inset-0 bg-gradient-to-t from-background to-transparent opacity-60"></div>
<div class="absolute bottom-8 left-8">
<div class="font-label-caps text-label-caps text-primary mb-2" data-i18n="card_social_label">COLABORAÇÃO SOCIAL</div>
<div class="font-headline-md text-headline-md" data-i18n="card_social_title">A Praça</div>
</div>
</div>
</div>
</section>
<!-- CTA Section -->
<section class="py-32 px-margin-desktop">
<div class="max-w-container-max mx-auto glass-panel p-20 rounded-lg text-center overflow-hidden relative">
<div class="relative z-10">
<h2 class="font-display-lg text-display-lg-mobile md:text-display-lg mb-8" data-i18n="cta_title">Junte-se à Vanguarda do <span class="italic text-secondary">Aprendizado.</span></h2>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto mb-12" data-i18n="cta_desc">Descubra nossos programas, visite nossos campi e torne-se parte de um legado que está remodelando o futuro da liderança sul-americana.</p>
<div class="flex flex-col md:flex-row gap-6 justify-center">
<button class="bg-primary text-on-primary font-button-text text-button-text px-12 py-5 rounded-full hover:scale-95 transition-transform duration-200 ease-out-quint" data-i18n="btn_apply">Inscrever-se Agora</button>
<button class="border border-primary text-primary font-button-text text-button-text px-12 py-5 rounded-full hover:bg-primary/10 transition-all duration-300" data-i18n="btn_info">Solicitar Informações</button>
</div>
</div>
<div class="absolute -right-20 -top-20 w-80 h-80 bg-primary opacity-5 blur-[120px] rounded-full"></div>
<div class="absolute -left-20 -bottom-20 w-80 h-80 bg-secondary opacity-5 blur-[120px] rounded-full"></div>
</div>
</section>
</main>
<!-- Footer -->
<footer class="w-full py-20 bg-surface-container-lowest border-t border-glass-stroke mt-32">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter px-margin-desktop max-w-container-max mx-auto">
<div>
<div class="font-headline-xl text-headline-xl text-primary opacity-20 mb-8">Carlos Bernardo</div>
<p class="font-body-md text-body-md text-on-surface-variant max-w-md" data-i18n="footer_copy">© 2024 Carlos Bernardo. Todos os direitos reservados. Liderança Empresarial e Educação de Alto Nível. Universidad Interamericana é uma instituição dedicada à excelência.</p>
</div>
<div class="grid grid-cols-2 gap-8 md:justify-items-end">
<div class="flex flex-col gap-4">
<span class="font-label-caps text-label-caps text-primary" data-i18n="foot_inst">INSTITUIÇÃO</span>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="foot_privacy" href="#">Política de Privacidade</a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="foot_terms" href="#">Termos de Serviço</a>
</div>
<div class="flex flex-col gap-4">
<span class="font-label-caps text-label-caps text-primary" data-i18n="foot_connect">CONECTAR</span>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="foot_press" href="#">Press Kit</a>
<a class="font-body-md text-body-md text-on-surface-variant hover:text-secondary-fixed-dim transition-colors duration-300" data-i18n="foot_linkedin" href="#">LinkedIn</a>
</div>
</div>
</div>
</footer>
<script>
        const dictionary = {
            'pt-BR': {
                nav_trajectory: 'TRAJETÓRIA',
                nav_projects: 'PROJETOS',
                nav_university: 'UNIVERSIDADE',
                nav_contact: 'CONTATO',
                hero_tag: 'VISÃO INSTITUCIONAL',
                hero_title: 'O Futuro da Educação é <span class="italic text-secondary">Sem Fronteiras.</span>',
                hero_desc: 'A Universidad Interamericana destaca-se como um farol de educação superior de alta qualidade, transformando vidas em toda a região através da liderança visionária de Carlos Bernardo.',
                mission_title: 'Nossa Missão',
                mission_text: 'Democratizar o acesso ao ensino de elite, fundindo o rigor acadêmico tradicional com as necessidades dinâmicas da força de trabalho moderna. Focamos na formação de líderes que compreendem tanto o impacto local quanto a estratégia global.',
                stats_label: 'ESTUDANTES ATIVOS',
                stats_desc: 'Construindo uma comunidade acadêmica em toda a América do Sul.',
                values_title: 'Excelência Acessível',
                values_desc: 'Acreditamos que barreiras financeiras ou geográficas nunca devem sufocar o potencial. Nossa infraestrutura é projetada para fomentar a inovação, de laboratórios de ponta a espaços sociais colaborativos.',
                sub_infra_label: 'INFRAESTRUTURA',
                sub_infra_text: 'Campi digitais integrados e excelência física.',
                sub_curriculum_label: 'CURRÍCULO',
                sub_curriculum_text: 'Programas bilíngues focados em agilidade profissional.',
                founder_quote: '"A educação é a ferramenta mais poderosa para a soberania regional."',
                founder_tag: 'PALAVRA DO FUNDADOR',
                founder_p1: 'Durante décadas, meu compromisso tem sido encurtar a distância entre o sonho e a realidade. Na Universidad Interamericana, não ensinamos apenas teoria; cultivamos a resiliência e a visão necessárias para liderar em um mundo complexo.',
                founder_p2: 'Nosso legado não é medido pelos edifícios que construímos, mas pelo impacto que nossos graduados têm em suas famílias e nações. Estamos construindo um legado de liberdade intelectual e dignidade profissional.',
                btn_manifesto: 'Ler Manifesto Completo',
                btn_trajectory: 'Ver Trajetória',
                infra_title: 'Um Espaço para a <span class="text-primary italic">Inovação.</span>',
                infra_desc: 'Arquitetura que inspira. Cada canto do nosso campus é projetado para facilitar a troca, o foco e a busca pela excelência.',
                card_hub_label: 'CENTRO DE CONHECIMENTO',
                card_hub_title: 'Biblioteca Central',
                card_science_label: 'PROGRESSO CIENTÍFICO',
                card_science_title: 'Laboratórios de Pesquisa',
                card_social_label: 'COLABORAÇÃO SOCIAL',
                card_social_title: 'A Praça',
                cta_title: 'Junte-se à Vanguarda do <span class="italic text-secondary">Aprendizado.</span>',
                cta_desc: 'Descubra nossos programas, visite nossos campi e torne-se parte de um legado que está remodelando o futuro da liderança sul-americana.',
                btn_apply: 'Inscrever-se Agora',
                btn_info: 'Solicitar Informações',
                footer_copy: '© 2024 Carlos Bernardo. Todos os direitos reservados. Liderança Empresarial e Educação de Alto Nível. Universidad Interamericana é uma instituição dedicada à excelência.',
                foot_inst: 'INSTITUIÇÃO',
                foot_privacy: 'Política de Privacidade',
                foot_terms: 'Termos de Serviço',
                foot_connect: 'CONECTAR',
                foot_press: 'Press Kit',
                foot_linkedin: 'LinkedIn'
            },
            'es-419': {
                nav_trajectory: 'TRAYECTORIA',
                nav_projects: 'PROYECTOS',
                nav_university: 'UNIVERSIDAD',
                nav_contact: 'CONTACTO',
                hero_tag: 'VISIÓN INSTITUCIONAL',
                hero_title: 'El Futuro de la Educación es <span class="italic text-secondary">Sin Fronteras.</span>',
                hero_desc: 'La Universidad Interamericana se destaca como un faro de educación superior de alta calidad, transformando vidas en toda la región bajo el liderazgo visionario de Carlos Bernardo.',
                mission_title: 'Nuestra Misión',
                mission_text: 'Democratizar el acceso a la educación de élite, fusionando el rigor académico tradicional con las necesidades dinámicas de la fuerza laboral moderna. Formamos líderes que entienden el impacto local y la estrategia global.',
                stats_label: 'ESTUDIANTES ACTIVOS',
                stats_desc: 'Construyendo una comunidad académica en toda Sudamérica.',
                values_title: 'Excelencia Accesible',
                values_desc: 'Creemos que las barreras financieras o geográficas nunca deben frenar el potencial. Nuestra infraestructura fomenta la innovación, desde laboratorios de vanguardia hasta espacios sociales.',
                sub_infra_label: 'INFRAESTRUCTURA',
                sub_infra_text: 'Campus digitales integrados y excelencia física.',
                sub_curriculum_label: 'CURRÍCULO',
                sub_curriculum_text: 'Programas bilingües enfocados en agilidad profesional.',
                founder_quote: '"La educación es la herramienta más poderosa para la soberanía regional."',
                founder_tag: 'PALABRA DEL FUNDADOR',
                founder_p1: 'Por décadas, mi compromiso ha sido cerrar la brecha entre el sueño y la realidad. En la Universidad Interamericana, no solo enseñamos teoría; cultivamos la resiliencia para liderar un mundo complejo.',
                founder_p2: 'Nuestro legado no se mide por edificios, sino por el impacto de nuestros graduados en sus familias y naciones. Construimos un legado de libertad intelectual y dignidad profesional.',
                btn_manifesto: 'Leer Manifiesto Completo',
                btn_trajectory: 'Ver Trayectoria',
                infra_title: 'Un Espacio para la <span class="text-primary italic">Innovación.</span>',
                infra_desc: 'Arquitectura que inspira. Cada rincón está diseñado para facilitar el intercambio, el enfoque y la búsqueda de la excelencia.',
                card_hub_label: 'CENTRO DE CONOCIMIENTO',
                card_hub_title: 'Biblioteca Central',
                card_science_label: 'PROGRESO CIENTÍFICO',
                card_science_title: 'Laboratorios de Investigación',
                card_social_label: 'COLABORACIÓN SOCIAL',
                card_social_title: 'La Plaza',
                cta_title: 'Únete a la Vanguardia del <span class="italic text-secondary">Aprendizaje.</span>',
                cta_desc: 'Descubre nuestros programas, visita nuestros campus y forma parte de un legado que redefine el futuro del liderazgo sudamericano.',
                btn_apply: 'Postularse Ahora',
                btn_info: 'Solicitar Información',
                footer_copy: '© 2024 Carlos Bernardo. Todos los derechos reservados. Liderazgo Empresarial y Educación Superior.',
                foot_inst: 'INSTITUCIÓN',
                foot_privacy: 'Política de Privacidad',
                foot_terms: 'Términos de Servicio',
                foot_connect: 'CONECTAR',
                foot_press: 'Kit de Prensa',
                foot_linkedin: 'LinkedIn'
            },
            'en': {
                nav_trajectory: 'TRAJECTORY',
                nav_projects: 'PROJECTS',
                nav_university: 'UNIVERSITY',
                nav_contact: 'CONTACT',
                hero_tag: 'INSTITUTIONAL VISION',
                hero_title: 'The Future of Education is <span class="italic text-secondary">Borderless.</span>',
                hero_desc: 'Universidad Interamericana stands as a beacon of high-quality higher education, transforming lives across the region through the visionary leadership of Carlos Bernardo.',
                mission_title: 'Our Mission',
                mission_text: 'To democratize access to elite education, blending traditional academic rigor with the dynamic needs of the modern workforce. We focus on creating leaders who understand local impact and global strategy.',
                stats_label: 'ACTIVE STUDENTS',
                stats_desc: 'Building a community of scholars across South America.',
                values_title: 'Accessible Excellence',
                values_desc: 'We believe that financial or geographical barriers should never stifle potential. Our infrastructure is designed to foster innovation, from state-of-the-art labs to collaborative social spaces.',
                sub_infra_label: 'INFRASTRUCTURE',
                sub_infra_text: 'Integrated digital campuses and physical excellence.',
                sub_curriculum_label: 'CURRICULUM',
                sub_curriculum_text: 'Bilingual programs focused on professional agility.',
                founder_quote: '"Education is the most powerful tool for regional sovereignty."',
                founder_tag: 'WORD FROM THE FOUNDER',
                founder_p1: 'For decades, my commitment has been to bridge the gap between dream and reality. At Universidad Interamericana, we don\'t just teach theory; we cultivate resilience and vision to lead in a complex world.',
                founder_p2: 'Our legacy is not measured by buildings, but by the impact our graduates have on their families and nations. We are building a legacy of intellectual freedom and professional dignity.',
                btn_manifesto: 'Read Full Manifesto',
                btn_trajectory: 'View Trajectory',
                infra_title: 'A Space for <span class="text-primary italic">Innovation.</span>',
                infra_desc: 'Architecture that inspires. Every corner of our campus is designed to facilitate exchange, focus, and the pursuit of excellence.',
                card_hub_label: 'KNOWLEDGE HUB',
                card_hub_title: 'Central Library',
                card_science_label: 'SCIENTIFIC PROGRESS',
                card_science_title: 'Research Labs',
                card_social_label: 'SOCIAL COLLABORATION',
                card_social_title: 'The Plaza',
                cta_title: 'Join the Vanguard of <span class="italic text-secondary">Learning.</span>',
                cta_desc: 'Discover our programs, visit our campuses, and become part of a legacy that is reshaping the future of South American leadership.',
                btn_apply: 'Apply Now',
                btn_info: 'Request Information',
                footer_copy: '© 2024 Carlos Bernardo. All rights reserved. High-end Leadership & Education.',
                foot_inst: 'INSTITUTION',
                foot_privacy: 'Privacy Policy',
                foot_terms: 'Terms of Service',
                foot_connect: 'CONNECT',
                foot_press: 'Press Kit',
                foot_linkedin: 'LinkedIn'
            },
            'zh-CN': {
                nav_trajectory: '成长历程',
                nav_projects: '战略项目',
                nav_university: '大学愿景',
                nav_contact: '联系我们',
                hero_tag: '机构愿景',
                hero_title: '教育的未来是 <span class="italic text-secondary">无国界的。</span>',
                hero_desc: '泛美大学是高质量高等教育的灯塔，在卡洛斯·贝尔纳多的远见领导下，正在改变整个地区的生命轨迹。',
                mission_title: '我们的使命',
                mission_text: '让精英教育普惠化，将传统学术严谨性与现代劳动力的动态需求相结合。我们致力于培养既懂本土影响又具全球战略的领导者。',
                stats_label: '在校学生',
                stats_desc: '在整个南美洲建立一个学者社区。',
                values_title: '普惠卓越',
                values_desc: '我们相信经济或地理障碍绝不应扼杀潜力。我们的基础设施旨在促进创新，从最先进的实验室到协作社交空间。',
                sub_infra_label: '基础设施',
                sub_infra_text: '集成的数字校园和物理卓越性。',
                sub_curriculum_label: '课程体系',
                sub_curriculum_text: '专注于职业敏捷性的双语项目。',
                founder_quote: '“教育是实现地区主权最强大的工具。”',
                founder_tag: '创始人寄语',
                founder_p1: '几十年来，我一直致力于弥合梦想与现实之间的差距。在泛美大学，我们不仅教授理论，还培养在复杂世界中领导所需的韧性和愿景。',
                founder_p2: '我们的遗产不是由建筑来衡量的，而是由我们的毕业生对家庭和国家产生的影响。我们正在建立智力自由和专业尊严的遗产。',
                btn_manifesto: '阅读完整宣言',
                btn_trajectory: '查看历程',
                infra_title: '一个 <span class="text-primary italic">创新空间。</span>',
                infra_desc: '激发灵感的建筑。校园的每个角落都旨在促进交流、专注和对卓越的追求。',
                card_hub_label: '知识枢纽',
                card_hub_title: '中央图书馆',
                card_science_label: '科学进步',
                card_science_title: '研究实验室',
                card_social_label: '社交协作',
                card_social_title: '中央广场',
                cta_title: '加入 <span class="italic text-secondary">学习的先锋。</span>',
                cta_desc: '探索我们的课程，参观我们的校园，成为重塑南美领导力未来遗产的一部分。',
                btn_apply: '立即申请',
                btn_info: '索取信息',
                footer_copy: '© 2024 卡洛斯·贝尔纳多。保留所有权利。高端业务领导力与教育。',
                foot_inst: '机构',
                foot_privacy: '隐私政策',
                foot_terms: '服务条款',
                foot_connect: '联系',
                foot_press: '新闻资料',
                foot_linkedin: '领英'
            }
        };

        function setLanguage(lang) {
            document.documentElement.lang = lang;
            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dictionary[lang] && dictionary[lang][key]) {
                    el.innerHTML = dictionary[lang][key];
                } else if (dictionary['pt-BR'][key]) {
                    el.innerHTML = dictionary['pt-BR'][key];
                }
            });
            localStorage.setItem('preferredLang', lang);
        }

        // Initialize language
        document.addEventListener('DOMContentLoaded', () => {
            const savedLang = localStorage.getItem('preferredLang') || 'pt-BR';
            setLanguage(savedLang);
        });

        // Animation Observers
        const observerOptions = { threshold: 0.1 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('staggered-entrance');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('section, .glass-panel, .group').forEach(el => {
            el.style.opacity = '0';
            observer.observe(el);
        });

        // Interactive Hero Parallax
        const hero = document.querySelector('section.relative');
        hero.addEventListener('mousemove', (e) => {
            const img = hero.querySelector('img');
            const x = (e.clientX / window.innerWidth - 0.5) * 15;
            const y = (e.clientY / window.innerHeight - 0.5) * 15;
            img.style.transform = `scale(1.05) translate(${x}px, ${y}px)`;
        });

        hero.addEventListener('mouseleave', () => {
            const img = hero.querySelector('img');
            img.style.transform = `scale(1) translate(0, 0)`;
        });
    </script>
</body></html>

<!-- Carlos Bernardo - Project PRD & Brief -->
# Project Brief & Product Requirements Document (PRD)

## 1. Project Overview
**Project Name:** Carlos Bernardo Institutional Ecosystem  
**Client:** Carlos Bernardo (Business Leader, Educator, and Visionary)  
**Objective:** Develop a high-fidelity, premium institutional website that establishes Carlos Bernardo's authority in high-level leadership and education, showcasing his professional trajectory, strategic projects (Grupo Monarca), and educational legacy (Universidad Interamericana).

## 2. Visual Identity & Design System
**Design System Name:** Cinematic Editorial (`{{DATA:DESIGN_SYSTEM:DESIGN_SYSTEM_1}}`)  
**Core Aesthetic:** A "Cinematic Editorial" style characterized by luxury typography, high-contrast imagery, and purposeful negative space. It balances the authority of a business leader with the accessibility of an educator.

### Design Tokens:
*   **Color Palette:**
    *   **Surface:** Dark/Ink (#131312) providing a premium, nocturnal foundation.
    *   **Accent:** Copper/Gold (#c17f59) used for highlights, icons, and CTA elements.
    *   **Text:** Cream/Muted Gray for legibility and sophistication.
*   **Typography:** *Playfair Display* (Headlines) and *Inter/Lora* (Body), utilizing serif styles for an editorial look.
*   **Interactions:** Smooth `cubic-bezier` entry animations, mouse-tracking hover effects, and horizontal looping "Instagram-style" story feeds.

## 3. Technical Architecture (i18n)
The project utilizes a custom reactive Internationalization (i18n) engine.
*   **Supported Languages:** Portuguese (pt-BR), Spanish (es-419), English (en), and Mandarin (zh-CN).
*   **State Management:** Instant DOM-level updates without full page reloads.
*   **Fallback Policy:** `pt-BR` is the root locale. Any missing translation key in other dictionaries automatically falls back to the Portuguese string.
*   **Data Structure:** 100% of strings are mapped to semantic JSON dictionaries; no hardcoded text in components.

## 4. Site Map & Screen Inventory
The ecosystem consists of 5 core desktop screens:

1.  **Home (Hero Cinematográfica):**
    *   **Feature:** Cinematic portrait of Carlos Bernardo with integrated dynamic highlights.
    *   **Feature:** "Instagram Highlights" style feed for Technology, Agribusiness, Education, Health, and Infrastructure.
2.  **Trajetória (Trajectory):**
    *   **Feature:** Chronological narrative of his roots (Carajá) to his binational legacy.
    *   **Focus:** Humanization, Integration, and Innovation.
3.  **Projetos (Projects):**
    *   **Feature:** Strategic portfolio highlighting Grupo Monarca and Global Ventures.
    *   **Focus:** Impact metrics (484 families, 12k+ hectares, 15 tech ventures).
4.  **Universidad:**
    *   **Feature:** Dedicated space for Universidad Interamericana.
    *   **Focus:** Mission, infrastructure (Labs, Library, Plaza), and a bilingual manifesto.
5.  **Contato (Contact):**
    *   **Feature:** Minimalist lead capture form for institutional relations.
    *   **Focus:** Location mapping and direct communication channels.

## 5. Component Specifications
*   **TopNavBar:** Fixed position with a quadrimodal language switcher (PT | ES | EN | ZH).
*   **Dynamic Feed:** Horizontal auto-scrolling ticker/feed for "Impact Metrics" and "Latest News".
*   **Editorial Grid:** Responsive layouts that adapt typography alignment based on the negative space of photographic assets.
*   **Footer:** Minimalist structure with legal links, social icons, and professional credits.

## 6. Constraints & Compliance
*   **Imagery:** Use high-resolution, premium editorial photography only.
*   **Exclusions:** No references to political parties or elective offices.
*   **Language:** Strict adherence to localized terminology (e.g., specific terms for Paraguayan/South American educational contexts).
