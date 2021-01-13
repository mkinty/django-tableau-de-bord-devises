from django.shortcuts import render, redirect
import api


# Create your views here.
def dashboard(request, days_range=60, currencies="CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    days_str = {7: "Semaine", 30: "Mois", 365: "Année"}
    page_label = days_str.get(days_range, "Personnalisé")
    themes = ["light", "dark"]
    default_theme = "light"
    context = {
        "default": default_theme,
        'themes': themes,
        'data': rates,
        'days_labels': days,
        'days_str': days_str,
        'page_label': page_label,
        'currencies': currencies,
    }
    return render(request, "devise/index.html", context=context)


def redirect_index(request):
    return redirect("home", days_range=30, currencies='CAD,USD')
