# -*- coding: utf-8 -*-

from fanstatic import Resource, Library
from js.jquery import jquery


GalleryResources = Library("photoalbum.resources", 'resources')

gallery_css = Resource(
    GalleryResources, "gallery.css")

gallerific = Resource(
    GalleryResources, "jquery.galleriffic.min.js", depends=[jquery])

animated_gallery = Resource(
    GalleryResources, "gallery.js", depends=[gallerific, gallery_css])
