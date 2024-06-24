import io
import json
from openai import OpenAI


class Chat(object):
    def __init__(self, api_key, model):
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.messages = []
        self.responses = None
        self.speech_text = []

    def send(self):
        # 创建请求，发送message
        print(self.messages)
        self.response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

    def set_message(self, message):
        # 输入message，录入内存
        self.messages.append(message)

    def get_response(self, res_type='obj'):
        # 获取openai 的结果
        if self.responses is None:
            self.send()
        if res_type == 'obj':
            return self.response.choices[0]
        return json.dumps(json.loads(self.response.model_dump_json()), indent=4)

    def get_all_message(self):
        return self.messages

    def clear(self):
        # 清除message
        self.messages.clear()

    def upload(self, audio_file):
        # 上传音频文件，只能英语识别
        self.transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        self.speech_text.append(self.transcription.text)

    def get_transcription(self):
        # 获取响应内容
        return self.speech_text

    def set_audio_name(self, name):
        "设置音频文件名"
        self.audio_name = name

    def text_to_speech(self, audio_text):
        """文件转音频，并保存在文件中"""
        if self.audio_name is None:
            raise Exception('Audio name is None')
        self.speech_file_path = io.BytesIO()
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=audio_text
        )

        response.stream_to_file(self.audio_name)

    def get_audio_file(self):
        """获取音频文件"""
        with open(self.audio_name, 'rb') as audio_file:
            file_res = audio_file.read()
            return file_res


if __name__ == '__main__':
    api_key = ''
    model = 'gpt-3.5-turbo'
    chat = Chat(api_key, model)
    chat.set_message({'role': 'system', 'content': '你是一个聊天机器人'})
    print('GPT TEST')
    while True:
        message = input('')
        if message == 'n':
            break
        chat.set_message({'role': 'user', 'content': message})
        response = chat.get_response()
        print(response.message.content)
        chat.set_message({'role': response.message.role, 'content': response.message.content})
