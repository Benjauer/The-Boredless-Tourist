# list of destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# list of attractions
attractions = [[], [], [], [], [], ]

# function for destination index
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# function for traveler location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# function to add and display attractions
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
        return attractions_for_destination
    except ValueError:
        print('Value Error Occured')
        

# attractions list filled
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# function to find attraction for traveler
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interests = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interests.append(possible_attraction[0])
    return attractions_with_interests



# function to find attraction for traveler
def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0]
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    
    
    
    interests_string = 'Hi ' + traveler_name + ', we think you\'ll like these places around ' + traveler_destination + ': ' + str(traveler_attractions)
    return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)