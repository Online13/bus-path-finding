from collections import deque
from app.DataModel import DataModel
from data import NODE_INDEX as ni


class Solver:
    data_model: DataModel

    def __init__(self, data_model: DataModel):
        self.data_model = data_model

    def has_path(self, bus_stop_start, bus_stop_end):
        # Create a set to track visited nodes
        visited = set()

        # Create a queue for BFS
        queue = deque([bus_stop_start])

        while queue:
            current_node = queue.popleft()
            # Check if the current node is the target node
            if current_node == bus_stop_end:
                return True
            # Mark the current node as visited
            visited.add(current_node)
            # Add unvisited neighbors to the queue
            for neighbor in [
                bse for bss, bse in self.data_model.links if bss == current_node
            ]:
                if neighbor not in visited:
                    queue.append(neighbor)

        # If the queue is empty and the target node hasn't been reached, there is no path
        return False

    def make_arc_consistency(self, bus_stop_start, bus_stop_end):
        bus_stop_to_remove = []
        for bus_stop in self.data_model.bus_stops:
            if not self.has_path(bus_stop_start, bus_stop) or not self.has_path(
                bus_stop, bus_stop_end
            ):
                bus_stop_to_remove.append(bus_stop)
                self.data_model.remove_bus_stop(bus_stop)
        return bus_stop_to_remove

    def find_path(self, bus_stop_start, bus_stop_end):
        solutions = []
        queue = deque(
            [
                (bus_stop_start, bus, [(bus_stop_start, bus, 1, 0)])
                for _, bus, _ in self.data_model.get_neighbor_node(
                    (bus_stop_start, None)
                )
            ]
        )

        while queue:
            node = queue.popleft()
            bus_stop_node, bus_node, solution = node

            if bus_stop_node == bus_stop_end:
                solutions.append(solution)
                continue

            for bus_stop, bus, time in self.data_model.get_neighbor_node(
                (bus_stop_node, bus_node)
            ):
                result = solution[-1]
                new_change_bus_time = result[ni["change_bus_time"]] + int(
                    bus != bus_node
                )
                new_time = result[ni["time"]] + time
                if new_time > 120 or new_change_bus_time > 3:
                    continue
                new_solution = solution + [
                    (bus_stop, bus, new_change_bus_time, new_time)
                ]
                queue.append(
                    (
                        bus_stop,
                        bus,
                        new_solution,
                    )
                )

        return solutions

    def summary(self, solutions):
        summaries = []
        for solution in solutions:
            group = {}
            for bus_stop, bus, key, time in solution:
                K = f"{bus}-{key}"
                if K not in group:
                    group[K] = []
                group[K] += [bus_stop]
            summaries.append(
                {
                    "itinerary": [
                        f'{bus.split("-")[0]} ({bus_stops[0]}, {bus_stops[-1]})'
                        for bus, bus_stops in group.items()
                    ],
                    "change_bus_time": solution[-1][ni["change_bus_time"]],
                    "time": solution[-1][ni["time"]],
                }
            )
        for s in summaries:
            print("change_bus_time=", s["change_bus_time"])
            print("duration=", str(s["time"]) + "min")
            for itinerary in s["itinerary"]:
                print(f" {itinerary}")
            print("")
