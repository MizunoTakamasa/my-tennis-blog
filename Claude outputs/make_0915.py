from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Tennis_footwork_fundamentals_exp…_202606071916.jpeg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_0915"

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

W, H = 1080, 1080

# --- Slide 01: Cover ---
img = slide_base()
draw = ImageDraw.Draw(img)
PAD = 160
draw.rectangle([PAD-60, 60, PAD-40, H-60], fill=(255,200,50))
draw.text((PAD, 72), "9月15日 昼トレ記録", font=font(30), fill=(255,200,50))
draw.text((PAD, 150), "スプリット×\n体重移動×\nスキージャンプ", font=font(72), fill=(255,255,255))
draw.text((PAD, 460), "フォアバック50往復で体に刷り込む", font=font(34), fill=(200,220,255))
draw.text((PAD, H-120), "→ 詳しくはブログへ（プロフリンク）", font=font(32), fill=(160,180,220))
img.save(f"{OUT_DIR}/01_cover.png")
print("01 done")

# --- Slide 02: 今日の練習 ---
img = slide_base()
draw_slide(img, "今日の練習", [
    "今日も昼トレ。",
    "シャドースイングを実施した。",
    "",
    "腕より先に、",
    "スプリット・移動・",
    "打点への入りを意識して行った。",
], tag="Noon Training")
img.save(f"{OUT_DIR}/02_intro.png")
print("02 done")

# --- Slide 03: 腕より先に ---
img = slide_base()
draw_slide(img, "腕より先に\n足を動かす", [
    "今日意識したのは",
    "腕を動かすことより——",
    "",
    "①スプリットステップで",
    "　スタンスを広くする",
    "②移動して打点に入る",
    "③そこで体を動かす",
], tag="意識①")
img.save(f"{OUT_DIR}/03_feet_first.png")
print("03 done")

# --- Slide 04: 後ろから前へ ---
img = slide_base()
draw_slide(img, "打点への入りは\n後ろから前へ", [
    "前から後ろに重心が逃げると",
    "体重移動が生きない。",
    "",
    "後ろから前に向かって",
    "打点に入ることで——",
    "",
    "体重が打球方向に乗っていく。",
], tag="意識②")
img.save(f"{OUT_DIR}/04_forward_entry.png")
print("04 done")

# --- Slide 05: 体重移動+スキージャンプ ---
img = slide_base()
draw_slide(img, "体重移動と\nスキージャンプを\n同時に", [
    "打点に入ったら——",
    "",
    "体重移動＋スキージャンプを",
    "同時に行う。",
    "",
    "下半身の力が上に伝わり",
    "体全体が連動する感覚。",
], tag="意識③")
img.save(f"{OUT_DIR}/05_weight_ski.png")
print("05 done")

# --- Slide 06: フォアバック交互 ---
img = slide_base()
draw_slide(img, "フォアバック\n交互に繰り返す", [
    "フォアとバックを交互に。",
    "",
    "スプリット→移動→打点入り",
    "→体重移動＋スキージャンプ",
    "",
    "この流れを繰り返すことで",
    "動きを体に刷り込んでいく。",
], tag="練習方法")
img.save(f"{OUT_DIR}/06_fore_back.png")
print("06 done")

# --- Slide 07: 50往復 ---
img = slide_base()
draw_slide(img, "50往復で\n体全体が疲れた", [
    "フォアバック交互に50往復。",
    "",
    "腕だけではなく",
    "脚・体幹・体全体が連動して",
    "動いている疲れ。",
    "",
    "方向性として正しいと感じた。",
], tag="成果")
img.save(f"{OUT_DIR}/07_50reps.png")
print("07 done")

# --- Slide 08: 続けて体力を ---
img = slide_base()
draw_slide(img, "続けることで\n体力がついてくる", [
    "50往復でかなり疲れたが——",
    "",
    "続けることで体力がつく。",
    "",
    "毎回の昼トレで積み上げれば",
    "試合でも体全体が",
    "自然に連動するようになる。",
], tag="目標")
img.save(f"{OUT_DIR}/08_keep_going.png")
print("08 done")

# --- Slide 09: まとめ ---
img = slide_base()
draw_slide(img, "今日の収穫", [
    "✅ 腕より先にスプリット・移動・打点入り",
    "✅ 打点への入りは後ろから前へ",
    "✅ 体重移動＋スキージャンプを同時に",
    "📌 フォアバック交互50往復",
    "💡 体全体が連動している疲れを実感",
    "🎯 続けて体力をつけていく",
], tag="まとめ")
img.save(f"{OUT_DIR}/09_summary.png")
print("09 done")

# --- Slide 10: CTA ---
img = slide_base()
draw = ImageDraw.Draw(img)
PAD = 160
draw.rectangle([PAD-60, 60, PAD-40, H-60], fill=(255,200,50))
draw.text((PAD, 72), "ブログで詳しく読む", font=font(30), fill=(255,200,50))
draw.text((PAD, 150), "もっと詳しく\n読みたい方へ", font=font(72), fill=(255,255,255))
draw.text((PAD, 380), "昼トレの気づき詳細を", font=font(38), fill=(200,220,255))
draw.text((PAD, 440), "ブログで公開しています。", font=font(38), fill=(200,220,255))
draw.text((PAD, 560), "プロフィールのリンクから", font=font(40), fill=(255,200,50))
draw.text((PAD, 620), "チェックしてみてください！", font=font(40), fill=(255,200,50))
draw.text((PAD, H-120), "#テニス #シャドースイング #スプリットステップ #テニス上達", font=font(28), fill=(160,180,220))
img.save(f"{OUT_DIR}/10_cta.png")
print("10 done")

# --- Blog Header (alpha=0, text-free) ---
W, H = 1200, 630
img = make_base(W, H, alpha=0)
img.save(f"{OUT_DIR}/tennis-0915-shadow-swing-split-step-weight-transfer-footwork-header.png")
print("header done")

print("All done!")
