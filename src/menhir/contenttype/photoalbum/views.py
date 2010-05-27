# -*- coding: utf-8 -*-

import grokcore.component as grok

from dolmen.app.viewselector import AlternativeView
from menhir.contenttype import image, photoalbum

from zope.component import getUtility
from zope.intid.interfaces import IIntIds


class Animated(AlternativeView):
    grok.name('gallery_view')
    grok.title('Animated gallery')
    grok.context(photoalbum.IPhotoAlbum)
    
    def update(self):
        photoalbum.animated_gallery.need()
        self.url = str(self.request.URL)
        self.contents = self.context.values()


class Simple(AlternativeView):
    grok.name('thumbnails_view')
    grok.title('Simple gallery')
    grok.context(photoalbum.IPhotoAlbum)
    
    def update(self):
        image.ImagePopup.need()
        photoalbum.gallery_css.need()
        self.contents = self.context.values()
        self.uid = getUtility(IIntIds).queryId(self.context)
