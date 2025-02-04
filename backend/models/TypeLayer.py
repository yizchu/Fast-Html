_engine_data = {  # layer._engine_data
    'EngineDict': {
        'Editor': {
            'Text': '联系我们\r'  # 文本内容
        },
        'ParagraphRun': {
            'DefaultRunData': {
                'ParagraphSheet': {
                    'DefaultStyleSheet': 0,  # 默认样式表的索引
                    'Properties': {}  # 段落属性
                },
                'Adjustments': {
                    'Axis': [1.0, 0.0, 1.0],  # 坐标轴调整
                    'XY': [0.0, 0.0]  # XY坐标调整
                }
            },
            'RunArray': [{
                'ParagraphSheet': {
                    'DefaultStyleSheet': 0,  # 默认样式表的索引
                    'Properties': {
                        'Justification': 0,  # 对齐方式（0: 左对齐，1: 右对齐，2: 居中）
                        'FirstLineIndent': 0.0,  # 首行缩进
                        'StartIndent': 0.0,  # 起始缩进
                        'EndIndent': 0.0,  # 结束缩进
                        'SpaceBefore': 0.0,  # 段前间距
                        'SpaceAfter': 0.0,  # 段后间距
                        'AutoHyphenate': True,  # 是否自动断字
                        'HyphenatedWordSize': 6,  # 断字词大小
                        'PreHyphen': 2,  # 断字前的间隔
                        'PostHyphen': 2,  # 断字后的间隔
                        'ConsecutiveHyphens': 8,  # 连续连字符数
                        'Zone': 36.0,  # 区域（与文本的排版区相关）
                        'WordSpacing': [0.8, 1.0, 1.33],  # 单词间距
                        'LetterSpacing': [0.0, 0.0, 0.0],  # 字母间距
                        'GlyphSpacing': [1.0, 1.0, 1.0],  # 字形间距
                        'AutoLeading': 1.75,  # 自动行距
                        'LeadingType': 1,  # 行距类型
                        'Hanging': False,  # 是否悬挂（对齐方式的一种）
                        'Burasagari': False,  # 是否有符号挂起
                        'KinsokuOrder': 0,  # 禁止连字顺序
                        'EveryLineComposer': False  # 每行作曲器
                    }
                },
                'Adjustments': {
                    'Axis': [1.0, 0.0, 1.0],  # 坐标轴调整
                    'XY': [0.0, 0.0]  # XY坐标调整
                }
            }],
            'RunLengthArray': [5],  # 每个段落的字符数
            'IsJoinable':
            1  # 是否可以连接
        },
        'StyleRun': {
            'DefaultRunData': {
                'StyleSheet': {
                    'StyleSheetData': {}  # 样式表数据（字体、大小、颜色等）
                }
            },
            'RunArray': [{
                'StyleSheet': {
                    'StyleSheetData': {
                        'Font': 0,  # 字体索引
                        'FontSize': 15.0,  # 字体大小
                        'AutoLeading': False,  # 是否自动行距
                        'Leading': 24.99999,  # 行距
                        'AutoKerning': True,  # 是否自动字距调整
                        'Kerning': 0,  # 字距调整
                        'FillColor': {
                            'Type': 1,  # 填充颜色类型
                            'Values': [1.0, 1.0, 1.0, 1.0]  # 填充颜色值（RGBA）
                        },
                        'HindiNumbers': False  # 是否使用印地语数字
                    }
                }
            }],
            'RunLengthArray': [5],  # 每个样式段的字符数
            'IsJoinable':
            2  # 是否可以连接
        },
        'GridInfo': {
            'GridIsOn': False,  # 网格是否开启
            'ShowGrid': False,  # 是否显示网格
            'GridSize': 18.0,  # 网格大小
            'GridLeading': 22.0,  # 网格行距
            'GridColor': {
                'Type': 1,  # 网格颜色类型
                'Values': [0.0, 0.0, 0.0, 1.0]  # 网格颜色（RGBA）
            },
            'GridLeadingFillColor': {
                'Type': 1,  # 行距填充颜色类型
                'Values': [0.0, 0.0, 0.0, 1.0]  # 行距填充颜色（RGBA）
            },
            'AlignLineHeightToGridFlags': False  # 是否将行高对齐到网格
        },
        'AntiAlias': 6,  # 抗锯齿类型
        'UseFractionalGlyphWidths': True,  # 是否使用分数字形宽度
        'Rendered': {
            'Version': 1,  # 渲染版本
            'Shapes': {
                'WritingDirection':
                0,  # 排版方向（0: 从左到右，1: 从右到左）
                'Children': [{
                    'ShapeType': 0,  # 图形类型
                    'Procession': 0,  # 流程
                    'Lines': {
                        'WritingDirection': 0,  # 排版方向
                        'Children': []  # 子图形
                    },
                    'Cookie': {
                        'Photoshop': {
                            'ShapeType': 0,  # Photoshop图形类型
                            'PointBase': [0.0, 0.0],  # 点基准
                            'Base': {
                                'ShapeType': 0,  # 基准图形类型
                                'TransformPoint0': [1.0, 0.0],  # 变换点0
                                'TransformPoint1': [0.0, 1.0],  # 变换点1
                                'TransformPoint2': [0.0, 0.0]  # 变换点2
                            }
                        }
                    }
                }]
            }
        }
    },
    'ResourceDict': {
        'KinsokuSet': [
            {  # 禁止规则字符集
                'Name': 'PhotoshopKinsokuHard',  # 硬规则字符集名称
                'NoStart': '、。，．・：；？！ー―’”）〕］｝〉》」』】ヽヾゝゞ々ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮヵヶ゛゜?!)]},.:;℃℉¢％‰',  # 不允许作为起始的字符
                'NoEnd': '‘“（〔［｛〈《「『【([{￥＄£＠§〒＃',  # 不允许作为结尾的字符
                'Keep': '―‥',  # 始终保留的字符
                'Hanging': '、。.,'  # 悬挂字符
            },
            {
                'Name': 'PhotoshopKinsokuSoft',  # 软规则字符集名称
                'NoStart': '、。，．・：；？！’”）〕］｝〉》」』】ヽヾゝゞ々',  # 不允许作为起始的字符
                'NoEnd': '‘“（〔［｛〈《「『【',  # 不允许作为结尾的字符
                'Keep': '―‥',  # 始终保留的字符
                'Hanging': '、。.,'  # 悬挂字符
            }
        ],
        'MojiKumiSet': [  # 文字组合设置
            {
                'InternalName': 'Photoshop6MojiKumiSet1'
            },  # 第一个文字组合设置的内部名称
            {
                'InternalName': 'Photoshop6MojiKumiSet2'
            },  # 第二个文字组合设置的内部名称
            {
                'InternalName': 'Photoshop6MojiKumiSet3'
            },  # 第三个文字组合设置的内部名称
            {
                'InternalName': 'Photoshop6MojiKumiSet4'
            }  # 第四个文字组合设置的内部名称
        ],
        'TheNormalStyleSheet':
        0,  # 默认样式表的索引
        'TheNormalParagraphSheet':
        0,  # 默认段落样式表的索引
        'ParagraphSheetSet': [{  # 段落样式表集合
            'Name': '正常 RGB',  # 段落样式的名称
            'DefaultStyleSheet': 0,  # 默认样式表索引
            'Properties': {  # 段落属性
                'Justification': 0,  # 对齐方式（0: 左对齐，1: 右对齐，2: 居中）
                'FirstLineIndent': 0.0,  # 首行缩进
                'StartIndent': 0.0,  # 起始缩进
                'EndIndent': 0.0,  # 结束缩进
                'SpaceBefore': 0.0,  # 段前间距
                'SpaceAfter': 0.0,  # 段后间距
                'AutoHyphenate': True,  # 是否自动断字
                'HyphenatedWordSize': 6,  # 断字的最小单词长度
                'PreHyphen': 2,  # 断字前字符数
                'PostHyphen': 2,  # 断字后字符数
                'ConsecutiveHyphens': 8,  # 允许连续的连字符数量
                'Zone': 36.0,  # 段落排版区域宽度
                'WordSpacing': [0.8, 1.0, 1.33],  # 单词间距（最小值、默认值、最大值）
                'LetterSpacing': [0.0, 0.0, 0.0],  # 字母间距
                'GlyphSpacing': [1.0, 1.0, 1.0],  # 字形间距
                'AutoLeading': 1.2,  # 自动行距
                'LeadingType': 0,  # 行距类型
                'Hanging': False,  # 是否悬挂
                'Burasagari': False,  # 是否启用日文悬挂字符
                'KinsokuOrder': 0,  # 禁则字符的处理顺序
                'EveryLineComposer': False  # 是否启用每行作曲器
            }
        }],
        'StyleSheetSet': [{  # 样式表集合
            'Name': '正常 RGB',  # 样式表名称
            'StyleSheetData': {  # 样式表数据
                'Font': 2,  # 字体索引
                'FontSize': 12.0,  # 字体大小
                'FauxBold': False,  # 是否伪粗体
                'FauxItalic': False,  # 是否伪斜体
                'AutoLeading': True,  # 是否自动行距
                'Leading': 0.0,  # 行距
                'HorizontalScale': 1.0,  # 水平缩放比例
                'VerticalScale': 1.0,  # 垂直缩放比例
                'Tracking': 0,  # 字符间距调整
                'AutoKerning': True,  # 是否自动字距调整
                'Kerning': 0,  # 字距值
                'BaselineShift': 0.0,  # 基线偏移
                'FontCaps': 0,  # 字体大写样式
                'FontBaseline': 0,  # 字体基线
                'Underline': False,  # 是否下划线
                'Strikethrough': False,  # 是否删除线
                'Ligatures': True,  # 是否启用连字
                'DLigatures': False,  # 是否禁用某些连字
                'BaselineDirection': 2,  # 基线方向（2: 垂直）
                'Tsume': 0.0,  # 字符紧缩度
                'StyleRunAlignment': 2,  # 样式对齐方式
                'Language': 0,  # 语言
                'NoBreak': False,  # 是否禁用换行
                'FillColor': {  # 填充颜色
                    'Type': 1,  # 颜色类型
                    'Values': [1.0, 0.0, 0.0, 0.0]  # 颜色值（RGBA）
                },
                'StrokeColor': {  # 描边颜色
                    'Type': 1,  # 颜色类型
                    'Values': [1.0, 0.0, 0.0, 0.0]  # 颜色值（RGBA）
                },
                'FillFlag': True,  # 是否启用填充
                'StrokeFlag': False,  # 是否启用描边
                'FillFirst': True,  # 是否优先填充
                'YUnderline': 1,  # 下划线类型
                'OutlineWidth': 1.0,  # 描边宽度
                'CharacterDirection': 0,  # 字符方向
                'HindiNumbers': False,  # 是否使用印地数字
                'Kashida': 1,  # 阿拉伯文本填充比例
                'DiacriticPos': 2  # 阿拉伯重音符位置
            }
        }],
        'FontSet': [
            {  # 字体集合
                'Name': 'MicrosoftYaHei',  # 字体名称
                'Script': 3,  # 字体脚本类型（3: 简体中文）
                'FontType': 1,  # 字体类型（1: TrueType字体）
                'Synthetic': 0  # 是否为合成字体
            },
            {
                'Name': 'AdobeInvisFont',  # 字体名称
                'Script': 0,  # 脚本类型（0: 通用）
                'FontType': 0,  # 字体类型
                'Synthetic': 0  # 是否为合成字体
            },
            {
                'Name': 'SimSun',  # 字体名称
                'Script': 3,  # 脚本类型（简体中文）
                'FontType': 1,  # 字体类型
                'Synthetic': 0  # 是否为合成字体
            }
        ],
        'SuperscriptSize':
        0.583,  # 上标字体大小比例
        'SuperscriptPosition':
        0.333,  # 上标位置
        'SubscriptSize':
        0.583,  # 下标字体大小比例
        'SubscriptPosition':
        0.333,  # 下标位置
        'SmallCapSize':
        0.7  # 小型大写字母大小比例
    }
}
