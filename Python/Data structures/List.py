Ist = ["Apple", "Guava", "Banana", "Mango", "Orange"]
print("Length of List is:", len(Ist))
print("First Element:", Ist[0])
print("Last Element:", Ist[ -1])
Ist.append("Papaya")
print("Updated List:", Ist)
Ist.remove("Guava")
print("Updated List after removing Guava:", Ist)
Ist.sort()
print("Sorted List:", Ist)
Ist.pop(1)
print("Updated List after popping index 1:", Ist)
Ist.reverse()
print("Reversed List:", Ist)
print("Multiplication on List:", Ist * 2)
print("Sliced list (first 4 elements):", Ist[:4])
Ist.clear()
print("Updated List after clearing:", Ist)


