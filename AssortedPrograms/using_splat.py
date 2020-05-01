class vector_math:
    '''
    This is the base class for vector math - which allows for initialization with two vectors.
    This is how I would go back through and change using the spat method
    Allowing one to just pass a set of vectors as a list of lists
    '''
    
    def __init__(self, vectors = [[1,2,2],[3,4,3]]):
        self.vect = vectors
        
    def set_vects(self, vectors):
        self.vect = vectors
    
    def sum_vects(self):
        return [x + y for x, y in zip(*self.vect)]
    
    def sub_vects(self):
        # default should be [-2,-2,-1]
        return [x - y for x, y in zip(*self.vect)]
        # Can expand out to for x, y in zip: ... to show what it and sum do
    
    def multi_vects(self):
        #default should be [3,8,6]
        return [x * y for x, y in zip(*self.vect)]
    
    def multi_scalar(self, scalar, vect):
        return [e * scalar for e in vect]
        # Show difference between just element * number and using tuple from zip()
        
    def multi_scalar_l(self, scalar, vect):
        return lambda e: e * scalar, vect
        
    def mean_vects(self):
        mean_vect = self.sum_vects()
        return self.multi_scalar(1/len(mean_vect), mean_vect)
        
    def dot_product(self):
        return sum(self.multi_vects())
    
vect = vector_math()

sum_vect = vect.sum_vects()
print("Sum of vectors = {}".format(sum_vect))

print("Subtraction of vectors = {}".format(vect.sub_vects()))
print("Product of vectors = {}".format(vect.multi_vects()))
print("Product of Sum of vectors and 2 = {}\n".format(vect.multi_scalar(2, sum_vect)))
# Yep can still use character returns and others in format

print("Average of vectors = {}".format(["{:.2f}".format(e) for e in vect.mean_vects()]))

print("The Dot Product is {}".format(vect.dot_product()))
