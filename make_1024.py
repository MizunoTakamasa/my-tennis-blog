from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BG_SRC = "/mnt/user-data/uploads/my-tennis-blog/public/images/Tennis_coaching_infographic_with…_20261024211646.jpg"
NAVY = (10, 35, 66)
OUT_DIR = "/home/claude/instagram_1024"
SLUG = "tennis-1024-flat-foot-ground-force-serve-stroke-breakthrough"

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
draw.text((PAD, 72), "2026.10.24 壁打ち", font=font(30), fill=(255,200,50))
title_lines = ["べた足で、", "地面の力を解放する"]
y = 160
for line in title_lines:
    draw.text((PAD, y), line, font=font(78), fill=(255,255,255))
    y += 100
draw.text((PAD, y+20), "自己最高サーブ・ストローク突然開眼", font=font(36), fill=(200,200,200))
draw.text((PAD, 960), "@tennis_diary", font=font(32), fill=(180,180,180))
img.save(f"{OUT_DIR}/01_cover.png")
print("✓ 01_cover")

# ──────────────────────────────────────────────
# 02 今日の練習
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日の壁打ち",
    [
        "昨日の母指球の話を実践しようと",
        "壁打ちへ",
        "",
        "目標：後ろ脚→前足→スキージャンプの動き",
        "",
        "結果——",
        "",
        "できなかった",
        "",
        "タイミングが合わず、ボールが弱い",
    ],
    tag="壁打ち / 課題"
)
img.save(f"{OUT_DIR}/02_practice.png")
print("✓ 02_practice")

# ──────────────────────────────────────────────
# 03 べた足という発見
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "べた足という発見",
    [
        "ゴルフの「べた足」を思い出した",
        "",
        "地面からの力を得るために",
        "足裏を地面に密着させて構える",
        "",
        "テニスでも同じ——",
        "",
        "打つ瞬間は足裏全体で地面を捉える",
        "昨日の母指球の話とつながった",
    ],
    tag="発見 / べた足"
)
img.save(f"{OUT_DIR}/03_flat_foot.png")
print("✓ 03_flat_foot")

# ──────────────────────────────────────────────
# 04 地面反力のメカニズム
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "地面の力を使う\nメカニズム",
    [
        "動く・準備する → 母指球重心",
        "打つ瞬間 → 足裏全体で地面を押す",
        "",
        "地面からの反力を",
        "下半身 → 上半身 → 腕 → ラケット",
        "へと伝える",
        "",
        "サーブで先にこれが実感できていた",
    ],
    tag="地面反力 / メカニズム"
)
img.save(f"{OUT_DIR}/04_ground_force.png")
print("✓ 04_ground_force")

# ──────────────────────────────────────────────
# 05 自己最高サーブ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "自己最高サーブが\n出た",
    [
        "べた足の意識をさらに強くして",
        "サーブを打った",
        "",
        "軽い力なのに",
        "壁に強く当たって音が大きい",
        "",
        "自己最高の一本",
        "",
        "地面の力を使えばこうなる",
    ],
    tag="サーブ / 自己最高"
)
img.save(f"{OUT_DIR}/05_best_serve.png")
print("✓ 05_best_serve")

# ──────────────────────────────────────────────
# 06 サーブを起点に
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "サーブを起点に\nストロークを繰り返す",
    [
        "強いサーブ → 力強い返球",
        "",
        "そのボールを打ち返しながら",
        "ストロークを10本続けた",
        "",
        "ボールの力を借りながら打つのは",
        "本質からは少し離れるが——",
        "",
        "練習として機能した",
    ],
    tag="練習法 / サーブ起点"
)
img.save(f"{OUT_DIR}/06_serve_to_stroke.png")
print("✓ 06_serve_to_stroke")

# ──────────────────────────────────────────────
# 07 ストローク開眼
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "突然、ストロークが\n変わった",
    [
        "10本続けたあと——",
        "",
        "球出しで打ったら",
        "かなり強いボールが打てた",
        "",
        "今まで何をやっていたんだろう",
        "",
        "そう感じる瞬間がまたきた",
    ],
    tag="ストローク / 開眼"
)
img.save(f"{OUT_DIR}/07_stroke_breakthrough.png")
print("✓ 07_stroke_breakthrough")

# ──────────────────────────────────────────────
# 08 コーチへの感謝
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "コーチへの感謝",
    [
        "「歩きながら打つ」を",
        "レッスンに入れてくれたコーチ",
        "",
        "自分ができていないことを",
        "見抜いて、取り入れてくれる",
        "",
        "今日の感覚は",
        "あのレッスンなしには出てこなかった",
    ],
    tag="感謝 / レッスン"
)
img.save(f"{OUT_DIR}/08_coach_thanks.png")
print("✓ 08_coach_thanks")

# ──────────────────────────────────────────────
# 09 まとめ
# ──────────────────────────────────────────────
img = slide_base()
draw_slide(img,
    "今日のまとめ",
    [
        "✅ 動く・準備中 → 母指球重心",
        "✅ 打つ瞬間 → べた足・足裏全体",
        "✅ 地面反力を下から上へ伝える",
        "",
        "サーブ → 自己最高",
        "ストローク → 10本で突然開眼",
        "",
        "来週はサーブのレッスン。楽しみだ",
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
