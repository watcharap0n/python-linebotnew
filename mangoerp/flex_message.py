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
    alt_text='erpshow',
    contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.mangoconsultant.com/images/Kukkai/content001122018/800x800_003122018.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Mango Consultant",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "ยินดีให้บริการ",
                "wrap": True,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              }
            ]
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ทักทาย",
              "text": "สวัสดี"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Mango ERP คืออะไร",
              "text": "Mango ERP"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ที่อยู่บริษัท",
              "text": "ตำแหน่งที่อยู่"
            },
            "style": "secondary"
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
              "type": "message",
              "label": "ขอใบเสนอราคา",
              "text": "@quote"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.mangoconsultant.com/images/Kukkai/content001122018/800x800_005122018.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Mango ERP",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ขอนัด DEMO",
              "text": "ขอdemo"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Mango Consultant",
              "uri": "https://www.mangoconsultant.com"
            },
            "style": "secondary"
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
            "style": "primary",
            "color": "#FF0000",
            "action": {
              "type": "datetimepicker",
              "label": "Datetime",
              "data": "hello",
              "mode": "date"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 1,
            "gravity": "center",
            "action": {
              "type": "postback",
              "label": "More",
              "data": "more"
            }
          }
        ]
      }
    }
  ]
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
    "url": "https://www.mangoconsultant.com/images/Kukkai/mango_bohktor/smes.R1-2.png",
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
