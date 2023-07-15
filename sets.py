
class SetTutorial:
    def __init__(self):
        data =  set()


    def addItems(self,value):
        self.data.add(value)
        #self.data.update(value)

    def removeItem(self,value):
        self.data.remove(value)
            
    #convert array to set
    numbers = [1,2,3,3,4,5,6,6,7]
    uniqueNumber = set(numbers)

    def union(self,set1,set2):  
        newset=  set1 |set2
        return newset
    
    def intersetction (self,set1,set2):
        newset = set1 & set2
        return newset
    
    def difference(self,set1,set2):
        """
        difference() Method:

        Syntax: set1.difference(set2) or set1 - set2
        Returns a new set that contains elements present in set1 but not in set2.
        In other words, it returns the set difference of set1 and set2.
        The original sets set1 and set2 are not modified.
        
        """
        difference = set1-set2
        return difference
    
    def symmetricDifference(self,set1,set2):
        """
        Syntax: set1.symmetric_difference(set2) or set1 ^ set2
        Returns a new set that contains elements present in either set1 or set2, but not in both.
        In other words, it returns the set of elements that are unique to either set1 or set2.
        """
        defference = set1^set2
        return defference
    
    def clearItems(self,set):
        """Clear all items"""

        return set.clear()
    
    def copySet(self,set1):
        newSet = set1.copy()
        return newSet

    for i in range(6,14,2):
        uniqueNumber.add(i)
    print (uniqueNumber)
    uniqueNumber.discard(12)
    print(uniqueNumber)
    #remove value 
    value = uniqueNumber.pop()
    print (value)