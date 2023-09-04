from rest_framework import viewsets
from rest_framework.response import Response

import pystac
from pystac import Catalog, get_stac_version


class StacViewSet(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):

        catalog = Catalog.from_file("./example-catalog/catalog.json")
        return Response(f"Stac App: {catalog.title}")

    def retrieve(self, request, *args, **kwargs):
        catalog = Catalog(
            id='tutorial-catalog',
            description='This catalog is a basic demonstration catalog utilizing a scene from SpaceNet 5.')
        catalog.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)
        return Response(f"Stac Created: {catalog.title}")
