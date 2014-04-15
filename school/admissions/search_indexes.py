from haystack import indexes
from admissions.models import Institution
import datetime


class InstitutionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    address = indexes.CharField(model_attr='address')
    state = indexes.CharField(model_attr='state')

    def get_model(self):
        return Institution

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()