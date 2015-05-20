from modeltranslation.translator import translator, TranslationOptions
from page.models import *

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(Page, PageTranslationOptions)

class PostTranslationOptions(TranslationOptions):
    pass
translator.register(Post, PostTranslationOptions)
