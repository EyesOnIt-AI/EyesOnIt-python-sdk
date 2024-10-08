# EYESONIT Python SDK #

EyesOnIt makes advanced computer vision accessible to anyone without data science or computer programming skills. Through the EyesOnIt configuration user interface, you can use English text to describe the objects and events that you want to detect. You can monitor your video streams and start receiving alerts by text message in just a few minutes. If you have basic programming skills, you can use our SDK or REST API to quickly enable endless scenarios like these:

- Motion-based detection: trigger computer vision after motion is detected
- Event recording: capture and store your own data about detections
- Image categorization: categorize a collection of images according to the contents

Traditional computer vision involves a complex process to train and tune a computer vision model. This process typically requires weeks or months of time from experts with an advanced and specialized skillset. The cost for this process is often $50,000 to $100,000 USD or more. EyesOnIt is different. With EyesOnIt, you describe what you want to detect with English text. EyesOnIt compares your text to your image or video and tells you if it detected what you described.

See this documentation to learn how to download and run the EyesOnIt Docker container:
https://developer.eyesonit.us/documentation/

### Installation ###

The python SDK can be installed with PIP

```
pip install EyesOnIt
```

### Usage ###

```
from EyesOnIt import EyesOnItSDK, EOIPrompt, EOIRegion


prompt_one = EOIPrompt(text='person', background_prompt=False, threshold=90)
prompt_two = EOIPrompt(text='trees', background_prompt=True)
prompts = [prompt_one, prompt_two]

region_one = EOIRegion(top_left_x=4, top_left_y=9, width=300, height=300)
regions = [region_one]


app = EyesOnItSDK('http://127.0.0.1:8000')

result = app.process_image(prompts=prompts, regions=regions, image="my_image.png")
print(result.success)
print(result.message)

```

### Questions? ###

email us at support@eyesonit.us
