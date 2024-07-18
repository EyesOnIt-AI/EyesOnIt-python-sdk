import base64
from typing import List
import requests
import json
from .elements.eoi_object_description import EOIObjectDescription
from .elements.eoi_alerting import EOIAlerting
from .elements.eoi_bounding_box import EOIBoundingBox
from .elements.eoi_motion_detection import EOIMotionDetection
from .elements.eoi_region import EOIRegion
from .eoi_add_stream_inputs import EOIAddStreamInputs
from .eoi_monitor_stream_inputs import EOIMonitorStreamInputs
from .eoi_process_image_inputs import EOIProcessImageInputs
from .eoi_stream_url_input import EOIStreamUrlInput
from .eoi_response import EOIResponse
from .eoi_utils import decode_image


class EyesOnItSDK:

    def __init__(self, base_url):
        self.__base_url = base_url
        self.__process_image_path = "/process_image"
        self.__add_stream_path = "/add_stream"
        self.__remove_stream_path = "/remove_stream"
        self.__monitor_stream_path = "/monitor_stream"
        self.__stop_monitor_stream_path = "/stop_monitoring"
        self.__get_streams_info_path = "/get_streams_info"
        self.__get_last_detection_info_path = "/get_last_detection_info"
        self.__get_preview_video_frame_path = "/get_preview_video_frame"
        self.__get_video_frame_path = "/get_video_frame"
        self.__get_bounding_box_objects_path = "/get_bounding_box_objects"

    def process_image(self, object_descriptions: List[EOIObjectDescription], regions: List[EOIRegion], object_size: int, image):
        try:
            endpoint = self.__base_url + self.__process_image_path
            with open(image, "rb") as image_file:
                image = image_file.read()
            encoded_image = base64.b64encode(image).decode('utf-8')

            process_image_inputs = EOIProcessImageInputs(prompts=object_descriptions, regions=regions, object_size=object_size, file=encoded_image)
            response = requests.post(endpoint, json=process_image_inputs.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text["message"]
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def add_stream(self,
                   stream_url: str,
                   name: str,
                   regions: List[EOIRegion],
                   object_size: int,
                   object_descriptions: List[EOIObjectDescription],
                   alerting: EOIAlerting,
                   motion_detection: EOIMotionDetection = EOIMotionDetection(),
                   bounding_box: EOIBoundingBox = EOIBoundingBox(),
                   frame_rate: int = 5):
        try:
            endpoint = self.__base_url + self.__add_stream_path

            add_stream_inputs = EOIAddStreamInputs(stream_url=stream_url,
                                                   name=name,
                                                   regions=regions,
                                                   object_size=object_size,
                                                   prompts=object_descriptions,
                                                   alerting=alerting,
                                                   efficient_detection=motion_detection,
                                                   bounding_box=bounding_box,
                                                   frame_rate=frame_rate)

            response = requests.post(endpoint, json=add_stream_inputs.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text["message"]
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def monitor_stream(self, stream_url: str, duration_seconds: float = None):
        try:
            endpoint = self.__base_url + self.__monitor_stream_path
            monitor_stream_inputs = EOIMonitorStreamInputs(stream_url=stream_url, duration_seconds=duration_seconds)
            response = requests.post(endpoint, json=monitor_stream_inputs.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text["message"]
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def stop_monitoring(self, stream_url: str):
        try:
            endpoint = self.__base_url + self.__stop_monitor_stream_path
            stream_url_input = EOIStreamUrlInput(stream_url=stream_url)
            response = requests.post(endpoint, json=stream_url_input.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text["message"]
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def remove_stream(self, stream_url: str):
        try:
            endpoint = self.__base_url + self.__remove_stream_path
            stream_url_input = EOIStreamUrlInput(stream_url=stream_url)
            response = requests.post(endpoint, json=stream_url_input.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text["message"]
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def get_streams_info(self):
        try:
            endpoint = self.__base_url + self.__get_streams_info_path
            response = requests.get(endpoint)
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def get_video_frame(self, stream_url: str):
        try:
            endpoint = self.__base_url + self.__get_video_frame_path
            stream_url_input = EOIStreamUrlInput(stream_url=stream_url)
            response = requests.post(endpoint, json=stream_url_input.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                base64_image = response_text['image']
                image = decode_image(base64_image)
                response_text['image'] = image
                message = response_text
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def get_last_detection_info(self, stream_url: str):
        try:
            endpoint = self.__base_url + self.__get_last_detection_info_path
            stream_url_input = EOIStreamUrlInput(stream_url=stream_url)
            response = requests.post(endpoint, json=stream_url_input.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                base64_image = response_text['image']
                image = decode_image(base64_image)
                response_text['image'] = image
                message = response_text
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def get_preview_video_frame(self, stream_url: str):
        try:
            endpoint = self.__base_url + self.__get_preview_video_frame_path
            stream_url_input = EOIStreamUrlInput(stream_url=stream_url)
            response = requests.post(endpoint, json=stream_url_input.model_dump())
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                base64_image = response_text['image']
                image = decode_image(base64_image)
                response_text['image'] = image
                message = response_text
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))

    def get_bounding_box_objects(self):
        try:
            endpoint = self.__base_url + self.__get_bounding_box_objects_path
            response = requests.get(endpoint)
            response_text = json.loads(response.text)
            success = True if response.status_code == 200 else False

            if success:
                message = response_text
            else:
                message = response_text["detail"]

            eoi_response = EOIResponse(success, message=message)
            return eoi_response

        except Exception as e:
            return EOIResponse(success=False, message=repr(e))
