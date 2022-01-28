# Robocup 2022 Model Deployment Repository

This repository is for deployment purpose inside the robot computer, which containerizes 3 models into 2 containers using docker-compose. The current models and their repositories are pulled from these repos:
* Pose Estimation: https://github.com/icetenny/RoboCup-PoseEstimation, Object Detection: https://github.com/robocup-eic/cv
* Person Tracking: https://robocupai2022.slack.com/archives/C02DXAD575E/p1643349758470469

All of the container acts as a Socket.io clients which will communicate with host's Python2 Socket.io (acting as a Socket.io server)