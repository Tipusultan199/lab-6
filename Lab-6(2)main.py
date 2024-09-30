import sympy as sp

# Define symbolic variables for joint angles
t1, t2, t3, t4 = sp.symbols('t1 t2 t3 t4')

# Define the skew-symmetric matrices for symbolic computation
z_hat_bracket = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
y_hat_bracket = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])

# Rodrigues' formula for symbolic computation
def rodrigues_formula_sym(hat_matrix, theta):
    return sp.eye(3) + sp.sin(theta) * hat_matrix + (1 - sp.cos(theta)) * (hat_matrix * hat_matrix)

# Compute the exponentials
e_bracket_z_t1 = rodrigues_formula_sym(z_hat_bracket, t1)
e_bracket_y_t2 = rodrigues_formula_sym(y_hat_bracket, t2)
e_bracket_y_t3 = rodrigues_formula_sym(y_hat_bracket, t3)
e_bracket_y_t4 = rodrigues_formula_sym(y_hat_bracket, t4)

# Multiply the exponentials to get the final orientation matrix
result = e_bracket_z_t1 @ e_bracket_y_t2 @ e_bracket_y_t3 @ e_bracket_y_t4

# Simplify the result
simplified_result = sp.simplify(result)

# Display the simplified result
sp.pprint(simplified_result)

# Now equate the result to the desired orientation and solve for the joint angles
desired_orientation = sp.Matrix([[-1, 0, 0], [0, 0, -1], [0, -1, 0]])

# Solve the system of equations
solution = sp.solve(sp.Eq(simplified_result, desired_orientation), [t1, t2, t3, t4])

# Print the solution
print("Joint angles that achieve the desired orientation:")
print(solution)
