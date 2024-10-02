import numpy as np

np.set_printoptions(suppress=True)

theta_1 = np.pi / 2
theta_2 = -np.pi / 4
theta_3 = 0
theta_4 = np.pi / 4


z_hat_bracket = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
y_hat_bracket = np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])


def rodrigues_formula(hat_matrix, theta):
    return np.eye(3) + np.sin(theta) * hat_matrix + (1 - np.cos(theta)) * np.dot(hat_matrix, hat_matrix)

e_z_hat_bracket_theta_1 = rodrigues_formula(z_hat_bracket, theta_1)
e_y_hat_bracket_theta_2 = rodrigues_formula(y_hat_bracket, theta_2)
e_y_hat_bracket_theta_3 = rodrigues_formula(y_hat_bracket, theta_3)
e_y_hat_bracket_theta_4 = rodrigues_formula(y_hat_bracket, theta_4)

R = np.dot(np.dot(np.dot(e_z_hat_bracket_theta_1, e_y_hat_bracket_theta_2), e_y_hat_bracket_theta_3), e_y_hat_bracket_theta_4)

# Print the final rotation matrix
print("Final Rotation Matrix R:")
print(R)
