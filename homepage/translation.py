from modeltranslation.translator import translator, TranslationOptions
from homepage.models import Section

class SectionTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Section, SectionTranslationOptions)