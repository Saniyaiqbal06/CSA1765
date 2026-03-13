import numpy as np

def tsp(cities):
    """
    Solve the Traveling Salesman Problem using the Nearest Neighbor heuristic.
    
    Parameters:
    cities: numpy array of shape (n, 2) containing city coordinates
    
    Returns:
    tour: list of city indices in the order visited
    total_distance: total distance of the tour
    """
    # Create a distance matrix
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])
    
    # Initialize variables
    tour = [0]
    unvisited_cities = set(range(1, n))
    total_distance = 0
    
    # Find the nearest unvisited city and add it to the tour
    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: dist_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        total_distance += dist_matrix[current_city][nearest_city]
    
    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += dist_matrix[tour[-2]][0]
    
    return tour, total_distance

# Example usage
if __name__ == "__main__":
    # Generate random cities (5 cities with 2D coordinates)
    np.random.seed(42)  # For reproducibility
    cities = np.random.rand(5, 2) * 100
    
    print("City coordinates:")
    for i, (x, y) in enumerate(cities):
        print(f"  City {i}: ({x:.2f}, {y:.2f})")
    
    # Solve TSP
    tour, distance = tsp(cities)
    
    print(f"\nOptimal tour (Nearest Neighbor): {tour}")
    print(f"Total distance: {distance:.2f}")
    
    # Verify the tour distance manually
    verified_distance = 0
    for i in range(len(tour)-1):
        verified_distance += np.linalg.norm(cities[tour[i]] - cities[tour[i+1]])
    print(f"Verified distance: {verified_distance:.2f}")