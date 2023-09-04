from rest_framework import viewsets

from FileReader.models import HotFile
from FileReader.serializers import HotFileSerializer


class HotFileViewSet(viewsets.ModelViewSet):

    serializer_class = HotFileSerializer
    queryset = HotFile.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)