def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    n=fruits.count('apple')
    while i<n:
        fruits.pop(fruits.index('apple'))
        i+=1 
    return fruits
