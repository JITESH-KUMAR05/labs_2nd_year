
states = {
    "Telengana" : "Hyderabad",
    "Andhra pradesh" : "Amaravathi",
    "Karnataka" : "Bengaluru",
    "Maharashtra" : "Mumbai",
    "Tamil Nadu" : "Chennai",
    "Odissa" : "Bhubaneshwar"
}
print(states)
states["Rajasthan"] = "Jaipur"
states["Punjab"] = "Chandigarh"
print("Brfore Deletion")
print(states)
states.pop("Rajasthan")
print("After deletion")
print(states)