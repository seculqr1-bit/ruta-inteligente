from core_ml_routing import SmartRouteCore
import os

def run_demo():
    """
    Run the SmartRouteCore for principal Colombian cities and Pamplona.
    Demonstrates the functional ML logic for traffic prediction and routing.
    """
    cities = [
        "Pamplona, Colombia",
        "Bogotá, Colombia",
        "Medellín, Colombia",
        "Cali, Colombia"
    ]
    
    # Approximate central coordinates for demo purposes
    city_coords = {
        "Pamplona, Colombia": [(7.375, -72.648), (7.385, -72.640)],
        "Bogotá, Colombia": [(4.6097, -74.0817), (4.6500, -74.1000)],
        "Medellín, Colombia": [(6.2442, -75.5812), (6.2600, -75.5600)],
        "Cali, Colombia": [(3.4516, -76.5320), (3.4700, -76.5200)]
    }
    
    for city in cities:
        print(f"\n--- Processing {city} ---")
        try:
            core = SmartRouteCore(city)
            core.load_city_graph()
            core.train_model()
            
            origin, dest = city_coords[city]
            route = core.get_optimal_route(origin, dest)
            
            output_file = f"{city.split(',')[0].lower()}_route.html"
            core.visualize_route(route, output_file)
            print(f"Successfully generated route for {city}.")
            
        except Exception as e:
            print(f"Error processing {city}: {e}")

if __name__ == "__main__":
    run_demo()
