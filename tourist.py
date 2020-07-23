destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paolo, Brazil', 'Cairo, Egypt']
traveler_tst = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#getting the index of each element in destination list
def get_destination_i(destination):
    destination_i = 0
    for place in destinations:
        if place != destination:
            continue
        elif place == destination:
            destination_i = destinations.index(place)
            return destination_i
        
#Determining traveler location:
def traveler_loc(traveler):
    traveler_dest = traveler[1]
    traveler_dest_i = get_destination_i(traveler_dest)
    return traveler_dest_i

test_dest_i = traveler_loc(traveler_tst)
print(test_dest_i)