import haversine


#Example upcoming data from db

hospitals = [
    {
        "name":"Mero hospital",
        "services":["CT scan","ECG","Full body check","Blood test"],
        "ratings":13,
        "coordinates":[27.6664,85.268803]
    },
    {
        "name":"Tero hospital",
        "services":["ECG","Blood test"],
        "ratings":12,
        "coordinates":[27.6634,85.26303]
    },
    {
        "name":"Hamro hospital",
        "services":["Blood test"],
        "ratings":10,
        "coordinates":[27.6614,85.268103]
    }
]


def recommend(service_requested,coordinates):
    return_list = []
    for hospital in hospitals:
        if service_requested in hospital["services"]:
            return_list.append(hospital) 
    
    for hospital in return_list:
        distance = haversine.haversine(coordinates[0],coordinates[1],hospital["coordinates"][0],hospital["coordinates"][1])
        hospital["distance"] = distance
    
    return_list.sort(key=lambda x: x["distance"])


    
    return return_list


print(recommend("ECG",[26.310,23.449]))




