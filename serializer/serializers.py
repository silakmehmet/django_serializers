from datetime import datetime

from rest_framework import serializers

from .models import Student


# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get(
#             "first_name", instance.first_name)
#         instance.last_name = validated_data.get(
#             "last_name", instance.last_name)
#         instance.number = validated_data.get("number", instance.number)
#         instance.age = validated_data.get("age", instance.age)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    born_year = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id",)

    def get_born_year(self, obj):
        return datetime.now().year - obj.age
