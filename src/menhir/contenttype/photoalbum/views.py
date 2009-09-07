# -*- coding: utf-8 -*-

import grok
import zope.app.intid
import megrok.resourcelibrary
from zope.component import getUtility
from dolmen.app.layout import View
from menhir.library.jquery import JQueryBase
from menhir.contenttype.image import ImagePopup
from menhir.contenttype.photoalbum import IPhotoAlbum


class AnimatedGallery(megrok.resourcelibrary.ResourceLibrary):
    grok.name("menhir.contenttype.photoalbum.animated")
    megrok.resourcelibrary.depend(JQueryBase)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('jquery.galleriffic.min.js')
    megrok.resourcelibrary.include('gallery.js')
    megrok.resourcelibrary.include('gallery.css')


class SimpleGallery(megrok.resourcelibrary.ResourceLibrary):
    grok.name("menhir.contenttype.photoalbum.simple")
    megrok.resourcelibrary.depend(ImagePopup)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('gallery.css')


class Animated(View):
    grok.context(IPhotoAlbum)
    grok.name('gallery_view')
    grok.title('Animated gallery')
    
    def update(self):
        AnimatedGallery.need()
        self.url = str(self.request.URL)
        self.contents = self.context.values()


class Simple(View):
    grok.context(IPhotoAlbum)
    grok.name('thumbnails_view')
    grok.title('Simple gallery')
    
    def update(self):
        SimpleGallery.need()
        self.contents = self.context.values()
        self.uid = getUtility(zope.app.intid.IIntIds).queryId(self.context)
