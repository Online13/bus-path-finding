from app.DataModel import DataModel
from app.Visualizer import Visualizer
from app.Timer import Timer


def solve(_solver, bss, bse, show_summary=False, verbose=False):
    with Timer(verbose) as timer:
        solutions = _solver.find_path(bss, bse)
        if verbose:
            print("number of possibility = ", len(solutions))
    if show_summary:
        print("=" * 40)
        _solver.summary(solutions)
    return timer.get_duration()


def generate_plot(dir: str, model: DataModel):
    visualizer = Visualizer(dir, data_model=model)

    visualizer.introduction()
    visualizer.plot_graph()
    for bus in model.data_source.BUS:
        visualizer.plot_bus_path(bus)


def plot_bus_stop_to_remove(bus_stops: list[str], model: DataModel):
    visualizer = Visualizer("out-AC", data_model=model)

    visualizer.plot_bus_stop_to_remove(bus_stops)
