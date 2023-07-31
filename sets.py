# 1. add() -add a given element to a set
s = {'g', 'e', 'k', 's'}
s.add('f')
print('Set after updating:', s)  # Output: {'g', 'k', 's', 'e', 'f'}
#<------------------------------------------------------------------------->
#2. clear() -clear all elements
s = {'g', 'e', 'k', 's'}
s.clear()
print('Set after updating:', s)  # Output: set()
#<------------------------------------------------------------------------->
#3. discard() -remove the given element from a set
s = {'g', 'e', 'k', 's'}
s.discard('g')
print('Set after updating:', s)  # Output: {'k', 's', 'e'}
#<------------------------------------------------------------------------->
#4. pop() -remove the random element
s = {'g', 'e', 'k', 's'}
popped_element = s.pop()
print('Popped element:', popped_element)  # Output: Randomly selected element
#<------------------------------------------------------------------------->
#5. difference() difference b/w 2-sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff = set1.difference(set2)
print('Difference between set1 and set2:', diff)  # Output: {1, 2, 3}
#<------------------------------------------------------------------------->
#6. intersection() -Common b/w 2-sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print('Intersection of set1 and set2:', intersection)  # Output: {4, 5}
#<------------------------------------------------------------------------->
#7.union() - Retuen all elements in all set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print('Union of set1 and set2:', union)  # Output: {1, 2, 3, 4, 5}



