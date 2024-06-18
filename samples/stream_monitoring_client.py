import time
from EyesOnIt import EyesOnItSDK
from data.elements.eoi_prompt import EOIPrompt
from data.elements.eoi_region import EOIRegion
from data.elements.eoi_alerting import EOIAlerting
from data.elements.eoi_efficient_detection import EOIEfficientDetection
from data.elements.eoi_bounding_box import EOIBoundingBox


prompt_one = EOIPrompt(text='person', background_prompt=False, threshold=90)
prompt_two = EOIPrompt(text='trees', background_prompt=True)
prompts = [prompt_one, prompt_two]

region_one = EOIRegion(top_left_x=4, top_left_y=9, width=500, height=300)
regions = [region_one]

alerting_settings = EOIAlerting(alert_seconds_count=2, reset_seconds_count=60)

efficient_detection_settings = EOIEfficientDetection(periodic_check_enabled=True, periodic_check_seconds=1)

bounding_box_settings = EOIBoundingBox(bounding_box_enabled=False)

app = EyesOnItSDK('http://127.0.0.1:8000')


result = app.add_stream(stream_url='rtsp://192.168.0.10:654/00000001-0000-babe-0000-b8a44f754706/live',
                        name='my_demo_stream',
                        frame_rate=5,
                        prompts=prompts,
                        regions=regions,
                        alerting=alerting_settings,
                        efficient_detection=efficient_detection_settings,
                        bounding_box=bounding_box_settings)
print(result.success)
print(result.message)

time.sleep(5)

# if you don't specify duration_seconds the stream is monitored indefinitely
result = app.monitor_stream(stream_url='rtsp://192.168.0.10:654/00000001-0000-babe-0000-b8a44f754706/live',
                            duration_seconds=120)
print(result.success)
print(result.message)

time.sleep(15)

result = app.get_bounding_box_objects()
print(result.success)
print(result.message)

time.sleep(5)

result = app.get_streams_info()
print(result.success)
print(result.message)

time.sleep(5)

result = app.get_video_frame(stream_url='rtsp://192.168.0.10:654/00000001-0000-babe-0000-b8a44f754706/live')
print(result.success)
image_from_stream = result.message['image']
image_from_stream.save('my_video_frame.jpg')

time.sleep(5)

result = app.stop_monitoring(stream_url='rtsp://192.168.0.10:654/00000001-0000-babe-0000-b8a44f754706/live')
print(result.success)
print(result.message)

time.sleep(5)

result = app.remove_stream(stream_url='rtsp://192.168.0.10:654/00000001-0000-babe-0000-b8a44f754706/live')
print(result.success)
print(result.message)
