from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/姿勢改善で安定するテニスストローク.png"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1021"
SLUG = "tennis-1021-posture-hip-joint-lower-body-lead-serve-recovery"

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
draw.text((PAD, 72), "2026.10.21 昼トレ", font=font(30), fill=(255,200,50))
title_lines = ["いいレッスンの翌日は", "いい昼トレになる。"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(74), fill=(255,255,255))
    y += 96
draw.text((PAD, y+20), "股関節・下半身リード・サーブの落ち際", font=font(38), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 なぜいい昼トレになるのか
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "なぜ？",
    [
        "いいレッスンでは",
        "コーチの言葉・感覚が体に残る",
        "",
        "翌日の昼トレで",
        "それをなぞることができる",
        "",
        "逆に言えば——",
        "悪いレッスンの翌日は",
        "いい昼トレにはなりにくい",
    ],
    tag="気づき / レッスンと昼トレ"
)
img.save(f"{OUT_DIR}/02_why.png")
print("✓ 02_why")

# ──────────────────────────────────────────────
# 03 いい姿勢とは
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "「いい姿勢」の\n正体",
    [
        "❌ 胸を張って反り腰",
        "  → これはいい姿勢ではない",
        "",
        "✅ 股関節の上に体が乗っている",
        "  → これが正解の姿勢",
        "",
        "この違いがストロークの",
        "土台になる",
    ],
    tag="姿勢 / 気づき"
)
img.save(f"{OUT_DIR}/03_posture.png")
print("✓ 03_posture")

# ──────────────────────────────────────────────
# 04 テニスの動きの流れ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "テニスの\n動きの流れ",
    [
        "① 上体を回転できる位置へ足で移動",
        "",
        "② 股関節の上に体が乗る姿勢を保つ",
        "",
        "③ 下半身主導で上体を回す",
        "",
        "④ 腕を走らせ、ラケットを走らせる",
        "",
        "⑤ ボールをヒット",
    ],
    tag="姿勢 / 動きの流れ"
)
img.save(f"{OUT_DIR}/04_flow.png")
print("✓ 04_flow")

# ──────────────────────────────────────────────
# 05 打点：近くで丁寧に
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "打点は\n近くで丁寧に",
    [
        "バック・フォア共通",
        "",
        "いつもより引きつけて",
        "近い打点でとらえる",
        "",
        "力任せに振らない",
        "その位置でしっかりミートする",
        "",
        "丁寧に打つと",
        "自分の打点の癖がわかってくる",
    ],
    tag="意識① / 打点"
)
img.save(f"{OUT_DIR}/05_contact_point.png")
print("✓ 05_contact_point")

# ──────────────────────────────────────────────
# 06 後ろ脚→前足→ラケット
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "後ろ脚 → 前足\n→ ラケット",
    [
        "ヒットするときの流れ",
        "",
        "① 後ろ脚を踏む",
        "② 前足を踏む",
        "③ ラケットが走る",
        "",
        "脚の踏みかえが",
        "ラケットの走りにつながる",
        "",
        "一球一球この連動を確かめた",
    ],
    tag="意識② / 下半身リード"
)
img.save(f"{OUT_DIR}/06_footwork.png")
print("✓ 06_footwork")

# ──────────────────────────────────────────────
# 07 サーブ：落ち際に一気に
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "サーブ：\n落ち際に一気に打つ",
    [
        "レッスンでは崩れっぱなしだった",
        "",
        "今日の意識はひとつだけ",
        "",
        "トスして——",
        "落ち際にかけて一気に打つ",
        "",
        "難しく考えず",
        "落ちてくるタイミングに",
        "体を解放する",
    ],
    tag="意識③ / サーブ"
)
img.save(f"{OUT_DIR}/07_serve.png")
print("✓ 07_serve")

# ──────────────────────────────────────────────
# 08 病み上がりの昼トレ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "病み上がりでも\nコートに出た",
    [
        "体の感覚を確かめながら",
        "丁寧に一球一球を積み上げた",
        "",
        "量より質の昼トレ",
        "",
        "病み上がりとしては",
        "いい練習だったと思っている",
    ],
    tag="振り返り"
)
img.save(f"{OUT_DIR}/08_recovery.png")
print("✓ 08_recovery")

# ──────────────────────────────────────────────
# 09 まとめ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日のまとめ",
    [
        "✅ いいレッスン翌日 → いい昼トレ",
        "✅ 姿勢 = 股関節の上に体が乗ること",
        "✅ 打点は近くで丁寧にとらえる",
        "✅ 後ろ脚→前足→ラケットの連動",
        "✅ サーブは落ち際に一気に打つ",
        "",
        "📌 積み上げが体に残っている",
        "  それを昼トレで確かめることが大事",
    ],
    tag="まとめ"
)
img.save(f"{OUT_DIR}/09_summary.png")
print("✓ 09_summary")

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
