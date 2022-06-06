from modeltranslation.translator import TranslationOptions, translator

from . import models


class MapsTranslationOptions(TranslationOptions):
    fields = ("name", "address_description")


class CategoryofMapsTranslation(TranslationOptions):
    fields = ("name",)


translator.register(models.Maps, MapsTranslationOptions)
translator.register(models.CategoryofMaps, CategoryofMapsTranslation)
