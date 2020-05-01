#We will use a standard version using a generator
#Wanted to ensure a recursive version was provided as well though

def squash(vec):
    if not vec:
        return [] #if empty return empty
    return [e for e in flatten(vec) if e]
        

def flatten(v):
    if not v:
        return []
    if hasattr(v[0], '__iter__') and not isinstance(v[0], str):
        memorize = flatten(v[0])
        memorize.extend(flatten(v[1:]))
        return memorize
    else:
        memorize = flatten(v[1:])
        memorize.insert(0, v[0])
        return memorize

a = ['a', ['b', ['e', 'f'], 'd'], 'c']
print(squash(a))
