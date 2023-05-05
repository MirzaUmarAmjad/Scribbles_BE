from rest_framework.response import Response
from rest_framework.decorators import api_view
import whisper


# Create your views here.
@api_view(['GET'])
def convertAudioToText(request):
    model = whisper.load_model("base")
    result = model.transcribe("Scribbles_BE/api/files/audio.mp3")

    return Response(result["text"])