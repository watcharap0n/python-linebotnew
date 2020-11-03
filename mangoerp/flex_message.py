from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage,
                            ImagemapSendMessage,
                            BaseSize, URIImagemapAction, ImagemapArea, QuickReply, QuickReplyButton, MessageAction)


def flex_erp():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2020/10/15/bWGj1R.md.png",
                "size": "full",
                "aspectRatio": "3:5",
                "aspectMode": "cover"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "uri": "https://liff.line.me/1655104822-8nMB6y2m",
                            "label": "ขอใบเสนอราคา"
                        }
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_test


def flex_product():
    flex_message = FlexSendMessage(
        alt_text='Product Mango',
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://sv1.picz.in.th/images/2020/10/08/OLdApf.png",
                        "size": "full"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ราคามีทั้งแบบซื้อและแบบเช่ารายเดือน",
                                "size": "md",
                                "color": "#ffffff",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "ขึ้นอยู่กับ Package และจำนวน User ที่ต้องการ",
                                "size": "xs",
                                "color": "#ffffff",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "ใช้งาน โดยราคาเริ่มตั้งแต่หลักหมื่น",
                                "size": "xs",
                                "color": "#ffffff",
                                "weight": "bold"
                            }
                        ],
                        "backgroundColor": "#008891"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ข้อมูลเพิ่มเติม",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-construction-2"
                                        }
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "backgroundColor": "#008891",
                                "spacing": "sm",
                                "height": "35px",
                                "borderWidth": "1px",
                                "borderColor": "#ffffff",
                                "flex": 0,
                                "cornerRadius": "4px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ขอใบเสนอราคา",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://liff.line.me/1655104822-k5dRGJez"
                                        }
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "backgroundColor": "#008891",
                                "spacing": "sm",
                                "height": "35px",
                                "borderWidth": "1px",
                                "borderColor": "#ffffff",
                                "flex": 0,
                                "cornerRadius": "4px",
                                "margin": "md"
                            }
                        ],
                        "backgroundColor": "#008891"
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://sv1.picz.in.th/images/2020/10/08/OLSzAy.png",
                        "size": "full"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ราคามีทั้งแบบซื้อและแบบเช่ารายเดือน",
                                "size": "md",
                                "color": "#ffffff",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "ขึ้นอยู่กับ Package และจำนวน User ที่ต้องการ",
                                "size": "xs",
                                "color": "#ffffff",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "ใช้งาน โดยราคาเริ่มตั้งแต่หลักหมื่น",
                                "size": "xs",
                                "weight": "bold",
                                "color": "#ffffff"
                            }
                        ],
                        "backgroundColor": "#008891"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ข้อมูลเพิ่มเติม",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-real-estate"
                                        }
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "backgroundColor": "#008891",
                                "spacing": "sm",
                                "height": "35px",
                                "borderWidth": "1px",
                                "borderColor": "#ffffff",
                                "cornerRadius": "4px",
                                "flex": 0
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ขอใบเสนอราคา",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0,
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://liff.line.me/1655104822-EKonO759"
                                                }
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://liff.line.me/1655104822-EKonO759"
                                        }
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "backgroundColor": "#008891",
                                "spacing": "sm",
                                "height": "35px",
                                "borderWidth": "1px",
                                "borderColor": "#ffffff",
                                "flex": 0,
                                "cornerRadius": "4px",
                                "margin": "md"
                            }
                        ],
                        "backgroundColor": "#008891"
                    }
                }
            ]
        })
    return flex_message


