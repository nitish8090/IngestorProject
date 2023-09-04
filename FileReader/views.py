
import logging
from rest_framework import viewsets

from FileReader.models import HotFile
from FileReader.serializers import HotFileSerializer

logger = logging.getLogger('file-reader')

class HotFileViewSet(viewsets.ModelViewSet):

    serializer_class = HotFileSerializer
    queryset = HotFile.objects.all()

    def list(self, request, *args, **kwargs):
        logger.info("List Hol files called.")
        return super().list(request, *args, **kwargs)