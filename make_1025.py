from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Tennis_coaching_infographic_with…_20261024211646.jpg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1025"
SLUG = "tennis-1025-trajectory-swing-stroke-upgrade"

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
draw.text((PAD, 72), "2026.10.25 壁打ち", font=font(30), fill=(255,200,50))
title_lines = ["点から線へ。", "ストローク、", "バージョンアップ"]
y = 150
for line in title_lines:
    draw.text((PAD, y), line, font=font(80), fill=(255,255,255))
    y += 100
draw.text((PAD, y+10), "軌道に沿ってラケットを走らせる", font=font(36), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 母指球とべったりのリズム
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "母指球とべったりの\nリズムを作る",
    [
        "移動 → 母指球重心（タタッタ）",
        "打つ → べったり（ターン）",
        "",
        "音と動きを合わせながら",
        "繰り返し練習",
        "",
        "リズムにすると",
        "体の切り替えが自然になる",
    ],
    tag="フットワーク / リズム"
)
img.save(f"{OUT_DIR}/02_rhythm.png")
print("✓ 02_rhythm")

# ──────────────────────────────────────────────
# 03 点から線へ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "点から線へ",
    [
        "以前：「点」で打つ",
        "→ ボールが来た瞬間に当てる",
        "",
        "今日：「線」で打つ",
        "→ ボールの軌道に沿って",
        "　 ラケットを走らせながらヒット",
        "",
        "落ち際をラケットの振り上げで",
        "とらえる感覚とも一致する",
    ],
    tag="ストローク / 軌道"
)
img.save(f"{OUT_DIR}/03_point_to_line.png")
print("✓ 03_point_to_line")

# ──────────────────────────────────────────────
# 04 移動できて初めて上体の捻りができる
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "移動できて初めて\n上体が動く",
    [
        "移動・打点が整うと——",
        "",
        "今まで教わってきた",
        "上体の捻りや",
        "スキージャンプの動きが",
        "自然にできるようになる",
        "",
        "移動が先。捻りは後からついてくる",
    ],
    tag="気づき ①"
)
img.save(f"{OUT_DIR}/04_move_first.png")
print("✓ 04_move_first")

# ──────────────────────────────────────────────
# 05 気づいた課題①
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "気づいた課題 ①",
    [
        "上体を捻ったまま",
        "移動できていないことが多い",
        "",
        "移動中に捻りが戻ってしまっている",
        "",
        "打点に着く前に",
        "ほどけてしまっている",
        "",
        "捻りを保ったまま動くこと",
    ],
    tag="課題 ①"
)
img.save(f"{OUT_DIR}/05_issue1.png")
print("✓ 05_issue1")

# ──────────────────────────────────────────────
# 06 気づいた課題②
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "気づいた課題 ②",
    [
        "ボールをラケット面より",
        "上側に当てられていない",
        "",
        "軌道に沿って打つには",
        "ラケット面の上側でとらえる",
        "",
        "まだここが安定していない",
        "",
        "次の意識ポイントが見えてきた",
    ],
    tag="課題 ②"
)
img.save(f"{OUT_DIR}/06_issue2.png")
print("✓ 06_issue2")

# ──────────────────────────────────────────────
# 07 限界は心が決める
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "限界は心が\n勝手に決める",
    [
        "続けるほどストロークの",
        "いいイメージが積み上がる",
        "",
        "足が動かなくなってきた",
        "それでも続けた",
        "",
        "最終的には体力が尽きて終了",
        "",
        "ストロークはバージョンアップした",
    ],
    tag="メンタル / 練習"
)
img.save(f"{OUT_DIR}/07_mindset.png")
print("✓ 07_mindset")

# ──────────────────────────────────────────────
# 08 今までの練習の意味
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今までの練習の\n意味がつながった",
    [
        "移動・母指球・べた足",
        "スキージャンプの動き",
        "軸足・前足……",
        "",
        "すべて「軌道に沿って打つ」",
        "ためのものだった",
        "",
        "軌道で打てると、ミスが減る",
    ],
    tag="気づき / 全体像"
)
img.save(f"{OUT_DIR}/08_meaning.png")
print("✓ 08_meaning")

# ──────────────────────────────────────────────
# 09 まとめ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日のまとめ",
    [
        "✅ タタッタ（母指球）→ターン（べったり）",
        "✅ 点で打つ → 線で打つ（軌道）",
        "✅ 移動できて捻りができる",
        "",
        "課題：捻りを保ったまま移動",
        "課題：ラケット面より上でとらえる",
        "",
        "次：レッスンで人とストローク",
        "どうなるか楽しみだ",
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
