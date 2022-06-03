from modeltranslation.translator import translator, TranslationOptions

from . import models


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(models.News, NewsTranslationOptions)
