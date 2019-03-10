from django.shortcuts import redirect
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from beer import serializers
from beer.models import Beer
from beer.tasks import add_beer_image_task


class BeerUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BeerSerializer
    template_name = 'beer_form.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return Beer.objects.all()

    def get(self, *args, **kwargs):
        return Response()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        return redirect(reverse('beer:list'))

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return redirect(reverse('beer:list', request=request))


class BeerListView(generics.CreateAPIView):
    serializer_class = serializers.BeerSerializer
    template_name = 'beer_list.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return Beer.objects.all()

    def get(self, *args, **kwargs):
        return Response({'beers': self.get_queryset()})


class BeerCreateView(generics.CreateAPIView):
    template_name = 'beer_form.html'
    serializer_class = serializers.BeerSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, *args, **kwargs):
        return Response({})

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            add_beer_image_task.delay(serializer.instance.pk)

        return redirect(reverse('beer:list'))
