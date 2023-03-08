from rest_framework import serializers

from trackerapi.models import Baby


class BabySerializer(serializers.ModelSerializer):

    class Meta:
        model = Baby
        fields = ("name", "gender", "dob", "time_of_birth", "due_day",)
