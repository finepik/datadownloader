import os
import shutil
import tempfile
import zipfile
from dateutil.relativedelta import relativedelta
from django.core.files import File
from django.db.models import FileField
from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import DbDownload
from .serializers import DocumentSerializer
import sqlite3
def main_unpacker(data):
    zip = zipfile.ZipFile(data['file'])
    files_in_zip = zip.namelist()
    if (len(files_in_zip) > 0):
        file_in_zip_name = files_in_zip[0]
        data['file_name'] = file_in_zip_name
        set = DbDownload.objects.filter(file_name=file_in_zip_name).order_by('version')
        if set.count() > 0:
            data['version'] = set.last().version + 1
        else:
            data['version'] = 1
        # исправить на 3
        split_name, split_extention = os.path.splitext(data['file_name'])
        new_file_name = split_name + '-Version-' + str(data['version']) + split_extention

        f = zip.open(file_in_zip_name)
        content = f.read()
        final_f = open('documents/unpack/' + new_file_name, 'wb')
        final_f.write(content)
        final_f.close()

        serializer = DocumentSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return 'success'
    return 'error - archive is empty'