from pivo import celery_app
from beer.models import Beer
from beer.service.add_beer_image import add_beer_image
from celery import current_app


@celery_app.task()
def add_beer_image_task(beer_id):
    add_beer_image(beer_id)


current_app.register_task(add_beer_image_task)
