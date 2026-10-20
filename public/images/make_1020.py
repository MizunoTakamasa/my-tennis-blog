from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/姿勢改善で安定するテニスストローク.png"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1020"
SLUG = "tennis-1020-posture-core-hip-stretch-stroke-improvement"

os.makedirs(OUT_DIR, exist_ok=True)

def make_base(W, H, alpha=220):
    bg = Image.open(BG_SRC).convert("RGB")
    bw, bh = bg.size
    s = max(W/bw, H/bh)
    nw, nh = int(bw*s), int(bh*s)
    bg = bg.resize((nw, nh), Image.LANCZOS)
    bg = bg.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    bg = bg.filter(ImageFilter.GaussianBlur(radius=0))
    ov = Image.new("RGBA", (W, H), NAVY+(alpha,))
    return Image.alpha_composite(bg.convert("RGBA"), ov).convert("RGB")

def slide_base(W=1080, H=1080):
    return make_base(W, H, alpha=220)

def font(size):
    return ImageFont.truetype(FONT, size)

def wrap_text(draw, text, fnt, max_width):
    lines = []
    for paragraph in text.split('\n'):
        line = ''
        for char in paragraph:
            test = line + char
            if draw.textlength(test, font=fnt) <= max_width:
                line = test
            else:
                if line:
                    lines.append(line)
                line = char
        lines.append(line)
    return lines

def draw_slide(img, title, body_lines, tag="", accent=(255,200,50)):
    draw = ImageDraw.Draw(img)
    W, H = img.size
    PAD = 160
    draw.rectangle([PAD-60, 60, PAD-40, H-60], fill=accent)
    if tag:
        tf = font(28)
        draw.text((PAD, 72), tag, font=tf, fill=accent)
    tf = font(64)
    y = 130
    for line in wrap_text(draw, title, tf, W-PAD-60):
        draw.text((PAD, y), line, font=tf, fill=(255,255,255))
        y += 80
    bf = font(38)
    y += 20
    for line in body_lines:
        draw.text((PAD, y), line, font=bf, fill=(220,220,220))
        y += 54
    return img

# ──────────────────────────────────────────────
# Blog header (alpha=0, text-free)
# ──────────────────────────────────────────────
W, H = 1200, 630
img = make_base(W, H, alpha=0)
img.save(f"{OUT_DIR}/{SLUG}-header.png")
print("✓ blog header")

# ──────────────────────────────────────────────
# 01 Cover
# ──────────────────────────────────────────────
img = slide_base()
draw = ImageDraw.Draw(img)
PAD = 160
draw.rectangle([PAD-60, 60, PAD-40, 1020], fill=(255,200,50))
draw.text((PAD, 72), "2026.10.20 テニス", font=font(30), fill=(255,200,50))
title_lines = ["姿勢がいいと", "テニスはうまくなる？"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(80), fill=(255,255,255))
    y += 100
draw.text((PAD, y+20), "体幹・股関節トレーニングで軸を安定させる", font=font(38), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 結論
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "結論：\n軸の安定が大事",
    [
        "「背筋をピンと伸ばす」姿勢ではなく",
        "",
        "頭から骨盤までの軸が",
        "安定していること",
        "",
        "それがストロークの土台になる",
    ],
    tag="姿勢 / 結論"
)
img.save(f"{OUT_DIR}/02_conclusion.png")
print("✓ 02_conclusion")

# ──────────────────────────────────────────────
# 03 理由①②
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "姿勢が良いと\nストロークが変わる",
    [
        "① 回転がスムーズになる",
        "  軸を中心に体をきれいに回せる",
        "  猫背だと「手打ち」になりやすい",
        "",
        "② 打点が安定する",
        "  頭がぶれないと目線が安定する",
        "  ボールとの距離感をつかみやすい",
    ],
    tag="理由 ①②"
)
img.save(f"{OUT_DIR}/03_reason_12.png")
print("✓ 03_reason_12")

# ──────────────────────────────────────────────
# 04 理由③ + 注意点
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "③ バランスを\n崩しにくい",
    [
        "打ったあとに体が流れないため",
        "次のボールへの戻りが早くなる",
        "",
        "⚠ 棒立ちはNG",
        "膝を軽く曲げた「アスレチックな構え」",
        "直立とは違う",
        "",
        "⚠ 姿勢だけでは決まらない",
        "フットワーク・打点・ラケットワークも重要",
    ],
    tag="理由③ / 注意点"
)
img.save(f"{OUT_DIR}/04_reason3_caution.png")
print("✓ 04_reason3_caution")

