from rest_framework import serializers

from FileReader.models import HotFile


class HotFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotFile
        fields = '__all__'
