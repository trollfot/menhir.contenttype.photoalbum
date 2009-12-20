# -*- coding: utf-8 -*-

import grok

from hurry import jquery
from megrok import resource

from dolmen.app.viewselector import AlternateView
from menhir.contenttype import photoalbum

from zope.component import getUtility
from zope.intid.interfaces import IIntIds


class Animated(AlternateView):
    grok.name('gallery_view')
    grok.title('Animated gallery')
    grok.context(photoalbum.IPhotoAlbum)
    resource.include(photoalbum.animated_gallery)
    
    def update(self):
        self.url = str(self.request.URL)
        self.contents = self.context.values()


class Simple(AlternateView):
    grok.name('thumbnails_view')
    grok.title('Simple gallery')
    grok.context(photoalbum.IPhotoAlbum)
    resource.include(photoalbum.simple_gallery)
    
    def update(self):
        self.contents = self.context.values()
        self.uid = getUtility(zope.intid.IIntIds).queryId(self.context)
