from django.shortcuts import render

from solarkit.viewer import Viewer
from solarkit import utils

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def orbits_default(request):
    viewer = Viewer(system=utils.load_system_from_csv("app/static/data/planet_data.csv"))
    viewer.initialise_plotter()
    viewer.system_orbits()
    viewer.add_grid()
    viewer.add_legend()
    viewer.save_figure(path="app\static\images", filename="orbits")
    
    return render(request, "app/orbits.html")