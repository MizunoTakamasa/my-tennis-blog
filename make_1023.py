from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Tennis_footwork_coaching_infogra…_20261024195457.jpg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1023"
SLUG = "tennis-1023-heel-toe-weight-small-step-axis-foot-adjustment"

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
draw.text((PAD, 72), "2026.10.23 昼トレ", font=font(30), fill=(255,200,50))
title_lines = ["踵は、", "いつ浮かすのか？"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(88), fill=(255,255,255))
    y += 110
draw.text((PAD, y+20), "母指球重心・スモールステップ・軸足の使い分け", font=font(36), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 今日の昼トレ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日の昼トレ",
    [
        "スキージャンプの動きでヒットする",
        "イメージで練習していた",
        "",
        "そこで疑問が浮かんだ——",
        "",
        "「踵は、どのタイミングで浮かすのか？」",
        "",
        "調べてみた",
    ],
    tag="昼トレ / 疑問"
)
img.save(f"{OUT_DIR}/02_question.png")
print("✓ 02_question")

# ──────────────────────────────────────────────
# 03 答え：常に浮かすわけではない
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "常に踵を\n浮かすわけではない",
    [
        "本質は——",
        "",
        "「踵を浮かせる」ではなく",
        "",
        "体重を母指球（拇指球）側に",
        "乗せておくこと",
        "",
        "これが答えだ",
    ],
    tag="調査 / 答え"
)
img.save(f"{OUT_DIR}/03_answer.png")
print("✓ 03_answer")

# ──────────────────────────────────────────────
# 04 踵が浮く場面
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "踵が浮いている場面",
    [
        "✅ スプリットステップ",
        "✅ レディポジション",
        "✅ 素早く動き出すとき",
        "✅ 細かくステップを合わせるとき",
        "",
        "踵がべったりついていると",
        "初動が遅れる",
        "",
        "紙一枚分浮いている程度でOK",
    ],
    tag="フットワーク / 母指球重心"
)
img.save(f"{OUT_DIR}/04_heel_up.png")
print("✓ 04_heel_up")

# ──────────────────────────────────────────────
# 05 踵がつく場面
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "踵がしっかり\nつく場面",
    [
        "✅ ストロークの踏み込み・軸足設定",
        "✅ 大きく踏ん張って切り返すとき",
        "✅ サーブの構え",
        "✅ ポイント間の休息時",
        "",
        "打つ瞬間は地面の反力を使う",
        "→ 足裏全体で地面を捉える",
        "",
        "ずっとつま先立ちは疲れの原因",
    ],
    tag="フットワーク / 踏み込み"
)
img.save(f"{OUT_DIR}/05_heel_down.png")
print("✓ 05_heel_down")

# ──────────────────────────────────────────────
# 06 調整の順番①
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "打点の合わせ方\n① スモールステップ",
    [
        "打てる地点に着いたあとも——",
        "",
        "細かい足踏みで",
        "ボールとの距離を合わせ続ける",
        "",
        "ここで大半のズレを吸収するのが理想",
        "",
        "アジャストステップとも呼ばれる",
    ],
    tag="調整の順番 ①"
)
img.save(f"{OUT_DIR}/06_small_step.png")
print("✓ 06_small_step")

# ──────────────────────────────────────────────
# 07 調整の順番②
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "打点の合わせ方\n② 軸足の位置決め",
    [
        "ボールとの「距離」を決めるのは",
        "主に軸足（後ろ足）",
        "",
        "軸足をボールの後ろ・横の",
        "適切な位置にセットできれば——",
        "",
        "打点はほぼ決まる",
    ],
    tag="調整の順番 ②"
)
img.save(f"{OUT_DIR}/07_axis_foot.png")
print("✓ 07_axis_foot")

# ──────────────────────────────────────────────
# 08 調整の順番③
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "打点の合わせ方\n③ 前足で最終調整",
    [
        "ボールが近い",
        "→ 踏み込みを外側 or オープン気味に",
        "",
        "ボールが遠い",
        "→ 踏み込みを大きく、ボール方向へ",
        "",
        "打点が後ろになりそう",
        "→ 踏み込みを短めに or オープンスタンス",
        "",
        "前足だけに頼りすぎない",
    ],
    tag="調整の順番 ③"
)
img.save(f"{OUT_DIR}/08_front_foot.png")
print("✓ 08_front_foot")

# ──────────────────────────────────────────────
# 09 まとめ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日のまとめ",
    [
        "✅ 動く・準備中 → 母指球重心",
        "✅ 打つとき・踏ん張り → 足裏全体",
        "",
        "打点の合わせ方の順番",
        "① スモールステップで大半を吸収",
        "② 軸足でボールとの距離を決める",
        "③ 前足で最終微調整",
        "",
        "📌 明日のサークルで実践する",
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
