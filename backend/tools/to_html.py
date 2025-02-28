from models.layers import Layer


def init_html_content(file_name: str) -> str:
    """
    Initialize the html content with the necessary tags and styles.
    """
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name=”viewport” content="width=device-width, initial-scale=1.0">
        <title>{file_name}</title>
        <link rel="stylesheet" href="static/css/{file_name}.css" />
        <style>
            body,
            html {{
                    margin: 0;
                    padding: 0;
                    font-family: Arial, sans-serif;
                    scroll-behavior: smooth;
                }}
        </style>
    </head>
    <body>
    '''


def end_html(html_content: str, html_path: str) -> None:
    """
    Add the closing tags to the html content and write it to the output file.
    """
    html_content += '''
    </body>
    </html>
    '''
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


def end_css(style_content: str, css_path: str) -> None:
    """
    Write the style content to the css file.
    """
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(style_content)
