from django.utils import timezone
from .models import History


def log_user_activity(request):

    if request.user.is_authenticated:

        data = {
            'request_method': request.method,
            'user': request.user,
            'url': request.build_absolute_uri(),
            'request': request,
            'user_agent': request.headers['User-Agent'],
        }

        # Write data in database
        history = History(**data)
        history.save()
    

    return {}
