#!/usr/bin/python
# -*- coding: utf-8 -*-

import dolmen.content as content
from menhir.contenttype.image import IImage
from dolmen.app.content import IDynamicLayout
from zope.interface import implements
from zope.app.container.constraints import contains


class IPhotoAlbum(IDynamicLayout):
    """Defines a folder that can only contain IImage providing objects.
    """
    contains(IImage)


class PhotoAlbum(content.Container):
    """A folder that contains images.
    """
    content.name(u"Photo album")
    content.icon("resources/album.png")
    
    implements(IPhotoAlbum)
    layout = u"thumbnails_view"
