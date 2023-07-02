from rest_framework.serializers import ModelSerializer, FileField
from .models import *
# Serializers define the API representation.


class DocumentSerializer(ModelSerializer):

    class Meta:
        model = DbDownload
        fields = "__all__"