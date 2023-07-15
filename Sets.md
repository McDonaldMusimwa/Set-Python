# **Sets**
1. [Characterics](#characteristic) 
2. [Hashing](#hashing)
3. [Operations](#operations)
4. [Interview Questions](#interview)

## Characteristic
Another data structure in Python is a Set.Unlick lists,stacks and queues that track the location of each item in memory, Sets are not ordered and eliminate duplicates.
The absence or order and duplication gives sets an edge in performance o(1).Data is uniquely stored and allows for testing of membership.Through hashing sets allows to add ,remove and test for membership.  

# declare sets by   
1. open a variable then within the varibale call the function set()
2. convert an array to a set variable = 
3. open variable and store empty curly braces

# Hashing  
Sets in Python achieve an average time complexity of *O(1)* for common operations, such as adding, removing, and checking membership of elements. This constant-time complexity is possible because sets are implemented using a data structure called a hash table, also known as a hash set or a hash map.

A hash table uses a hash function to map each element to a specific index in an underlying array. This index is where the element is stored. When you perform operations like adding or removing an element, the hash function is used to determine the index and access the element directly.

The key factor that enables the *O(1)* time complexity is that the hash function provides a constant-time mapping from the element to its index. This allows efficient retrieval and storage of elements, regardless of the size of the set.

To achieve this constant-time complexity, the hash function should distribute the elements uniformly across the array to minimize collisions (i.e., multiple elements mapping to the same index). Additionally, the hash table implementation in Python dynamically adjusts its size as elements are added or removed, ensuring an optimal balance between the number of elements and the size of the underlying array.

It's important to note that while the average time complexity of set operations is *O(1)*, there can be worst-case scenarios where the time complexity increases to *O(n)*. This occurs when multiple elements have the same hash value, causing more collisions and degrading performance. However, in practice, such scenarios are rare, and the average constant-time behavior holds for most sets.

Overall, sets achieve *O(1)* time complexity by leveraging hash tables, efficient hash functions, and dynamic resizing strategies. This allows for fast operations regardless of the size of the set, making sets an effective choice for handling collections of unique elements.

# Operations  
<img src="Python-Set-Operations.png" width="600px"/>

- **clear()**: Removes all elements from the set, making it empty.

- **copy()**: Creates a shallow copy of the set. Any modifications made to the copy will not affect the original set.  
- **intersection()**: Return the elements common in two sets.  
- **union()**: Combines two sets and eleminates duplicate.

- **issubset(other_set)**: Checks if the set is a subset of another set (other_set). Returns True if all elements of the set are present in the other set, and False otherwise.

- **issuperset(other_set)**: Checks if the set is a superset of another set (other_set). Returns True if the set contains all elements of the other set, and False otherwise.

- **difference(other_set)**: Returns a new set containing the elements that are present in the set but not in the other set (other_set).

- **symmetric_difference(other_set)**: Returns a new set containing the elements that are present either in the set or in the other set, but not in both.

- **difference_update(other_set)**: Modifies the set in-place by removing the elements that are also present in the other set (other_set).

- **add(element)**: Adds an element to the set. If the element is already present, it is not added again.

- **remove(element)**: Removes an element from the set. Raises a KeyError if the element is not found in the set.  

## Examples:
        numbers1 = [1,2,3,4] =>lists
        numbers2 = [3,5,6,7] => lists

        numbers1 = set(numbers1) =>convert to set
        numbers2 = set(numbers2) => convert to set

        combinedsets = numbers1.union(numbers2) combinesets
        intersection = numbers1.intesection(numbers2)
         
        newsetnumbers = numbers1.update(numbers2) =>The update() method inserts the items in set2 into set1:

        numbers1.intersection_update(numbers2) =>Keep the items that exist in both sets


# Interview  
1. ***How would you describe the performance of a set?***  
- Insertion and Deletion: The average time complexity for adding or removing an element from a set is O(1). This is because sets use hash tables internally, which allows for constant-time operations. However, in rare cases, the time complexity can be O(n) in the worst case when there are collisions in the hash table.

- Membership Test: Checking if an element is present in a set has an average time complexity of O(1). This is because sets use hash tables, which provide fast lookup based on the element's hash value. However, in rare cases, the time complexity can be O(n) in the worst case when there are many hash collisions.

- Set Operations: Set operations such as union, intersection, difference, and symmetric difference also have an average time complexity of O(1), assuming the sets involved are of similar sizes. However, the worst-case time complexity for these operations can be O(n) if one set is significantly larger than the other.

- Iteration: Iterating over a set takes time proportional to the number of elements in the set, which is O(n). The order of iteration is arbitrary and not based on the insertion order.

- Space Complexity: The space complexity of a set is proportional to the number of elements stored in it. It requires additional memory to store the hash table and related data structures. The space complexity of a set is O(n), where n is the number of elements in the set.

2. ***What is hashing and why is it used with a set?***    
In the context of sets in Python, hashing is used to efficiently store and retrieve elements. When an element is added to a set, its hash value is computed using a hash function, and the element is stored in a specific location within a hash table based on its hash value. This process allows for quick insertion and retrieval of elements.



- Fast Lookup: Hashing allows for constant-time lookup of elements in a set. Since the hash value of an element determines its storage location within the hash table, retrieving an element involves a simple computation and direct access to the corresponding location.

- Elimination of Duplicates: Hashing ensures that duplicate elements are automatically eliminated in a set. When attempting to add an element with the same hash value as an existing element, the hash table can quickly determine that the element is already present and avoid adding it again.

- Efficient Set Operations: Hashing enables efficient set operations such as union, intersection, difference, and symmetric difference. By comparing the hash values of elements, these operations can be performed with high efficiency by manipulating the hash tables of the involved sets.

- Space Optimization: Hashing allows for memory optimization by storing unique elements only once. The hash table eliminates the need to store duplicate elements separately, resulting in efficient memory usage.

3. ***When would you use a set instead of a List?***  
- Removing Duplicates: If you have a list with duplicate elements and you want to eliminate the duplicates, you can convert the list to a set. Since sets only store unique elements, converting a list to a set automatically removes any duplicates.

- Checking Membership: Sets provide a very efficient way to check if an element is present or not. The membership test for a set takes O(1) time complexity, whereas in a list, it takes O(n) time complexity, as it requires iterating through the list.

- Set Operations: Sets in Python support various set operations like union, intersection, difference, and symmetric difference. These operations make it convenient to perform set-related calculations and comparisons. For example, you can easily find common elements between two sets, elements unique to each set, or merge multiple sets together.

- Mathematical Modeling: Sets are often used in mathematical modeling or solving problems that involve concepts like set theory, graph theory, or combinatorics. Sets provide a natural way to represent and manipulate sets of objects, subsets, or relationships between elements.

- Hashing: Sets use hash tables internally, which makes them suitable for scenarios where efficient hashing and lookup are required. If you have a large collection of elements and need to frequently check for membership or eliminate duplicates, sets can offer better performance compared to lists.

