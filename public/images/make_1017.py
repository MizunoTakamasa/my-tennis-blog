from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Man_playing_tennis_sports_illust…_20261017181336.jpg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1017"
SLUG = "tennis-1017-match-4wins-spin-stroke-return-serve"

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
draw.text((PAD, 72), "2026.10.17 テニス", font=font(30), fill=(255,200,50))
title_lines = ["4戦全勝。", "スピンが効いた。"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(88), fill=(255,255,255))
    y += 110
draw.text((PAD, y+20), "上手い人との練習で気づいた現在地", font=font(42), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 上手い人との練習
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "上手い人との\n練習",
    [
        "ボールが速すぎて空振り2回",
        "",
        "でも打てるボールはしっかり打てた",
        "",
        "スピンが効いたストロークを打つと",
        "「スピンがすごい」と言われた",
        "",
        "今まで言われたことのない言葉だった",
    ],
    tag="練習 / スピン"
)
img.save(f"{OUT_DIR}/02_practice.png")
print("✓ 02_practice")

# ──────────────────────────────────────────────
# 03 試合結果
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "試合：4戦全勝",
    [
        "空振り2回あっても勝った",
        "",
        "サーブがキープできない場面もあった",
        "",
        "でも——",
        "",
        "リターンが好調だった",
        "ブレークを重ねて全試合制した",
    ],
    tag="試合 / 結果"
)
img.save(f"{OUT_DIR}/03_match_result.png")
print("✓ 03_match_result")

# ──────────────────────────────────────────────
# 04 リターンで勝った
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "リターンで\nブレークした",
    [
        "サーブキープできない場面はあった",
        "",
        "それでもリターンゲームで取り返した",
        "",
        "リターンで相手のサービスゲームを",
        "ブレークし続けた",
        "",
        "これが今日の勝因",
    ],
    tag="試合 / リターン"
)
img.save(f"{OUT_DIR}/04_return.png")
print("✓ 04_return")

# ──────────────────────────────────────────────
# 05 自分の現在地
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "自分の現在地",
    [
        "4勝という結果に、当然だと思っている",
        "",
        "難所はストロークだった",
        "それと向き合い、解決し、実施する",
        "その段階に来ている",
        "",
        "サークルで負ける人は",
        "もう1人か2人",
    ],
    tag="振り返り / 現在地"
)
img.save(f"{OUT_DIR}/05_current_level.png")
print("✓ 05_current_level")

# ──────────────────────────────────────────────
# 06 スピンを認められた
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "スピンを\n認められた",
    [
        "「スピンがすごい」",
        "",
        "今まで言われたことがなかった",
        "",
        "自分のストロークのスピンを",
        "誰かに認められた初めての瞬間",
        "",
        "積み重ねてきたものが",
        "外から見えるようになってきた",
    ],
    tag="気づき / スピン"
)
img.save(f"{OUT_DIR}/06_spin_praised.png")
print("✓ 06_spin_praised")

# ──────────────────────────────────────────────
# 07 サーブの課題
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "次の課題①\nサーブの安定",
    [
        "今日はキープできない場面があった",
        "",
        "リターンでカバーできたから勝てた",
        "",
        "でも——",
        "サーブが安定すれば",
        "もっと楽に勝てる",
        "",
        "サーブは次の重点テーマ",
    ],
    tag="課題 / サーブ"
)
img.save(f"{OUT_DIR}/07_serve_issue.png")
print("✓ 07_serve_issue")

# ──────────────────────────────────────────────
# 08 ストロークの課題
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "次の課題②\nストロークの安定",
    [
        "スピンを褒められた",
        "でも——",
        "",
        "打てる場面と打てない場面がある",
        "",
        "どんな球にも安定して",
        "スピンをかけられるようにしたい",
        "",
        "それが次のステージへの鍵",
    ],
    tag="課題 / ストローク"
)
img.save(f"{OUT_DIR}/08_stroke_issue.png")
print("✓ 08_stroke_issue")

# ──────────────────────────────────────────────
# 09 まとめ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日のまとめ",
    [
        "✅ 4戦全勝",
        "✅ スピンを初めて褒められた",
        "✅ リターンでブレーク連発",
        "",
        "📌 課題：サーブの安定",
        "📌 課題：ストロークをどんな球でも安定",
        "",
        "今日の4勝は通過点",
        "もっと強くなれる",
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
