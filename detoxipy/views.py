from django.shortcuts import render


def panel_view(request):
    """ Returns the panel html to be rendered
    """
    return render(request, 'generic/panel.html')


def config_view(request):
    """ Returns the config html to be rendered
    """
    return render(request, 'generic/config.html')
