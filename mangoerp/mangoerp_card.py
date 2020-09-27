from linebot.models import (ImagemapSendMessage, BaseSize, URIImagemapAction, ImagemapArea)

def mangoerp():
    imagemap_message = ImagemapSendMessage(
        base_url='https://sv1.picz.in.th/images/2020/08/28/EyNVgv.png',
        alt_text='imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-construction-2',
                area=ImagemapArea(
                    x=34, y=149, width=970, height=170
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-real-estate',
                area=ImagemapArea(
                    x=34, y=325, width=970, height=170
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/customer-service-management',
                area=ImagemapArea(
                    x=34, y=501, width=970, height=170
                )
            ),
            URIImagemapAction(
                link_uri='https://www.mangoconsultant.com/th/project-planning',
                area=ImagemapArea(
                    x=34, y=678, width=970, height=170
                )
            ),

        ])
    return imagemap_message
