from linebot.models import (ImagemapSendMessage, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction,
                            TemplateSendMessage, PostbackAction, MessageAction, URIAction, ButtonsTemplate, CarouselColumn, CarouselTemplate,
                            CameraAction, CameraRollAction, DatetimePickerAction, LocationAction, ImageCarouselColumn, ImageCarouselTemplate)


def mangoerp():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/10/08/OJlDee.jpg',
        alt_text='imagemap',
        base_size=BaseSize(height=1920, width=1020),
        actions=[
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-construction-2',
                area=ImagemapArea(
                    x=34, y=300, width=1020, height=390
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-real-estate',
                area=ImagemapArea(
                    x=34, y=650, width=1020, height=500
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/customer-service-management',
                area=ImagemapArea(
                    x=34, y=1000, width=1020, height=390
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/project-planning',
                area=ImagemapArea(
                    x=34, y=1260, width=1020, height=390
                )
            ),
        ])
    return imagemap_message


def product_action():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/10/08/OJlDee.jpg',
        alt_text='Product',
        base_size=BaseSize(height=1920, width=1020),
        actions=[
            MessageImagemapAction(
                text='@ERPSoftware',
                area=ImagemapArea(
                    x=34, y=300, width=1020, height=390
                )
            ),
            MessageImagemapAction(
                text='@ERPSoftware',
                area=ImagemapArea(
                    x=34, y=650, width=1020, height=500
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/customer-service-management',
                area=ImagemapArea(
                    x=34, y=1000, width=1020, height=390
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/project-planning',
                area=ImagemapArea(
                    x=34, y=1260, width=1020, height=390
                )
            ),
        ])
    return imagemap_message


def product_buttons():
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://sv1.picz.in.th/images/2020/10/08/OJlDee.jpg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackAction(
                            label='postback1',
                            display_text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
                        URIAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://sv1.picz.in.th/images/2020/10/08/OJlDee.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackAction(
                            label='postback2',
                            display_text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageAction(
                            label='message2',
                            text='message text2'
                        ),
                        URIAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template_message


def productR4():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/10/22/bflT71.jpg',
        alt_text='imagemap',
        base_size=BaseSize(height=1600, width=1040),
        actions=[
            MessageImagemapAction(
                text='@ERPSoftware',
                area=ImagemapArea(
                    x=350, y=248, width=1037, height=400
                )
            ),
            MessageImagemapAction(
                text='@NewFeature',
                area=ImagemapArea(
                    x=49, y=1108, width=294, height=294
                )
            ),
            MessageImagemapAction(
                text='@Optional',
                area=ImagemapArea(
                    x=759, y=1148, width=280, height=280
                )
            ),
            URIImagemapAction(
                link_uri='https://liff.line.me/1655104822-OmWMl8NA',
                area=ImagemapArea(
                    x=164, y=1421, width=863, height=200
                )
            ),
            URIImagemapAction(
                link_uri='https://liff.line.me/1655104822-V86LlWPo',
                area=ImagemapArea(
                    x=366, y=1118, width=280, height=280
                )
            ),
            MessageImagemapAction(
                text='@Business',
                area=ImagemapArea(
                    x=511, y=720, width=400, height=400
                )
            )
        ])
    return imagemap_message


def productR7():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/10/22/bflw2D.jpg',
        alt_text='imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='@ERPSoftware',
                area=ImagemapArea(
                    x=134, y=169, width=240, height=300
                )
            ),
            MessageImagemapAction(
                text='@Business',
                area=ImagemapArea(
                    x=625, y=184, width=240, height=300
                )
            ),
            MessageImagemapAction(
                text='@NewFeature',
                area=ImagemapArea(
                    x=44, y=585, width=240, height=300
                )
            ),
            URIImagemapAction(
                link_uri='https://liff.line.me/1655104822-V86LlWPo',
                area=ImagemapArea(
                    x=369, y=591, width=240, height=300
                )
            ),
            MessageImagemapAction(
                text='@Optional',
                area=ImagemapArea(
                    x=730, y=581, width=240, height=300
                )
            ),
            URIImagemapAction(
                link_uri='https://liff.line.me/1655104822-OmWMl8NA',
                area=ImagemapArea(
                    x=301, y=940, width=748, height=180
                )
            ),
        ])
    return imagemap_message


def destiny():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/10/21/bNlb2V.png',
        alt_text='imagemap',
        base_size=BaseSize(height=884, width=1300),
        actions=[
            URIImagemapAction(
                link_uri='https://horoscope.sanook.com/play/tarot/',
                area=ImagemapArea(
                    x=11, y=181, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/7days/',
                area=ImagemapArea(
                    x=372, y=238, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/weekly/',
                area=ImagemapArea(
                    x=707, y=237, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/monthly/',
                area=ImagemapArea(
                    x=1048, y=229, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/yearly/',
                area=ImagemapArea(
                    x=32, y=513, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/zodiac/',
                area=ImagemapArea(
                    x=370, y=508, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/career/',
                area=ImagemapArea(
                    x=709, y=518, width=250, height=250
                )
            ),
            URIImagemapAction(
                link_uri='https://www.sanook.com/horoscope/myhoro/birthdaybyzodiac/',
                area=ImagemapArea(
                    x=1059, y=520, width=250, height=250
                )
            ),


        ])
    return imagemap_message


def promotion():
    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://sv1.picz.in.th/images/2020/11/01/biNgsP.jpg',
                    action=URIAction(
                        label='คลิก',
                        uri='https://liff.line.me/1655104822-8nMB6y2m'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://sv1.picz.in.th/images/2020/11/01/biNBsf.jpg',
                    action=URIAction(
                        label='คลิก',
                        uri='https://liff.line.me/1655104822-8nMB6y2m'
                    )
                )
            ]
        )
    )
    return image_carousel_template_message