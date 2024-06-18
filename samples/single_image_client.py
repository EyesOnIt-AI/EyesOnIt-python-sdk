from EyesOnIt import EyesOnItSDK
from data.elements.eoi_prompt import EOIPrompt
from data.elements.eoi_region import EOIRegion

prompt_one = EOIPrompt(text='person', background_prompt=False, threshold=90)
prompt_two = EOIPrompt(text='trees', background_prompt=True)
prompts = [prompt_one, prompt_two]

region_one = EOIRegion(top_left_x=4, top_left_y=9, width=300, height=300)
regions = [region_one]


app = EyesOnItSDK('http://127.0.0.1:8000')

result = app.process_image(prompts=prompts, regions=regions, image="my_image.png")
print(result.success)
print(result.message)
