from rest_framework.serializers import Serializer, FileField
from xml_converter.converter import convert_to_dict



class CreateXMLtoDictAPISerializer(Serializer):
    
    class Meta:
        fields = ["file"]

    # file = FileField(validators=[validate_file_format])
    file = FileField()

    def create(self, validated_data):
        return convert_to_dict(validated_data["file"])