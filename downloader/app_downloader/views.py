from dateutil.relativedelta import relativedelta
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from .utils import *
from .models import DbDownload
from .serializers import DocumentSerializer
import sqlite3
import os


# ViewSets define the view behavior.
class DocumentViewSet(ModelViewSet):
    queryset = DbDownload.objects.all()
    serializer_class = DocumentSerializer

    @action(methods=['get'], detail=False)
    def get(self, request):
        # loading in modules

        # creating file path
        cwd = os.getcwd()
        dbfile = cwd + "\\YERMAK_T2.sqlite"
        # Create a SQL connection to our SQLite database
        con = sqlite3.connect(dbfile)

        # creating cursor
        cur = con.cursor()

        # reading all table names
        table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
        # here is you table list
        print(len(table_list))

        # Be sure to close the connection
        con.close()
        json_array = json.dumps(table_list)
        return Response({json_array})

    @action(methods=['post'], detail=False)
    def post(self, request):
        data = request.data
        row_for_check_ip = DbDownload.objects.filter(ip=data['ip'])
        print(row_for_check_ip)
        print(row_for_check_ip.exists())
        if row_for_check_ip.exists():
            row_for_check_ip = row_for_check_ip.last()
            delta = relativedelta(now(), row_for_check_ip.time_create)
            if delta.minutes >= 30:
                return Response({'post': main_unpacker(data)})

            else:
                return Response({'post': 'Превышен лимит допустимых загрузок (2 загрузки в 1 час)'})
        else:
            return Response({'post': main_unpacker(data)})
