# -*- coding: utf-8 -*-

import grokcore.component as grok

from dolmen import menu
from dolmen.app.layout import Page
from dolmen.app.viewselector import SelectableViewsMenu
from menhir.contenttype import image, photoalbum
from zope.component import getUtility
from zope.intid.interfaces import IIntIds

from menhir.contenttype.photoalbum import MCPMessageFactory as _

@menu.menuentry(SelectableViewsMenu)
class Animated(Page):
    grok.name('gallery_view')
    grok.title(_('label_animatedgallery', default=u"Animated gallery"))
    grok.context(photoalbum.IPhotoAlbum)
    
    def update(self):
        photoalbum.animated_gallery.need()
        self.url = str(self.request.URL)
        self.contents = self.context.values()


@menu.menuentry(SelectableViewsMenu)
class Simple(Page):
    grok.name('thumbnails_view')
    grok.title(_('label_simplegallery', default=u"Simple gallery"))
    grok.context(photoalbum.IPhotoAlbum)
    
    def update(self):
        image.ImagePopup.need()
        photoalbum.gallery_css.need()
        self.contents = self.context.values()
        self.uid = getUtility(IIntIds).queryId(self.context)
