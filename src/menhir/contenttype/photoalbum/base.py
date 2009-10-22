#!/usr/bin/python
# -*- coding: utf-8 -*-

import dolmen.content as content
from zope.interface import implements
from zope.app.container.constraints import contains
from menhir.contenttype.image import IImage
from dolmen.app.viewselector import IViewSelector


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
