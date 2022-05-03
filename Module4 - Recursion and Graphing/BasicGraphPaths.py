# let's start with the standard path
# In old comics you might see a "path character took"
# We are going to make a graph to follow these paths

# the basic idea (and basic graph) is to map each key as the person passes it
# Dictionaries are ordered so just use dict - older python use ordered_dict

# so if you moved from Home -> Corner Store: we'd know you passed the Library
# we can track that forward and backwards (the lists are adjacent items)
pathsMap = {'home': ['library'],
            'library': ['home', 'corner store'],
            'corner store':['library', 'book store', 'school'],
            'book store': ['corner store'],
            'park': ['book store', 'school'],
            'burgers n stuff': ['school', 'playground'],
            'school': ['corner store', 'park', 'burgars n stuff'],
            'playground': ['burgers n stuff' ]
           }

# Will find and return path from node start to node end
# These are recusive data structures so we'll use recursion
# We'll also use a helper method to check if they even give us valid keys
def find_path(start: str, end: str) -> list:
  if not start.lower() in pathsMap or not end.lower() in pathsMap:
    return None
  return true_find_path(start.lower(), end.lower(), [])

# So after calling from helper we know our keys exist
# So we load each branch (element from list)
  # Follow the path down that path
  # and add element if found, nothing if not found
  # Recursion starts when current node == end node
def true_find_path(start: str, end: str, path: []) -> list:
  path.extend([start])
  
  if start == end:
    return path
  for node in pathsMap[start]:
    if node not in path:
      newpath = true_find_path(node, end, path)
      if newpath: 
        return newpath
  return None

# --- main code here: Class later lesson --- #
# first simple test (always write first
# - does it exit when one or both nodes don't exist
print(find_path("nope", "park")) # first wrong
print(find_path("park", "nope")) # second wrong
print(find_path("nope", "nope")) # both wrong

print(find_path("HoMe", "PaRk")) # right should work even with case issues

# finally (or current final test) - backwards
print(find_path('playground', 'home'))

""" prints:
None
None
None
['home', 'library', 'corner store', 'book store', 'school', 'park']
['playground', 'burgers n stuff', 'school', 'corner store', 'library', 'home']
"""
