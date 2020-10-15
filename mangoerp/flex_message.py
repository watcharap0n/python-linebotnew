from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage,
                            ImagemapSendMessage,
                            BaseSize, URIImagemapAction, ImagemapArea, QuickReply, QuickReplyButton, MessageAction)


def flex_ans():
    flex_message = FlexSendMessage(
        alt_text='เลือกเลยจ้า',
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "size": "micro",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Question?",
                                "color": "#000000",
                                "align": "start",
                                "size": "md",
                                "gravity": "center"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "สวัสดี",
                                    "text": "ชื่ออะไร"
                                },
                                "color": "#000000"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ชื่ออะไร",
                                    "text": "ชื่ออะไร"
                                },
                                "color": "#000000"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ทำอะไรได้บ้าง",
                                    "text": "ทำอะไรได้บ้าง"
                                },
                                "color": "#000000"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "Mango ERP",
                                    "text": "mango ERP"
                                },
                                "color": "#000000"
                            }
                        ],
                        "backgroundColor": "#00FF00",
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Your choice",
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "styles": {
                        "footer": {
                            "separator": False
                        }
                    }
                },
                {
                    "type": "bubble",
                    "size": "micro",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Question?",
                                "color": "#ffffff",
                                "align": "start",
                                "size": "md",
                                "gravity": "center"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "การหักเงินอื่นๆ ผู้รับเหมา",
                                    "text": "การหักเงินอื่นๆ ผู้รับเหมา"
                                },
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ดูประวัติการเบิกผลงานผู้รับเหมา",
                                    "text": "ดูประวัติการเบิกผลงานผู้รับเหมา"
                                },
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "เบิกผลงานผู้รับเป็นเปอร์เซนต์",
                                    "text": "เบิกผลงานผู้รับเป็นเปอร์เซนต์"
                                },
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ที่อยู่บริษัท",
                                    "text": "ที่อยู่บริษัท"
                                },
                                "color": "#FFFFFF"
                            }
                        ],
                        "backgroundColor": "#FF6B6E",
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Your choice",
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "styles": {
                        "footer": {
                            "separator": False
                        }
                    }
                }
            ]
        }
    )
    return flex_message


def flex_erp():
    flex_test = FlexSendMessage(
        alt_text='Flex message',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2020/10/15/bWGj1R.md.png",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                },
                "position": "relative",
                "aspectRatio": "3:5"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Mango Anywhere",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "4.9",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "โปร",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": "เช่าสุดคุ้ม เหมาจ่ายรายปี แถมฟรี 2 ต่อ  ต่อที่ 1 ใช้บริการ ฟรี! 1 เดือน *จ่ายเพียง 11 เดือน ต่อที่ 2 รับส่วนลดค่า SetUp Master มูลค่า 50,000 บาท ",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "เงื่อนไข",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": "ชำระค่าบริการรายเดือนล่วงหน้า 11 เดือน (ไม่รวมภาษีมูลค่าเพิ่ม) แถมฟรี 1 เดือน ระยะสัญญา 12 เดือน ตามเงื่อนไขที่บริษัทกำหนด",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                ]
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
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ข้อมูลเพิ่มเติม",
                            "uri": "https://linecorp.com"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "ขอใบเสนอราคา",
                            "data": "quote"
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


def flex_msg():
    flex_message = FlexSendMessage(
        alt_text='hello',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://www.mangoconsultant.com",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                },
                "position": "relative"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Mango Anywhere",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "4.0",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "แนะนำตัว",
                                "weight": "bold",
                                "size": "md",
                                "margin": "none",
                                "decoration": "none",
                                "align": "start"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "สวัสดี",
                                    "text": "สวัสดี"
                                },
                                "height": "sm",
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ชื่ออะไร",
                                    "text": "ชื่ออะไร"
                                },
                                "height": "sm",
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "ทำอะไรได้บ้าง",
                                    "text": "ทำอะไรได้บ้าง"
                                },
                                "height": "sm",
                                "style": "primary"
                            }
                        ],
                        "action": {
                            "type": "message",
                            "label": "action",
                            "text": "hello"
                        }
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
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "Program ERP",
                            "text": "Program ERP คืออะไร"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "เบิกผลงานผู้รับเป็นเปอร์เซนต์ (%)",
                            "text": "เบิกผลงานผู้รับเป็นเปอร์เซนต์ (%)"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "datetimepicker",
                            "label": "Calendar",
                            "data": "hello",
                            "mode": "date"
                        },
                        "style": "secondary"
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                ],
                "flex": 0
            }
        })
    return flex_message


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
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ขอใบเสนอราคา",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0,
                                                "action": {
                                                    "type": "postback",
                                                    "label": "action",
                                                    "data": "quoteq"
                                                }
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm"
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
                                                "type": "icon",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "ขอใบเสนอราคา",
                                                "color": "#ffffff",
                                                "size": "lg",
                                                "flex": 0,
                                                "action": {
                                                    "type": "postback",
                                                    "label": "action",
                                                    "data": "quoteq"
                                                }
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm"
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
                                "margin": "md"
                            }
                        ],
                        "backgroundColor": "#008891"
                    }
                }
            ]
        })
    return flex_message
