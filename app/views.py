from django.shortcuts import render

from solarkit.viewer import Viewer
from solarkit import utils



def create_viewer_from_querydict(query_dict: dict) -> Viewer:
    """_summary_
    Creates a solarkit.Viewer object from request

    
    Args:
        query_dict (dict): query dictionary

    Returns:
        Viewer: solarkit.Viewer using request as arguments
    """
    query_dict = {key: True for key, value in query_dict.items() if value}
    
    planets_to_use = [key.capitalize() for key, value in query_dict.items() if value and key != "compute_3D"]
    
    if "compute_3D" in query_dict.keys():
        compute_3D = True
    else:
        compute_3D = False
        
    system = utils.load_system_from_csv("app\data\planet_data.csv")
    
    return Viewer(system=system, planets_to_use=planets_to_use, compute_3D=compute_3D)


# Create your views here.
def index(request):
    
    return render(request, "app/index.html")

def orbits(request):
    
    context = {}
    
    if request.GET:
        viewer = create_viewer_from_querydict(query_dict=request.GET)
    
        viewer.server_mode()
        viewer.initialise_plotter()
        viewer.system_orbits()
        viewer.add_grid()
        viewer.add_legend()
        
        context["graph"] = viewer.get_figure_data()
    
    
    return render(request, "app/orbits.html", context)


def spinograph(request):
    
    context = {}
    
    if request.GET:
        viewer = create_viewer_from_querydict(query_dict=request.GET)
    
        viewer.server_mode()
        viewer.initialise_plotter()
        viewer.spinograph()
        viewer.add_grid()
        viewer.add_legend()
        
        context["graph"] = viewer.get_figure_data()
    
    
    return render(request, "app/spinograph.html", context)

def heliocentric(request):
    context = {}
    
    if request.GET:
        viewer = create_viewer_from_querydict(query_dict=request.GET)
    
        viewer.server_mode()
        viewer.initialise_plotter()
        viewer.heliocentric_model(origin_planet_name="Earth")
        viewer.add_grid()
        viewer.add_legend()
        
        context["graph"] = viewer.get_figure_data()
    
    
    return render(request, "app/heliocentric.html", context)
    
def third_law(request):
    context = {}
    system = utils.load_system_from_csv("app\data\planet_data.csv")
    viewer = Viewer(system=system)

    viewer.server_mode()
    viewer.initialise_plotter()
    viewer.third_law()
    viewer.add_grid()
    viewer.add_legend()
    
    context["graph"] = viewer.get_figure_data()
    
    
    return render(request, "app/third_law.html", context)