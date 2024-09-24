# Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset(["hello", "world"])
print(frozen_set)

# Try to add "!" to frozen_set. What happens?
# you cannot add an element into a frozenset as they are immutable
#frozen_set.add("!")  #AttributeError: 'frozenset' object has no attribute 'add'
#the above error is thrown up when you try to add to a frozenset

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {
    "let's",
    "learn"
}
# Try to add frozen_set to normal_set. Why does it work? Explain.
# Print normal_set.
normal_set.add(frozen_set)
print(normal_set)

#it works because the elements inside frozen_set remain unchanged.

# Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
#the order of the elements changes every time, except the elements inside frozen_set are always next to each other

# What makes a frozen set different to a normal set? Explain.
#Frozen set is just an immutable version of a Python set object.
#While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
#Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.