# ──────────────────────────────────────────────
# 05 体幹トレ①②
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "体幹トレーニング\n① プランク・② サイドプランク",
    [
        "① プランク（基本）",
        "  頭からかかとまで一直線に静止",
        "  20〜30秒 × 2〜3セット",
        "",
        "② サイドプランク",
        "  横向きで腰を持ち上げる",
        "  腹斜筋を鍛えてスイングの軸を安定",
        "  左右各20〜30秒 × 2セット",
    ],
    tag="体幹 ①②"
)
img.save(f"{OUT_DIR}/05_core_12.png")
print("✓ 05_core_12")

# ──────────────────────────────────────────────
# 06 体幹トレ③④
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "体幹トレーニング\n③ デッドバグ・④ ツイスト",
    [
        "③ デッドバグ",
        "  仰向けで腕・脚を交互に伸ばす",
        "  腰を傷めにくく体幹を安定させる",
        "  左右交互10回 × 2セット",
        "",
        "④ メディシンボールツイスト",
        "  座って上体を左右にひねる",
        "  ストロークのひねりに近い動き",
        "  左右10回 × 2セット",
    ],
    tag="体幹 ③④"
)
img.save(f"{OUT_DIR}/06_core_34.png")
print("✓ 06_core_34")

# ──────────────────────────────────────────────
# 07 股関節ストレッチ①②
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "股関節ストレッチ\n① ランジ・② お尻",
    [
        "① ランジストレッチ（股関節前側）",
        "  片膝をついて腰を前に押し出す",
        "  左右各30秒",
        "",
        "② お尻のストレッチ（臀部）",
        "  仰向けで「4の字」に足を組む",
        "  太ももを胸に引き寄せる",
        "  左右各30秒",
    ],
    tag="股関節 ①②"
)
img.save(f"{OUT_DIR}/07_hip_12.png")
print("✓ 07_hip_12")

# ──────────────────────────────────────────────
# 08 股関節ストレッチ③④
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "股関節ストレッチ\n③ スクワット・④ 股関節回し",
    [
        "③ 相撲スクワット（内もも）",
        "  足を広げてつま先外向きで腰を落とす",
        "  低い姿勢での横移動に効く",
        "  20〜30秒 × 2回",
        "",
        "④ 股関節回し（動的）",
        "  立って片膝を上げて外回し・内回し",
        "  練習前のウォームアップに最適",
        "  左右各10回",
    ],
    tag="股関節 ③④"
)
img.save(f"{OUT_DIR}/08_hip_34.png")
print("✓ 08_hip_34")

# ──────────────────────────────────────────────
# 09 取り入れ方
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "スケジュールへの\n取り入れ方",
    [
        "練習前：動的ストレッチ（股関節回しなど）",
        "練習後・寝る前：静的ストレッチ",
        "",
        "体幹トレーニングは週2〜3回",
        "1回10分でも続ければ効果が出る",
        "",
        "プランクで覚えた",
        "「頭からかかとまで一直線」の感覚を",
        "ストロークのたびに思い出す",
    ],
    tag="取り入れ方"
)
img.save(f"{OUT_DIR}/09_schedule.png")
print("✓ 09_schedule")

# ──────────────────────────────────────────────
# 10 CTA
# ──────────────────────────────────────────────
img = slide_base()
draw = ImageDraw.Draw(img)
PAD = 160
W, H = img.size
draw.rectangle([PAD-60, 60, PAD-40, H-60], fill=(255,200,50))
draw.text((PAD, 100), "CTA", font=font(30), fill=(255,200,50))
lines_main = ["テニスの気づきを", "毎日発信中！"]
y = 200
for line in lines_main:
    draw.text((PAD, y), line, font=font(80), fill=(255,255,255))
    y += 100
draw.text((PAD, y+40), "フォロー＆いいねで", font=font(44), fill=(220,220,220))
draw.text((PAD, y+100), "モチベーションが上がります🎾", font=font(44), fill=(220,220,220))
draw.text((PAD, y+200), "ブログも更新中！", font=font(40), fill=(255,200,50))
draw.text((PAD, y+256), "プロフィールのリンクから", font=font(36), fill=(200,200,200))
draw.text((PAD, y+304), "ぜひ読んでみてください", font=font(36), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/10_cta.png")
print("✓ 10_cta")

print("\n✅ All done! Files saved to", OUT_DIR)
