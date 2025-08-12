from typing import Optional
from ninja import Router, Schema
from django.core.files.storage import default_storage
import json



router = Router()


class FileOut(Schema):
    filename: str

@router.get('/files/', response=dict[str,list[FileOut]])
def list_files(request):    
    directories, files = default_storage.listdir('/')

    return {'directories': [FileOut(filename=d) for d in directories], 
            'files': [FileOut(filename=f) for f in files]}

