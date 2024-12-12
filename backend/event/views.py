"""Views for Events App."""

from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def event_stream(request):
    def stream():
        for i in range(1, 11):
            yield f"data: Event #{i}\n\n"  # Formato estándar de SSE
            time.sleep(1)  # Intervalo de 1 segundo

    response = StreamingHttpResponse(stream(), content_type="text/event-stream")
    response["Cache-Control"] = "no-cache"  # Evitar cache en navegador
    return response
