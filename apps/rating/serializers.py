from rest_framework import serializers
from .models import Rating

# Create your tests here.
class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Rating
        exclude=["updated_at", "pkid"]

    def get_rater(sef, obj):
        return obj.rater.username
    
    def get_agent(self, obj):
        return obj.agent.user.username
        