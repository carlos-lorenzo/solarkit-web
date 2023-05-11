from django.shortcuts import render

from solarkit.viewer import Viewer
from solarkit import utils

from .forms import Viewer_Form
from .models import Viewer_Data


def create_viewer_from_object() -> Viewer:
    """
    Fetches Viewer_Data object to create solarkit.Viewer object

    Returns:
        Viewer: solarkit.Viewer using Viewer_Data as arguments
    """
    
    data = Viewer_Data.objects.all().values()[0]
    
    compute_3D = data["compute_3D"]
    
    planets_to_use = [key.capitalize() for key, value in data.items() if value == True and key != "compute_3D"]
    
    system = utils.load_system_from_csv("app\data\planet_data.csv")
    
    return Viewer(system=system, planets_to_use=planets_to_use, compute_3D=compute_3D)
    

# Create your views here.
def index(request):
    
    return render(request, "app/index.html")

def orbits(request):
    form = Viewer_Form()
    context = {"form": form}
    
    if request.method == "POST":
        if len(Viewer_Data.objects.all()) != 0:
            Viewer_Data.objects.all().delete()
        
        form = Viewer_Form(request.POST)
        
        if form.is_valid():
            form.save()
        
        create_viewer_from_object()
    
    viewer = create_viewer_from_object()
    viewer.server_mode()
    viewer.initialise_plotter()
    viewer.system_orbits()
    viewer.add_grid()
    viewer.add_legend()
    
    
    context["graph"] = viewer.get_figure_data()
    
    
    return render(request, "app/orbits.html", context)