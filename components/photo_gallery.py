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
                "img_style": {"height": "500px"},# {"width":"500px","height":"500px"},
                # "imgClassName": "",
            } for i, photo in enumerate(self.photos)],
            
            variant="dark",
        )
        return carousel