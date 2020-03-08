# list of destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# function for destination index
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# function for traveler location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

