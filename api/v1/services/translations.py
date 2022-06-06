from modeltranslation.translator import TranslationOptions, translator

from . import models


class ServiceTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "service_type",
        "description",
        "requirement_dockument",
        "orgination",
        "responsible_person",
        "legal_basis",
    )


class ServiceCategoryTranslation(TranslationOptions):
    fields = ("name",)


translator.register(models.Service, ServiceTranslationOptions)
translator.register(models.ServiceCategory, ServiceCategoryTranslation)
