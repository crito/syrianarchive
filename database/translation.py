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
      'acquired_from',

    	)

class InternationalInstrumentTranslationOptions(TranslationOptions):
    fields = ('name',)

class MediaContentTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

class SourceConnectionTranslationOptions(TranslationOptions):
    fields = ('name',)

class LocationPlaceTranslationOptions(TranslationOptions):
    fields = ('name',)

class DeviceTranslationOptions(TranslationOptions):
    fields = ('name',)

class ViolationTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

class CollectionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(DatabaseEntry, DatabaseEntryTranslationOptions)
translator.register(MediaContentType, MediaContentTypeTranslationOptions)
translator.register(InternationalInstrument, InternationalInstrumentTranslationOptions)
translator.register(SourceConnection, SourceConnectionTranslationOptions)
translator.register(LocationPlace, LocationPlaceTranslationOptions)
translator.register(Device, DeviceTranslationOptions)
translator.register(ViolationType, ViolationTypeTranslationOptions)
translator.register(Collection, CollectionTranslationOptions)