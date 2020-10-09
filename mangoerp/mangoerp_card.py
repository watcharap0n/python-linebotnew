from linebot.models import (ImagemapSendMessage, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction,
                            TemplateSendMessage, PostbackAction, MessageAction, URIAction, ButtonsTemplate, CarouselColumn, CarouselTemplate)


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
                text='@Construction',
                area=ImagemapArea(
                    x=34, y=300, width=1020, height=390
                )
            ),
            MessageImagemapAction(
                text='@Construction',
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

