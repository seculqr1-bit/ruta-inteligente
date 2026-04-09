import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import folium
import datetime
import random

class SmartRouteCore:
    """
    Core functional logic for SIR: Sistema Inteligente de Rutas.
    Handles data acquisition, ML model training for traffic prediction,
    and route optimization for Colombian cities.
    """
    
    def __init__(self, city_name="Pamplona, Colombia"):
        self.city_name = city_name
        self.graph = None
        self.model = None
        self.features = ['hour', 'day_of_week', 'is_weekend', 'distance']
        
    def load_city_graph(self):
        """Load the street network for the specified city using OSMnx."""
        print(f"Loading street network for {self.city_name}...")
        # Using 'drive' network type for vehicle routing
        self.graph = ox.graph_from_place(self.city_name, network_type='drive')
        # Add edge speeds and travel times
        self.graph = ox.add_edge_speeds(self.graph)
        self.graph = ox.add_edge_travel_times(self.graph)
        print("Network loaded successfully.")
        return self.graph

    def generate_synthetic_traffic_data(self, n_samples=1000):
        """
        Generate synthetic traffic data based on typical urban patterns in Colombia.
        In a real scenario, this would be replaced by historical API data.
        """
        print("Generating synthetic traffic data for training...")
        data = []
        for _ in range(n_samples):
            hour = random.randint(0, 23)
            day_of_week = random.randint(0, 6)
            is_weekend = 1 if day_of_week >= 5 else 0
            distance = random.uniform(0.1, 10.0) # km
            
            # Base travel time (minutes) = distance * 2 (avg 30km/h)
            base_time = distance * 2
            
            # Traffic multipliers for Colombia (Peak hours: 7-9 AM, 5-7 PM)
            multiplier = 1.0
            if 7 <= hour <= 9 or 17 <= hour <= 19:
                multiplier = random.uniform(1.5, 3.0) if not is_weekend else 1.2
            elif 12 <= hour <= 14: # Lunch rush
                multiplier = random.uniform(1.2, 1.8)
                
            travel_time = base_time * multiplier + random.normalvariate(0, 0.5)
            data.append([hour, day_of_week, is_weekend, distance, max(0.1, travel_time)])
            
        df = pd.DataFrame(data, columns=self.features + ['travel_time'])
        return df

    def train_model(self):
        """Train a Random Forest model to predict travel times."""
        df = self.generate_synthetic_traffic_data()
        X = df[self.features]
        y = df['travel_time']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Training Random Forest Regressor...")
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        score = self.model.score(X_test, y_test)
        print(f"Model trained. R^2 Score: {score:.4f}")
        return self.model

    def predict_edge_time(self, distance, timestamp=None):
        """Predict travel time for a specific edge distance and time."""
        if timestamp is None:
            timestamp = datetime.datetime.now()
            
        hour = timestamp.hour
        day_of_week = timestamp.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0
        
        input_data = pd.DataFrame([[hour, day_of_week, is_weekend, distance]], columns=self.features)
        return self.model.predict(input_data)[0]

    def get_optimal_route(self, origin_coords, dest_coords):
        """
        Calculate the optimal route between two points using the ML-predicted weights.
        origin_coords/dest_coords: (lat, lon)
        """
        if self.graph is None:
            self.load_city_graph()
        if self.model is None:
            self.train_model()
            
        # Find nearest nodes to the coordinates
        orig_node = ox.nearest_nodes(self.graph, origin_coords[1], origin_coords[0])
        dest_node = ox.nearest_nodes(self.graph, dest_coords[1], dest_coords[0])
        
        # Update edge weights with ML predictions
        # For simplicity in this functional core, we'll use the current time
        now = datetime.datetime.now()
        
        for u, v, k, data in self.graph.edges(data=True, keys=True):
            distance_km = data['length'] / 1000
            predicted_time = self.predict_edge_time(distance_km, now)
            data['ml_travel_time'] = predicted_time

        # Calculate shortest path using predicted travel time as weight
        route = nx.shortest_path(self.graph, orig_node, dest_node, weight='ml_travel_time')
        return route

    def visualize_route(self, route, output_file="route_map.html"):
        """Generate a Folium map showing the calculated route."""
        # Extract coordinates for the route
        route_coords = []
        for node in route:
            node_data = self.graph.nodes[node]
            route_coords.append((node_data['y'], node_data['x']))
            
        # Create a folium map centered on the route
        m = folium.Map(location=route_coords[0], zoom_start=15)
        folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(m)
        
        # Add markers for start and end
        folium.Marker(route_coords[0], popup="Start", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(route_coords[-1], popup="End", icon=folium.Icon(color='red')).add_to(m)
        
        m.save(output_file)
        print(f"Route visualization saved to {output_file}")
        return output_file

if __name__ == "__main__":
    # Example usage for Pamplona, Colombia
    core = SmartRouteCore("Pamplona, Colombia")
    
    # Coordinates for Pamplona (approximate central points)
    pamplona_center = (7.375, -72.648)
    pamplona_suburb = (7.385, -72.640)
    
    route = core.get_optimal_route(pamplona_center, pamplona_suburb)
    core.visualize_route(route, "pamplona_route.html")
