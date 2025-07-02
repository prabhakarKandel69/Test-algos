import haversine


#Example upcoming data from db

hospitals = [
    {
        "name":"Mero hospital",
        "services":["CT scan","ECG","Full body check","Blood test"],
        "ratings":4,
        "coordinates":[27.6664,85.268803]
    },
    {
        "name":"Tero hospital",
        "services":["ECG","Blood test"],
        "ratings":3,
        "coordinates":[27.6634,85.26303]
    },
    {
        "name":"Hamro hospital",
        "services":["Blood test"],
        "ratings":2,
        "coordinates":[27.6614,85.268103]
    }
]


def recommend(service_requested,coordinates):

    max_distance = 20
    return_list = []
    for hospital in hospitals:
        if service_requested in hospital["services"]:
            return_list.append(hospital) 
    
    for hospital in return_list:
        distance = haversine.haversine(coordinates[0],coordinates[1],hospital["coordinates"][0],hospital["coordinates"][1])
        norm_rating = hospital["ratings"] / 5.0
        norm_distance = min(distance/ max_distance,1.0)

        score = (0.6*norm_distance) + (0.4*norm_rating)
        hospital["score"] = score
    
    return_list.sort(key=lambda x: x["score"])
    return return_list

    

print(recommend("ECG",[26.310,23.449]))




