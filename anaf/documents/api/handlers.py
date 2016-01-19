# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement

__all__ = ['FolderHandler', 'FileHandler', 'DocumentHandler',
           'WebLinkHandler']

from anaf.core.api.handlers import ObjectHandler, getOrNone
from anaf.documents.models import Document, Folder, File, WebLink
from anaf.documents.forms import FolderForm, DocumentForm, FileForm, WebLinkForm


class FolderHandler(ObjectHandler):
    """Entrypoint for Folder model."""
    model = Folder
    form = FolderForm

    @classmethod
    def resource_uri(cls, obj=None):
        object_id = "id"
        if obj is not None:
            object_id = obj.id
        return ('api_documents_folders', [object_id])

    def flatten_dict(self, request):
        dct = super(FolderHandler, self).flatten_dict(request)
        dct["folder_id"] = None
        return dct


class CommonHandler(ObjectHandler):
    def check_create_permission(self, request, mode):
        if 'folder' in request.data:
            folder = getOrNone(Folder, pk=request.data['folder'])
            if not request.user.profile.has_permission(folder, mode='x'):
                request.data['folder'] = None
        return True

    def flatten_dict(self, request):
        dct = super(CommonHandler, self).flatten_dict(request)
        dct["folder_id"] = None
        return dct


class FileHandler(CommonHandler):
    "Entrypoint for File model."
    model = File
    form = FileForm

    @classmethod
    def resource_uri(cls, obj=None):
        object_id = "id"
        if obj is not None:
            object_id = obj.id
        return ('api_documents_files', [object_id])


class DocumentHandler(CommonHandler):
    "Entrypoint for Document model."
    model = Document
    form = DocumentForm

    @classmethod
    def resource_uri(cls, obj=None):
        object_id = "id"
        if obj is not None:
            object_id = obj.id
        return ('api_documents_documents', [object_id])


class WebLinkHandler(CommonHandler):
    "Entrypoint for WebLink model."
    model = WebLink
    form = WebLinkForm

    @classmethod
    def resource_uri(cls, obj=None):
        object_id = "id"
        if obj is not None:
            object_id = obj.id
        return ('api_documents_weblinks', [object_id])
