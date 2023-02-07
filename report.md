# Report

## Abstract:

The vital extraction challenge aims to extract the vitals of a patient from an image of the patient monitor. Monitoring vitals is a critical aspect of providing high-quality care to patients and is essential for ensuring the best possible patient outcomes. While current guidelines state that the nurse-to-patient ratio should be 1:6, various practical issues result in a much worse scenario. This is why it is important to find newer and more efficient solutions to help solve this problem.

While it would be preferable to skip the camera-based monitoring system and directly feed the vitals into a common server, we recognize the fact that this solution is not an efficient solution for ICUs around India that are already up and running. There is a need to augment the existing ICU environments in order to capture the necessary vitals from an “offline” patient monitor and feed it into an “online” server for monitoring.

Precisely, this is the task assigned to us. This challenge required the development of a pipeline to first detect and segment the screen of the monitor from the image and then detect, segment, and understand the various vitals present on the screen.

## Pipeline: 

We propose to solve the task with a 3-step solution namely, Preprocessing, Vital Detection, and OCR. Lastly, we tackled the HR Graph digitization 

### Preprocessing 

First, there is the segmentation of the monitor screen and separating it from the surroundings. Secondly, we have to scale the segmented screen to a uniform size for later stages, while preserving the original resolution as much as possible.

### Vital Detection 

The objective of this stage in the pipeline is to detect the appropriate vitals in the cropped and transformed monitor screen. However, there was a lot of unlabelled data, and manually annotating all 9000 images was not an option. And it will never be a good solution, in any real-world scenario. We identified two methods to deal with the vast amount of unlabelled data. 

One approach was to use a customized Semi-Supervised Learning Model, which would learn from the small amount of labeled data and use it to generate pseudo labels and then true labels for the unlabelled data. 

Another approach was to intelligently pick and manually annotate a small amount of unlabelled data, and then add it to the training dataset in order to bring maximum diversity and representation to the training data without much effort. This approach was chosen because of its better results and lesser computational requirement.

### OCR 

Finally, we applied an OCR to extract the values of the vitals. Considering the standardized fonts used on patient monitors, this was not a particularly difficult task. However, there were a few misreads in the final result, such as “0” being read as “o” or “O”, “1” being read as “I”, etc. Due to some detection inaccuracies, we would also see brackets creep into the detection box. Due to segmentation faults sometimes the numbers at the left corner of the screen (most usually 

### HR Graph Digitization: 

Initially we converted the HR graph segmented image into binary. In order to selectively obtain only the graph, the longest connected pixels row-wise were saved and the rest discarded. The 2-D binary image was then projected into a 1-D Time Series. The plot was further rescaled in the x and y variables.


## Segmentation:

| Model | Epochs | Box Precision | Box Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|---|
| YOLOv8n | 1 | 1 | 1 | 1 | 1 |
| YOLOv8s | 1 | 1 | 0.995 | 0.987 |
| Segformer | 35 | 
| Mask RCNN | 250 |  |  | 0.99 | 0.918 |

## Detection:

| Model | Epochs | Box Precision | Box Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|---|
| YOLOv8n | 25 | 0.986 | 0.993 | 0.99 | 0.831 |
| YOLOv8s | 100 | 0.983 | 0.989 | 0.988 | 0.849 |
| YOLOv8m | 100 | 0.981 | 0.988 | 0.989 | 0.841 |
| YOLOv7 (R) |  | 0.991 | 0.996 | 0.993 | 0.83 |
| YOLOv6 | 200 |  |  | 0.954 | 0.721 |
| DETR | 45 |  |  | 0.979 | 0.688 |
