Round 12 is a personal coaching application which allows boxers to demonstrate their punching technique and recieve feedback on their balance, positioning and overall punching technique.

Round 12 was created by [Muneeb Ansari](https://github.com/MuneebAnsari) and [Akram Eldamaty](https://github.com/AkramEld) as hack for Hack The 6ix 2018. For additional information please visit our submission on [devpost](https://devpost.com/software/hackthe6ix-g28jop)

Round 12 is an application that makes use of computer vision to detect and track keypoints on the humman body, which is known as human pose estimation. We used [tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation), a tensorflow and OpenCv based pose estimation library for python to detect and return the keypoints of the boxer.

Specific keypoints that were tracked include; (Head, left arm (shoulder, elbow wrist), right arm (shoulder, elbow, wrist), neck, torso, left leg, right leg)

![alt text](https://github.com/MuneebAnsari/ROUND-12/blob/master/testRun/full%20body/frame1ee625f7892a483dadf1c6a2cde9bfe1.jpg)

We processed a video of a boxer performing a punch, by analyzing the video in frames and determining the movement of the keypoints from frame to frame.

Depending on the relative poisition of the keypoints and the angles formed between certain keypoints we were able to determine the "correctness" of the punch. We compared the movement of the keypoints throuhgout the punch within a margin to determine if the punch was correct by focusing on the position of the boxer's guard/block arm, posture/positioning and jab extension.

Written feedback is provided on what the boxer did well and what the boxer should improve.


Next Steps: 
- Use data from professional boxers to train a model that determines what a correct punch truly is.
- Provide visual feedback, perhaps an overlay on the boxer's video demonstrating what their positioning should be.
