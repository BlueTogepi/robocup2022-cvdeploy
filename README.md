# Robocup 2022 Model Deployment Repository

This repository is for deployment purpose inside the robot computer, which containerizes 3 models into 3 containers using docker-compose. The current models and their repositories are pulled from these repos:
* Person Tracker: https://github.com/palmpalmpalm/robocup2022-cv-what-is-that (adapted from https://robocupai2022.slack.com/archives/C02DXAD575E/p1643349758470469)
* What is That: https://github.com/palmpalmpalm/robocup2022-cv-what-is-that (adapted from https://github.com/icetenny/RoboCup-PoseEstimation and https://github.com/robocup-eic/cv)
* Object Detection: https://github.com/palmpalmpalm/robocup2022-cv-object-detection

All of the container acts as a Socket.io clients which will communicate with host's Python2 Socket.io (acting as a Socket.io server)