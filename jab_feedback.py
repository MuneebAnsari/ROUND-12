import math

feedback_jab = open("feedback_jab.txt", "a")
jab_hand_file = open("./keypoint_movement/jab_hand_info.txt", "r")

right_shoulder_data = jab_hand_file.readline()
right_elbow_data = jab_hand_file.readline()
right_wrist_data = jab_hand_file.readline()

shoulder_wrist_angles = []

while right_shoulder_data:
    x = right_shoulder_data.split("|")
    z = right_elbow_data.split("|")
    y = right_wrist_data.split("|")

    if x and right_elbow_data and right_wrist_data:
        # x,y coordinates for keypoints on guard arm
        right_shoulder_x, right_shoulder_y = x[1], x[2]
        right_elbow_x, right_elbow_y = z[1], z[2]
        right_wrist_x, right_wrist_y = y[1], y[2]

        vector_A = (float(right_shoulder_x) - float(right_elbow_x), float(right_shoulder_y) - float(right_elbow_y))
        vector_B = (float(right_wrist_x) - float(right_elbow_x), float(right_wrist_y) - float(right_elbow_y))

        # vector_C = (float(right_shoulder_x) - float(right_wrist_x), float(right_shoulder_y) - float(right_elbow_y))
        A_dot_B = (vector_A[0] * vector_B[0]) + (vector_A[1] * vector_B[1])

        mag_A = math.sqrt(vector_A[0] ** 2 + vector_A[1] ** 2)
        mag_B = math.sqrt(vector_B[0] ** 2 + vector_B[1] ** 2)
        # mag_C = math.sqrt(vector_C[0] ** 2 + vector_C[1] ** 2)

        # Angle of guard arm
        shoulder_wrist_angle = math.degrees(math.acos(A_dot_B / (mag_A * mag_B)))
        shoulder_wrist_angles.append(shoulder_wrist_angle)

    # shoulder_wrist_angle = math.degrees((math.acos(mag_A**2 + mag_B**2 - mag_C**2) / (2*mag_A*mag_B)))
    right_shoulder_data = jab_hand_file.readline()
    right_elbow_data = jab_hand_file.readline()
    right_wrist_data = jab_hand_file.readline()


print(max(shoulder_wrist_angles))
if 130 <= max(shoulder_wrist_angles) < 170:
    feedback_jab.write("Great extension on that jab. With a jab as controlled as yours you will be able to "
                       "keep your distance from your opponents.")
elif 115 <= max(shoulder_wrist_angles) < 130:
    feedback_jab.write("Make sure to maximize your reach when you jab. An accurate and strong jab will help you get"
                       "away from tough situations.")
elif max(shoulder_wrist_angles) <= 115:
    feedback_jab.write("Throw that jab like you mean it. Half hartedness isn't going to get the job done.")
elif max(shoulder_wrist_angles) >= 170:
    feedback_jab.write("Loosen up! Extensive extension of the arm can cause injury.")
