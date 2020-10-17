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
    "aspectMode": "cover",
    "position": "relative",
    "aspectRatio": "3:5"
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
