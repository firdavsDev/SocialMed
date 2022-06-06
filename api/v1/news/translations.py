from modeltranslation.translator import TranslationOptions, translator

from . import models


class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description")


translator.register(models.News, NewsTranslationOptions)
