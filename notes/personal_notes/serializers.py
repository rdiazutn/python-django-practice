from rest_framework import serializers
from .models import PersonalNote


class PersonalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = PersonalNote
    fields = (
        "id",
        "title",
        "content",
        "created_at",
        "last_modified"
    )
    read_only_fields = ("id", "created", "last_modified")

