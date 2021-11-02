from typing import Optional


class Item:
    def __init__(self,
        title: str,
        price: int,
        image_urls: Optional[list[str]]=None,
    ):
        self.title = title
        self.price = price
        self.image_urls = image_urls or []
