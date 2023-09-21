from rest_framework.serializers import Serializer, FileField, JSONField
from xml_converter.converter import convert_to_dict



class CreateXMLtoDictAPISerializer(Serializer):
    
    class Meta:
        fields = ["file"]

    # file = FileField(validators=[validate_file_format])
    file = FileField()
    converted_data = JSONField(required=False)

    def create(self, validated_data):
        validated_data["converted_data"] = convert_to_dict(validated_data["file"])
        return validated_data
    