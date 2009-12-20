# -*- coding: utf-8 -*-

from hurry.jquery import jquery
from megrok import resource


class GalleryResources(resource.Library):
    resource.path('resources')
    resource.name("photoalbum.resources")


css_animated = resource.ResourceInclusion(
    GalleryResources, "gallery.css")

gallerific = resource.ResourceInclusion(
    GalleryResources, "jquery.galleriffic.min.js", depends=[jquery])

simple_gallery = resource.ResourceInclusion(
    GalleryResources, "gallery.css")

animated_gallery = resource.ResourceInclusion(
    GalleryResources, "gallery.js", depends=[gallerific, css_animated])
