from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Anime_tennis_player_wall_practice_202606012210.jpeg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_0913"

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
draw.text((PAD, 72), "9月13日 壁打ち記録", font=font(30), fill=(255,200,50))
draw.text((PAD, 150), "フォアの\n課題が\n見えてきた", font=font(76), fill=(255,255,255))
draw.text((PAD, 460), "体重移動×スキージャンプ同時意識", font=font(36), fill=(200,220,255))
draw.text((PAD, H-120), "→ 詳しくはブログへ（プロフリンク）", font=font(32), fill=(160,180,220))
img.save(f"{OUT_DIR}/01_cover.png")
print("01 done")

# --- Slide 02: 今日の練習 ---
img = slide_base()
draw_slide(img, "今日の練習", [
    "今日は壁打ち。",
    "",
    "50球（約45分）を",
    "集中して打ち込んだ。",
    "",
    "体重移動×スキージャンプを",
    "同時に意識して練習。",
], tag="Wall Practice")
img.save(f"{OUT_DIR}/02_intro.png")
print("02 done")

# --- Slide 03: 同時にやる ---
img = slide_base()
draw_slide(img, "体重移動と\nスキージャンプを\n同時にやる", [
    "今まで別々に考えていた。",
    "",
    "でも速いボールでは",
    "別々では間に合わない。",
    "",
    "→ 同時にやる意識で",
    "壁打ちをした。",
], tag="気づき①")
img.save(f"{OUT_DIR}/03_simultaneous.png")
print("03 done")

# --- Slide 04: バックはできている ---
img = slide_base()
draw_slide(img, "バックは\n下半身が先に動く", [
    "体重移動＋スキージャンプを",
    "同時にやると——",
    "",
    "バックハンドは",
    "下半身が先に動いて",
    "腕があとから出てくる。",
    "",
    "これはうまくいっている感覚。",
], tag="気づき②")
img.save(f"{OUT_DIR}/04_backhand_ok.png")
print("04 done")

# --- Slide 05: フォアは上体が先 ---
img = slide_base()
draw_slide(img, "フォアは\n上体が先に出る", [
    "フォアハンドになると——",
    "",
    "下半身より先に",
    "上体が出てしまっている。",
    "",
    "体で打つには下半身が主導。",
    "フォアで順番が逆になっていた。",
], tag="課題")
img.save(f"{OUT_DIR}/05_forehand_issue.png")
print("05 done")

# --- Slide 06: フォアの意識 ---
img = slide_base()
draw_slide(img, "フォアは腕を\n体のあとから出す", [
    "体重移動・スキージャンプを先に。",
    "",
    "腕はそのあとから",
    "自然に出てくるように。",
    "",
    "この意識を強くして",
    "繰り返し練習した。",
], tag="修正意識")
img.save(f"{OUT_DIR}/06_forehand_fix.png")
print("06 done")

# --- Slide 07: スプリット×スタンス ---
img = slide_base()
draw_slide(img, "スプリットで\nスタンスが大きくなる", [
    "スプリットステップを入れると",
    "移動のスタンスも大きくなる。",
    "",
    "反動を使って動き出せるため",
    "打球位置への移動がスムーズ。",
    "",
    "→ 太ももへの負担は大きい。",
], tag="気づき③")
img.save(f"{OUT_DIR}/07_split_stance.png")
print("07 done")

# --- Slide 08: 次の目標 ---
img = slide_base()
draw_slide(img, "次は200球\nが目標", [
    "今日は50球で疲れてやめた。",
    "",
    "正確な動きを優先したので",
    "悪くはないが——",
    "",
    "体力をつけるには足りない。",
    "次の壁打ちは200球を目指す。",
], tag="次の目標")
img.save(f"{OUT_DIR}/08_next_goal.png")
print("08 done")

# --- Slide 09: まとめ ---
img = slide_base()
draw_slide(img, "今日の収穫", [
    "✅ 体重移動×スキージャンプは同時に",
    "✅ バック：下半身が先→OK",
    "📌 フォア：上体が先に出てしまう",
    "📌 腕は体のあとから出す意識",
    "💡 スプリットでスタンスが大きくなる",
    "🎯 次は壁打ち200球へ",
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
draw.text((PAD, 380), "壁打ちの気づき詳細を", font=font(38), fill=(200,220,255))
draw.text((PAD, 440), "ブログで公開しています。", font=font(38), fill=(200,220,255))
draw.text((PAD, 560), "プロフィールのリンクから", font=font(40), fill=(255,200,50))
draw.text((PAD, 620), "チェックしてみてください！", font=font(40), fill=(255,200,50))
draw.text((PAD, H-120), "#テニス #壁打ち #体重移動 #スキージャンプ #テニス上達", font=font(28), fill=(160,180,220))
img.save(f"{OUT_DIR}/10_cta.png")
print("10 done")

# --- Blog Header (alpha=0, text-free) ---
W, H = 1200, 630
img = make_base(W, H, alpha=0)
img.save(f"{OUT_DIR}/tennis-0913-wall-practice-weight-shift-ski-jump-forehand-header.png")
print("header done")

print("All done!")