def flex_newfeature():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/f8dcb3d1e771e2dd48e64fa323c92164.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ราคามีทั้งแบบซื้อและแบบเช่า",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ขึ้นอยู่กับ Package และจำนวน User ที่ต้องการใช้งาน ราคาเริ่มตั้งแต่หลักหมื่น",
                                        "wrap": True,
                                        "weight": "regular",
                                        "size": "md",
                                        "flex": 0
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/project-planning"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "ขอใบเสนอราคา",
                                    "uri": "https://liff.line.me/1655104822-RnJlag2z"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/e1c5a9b7319796787b43b7333561cabc.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เหมาะสำหรับบริษัทฯ ที่ใช้ ERP Mango Anywhere",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "flex": 1,
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ราคาเริ่มตั้งแต่หลักหมื่น",
                                        "wrap": True,
                                        "weight": "regular",
                                        "size": "md",
                                        "flex": 0
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "flex": 2,
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/customer-service-management"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "ขอใบเสนอราคา",
                                    "data": "CSM"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/dd6a3a653ad96b804d5649a0d14f73e0.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เหมาะสำหรับบริษัทฯ ที่ใช้ ERP Mango Anywhere",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ราคาเริ่มตั้งแต่หลักหมื่น",
                                        "wrap": True,
                                        "weight": "regular",
                                        "size": "md",
                                        "flex": 0
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/news-knowledge/news/310-mango-erp-%E0%B9%80%E0%B8%9B%E0%B8%B4%E0%B8%94%E0%B8%95%E0%B8%B1%E0%B8%A7-feature-%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%87-%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%AA%E0%B8%B1%E0%B8%A1%E0%B8%A1%E0%B8%99%E0%B8%B2-%E2%80%9C%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-4%E2%80%9D"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "ขอใบเสนอราคา",
                                    "data": "QCM"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                }
            ]
        }
    )
    return flex_test


def flex_optional():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/7868315fea8b0cfc522bb760b0a89fc6.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "none",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เหมาะสำหรับบริษัทฯ ที่ใช้ ERP Mango Anywhere",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": []
                            }
                        ],
                        "margin": "none"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/products/optional/maintenance"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "ขอใบเสนอราคา",
                                    "data": "maintenance"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/50824e4f26e504ab1d3f3df65226369f.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เหมาะสำหรับบริษัทฯ ที่ใช้ ERP Mango Anywhere",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "flex": 2,
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/products/optional/rt-rental-mango"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "ขอใบเสนอราคา",
                                    "data": "rental"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "15:15",
                        "aspectMode": "cover",
                        "url": "https://www.img.in.th/images/36f2413e01c9533414e4f9fc910b2187.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เหมาะสำหรับบริษัทฯ ที่ใช้ ERP Mango Anywhere",
                                "wrap": True,
                                "weight": "bold",
                                "size": "lg",
                                "color": "#49B42D"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "รายละเอียดเพิ่มเติม",
                                    "uri": "https://www.mangoconsultant.com/th/products/optional/mrp-material-requirement-planning"
                                },
                                "style": "secondary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "ขอใบเสนอราคา",
                                    "data": "mrp"
                                },
                                "style": "primary"
                            }
                        ]
                    }
                }
            ]
        })
    return flex_test


def flex_bus():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://www.img.in.th/images/7471075939c62cfc41dfb3e50b599e3b.jpg",
                "size": "full",
                "aspectRatio": "23:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "BUSINESS CONSULTANT",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "text",
                        "text": "มีความเชี่ยวชาญระดับมืออาชีพพร้อมด้วย",
                        "decoration": "none",
                        "size": "sm",
                        "contents": [
                            {
                                "type": "span",
                                "text": "มีความเชี่ยวชาญระดับมืออาชีพพร้อมด้วย",
                                "size": "sm"
                            }
                        ],
                        "align": "start",
                        "margin": "sm"
                    },
                    {
                        "type": "text",
                        "contents": [
                            {
                                "type": "span",
                                "text": "ทีมงานผู้เชี่ยวชาญเฉพาะด้าน",
                                "size": "sm"
                            }
                        ],
                        "position": "relative",
                        "align": "start"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "uri",
                            "label": "CONSULTING",
                            "uri": "https://www.mangoconsultant.com/th/%E0%B8%A0%E0%B8%B9%E0%B8%AA%E0%B8%B4%E0%B8%97%E0%B8%98%E0%B8%B4%E0%B9%8C"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "TRAINING SERVICE",
                            "uri": "https://www.mangoconsultant.com/th/services/training-service"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "POWER BI",
                            "uri": "https://liff.line.me/1655104822-pR0REwNV"
                        }
                    },
                    {
                        "type": "spacer"
                    }
                ],
                "flex": 0
            }
        })
    return flex_test


