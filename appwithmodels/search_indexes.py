import datetime
from haystack import indexes
from appwithmodels.models import Mobiles_sub_category


class Mobiles_sub_categoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    price = indexes.CharField(model_attr='price')
    description = indexes.CharField(model_attr='description')
    name = indexes.CharField(model_attr='name')
    phone_number = indexes.CharField(model_attr='phone_number')
    city = indexes.CharField(model_attr='city')

    def get_model(self):
        return Mobiles_sub_category
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(price__lte=5000)
    
