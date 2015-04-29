from modeltranslation.translator import translator, TranslationOptions
from database.models import *

class DatabaseEntryTranslationOptions(TranslationOptions):
    fields = ('name', 
    	'description',
    	'chain_of_custody_notes_public',
    	'international_instrument_notes',
    	'landmarks',
    	'weather_in_media',
    	'weapons_used',
    	'urls_and_news',

    	)

class MediaContentTypeTranslationOptions(TranslationOptions):
    fields = ('name', 
    	)

translator.register(DatabaseEntry, DatabaseEntryTranslationOptions)
translator.register(MediaContentType, MediaContentTypeTranslationOptions)