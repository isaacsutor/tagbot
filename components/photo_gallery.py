import dash_bootstrap_components as dbc
from typing import List

class PhotoGalleryComponent:
    def __init__(self, photos: List):
        self.photos = photos
    def get_component(self):
        carousel = dbc.Carousel(
            items=[{
                "key": str(i),
                "src": photo,
                "header": 'With header',
                "caption": "and caption",
                "img_style": {"max-height": "500px"}# , "max-width": "75vh"},# {"width":"500px","height":"500px"},
                # "imgClassName": "",
            } for i, photo in enumerate(self.photos)],
            variant="dark",
        )
        full_car = dbc.Row([dbc.Col([
            carousel
        ], width=8)], justify="center")
        return full_car
