import os
import asyncio
from psd_tools import PSDImage
from PIL import Image, ImageFont, ImageDraw
from models import layers
import logging
from tools import to_html


async def create_directories(file_name, base_dir):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    files_in_static = [
        'css',
        'img',
    ]
    for file in files_in_static:
        dir_path = os.path.join(base_dir, file)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


async def init_html(file_name, temp_path):
    global html_content, style_content, html_content_lock, style_content_lock
    html_content_lock = asyncio.Lock()
    style_content_lock = asyncio.Lock()
    await create_directories(file_name, f"results/{file_name}/static")
    psd_file = PSDImage.open(temp_path)
    user_info = {'title': file_name, 'width': psd_file.width, 'height': psd_file.height}
    style_content = ""
    html_content = await to_html.init_html_content(file_name)
    for index, root_layer in enumerate(psd_file._layers):
        await get_layer(file_name, root_layer, user_info, index * 100)
    await to_html.end_html(html_content, f"results/{file_name}/{file_name}.html")
    await to_html.end_css(style_content, f"results/{file_name}/static/css/{file_name}.css")


async def get_layer(file_name, layer, user_info, index):
    global html_content, style_content, html_content_lock, style_content_lock
    if layer.is_group():
        if layer.visible:
            for sub_layer in layer._layers:
                await get_layer(file_name, sub_layer, user_info, index)
    elif layer.visible:
        for replacement in layers.replacements:
            layer.name = layer.name.replace(replacement, '-')
        if layer.kind == 'type':
            typelayer = layers.TypeLayer()
            typelayer.name = f"块_{layer.name}_{layer.left}_{layer.top}_{layer.width}_{layer.height}"
            typelayer.kind = 'type'
            typelayer.left = layer.left
            typelayer.top = layer.top
            typelayer.width = layer.width
            typelayer.height = layer.height
            typelayer.opacity = layer.opacity / 255
            typelayer.z_index = index
            if typelayer.left > user_info['width'] or typelayer.top > user_info['height'] or typelayer.left + typelayer.width < 0 or typelayer.top + typelayer.height < 0:
                return
            typelayer.text = layer.text.strip()
            run_array = layer.engine_dict.get('StyleRun', {}).get('RunArray', [{}])
            style_sheet_data = run_array[0].get('StyleSheet', {}).get('StyleSheetData', {})
            properties = run_array[0].get('ParagraphSheet', {}).get('Properties', {})
            typelayer.font_family = [fontset['Name'] for fontset in layer.resource_dict['FontSet']]
            typelayer.font_size = style_sheet_data.get('FontSize', 12)
            typelayer.fill_color = style_sheet_data.get('FillColor', {'Values': [1, 0, 0, 0]}).get('Values', [1, 0, 0, 0])
            typelayer.justification = properties.get('Justification', 0)
            typelayer.firstline_indent = style_sheet_data.get('FirstLineIndent', 0)
            typelayer.space_before = style_sheet_data.get('SpaceBefore', 0)
            typelayer.space_after = style_sheet_data.get('SpaceAfter', 0)
            typelayer.auto_hyphenate = properties.get('AutoHyphenate', False)
            typelayer.leading = "normal" if style_sheet_data.get('AutoLeading', True) else style_sheet_data.get('Leading', 0)
            typelayer.underline = style_sheet_data.get('Underline', False)
            typelayer.strikethrough = style_sheet_data.get('Strikethrough', False)

            # 误差校正
            typelayer.top -= 24
            typelayer.width += 28
            typelayer.height *= 2

            async with html_content_lock:
                html_content += await typelayer.generate_html()
            async with style_content_lock:
                style_content += await typelayer.generate_css()
        else:
            imagelayer = layers.ImageLayer()
            imagelayer.name = f"块_{layer.name}_{layer.left}_{layer.top}_{layer.width}_{layer.height}"
            imagelayer.kind = 'image'
            imagelayer.left = layer.left
            imagelayer.top = layer.top
            imagelayer.width = layer.width
            imagelayer.height = layer.height
            imagelayer.opacity = layer.opacity / 255
            imagelayer.z_index = index
            if imagelayer.left > user_info['width'] or imagelayer.top > user_info['height'] or imagelayer.left + imagelayer.width < 0 or imagelayer.top + imagelayer.height < 0:
                return
            layer_image = layer.composite()
            if layer_image:
                pil_image = Image.frombytes('RGBA', layer_image.size, layer_image.tobytes())
                try:
                    pil_image.save(f"results/{file_name}/static/img/{imagelayer.name}.png")
                    imagelayer.image_path = f"static/img/{imagelayer.name}.png"
                except:
                    return
            async with html_content_lock:
                html_content += await imagelayer.generate_html()
            async with style_content_lock:
                style_content += await imagelayer.generate_css()
