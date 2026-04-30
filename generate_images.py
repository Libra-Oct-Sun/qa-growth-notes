from PIL import Image, ImageDraw, ImageFont
import os

# 确保目标目录存在
output_dir = "source/images"
os.makedirs(output_dir, exist_ok=True)

# 配色方案
PRIMARY = (45, 90, 123)  # #2D5A7B
ACCENT = (230, 126, 34)   # #E67E22
DARK_BG = (26, 26, 46)    # #1a1a2e
LIGHT_BG = (240, 245, 250)
WHITE = (255, 255, 255)

def draw_gradient(img, color1, color2, direction="vertical"):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for i in range(height if direction == "vertical" else width):
        ratio = i / (height if direction == "vertical" else width)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if direction == "vertical":
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, height)], fill=(r, g, b))

def add_text_center(img, text, y_offset=0, font_size=48, color=WHITE):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    # 尝试使用系统字体
    try:
        font = ImageFont.truetype("simhei.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("msyh.ttc", font_size)
        except:
            font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2
    y = (height - text_h) // 2 + y_offset
    draw.text((x, y), text, fill=color, font=font)

def add_decorative_lines(img, y_pos, color=ACCENT):
    draw = ImageDraw.Draw(img)
    width, _ = img.size
    line_w = 120
    x = (width - line_w) // 2
    draw.rectangle([x, y_pos, x + line_w, y_pos + 4], fill=color)

# 1. banner-home.jpg (1920x1080) - 纯背景，无文字
print("Generating banner-home.jpg...")
img = Image.new("RGB", (1920, 1080))
draw_gradient(img, (35, 70, 100), (45, 90, 123), "vertical")
# 添加一些装饰圆点
draw = ImageDraw.Draw(img)
for cx, cy, r in [(200, 200, 80), (1700, 800, 120), (1500, 300, 60), (400, 900, 100)]:
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(55, 110, 150))
img.save(os.path.join(output_dir, "banner-home.jpg"), quality=85, optimize=True)

# 2. banner-post.jpg (1920x600) - 纯背景，无文字
print("Generating banner-post.jpg...")
img = Image.new("RGB", (1920, 600))
draw_gradient(img, (40, 80, 110), (50, 100, 135), "vertical")
draw = ImageDraw.Draw(img)
for cx, cy, r in [(300, 150, 60), (1600, 450, 90), (1400, 200, 50)]:
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(60, 120, 160))
img.save(os.path.join(output_dir, "banner-post.jpg"), quality=85, optimize=True)

# 3. cover-growth.jpg (800x600)
print("Generating cover-growth.jpg...")
img = Image.new("RGB", (800, 600))
draw_gradient(img, (45, 90, 123), (60, 115, 155), "vertical")
draw = ImageDraw.Draw(img)
# 绘制简单的上升阶梯图形
for i in range(4):
    x = 200 + i * 100
    h = 150 + i * 60
    draw.rectangle([x, 600-h, x+80, 600], fill=(230, 126, 34))
add_text_center(img, "成长之路", y_offset=-120, font_size=48, color=WHITE)
add_text_center(img, "从执行者到架构师", y_offset=40, font_size=28, color=(220, 230, 240))
img.save(os.path.join(output_dir, "cover-growth.jpg"), quality=85, optimize=True)

# 4. cover-playwright.jpg (800x600)
print("Generating cover-playwright.jpg...")
img = Image.new("RGB", (800, 600))
draw_gradient(img, (35, 75, 105), (50, 105, 145), "vertical")
draw = ImageDraw.Draw(img)
# 绘制简单的浏览器窗口图形
draw.rectangle([200, 180, 600, 420], fill=(255, 255, 255), outline=(230, 126, 34), width=4)
draw.rectangle([200, 180, 600, 220], fill=(230, 126, 34))
for i in range(3):
    draw.rectangle([230, 250 + i * 50, 570, 280 + i * 50], fill=(230, 240, 250))
add_text_center(img, "Playwright", y_offset=-180, font_size=48, color=WHITE)
add_text_center(img, "端到端测试实践", y_offset=180, font_size=28, color=(220, 230, 240))
img.save(os.path.join(output_dir, "cover-playwright.jpg"), quality=85, optimize=True)

# 5. cover-exploratory.jpg (800x600)
print("Generating cover-exploratory.jpg...")
img = Image.new("RGB", (800, 600))
draw_gradient(img, (40, 85, 115), (55, 110, 150), "vertical")
draw = ImageDraw.Draw(img)
# 绘制简单的探索路径
centers = [(200, 450), (320, 350), (450, 420), (580, 280), (680, 320)]
for i, (cx, cy) in enumerate(centers):
    r = 20 + i * 5
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(230, 126, 34))
    if i < len(centers) - 1:
        draw.line([(cx, cy), (centers[i+1][0], centers[i+1][1])], fill=(230, 126, 34), width=4)
add_text_center(img, "探索性测试", y_offset=-180, font_size=48, color=WHITE)
add_text_center(img, "自由探索，发现未知", y_offset=180, font_size=28, color=(220, 230, 240))
img.save(os.path.join(output_dir, "cover-exploratory.jpg"), quality=85, optimize=True)

print("All images generated successfully!")
