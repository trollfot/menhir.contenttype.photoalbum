from zope.i18nmessageid import MessageFactory

MCPMessageFactory = MessageFactory('menhir.contenttype.photoalbum')

from menhir.contenttype.photoalbum.album import IPhotoAlbum, PhotoAlbum
from menhir.contenttype.photoalbum.libraries import (
    gallery_css, galleriffic, animated_gallery)
