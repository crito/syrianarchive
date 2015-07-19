import datetime
from haystack import indexes
from database.models import DatabaseEntry


class DatabaseEntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    violations = indexes.CharField()

    def get_model(self):
        return DatabaseEntry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_violations(self, obj):
        our_string = ""
        if obj.type_of_violation != None:
            our_string = our_string + obj.type_of_violation.name + " "
        return our_string