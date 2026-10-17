from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Anime_tennis_training_composite_…_20261017172505.jpg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1016"
SLUG = "tennis-1016-posture-improvement-back-forehand-stroke-spine"

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
draw.text((PAD, 72), "2026.10.16 昼トレ", font=font(30), fill=(255,200,50))
title_lines = ["姿勢を正すと", "テニスが変わる"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(88), fill=(255,255,255))
    y += 110
draw.text((PAD, y+20), "猫背改善・胸を張る・体の使い方", font=font(44), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 昼トレ：3m間隔で打ち込む
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "昼トレ：3m間隔で\nひたすら素振り",
    [
        "フォアとバックを交互に繰り返した",
        "",
        "数をこなすことを意識した",
        "",
        "汗が出て、頭の中が真っ白になるまで",
        "",
        "考えながらではなく",
        "体に染み込ませていく感覚で続けた",
    ],
    tag="昼トレ / ストローク"
)
img.save(f"{OUT_DIR}/02_drill.png")
print("✓ 02_drill")

# ──────────────────────────────────────────────
# 03 コーチの言葉：胸を張って
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "コーチの言葉が\n蘇ってきた",
    [
        "バックの練習のとき、",
        "コーチに言われた一言——",
        "",
        "「 胸を張って 」",
        "",
        "体が疲れてきたころに",
        "前のめりになっている自分に気づいた",
        "",
        "あの言葉の意味が、今日わかった",
    ],
    tag="気づき / バックハンド"
)
img.save(f"{OUT_DIR}/03_coach_words.png")
print("✓ 03_coach_words")

# ──────────────────────────────────────────────
# 04 姿勢がテニスに直結する
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "姿勢がテニスに\n直結する",
    [
        "猫背だと肩が前に出て首も前傾する",
        "",
        "→ 腕だけで打とうとしてしまう",
        "→ 体の力がうまく伝わらない",
        "→ 打点がブレやすくなる",
        "",
        "体全体で打つには",
        "まず姿勢が整っていなければならない",
    ],
    tag="気づき / 姿勢"
)
img.save(f"{OUT_DIR}/04_posture_tennis.png")
print("✓ 04_posture_tennis")

# ──────────────────────────────────────────────
# 05 姿勢改善の3本柱
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "姿勢改善の\n3本柱",
    [
        "① 正しい形を意識する",
        "　耳・肩・腰・くるぶし一直線",
        "",
        "② 固まらないように動く",
        "　30分〜1時間に一度立ち上がる",
        "",
        "③ 支える筋肉を鍛える",
        "　ストレッチ＋体幹トレーニング",
    ],
    tag="改善 / 3本柱"
)
img.save(f"{OUT_DIR}/05_three_pillars.png")
print("✓ 05_three_pillars")

# ──────────────────────────────────────────────
# 06 猫背の仕組みと改善方向
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "猫背の仕組みと\n改善の方向",
    [
        "猫背の原因：",
        "　胸の前側（大胸筋）が縮んで硬くなる",
        "　背中側の筋肉が弱くなる",
        "",
        "改善の方向：",
        "　前をゆるめて、後ろを鍛える",
        "",
        "胸開きストレッチ＋Y・T・W体操",
        "肩甲骨寄せ＋あご引き",
    ],
    tag="改善 / 猫背メカニズム"
)
img.save(f"{OUT_DIR}/06_posture_mechanism.png")
print("✓ 06_posture_mechanism")

# ──────────────────────────────────────────────
# 07 ストレッチ・筋トレ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "取り入れたい\nエクササイズ",
    [
        "ストレッチ",
        "　・胸開き（前をゆるめる）",
        "　・チンタック（あご引き）",
        "　・肩甲骨寄せ",
        "",
        "筋トレ",
        "　・プランク（体幹を支える）",
        "　・Y・T・W体操（背中を使う）",
    ],
    tag="改善 / エクササイズ"
)
img.save(f"{OUT_DIR}/07_exercise.png")
print("✓ 07_exercise")

# ──────────────────────────────────────────────
# 08 環境整備
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "姿勢を崩さない\n環境を整える",
    [
        "PC画面は目の高さに合わせる",
        "",
        "椅子は深く座って背もたれを使う",
        "",
        "スマホは目の高さで持つ",
        "（下を向く動作が猫背を加速させる）",
        "",
        "道具と環境が姿勢を作る",
    ],
    tag="改善 / 環境"
)
img.save(f"{OUT_DIR}/08_environment.png")
print("✓ 08_environment")

# ──────────────────────────────────────────────
# 09 日常での意識
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "日常で意識する\n3つのこと",
    [
        "① みぞおちを持ち上げるイメージで立つ",
        "　→ 自然と胸が開く",
        "",
        "② 骨盤を立てる",
        "　→ 上半身の姿勢が変わる",
        "",
        "③ スマホは目の高さで",
        "　→ 首への負担が減る",
    ],
    tag="日常 / 意識"
)
img.save(f"{OUT_DIR}/09_daily_habits.png")
print("✓ 09_daily_habits")

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
