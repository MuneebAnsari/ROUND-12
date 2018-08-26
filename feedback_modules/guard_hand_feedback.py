import math

TARGET_ANGLE = 50

feedback_guard_hand = open("feedback_guard_hand.txt", "a")
guard_hand_file = open("../keypoint_movement/block_hand_info.txt", "r")

guard_arm_angles = []

left_shoulder_data = guard_hand_file.readline()

while left_shoulder_data:
    x = left_shoulder_data.split("|")
    left_elbow_data = guard_hand_file.readline().split("|")
    left_wrist_data = guard_hand_file.readline().split("|")

    # x,y coordinates for keypoints on guard arm
    left_shoulder_x, left_shoulder_y = x[1], x[2]
    left_elbow_x, left_elbow_y = left_elbow_data[1], left_elbow_data[2]
    left_wrist_x, left_wrist_y = left_wrist_data[1], left_wrist_data[2]



    vector_A = (float(left_shoulder_x) - float(left_elbow_x), float(left_shoulder_y) - float(left_elbow_y))

    vector_B = (float(left_wrist_x) - float(left_elbow_x), float(left_wrist_y) - float(left_elbow_y))


    A_dot_B = (vector_A[0] * vector_B[0]) + (vector_A[1] * vector_B[1])

    mag_A = math.sqrt(vector_A[0]**2 + vector_A[1]**2)

    mag_B = math.sqrt(vector_B[0]**2 + vector_B[1]**2)


    # Angle of guard arm
    guard_arm_angle = math.degrees(math.acos(A_dot_B / (mag_A * mag_B)))

    guard_arm_angles.append(guard_arm_angle)

    left_shoulder_data = guard_hand_file.readline()


guard_arm_angle_avg = sum(guard_arm_angles) / len(guard_arm_angles)

print(guard_arm_angle_avg)

if TARGET_ANGLE - 5 <= guard_arm_angle_avg <= TARGET_ANGLE + 5:
    feedback_guard_hand.write("Great way to protect yourself in the ring. Keep up the great work!")
elif TARGET_ANGLE - 15 <= guard_arm_angle_avg <= TARGET_ANGLE + 15:
    feedback_guard_hand.write("Good work, remember to keep your guard arm up at all times. Keep trying!")
else:
    feedback_guard_hand.write("Don't be lazy! Keep your guard hand up and protect yourself at all times")
