## Usage

#### Scenario #01
- Dataset image: `00.jpg`
- Recognized objects
    - `Number of person`: 1
    - `Number of flag`: 1
- Description:
    1. Detect person (index=0) and flag (index=1), 
    2. Merge detected person and flag.
    3. Draw its bounding box.
    4. Crop and save it.
- How to run:
```python
./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights -ext_output sample_dataset/00.jpg
```
- Generated results:
    - Image of person: `results/img_1_1_0_person.jpg.jpg`
    - Merged images: `results/merged_img_1_33_Person-Flag.jpg.jpg`
