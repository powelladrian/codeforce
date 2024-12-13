# Input number of events
n = int(input())

# Read and parse the events
events = [input().strip() for _ in range(n)]

# Initialize variables
s = 0 # Tracks the current number of people at the bus stop
results = [] # To store the results for each bus event

for event in events:
    event_type, value = event.split() # Split event into type and value
    value = int(value) # Convert value to integer

    if event_type == 'P': # People arrive
        s += value
    elif event_type == 'B': # Bus arrives
        if value > s: 
            results.append("YES")
        else: # Not enough seats
            results.append("NO")
        s -= min(value, s) # Update people at the stop
        
print("\n".join(results)) # Print all results