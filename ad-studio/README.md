<div dir="rtl">

# Ad Studio — صانع الإعلانات بـ Claude Code

مهارة تخلي Claude Code يسوي لك إعلان فيديو كامل لمنتجك أو تطبيقك، من الفكرة لين الفيديو الجاهز، بدون برامج مونتاج.

تسألك أول عن منتجك، وتعطيك ٣ أنواع إعلانات تختار منها:

| النوع | شو يطلع | يناسب |
|---|---|---|
| **A** شخصية تتكلم | موشن جرافيك ثنائي الأبعاد، وشخصية تقول الإعلان بصوت | أكل، قهوة، منتجات محلية |
| **B** على ستايل مرجع | تعطيها فيديو إعلان يعجبك، وتسوي نفس الإحساس لمنتجك | براندات راقية، لايف ستايل |
| **C** ثلاثي الأبعاد بالكود | فيلم منتج زجاجي يتفكك ويضوي، كله بالكود | أجهزة، ساعات، سماعات، تقنية |

وبعدين تمشي معك خطوة خطوة: السكربت، وبرومبتات الصور، والستوري بورد، والفيديو. وتشيّك عليه إطار إطار قبل ما تسلّمه.

## التثبيت

١. نزّل مجلد `ad-studio` من هذا المستودع.
٢. حطه داخل مجلد المهارات:
- لكل مشاريعك: `~/.claude/skills/ad-studio`
- لمشروع واحد: `.claude/skills/ad-studio` داخل مجلد المشروع

٣. افتح Claude Code وقول له: **«سوّ لي إعلان لمنتجي»**

## المتطلبات
- Claude Code
- ffmpeg و Python 3 و Node.js (وClaude يثبّت الناقص بنفسه)
- للإعلانات الثلاثية الأبعاد (النوع C): جهاز فيه كرت شاشة مثل ماك M1 وما بعده عشان يكون سريع. بدون كرت شاشة يشتغل، بس أبطأ وايد.

## حقوق
- النوع C يستخدم مكتبة **Lemo-Opuscar** المفتوحة المصدر لصاحبها **Lemomo**:
https://github.com/lemomo-ai/lemo-opuscar (رخصة MIT للكود). المهارة ما تنسخ المكتبة، تنزّلها من مكانها الأصلي.
- المهارة من تصميم **AMANI.AI**. استخدمها وعدّلها بحرية، وإذا نشرتها اذكر المصدر. حفظ الحقوق أمانة.

## تعلّم أكثر
شرح المهارة كامل بالفيديو، ومهارات ثانية جاهزة:
- يوتيوب: https://youtube.com/@amani_ai_ar
- تيليجرام: https://t.me/amani_ai_ar

زكاة العلم نشره 🤍

</div>

---

## English

**Ad Studio** lets Claude Code make a finished video ad for a product or an app — idea, script, image prompts, storyboard, render and QA — with no editing software. Three styles: (A) talking character 2D motion graphics, (B) motion graphics in the style of a reference ad, (C) a 3D product film made fully in code with the open-source [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) library by Lemomo (MIT).

Install: copy the `ad-studio` folder into `~/.claude/skills/`, then ask Claude Code: *"make an ad for my product"*.

By **AMANI.AI** · YouTube [@amani_ai_ar](https://youtube.com/@amani_ai_ar) · Telegram [t.me/amani_ai_ar](https://t.me/amani_ai_ar)
