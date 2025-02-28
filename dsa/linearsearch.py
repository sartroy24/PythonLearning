data = {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 1
}

def linearSearch(cards, query):
    #Create a variable position with value of 0
    position = 0
    
    #Set up a loop for repetition
    while True:
        
        #Check if element at the current position matches the query
        if cards[position] == query:
            
            #Answer found! Return and exit..
            return position
        
        #Increment the position
        position += 1
        
        #Check if we have reached the end of array
        if position == len(cards):
            
            #Number not found return -1
            return -1
            
print(linearSearch(data['cards'], data['query']))