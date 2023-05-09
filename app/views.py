from django.shortcuts import render

from solarkit.viewer import Viewer
from solarkit import utils
import matplotlib

import matplotlib.pyplot as plt

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def orbits_default(request):
    matplotlib.use("Agg")
    viewer = Viewer(system=utils.load_system_from_csv("app\data\planet_data.csv"), planets_to_use=["Earth", "Venus", "Mars"])
    viewer.initialise_plotter()
    viewer.heliocentric_model(origin_planet_name="Earth")
    viewer.add_grid()
    viewer.add_legend()
    viewer.save_figure(path="app\static\images", filename="orbits")
    plt.close()
    return render(request, "app/orbits.html")