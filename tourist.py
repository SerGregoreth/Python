destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paolo, Brazil', 'Cairo, Egypt']
test_subj = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#getting the index of each element in destination list
def get_destination_i(destination):
    destination_i = 0
    for place in destinations:
        if place != destination:
            continue
        elif place == destination:
            destination_i = destinations.index(place)
            return destination_i
        
print(get_destination_i('Tokyo, Japan'))