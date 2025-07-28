from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AccidentReport
from .serializers import AccidentReportSerializer

@api_view(['POST'])
def submit_accident_report(request):
    serializer = AccidentReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # .save() will also auto-calculate severity_score
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
