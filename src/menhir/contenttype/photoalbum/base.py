#!/usr/bin/python
# -*- coding: utf-8 -*-

import dolmen.content as content
from dolmen.app.viewselector import IViewSelector
from menhir.contenttype.image import IImage

from zope.interface import implements
from zope.container.constraints import contains


class IPhotoAlbum(IViewSelector):
    """Defines a folder that can only contain IImage providing objects.
    """
    contains(IImage)


class PhotoAlbum(content.OrderedContainer):
    """A folder that contains images.
    """
    content.name(u"Photo album")
    content.icon("resources/album.png")
    
    implements(IPhotoAlbum)
    selected_view = u"thumbnails_view"
