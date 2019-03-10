from tempfile import TemporaryFile
import random
import requests

from beer.models import Beer


__all__ = ['add_beer_image']

image_urls = [
    'https://static.boredpanda.com/blog/wp-content/uploads/2018/04/5acb63d83493f__700-png.jpg',
    'https://images-production.freetls.fastly.net/uploads/posts/off_site_promo_image/166842/why-do-cats-meow.jpg',
    'http://honesttopaws.com/wp-content/uploads/sites/5/2017/05/banana-cat-1.png',
]


def add_beer_image(beer_id):
    try:
        beer = Beer.objects.get(pk=beer_id)
    except Beer.DoesNotExist:
        return

    url = random.choice(image_urls)

    image_content = _download_image(url)

    with TemporaryFile() as f:
        f.write(image_content)
        beer.image = f

    beer.save()


def _download_image(url):
    response = requests.get(url)
    return response.content