def flex_destiny():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันอาทิตย์",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#FF4444"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ใช้เงินในการลงทุนเปิดธุรกิจใหม่",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "เกิดปัญหาด้านการเงิน",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ได้พบคนผิวสองสี มีเสน่ห์",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- ปลูกต้นใบเงินใบทองแล้วจะโชคดี",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  อำพัน",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล น้ำเงิน",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันจันทร์",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#FFDE00"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "เปลี่ยนงานใหม่จะประสบความสำเร็จ",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "มีเรื่องต้องจ่ายออกไปอย่างรวดเร็ว",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "กำลังเริ่มต้นความรักครั้งใหม่",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- ทำบุญเติมน้ำมันตะเกียงแล้วจะโชคดี",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  เทราเฮิร์ต",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล เทา",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันอังคาร",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#FF77D2"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ทำธุรกิจการค้าก็จะเป็นเงินเป็นทอง",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "มีโอกาสได้โชคแบบทุกข์ลาภ",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "มีโอกาสพบคนผิวสองสี",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- บูชาพระพิฆเนศแล้วจะโชคดี",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  เรดแจสเปอร์",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล แดง",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันพุธ",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#28FAA6"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ทำธุรกิจด้านขนส่งได้รับผลกำไรดี",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "หาเงินเก่งทันใช้จ่าย",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ได้พบรักโดยฉับพลัน",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- การทำบุญรักษาศีล5จะได้บุญมาก",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  โอปอล",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล เขียวอ่อน",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันพฤหัสบดี",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#FCA12A"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "นำบ้านเก่ามาปรับปรุงขายได้กำไรงาม",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "มีโชคจะได้รับเงินก้อนใหญ่",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "มีโอกาสพบรักแรกพบ",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- เดินทางท่องเที่ยวไหว้พระธาตุดอยสุเทพ",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  มรกต",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล เขียว",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันศุกร์",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#28D0FA"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ทำธุรกิจแบบฉายเดี่ยวจะดีที่สุด",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "การให้คนอื่นยืมเงินแล้วจะไม่ได้คืน ",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "พบความสัมพันธ์ที่มีความสุข",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- บูชาองค์พระพรหมแล้วจะโชคดี",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  โกเมน",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล ส้ม",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                },
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "วันเสาร์",
                                "weight": "bold",
                                "size": "xl",
                                "margin": "md",
                                "color": "#DB38FC"
                            },
                            {
                                "type": "text",
                                "text": "เช็คดวงประจำรายเดือน ตุลาคม 2563",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การงาน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ระวังขาดทุนเรื่องการค้า",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเงิน",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ซื้อของใหม่แทนของเก่าที่ชำรุด",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ความรัก",
                                                "size": "sm",
                                                "color": "#111111",
                                                "flex": 0,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "เกิดความสุขในชีวิตรัก",
                                                "size": "sm",
                                                "color": "#555555",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "เคล็ดลับการเสริมดวง",
                                        "margin": "xl",
                                        "color": "#111111",
                                        "size": "md",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- บูชาพระสิวลีแล้วจะรุ่งเรือง",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- อัญมณีมงคล  พลอยสีฟ้า",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "- สีมงคล น้ำเงิน",
                                                "margin": "none",
                                                "size": "sm"
                                            }
                                        ],
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "https://www.sanook.com/horoscope/",
                                        "color": "#aaaaaa",
                                        "size": "xs",
                                        "align": "start"
                                    }
                                ]
                            }
                        ]
                    },
                    "styles": {
                        "footer": {
                            "separator": True
                        }
                    }
                }
            ]
        })
    return flex_test


