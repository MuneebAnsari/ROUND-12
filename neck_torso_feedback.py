import math

TARGET_ANGLE = 150

feedback_neck_torso = open("feedback_neck_torso.txt", "a")
neck_torso_file = open("./keypoint_movement/neck_torso_info.txt", "r")

neck_torso_angles = []

nose_data = neck_torso_file.readline()
neck_data = neck_torso_file.readline()
torso_data = neck_torso_file.readline()
while nose_data and neck_data and torso_data:
    x = nose_data.split("|")
    y = neck_data.split("|")
    z = torso_data.split("|")

    if x and neck_data and torso_data:
        # x,y coordinates for keypoints from neck to torso
        nose_x, nose_y = x[1], x[2]
        neck_x, neck_y = y[1], y[2]
        torso_x, torso_y = z[1], z[2]

        vector_A = (float(nose_x) - float(neck_x), float(nose_y) - float(neck_y))
        vector_B = (float(torso_x) - float(neck_x), float(torso_y) - float(neck_y))

        A_dot_B = (vector_A[0] * vector_B[0]) + (vector_A[1] * vector_B[1])

        mag_A = math.sqrt(vector_A[0] ** 2 + vector_A[1] ** 2)
        mag_B = math.sqrt(vector_B[0] ** 2 + vector_B[1] ** 2)

        # Angle of neck and torso
        neck_torso_angle = math.degrees(math.acos(A_dot_B / (mag_A * mag_B)))

        neck_torso_angles.append(neck_torso_angle)

    nose_data = neck_torso_file.readline()
    neck_data = neck_torso_file.readline()
    torso_data = neck_torso_file.readline()

neck_torso_angle_avg = sum(neck_torso_angles) / len(neck_torso_angles)


if TARGET_ANGLE - 20 <= neck_torso_angle_avg <= TARGET_ANGLE + 20:
    feedback_neck_torso.write("Great posture/positioning to make moves offensively and defensively. "
                              "With your stance you can get a lot of power behind your punches.")
else:
    feedback_neck_torso.write("Posture is incorrect. Standing completely upright or bending forwards extensively will\
                              cause you to lose balance and you will have less power in your punches.")
