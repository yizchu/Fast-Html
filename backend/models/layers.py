from typing import Literal


class Layer:
    """
    Including all kinds of layers.
    """

    def __init__(self):
        self.name: str = ''
        self.kind: str = ''
        self.left: float = 0
        self.top: float = 0
        self.width: float = 0
        self.height: float = 0
        self.opacity: float = 0
        self.visible: bool = True
        self.z_index: float = 0

    async def get_self_attributes(self):
        return (key for key in self.__dict__.keys())


class ImageLayer(Layer):
    """
    layer.kind == 'image'(including 'pixel', 'shape' and 'smartobject')
    """

    def __init__(self):
        super().__init__()
        self.image_path: str = None

    def generate_html(self) -> str:
        return f'''
            <img src="{self.image_path}" alt="Not Found!" class="{self.name}"/>
        '''

    def generate_css(self) -> str:
        return f'''
            .{self.name} {{
                position: absolute;
                display: {"inline-block" if self.visible else "none"};\
                {f'left: {self.left}px;' if self.left else ''}\
                {f'top: {self.top}px;' if self.top else ''}\
                {f'width: {self.width}px;' if self.width else ''}\
                {f'height: {self.height}px;' if self.height else ''}\
                {f'opacity: {self.opacity};' if self.opacity else ''}\
                z-index: {self.z_index};
            }}
        '''


class TypeLayer(Layer):
    """
    layer.kind == 'type'
    """

    def __init__(self):
        super().__init__()
        self.text: str = ''
        self.font_family: list = []
        self.font_size: float = 0
        self.fill_color: list = []
        self.justification: int | None = None
        self.firstline_indent: float = 0
        self.space_before: float = 0
        self.space_after: float = 0
        self.auto_hyphenate: bool = False
        self.leading: str | float = None
        self.underline: bool = False
        self.strikethrough: bool = False

    def generate_html(self) -> str:
        return f'''
            <p class="{self.name}">{self.text} </p>
        '''

    def generate_css(self) -> str:
        return f'''
            .{self.name} {{
                position: absolute;
                display: {"inline-block" if self.visible else "none"};
                {f'left: {self.left}px;' if self.left else ''}\
                {f'top: {self.top}px;' if self.top else ''}\
                {f'width: {self.width}px;' if self.width else ''}\
                {f'height: {self.height}px;' if self.height else ''}\
                {f'opacity: {self.opacity};' if self.opacity else ''}\
                z-index: {self.z_index};\
                {f'font-family: {",".join(str(font) for font in self.font_family)};' if self.font_family else ''}\
                {f'font-size: {self.font_size}px;' if self.font_size else ''}\
                {f'color: rgba({self.fill_color[1] * 255}, {self.fill_color[2] * 255}, {self.fill_color[3] * 255}, {self.fill_color[0]});' if self.fill_color else ''}\
                {f'text-align: {"left" if self.justification == 0 else "center" if self.justification == 1 else "right" if self.justification == 2 else "justify"};' if self.justification is not None else ''}\
                {f'text-indent: {self.firstline_indent}px;' if self.firstline_indent else ''}\
                {f'margin-top: {self.space_before}px;' if self.space_before else ''}\
                {f'margin-bottom: {self.space_after}px;' if self.space_after else ''}\
                {f'hyphens: {"auto" if self.auto_hyphenate else "none"};' if self.auto_hyphenate else ''}\
                {f'line-height: {self.leading if type(self.leading) == str else f"{self.leading}px"};' if self.leading else ''}\
                {f'text-decoration: {"underline" if self.underline else "line-through" if self.strikethrough else "none"};' if self.underline or self.strikethrough else ''}
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
