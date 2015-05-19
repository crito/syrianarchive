from modeltranslation.translator import translator, TranslationOptions
from page.models import Page

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(Page, PageTranslationOptions)