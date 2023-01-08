from .models import *
from .forms import *

def home(request):
    return render(request, 'pages/home.html', context)

