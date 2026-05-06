from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Score

def index(request):
    return render(request, 'index.html')

def rankings(request, genre=None):
    return render(request, 'rankings.html', {'genre': genre})

def about(request):
    return render(request, 'about.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_scores(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            score = Score.objects.create(
                player_name=data.get('name', 'BAYANI'),
                score=data.get('score', 0),
                genre=data.get('genre', 'ph'),
                difficulty=data.get('difficulty', 'easy')
            )
            return JsonResponse({'success': True, 'message': 'Score saved!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    # GET: Retrieve top scores for a genre
    genre = request.GET.get('genre', 'ph')
    limit = int(request.GET.get('limit', 15))
    
    scores = Score.objects.filter(genre=genre)[:limit]
    scores_data = [
        {
            'name': s.player_name,
            'score': s.score,
            'difficulty': s.difficulty,
            'date': int(s.created_at.timestamp() * 1000)  # Convert to milliseconds for JS
        }
        for s in scores
    ]
    
    return JsonResponse({'scores': scores_data})
