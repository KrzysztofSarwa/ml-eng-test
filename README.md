# Machine Learning Engineer Test: Computer Vision and Object Detection

## Objective
This test aims to assess your skills in computer vision and object detection, with a specific focus on detecting room walls and identifying rooms in architectural blueprints or pre-construction plans.

This test evaluates your practical skills in applying advanced computer vision techniques to a specialized domain and your ability to integrate machine learning models into a simple API server for real-world applications.

Choose one of the visual tasks, one of the text extraction tasks, and the API Server task. We encourage you to submit your tests even if you can’t complete all tasks.

Good luck!


## Full test description
[Senior Machine Learning Engineer.pdf](https://github.com/TrueBuiltSoftware/ml-eng-test/files/14545316/Senior.Machine.Learning.Engineer.1.pdf)

## PS
Share your project with the following GitHub users:
- vhaine-tb
- omasri-tb
- alexwine36

## Building Docker Image:
```
cd src
docker build -t ml-eng-test .
```

## Running Docker Container:
```
docker run -it -p 8000:8000 ml-eng-test
```

## Testing API with cURL:
Example cURL:
```
cd src
curl -X POST "http://127.0.0.1:8000/run-inference?type=room" -F "image=@data/Rooms/Room_img_masked/mask__13.jpg"
```
