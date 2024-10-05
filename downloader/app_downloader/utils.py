import os
import zipfile

from .models import DbDownload
from .serializers import DocumentSerializer


def main_unpacker(data):
    zip_data = zipfile.ZipFile(data['file'])
    files_in_zip = zip_data.namelist()
    if len(files_in_zip) > 0:
        file_in_zip_name = files_in_zip[0]
        data['file_name'] = file_in_zip_name
        set = DbDownload.objects.filter(file_name=file_in_zip_name).order_by('version')
        if set.count() > 0:
            data['version'] = set.last().version + 1
        else:
            data['version'] = 1
        split_name, split_extention = os.path.splitext(data['file_name'])
        new_file_name = split_name + '-Version-' + str(data['version']) + split_extention

        f = zip_data.open(file_in_zip_name)
        content = f.read()
        final_f = open('documents/unpack/' + new_file_name, 'wb')
        final_f.write(content)
        final_f.close()

        serializer = DocumentSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return 'success'
    return 'error - archive is empty'
