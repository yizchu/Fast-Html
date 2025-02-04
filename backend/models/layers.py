from typing import Literal


class Layer:
    """
    Including all kinds of layers.
    """

    def __init__(self):
        self.name = None
        self.kind = None
        self.left = None
        self.top = None
        self.width = None
        self.height = None
        self.opacity: float = None
        self.visible: bool = True

    async def get_self_attributes(self):
        return (key for key in self.__dict__.keys())


class ImageLayer(Layer):
    """
    layer.kind == 'image'(including 'pixel', 'shape' and 'smartobject')
    """

    def __init__(self):
        super().__init__()
        self.image_path: str = None

    async def generate_html(self) -> str:
        return f'''
            <div class="{self.name}">
                <img src="{self.image_path}" alt="Not Found!"/>
            </div>\n
        '''

    async def generate_css(self) -> str:
        return f'''
            .{self.name} {{
                position: absolute;
                display: {"inline-block" if self.visible else "none"};
                left: {self.left}px;
                top: {self.top}px;
                width: {self.width}px;
                height: {self.height}px;
                opacity: {self.opacity};
            }}
        '''


class TypeLayer(Layer):
    """
    layer.kind == 'type'
    """

    def __init__(self):
        super().__init__()
        self.text = None
        self.font_family: list = None
        self.font_size: float = None
        self.fill_color: list = None
        self.justification: int = None
        self.firstline_indent: float = None
        self.space_before: float = None
        self.space_after: float = None
        self.auto_hyphenate: bool = None
        self.leading: str | float = None
        self.underline: bool = None
        self.strikethrough: bool = None

    async def generate_html(self) -> str:
        return f'''
            <div class="{self.name}">
                <p>{self.text} </p>
            </div>\n
        '''

    async def generate_css(self) -> str:
        return f'''
            .{self.name} {{
                position: absolute;
                display: {"inline-block" if self.visible else "none"};
                left: {self.left}px;
                top: {self.top}px;
                width: {self.width}px;
                height: {self.height}px;
                opacity: {self.opacity};
                font-family: {",".join(str(font) for font in self.font_family)};
                font-size: {self.font_size}px;
                color: rgba({self.fill_color[1] * 255}, {self.fill_color[2] * 255}, {self.fill_color[3] * 255}, {self.fill_color[0]});
                text-align: {"left" if self.justification == 0 else "center" if self.justification == 1 else "right" if self.justification == 2 else "justify"};
                text-indent: {self.firstline_indent}px;
                margin-top: {self.space_before}px;
                margin-bottom: {self.space_after}px;
                hyphens: {"auto" if self.auto_hyphenate else "none"};
                line-height: {"normal" if self.leading == "normal" else f"{self.leading}px"};
                text-decoration: {"underline" if self.underline else "line-through" if self.strikethrough else "none"};
            }}
        '''


replacements = [
    ' ',
    '.',
    '?',
    '!',
    '@',
    '#',
    '$',
    "%",
    "^",
    "&",
    "*",
    "-",
    "+",
    "=",
    ":",
    ";",
    ",",
    "<",
    ">",
    "/",
    "\\",
    "|",
    "{",
    "}",
    "[",
    "]",
    "(",
    ")",
    "'",
    '"',
    "`",
    "~",
    "，",
    "、",
    "。",
    "；",
    "：",
    "？",
    "！",
    "“",
    "”",
    "‘",
    "’",
    "（",
    "）",
    "【",
    "】",
    "《",
    "》",
    "——",
]
