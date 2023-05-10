from django.shortcuts import render

from solarkit.viewer import Viewer
from solarkit import utils
import matplotlib

import matplotlib.pyplot as plt
from io import StringIO


# Create your views here.
def index(request):
    return render(request, "app/index.html")

def orbits_default(request):
    context = {}
    
    
    viewer = Viewer(system=utils.load_system_from_csv("app\data\planet_data.csv"), planets_to_use=["Mercury", "Venus", "Earth", "Mars"], compute_3D=True)
    viewer.server_mode()
    viewer.initialise_plotter()
    viewer.system_orbits()
    viewer.add_grid()
    viewer.add_legend()
    
    
    context["graph"] = viewer.get_figure_data
    
    
    return render(request, "app/orbits.html", context)