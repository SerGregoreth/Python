destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paolo, Brazil', 'Cairo, Egypt']
traveler_tst = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#getting the index of each element in destinations list
def get_destination_i(destination):
    dest_i = destinations.index(destination)
    #print(dest_i)
    return dest_i
        
#Determining traveler location:
def traveler_loc(traveler):
    traveler_dest = traveler[1]
    traveler_dest_i = get_destination_i(traveler_dest)
    #print(traveler_dest_i)
    return traveler_dest_i

#test_dest_i = traveler_loc(traveler_tst)
#print(test_dest_i)

#adding attraction functionality
#this will make a list for every destination in destinations
attractions = [[] for place in destinations]
#print(attractions)

#this will add attractions to the list attractions by destination
def add_attraction(destination, attraction):
    try:
        dest_i = get_destination_i(destination)
        #print(dest_i)
    except ValueError:
        print('That Destination does not exist in our records.')
        return
    attraction_for_dest = attractions[dest_i]
    attraction_for_dest.append(attraction)
    return
    
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
#print(attractions)

#this will add attractions to the database
add_attraction('Paris, France', ['The Louvre', ['art', 'museum']])
add_attraction('Paris, France', ['Arc de Triomphe', ['historical site', 'monument']])
add_attraction('Shanghai, China', ['Yu Garden', ['garden', 'historical']])
add_attraction('Shanghai, China', ['Yuz Museum', ['art', 'museum']])
add_attraction('Shanghai, China', ['Oriental Pearl Tower', ['skyscraper', 'viewing deck']])
add_attraction('Los Angeles, USA', ['LACMA', ['art', 'museum']])
add_attraction('Sao Paolo, Brazil', ['Sao Paolo Zoo', ['Zoo']])
add_attraction('Sao Paolo, Brazil', ['Patio do Colegio', ['historical site']])
add_attraction('Cairo, Egypt', ['Pyrimids of Giza', ['monument', 'historical site']])
add_attraction('Cairo, Egypt', ['Egyptian Museum', ['museum']])
#print(attractions)

#this will find attractions that match the interest inputted
def find_attractions(destination, interests):
    dest_i = get_destination_i(destination)
    attractions_in_city = attractions[dest_i]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = possible_attraction[1]
        for tag in attraction_tags:
            for interest in interests:
                if interest == tag:
                    attractions_with_interest.append(possible_attraction[0])
                else:
                    continue
    return attractions_with_interest

#la_arts = find_attractions('Los Angeles, USA', ['art'])
#print(la_arts)

def get_attractions_for_travelers(traveler):
    traveler_dest = traveler[1]
    traveler_interest = traveler[2]
    traveler_attractions = find_attractions(traveler_dest, traveler_interest)
    interest_str = 'Hi, ' + traveler[0] + ', we think you will like these places around ' + traveler[1] + ': '
    for attraction in traveler_attractions:
        interest_str = interest_str + str(attraction)
    interest_str = interest_str + '.'
    return interest_str

traveler_recomendation = get_attractions_for_travelers(traveler_tst)
print(traveler_recomendation)