def flex_profile(imageurl, profile):
    flex_message = FlexSendMessage(
        alt_text='Product Mango',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": f"{imageurl}",
                                        "aspectMode": "cover",
                                        "size": "full"
                                    }
                                ],
                                "cornerRadius": "100px",
                                "width": "72px",
                                "height": "72px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": "สวัสดี",
                                                "weight": "bold",
                                                "color": "#000000",
                                                "size": "md"
                                            },
                                            {
                                                "type": "span",
                                                "text": "!",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "span",
                                                "text": f" {profile}",
                                                "color": "#60F7BB",
                                                "weight": "bold",
                                                "size": "md"
                                            }
                                        ],
                                        "size": "sm",
                                        "wrap": True
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "เลือกรายการ",
                                                "size": "md"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "margin": "md"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "text": "ขอข้อมูลผลิตภัณฑ์",
                                            "label": "ขอข้อมูลผลิตภัณฑ์"
                                        },
                                        "style": "primary"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ขอใบเสนอราคาทำยังไง",
                                            "text": "ขอใบเสนอราคาทำอย่างไร"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ลูกค้าที่ใช้งานโปรแกรม",
                                            "text": "ลูกค้าที่ใช้งานโปรแกรม"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ราคาโปรแกรม",
                                            "text": "hello"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ติดปัญหาการใช้งาน",
                                            "text": "ติดปัญหาการใช้งาน"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ติดต่ออบรมประจำเดือน",
                                            "text": "ติดต่ออบรมประจำเดือน"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ติดต่อขอฝึกงาน",
                                            "text": "ติดต่อขอฝึกงาน"
                                        },
                                        "style": "primary",
                                        "margin": "sm"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "https://www.mangoconsultant.com",
                        "color": "#bcbcbc",
                        "size": "xxs"
                    }
                ]
            }
        }
    )
    return flex_message


def flex_pF(image_url, displayName, firstname, email, company, tel, product, comment):
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": f"{image_url}",
                                        "aspectMode": "cover",
                                        "size": "full"
                                    }
                                ],
                                "cornerRadius": "100px",
                                "width": "72px",
                                "height": "72px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": "สวัสดี",
                                                "weight": "bold",
                                                "color": "#000000",
                                                "size": "md"
                                            },
                                            {
                                                "type": "span",
                                                "text": "!",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "span",
                                                "text": f" {displayName}",
                                                "color": "#60F7BB",
                                                "weight": "bold",
                                                "size": "md"
                                            }
                                        ],
                                        "size": "sm",
                                        "wrap": True
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ข้อมูลติดต่อ",
                                                "size": "md",
                                                "color": "#bcbcbc"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "margin": "md"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"ชื่อ : {firstname}"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"อีเมล : {email}"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"บริษัท : {company}"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"เบอร์ติดต่อ : {tel}"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"ผลิตภัณฑ์ : {product}"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": "ข้อมูลเพิ่มเติม : "
                                            }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "text": "hello, world",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": f"{comment}"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "www.mangoconsultant.com",
                        "color": "#bcbcbc",
                        "size": "xxs"
                    }
                ]
            }
        })
    return flex_test


def flex_profile_erp(image_url, displayName, status):
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": f"{image_url}",
                                        "aspectMode": "cover",
                                        "size": "full"
                                    }
                                ],
                                "cornerRadius": "100px",
                                "width": "72px",
                                "height": "72px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "contents": [
                                            {
                                                "type": "span",
                                                "text": "สวัสดี",
                                                "weight": "bold",
                                                "color": "#000000",
                                                "size": "md"
                                            },
                                            {
                                                "type": "span",
                                                "text": "!",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "span",
                                                "text": f" {displayName}",
                                                "color": "#60F7BB",
                                                "weight": "bold",
                                                "size": "md"
                                            }
                                        ],
                                        "size": "sm",
                                        "wrap": True
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": f"{status}",
                                                "size": "sm",
                                                "color": "#bcbcbc"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "margin": "md"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2020/10/23/bhN7RD.png",
                                        "aspectMode": "fit",
                                        "size": "full",
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "@ERPSoftware"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "Software ERP",
                                        "align": "center",
                                        "size": "xxs"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2020/10/23/bhNS69.png",
                                        "aspectMode": "fit",
                                        "size": "full",
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "@Business"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "Business Consultant",
                                        "align": "center",
                                        "size": "xxs"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2020/10/23/bhN41b.png",
                                        "aspectMode": "fit",
                                        "size": "full",
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "@NewFeature"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "New Feature",
                                        "size": "xxs",
                                        "align": "center"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2020/10/23/bhNhkq.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "@Optional"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "Optional",
                                        "size": "xxs",
                                        "align": "center"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://sv1.picz.in.th/images/2020/10/23/bhNBLa.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://liff.line.me/1655104822-OmWMl8NA"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "Application",
                                        "size": "xxs",
                                        "align": "center"
                                    }
                                ]
                            }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "https://www.mangoconsultant.com",
                        "color": "#bcbcbc",
                        "size": "xxs"
                    }
                ]
            }
        })
    return flex_test
