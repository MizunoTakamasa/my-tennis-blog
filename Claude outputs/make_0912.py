from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Tennis_coaching_storyboard_grid_…_202609022215.jpeg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_0912"

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
draw.text((PAD, 72), "9月12日 サークル記録", font=font(30), fill=(255,200,50))
draw.text((PAD, 150), "気持ちよく\n打てる感覚が\n出てきた", font=font(76), fill=(255,255,255))
draw.text((PAD, 460), "格上相手に好勝負できたサークル", font=font(38), fill=(200,220,255))
draw.text((PAD, H-120), "→ 詳しくはブログへ（プロフリンク）", font=font(32), fill=(160,180,220))
img.save(f"{OUT_DIR}/01_cover.png")
print("01 done")

# --- Slide 02: 今日の練習 ---
img = slide_base()
draw_slide(img, "今日の練習", [
    "今日はサークル。",
    "",
    "試合を何本かこなした。",
    "",
    "格上相手との試合で",
    "いい感覚が出てきた。",
], tag="Circle")
img.save(f"{OUT_DIR}/02_intro.png")
print("02 done")

# --- Slide 03: 気持ちよく打てるとき ---
img = slide_base()
draw_slide(img, "気持ちよく打てる\n感覚を言語化する", [
    "気持ちよく打てているときは",
    "体が動いていて",
    "自然にボールへ向かっている。",
    "",
    "崩れたときに立て直せるよう",
    "もっと言語化できるとよい。",
], tag="気づき①")
img.save(f"{OUT_DIR}/03_good_feeling.png")
print("03 done")

# --- Slide 04: 相手のポジショニング ---
img = slide_base()
draw_slide(img, "相手のポジションより\n自分のショット", [
    "相手の戦略的ポジショニングに",
    "惑わされてしまった。",
    "",
    "相手がどこにいても",
    "自分がどこに打つかを決めて",
    "打ち切ることが大事。",
], tag="気づき②")
img.save(f"{OUT_DIR}/04_positioning.png")
print("04 done")

# --- Slide 05: サーブの意識 ---
img = slide_base()
draw_slide(img, "サーブは\n必殺技にする", [
    "・縦・上を意識して振る",
    "・左足体重を意識する",
    "",
    "サーブが安定すれば",
    "試合の主導権を握れる。",
    "",
    "今日はサーブミスで負けた。",
], tag="気づき③")
img.save(f"{OUT_DIR}/05_serve.png")
print("05 done")

# --- Slide 06: 前衛の役割 ---
img = slide_base()
draw_slide(img, "前衛が決めないと\n後衛が苦しい", [
    "ダブルスで感じたこと。",
    "",
    "後衛が粘っても",
    "前衛がポイントを取れないと",
    "試合の流れは変わらない。",
    "",
    "決める場面で決める意識。",
], tag="気づき④")
img.save(f"{OUT_DIR}/06_net_player.png")
print("06 done")

# --- Slide 07: サークルについていける ---
img = slide_base()
draw_slide(img, "ついていける\nようになってきた", [
    "今のサークルは",
    "自分にとって大変なレベル。",
    "",
    "でも、だいぶ",
    "ついていけるようになってきた。",
    "",
    "少しずつ成長を実感。",
], tag="成長")
img.save(f"{OUT_DIR}/07_progress.png")
print("07 done")

# --- Slide 08: 格上相手に好勝負 ---
img = slide_base()
draw_slide(img, "格上相手に\n好勝負できた", [
    "試合後、相手から",
    "「負けそうだった」と言われた。",
    "",
    "サーブミスがなければ",
    "勝てたという実感もある。",
    "",
    "実力を出し切れれば勝てる。",
], tag="成果")
img.save(f"{OUT_DIR}/08_good_match.png")
print("08 done")

# --- Slide 09: まとめ ---
img = slide_base()
draw_slide(img, "今日の収穫", [
    "✅ 気持ちよく打てる感覚が出てきた",
    "✅ 格上相手に「負けそうだった」",
    "📌 崩れたとき→何が変わったか分析を",
    "📌 相手ポジションより自分のショット",
    "💡 サーブ：縦・上・左足体重",
    "💡 前衛が決めると後衛が楽になる",
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
draw.text((PAD, 380), "サークルでの気づき詳細を", font=font(38), fill=(200,220,255))
draw.text((PAD, 440), "ブログで公開しています。", font=font(38), fill=(200,220,255))
draw.text((PAD, 560), "プロフィールのリンクから", font=font(40), fill=(255,200,50))
draw.text((PAD, 620), "チェックしてみてください！", font=font(40), fill=(255,200,50))
draw.text((PAD, H-120), "#テニス #テニスサークル #ダブルス #サーブ #テニス上達", font=font(28), fill=(160,180,220))
img.save(f"{OUT_DIR}/10_cta.png")
print("10 done")

# --- Blog Header (alpha=0, text-free) ---
W, H = 1200, 630
img = make_base(W, H, alpha=0)
img.save(f"{OUT_DIR}/tennis-0912-circle-match-good-feeling-serve-lesson-header.png")
print("header done")

print("All done!")
