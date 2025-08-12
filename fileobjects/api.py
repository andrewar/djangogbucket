from typing import Optional
from ninja import Router, Schema, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from django.core.files.storage import default_storage
import json



router = Router()


class FileOut(Schema):
    filename: str

@router.get('/files/', response=dict[str,FileOut])
def list_files(request):    
    directories, files = default_storage.listdir('/')

    return {'directories': directories, 'files': files}

