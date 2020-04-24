from vector import Vector
v1 = Vector(3)
print("Vector(3): " + str(v1.values))
v1 = Vector((5, 8))
print("Vector((5,8)): " + str(v1.values))
v1 = Vector([10.0, 11.0, 12.0, 13.0])
print("v1.values: " + str(v1.values))
print("v1.size: " + str(v1.size))
v2 = v1 + 5
print("v1.__add__: " + str(v2))
v2 = v1.__radd__(5)
print("v1.__radd__: " + str(v2))
v2 = v1 - 5
print("v1.__sub__: " + str(v2))
v2 = v1.__rsub__(5)
print("v1.__rsub__: " + str(v2))
v2 = v1 / 5
print("v1.__truediv__: " + str(v2))
v2 = v1.__rtruediv__(5)
print("v1.__rtruediv__: " + str(v2))
v2 = v1 * 5
print("v1.__mul__: " + str(v2))
v2 = v1.__rmul__(5)
print("v1.__rmul__: " + str(v2))
print("v1.__str__: " + str(v1))
print("v1.__repr__(v1): " + str(v1.__repr__(v1)))
