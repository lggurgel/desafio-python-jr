from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.converter import convert_to_dict
from rest_framework.generics import CreateAPIView
from xml_converter.serializers import CreateXMLtoDictAPISerializer

def upload_page(request):
    if request.method == 'POST':
        # TODO: Convert the submitted XML file into a JSON object and return to the user.

        file = request.FILES.get("file")

        # validate_file_format(file)

        xml_converted = convert_to_dict(file)
        
        return JsonResponse(xml_converted)

    return render(request, "upload_page.html")


class CreateXMLtoDictAPI(CreateAPIView):

    serializer_class = CreateXMLtoDictAPISerializer