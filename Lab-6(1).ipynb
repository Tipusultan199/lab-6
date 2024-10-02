import numpy as np
# Set print options to avoid scientific notation
np.set_printoptions(suppress=True)
# Angles in radians
theta_1 = np.pi / 2
theta_2 = -np.pi / 4
theta_3 = 0
theta_4 = np.pi / 4

# Skew-symmetric matrices
z_hat_bracket = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
y_hat_bracket = np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])

# Rodrigues' formula to compute the exponentials
def rodrigues_formula(hat_matrix, theta):
    return np.eye(3) + np.sin(theta) * hat_matrix + (1 - np.cos(theta)) * np.dot(hat_matrix, hat_matrix)

# Calculate the rotation matrices
e_z_hat_bracket_theta_1 = rodrigues_formula(z_hat_bracket, theta_1)
e_y_hat_bracket_theta_2 = rodrigues_formula(y_hat_bracket, theta_2)
e_y_hat_bracket_theta_3 = rodrigues_formula(y_hat_bracket, theta_3)
e_y_hat_bracket_theta_4 = rodrigues_formula(y_hat_bracket, theta_4)

# Calculate the final rotation matrix (product of exponentials)
R = np.dot(np.dot(np.dot(e_z_hat_bracket_theta_1, e_y_hat_bracket_theta_2), e_y_hat_bracket_theta_3), e_y_hat_bracket_theta_4)

# Print the final rotation matrix
print("Final Rotation Matrix R:")
print(R)
