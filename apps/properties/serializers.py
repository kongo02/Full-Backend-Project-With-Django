from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews



class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    
    
    class Meta:
        model = Property
        fields = [
            "id",
            "user",
            "title",
            "slug",
            "ref_code",
            "description",
            "price",
            "country",
            "city",
            "state",
            "property_type",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status"
            "views"
        ]
        
    def get_user(self, obj):
        return obj.user.username
    
class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    
    class Meta:
        model = Property
        exclude = ["updated_at", "pkid"]
        
class PropertyViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]