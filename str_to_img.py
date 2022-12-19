from PIL import Image, ImageDraw, ImageFont

def ascii_to_image (lines : list[str], location : str ,font_width=27, font_height=20, padding=0):
    shape=(font_width*80+2*padding, font_height*len(lines)+3*padding)
    img = Image.new('RGB',shape, color=(0,0,0))
    drawer=ImageDraw.Draw(img)
    font=ImageFont.truetype('./assets/sourcecodepro.ttf',24)

    text_loc=(padding,padding)
    drawer.multiline_text(text_loc,'\n'.join(lines),font=font,fill=(255,255,255))
    print(f'saving to ./{location}')
    img.save(location)

