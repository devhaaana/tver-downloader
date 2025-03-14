import os
import re
import sys
import shlex
import pathlib
import urllib3
import urllib.parse
import subprocess

from utils import *

class Tver_Downloader():
    def __init__(self):
        self.tver_platform_api = f'https://platform-api.tver.jp'
        self.platform_type = 'web'
        self.device_type = 'pc'
        
        self.http = urllib3.PoolManager()
        self.headers = {
            'x-tver-platform-type': self.platform_type
        }
        
        self.tab = '    '
        self.url, self.mode, self.content_id  = self.get_url()
        self.content = self.get_Episode_Info()
        self.sep_bar = f"\n{'=' * (len(self.content['title']) * 4)}\n"
        self.check_content()
        
    def get_url(self):
        while True:
            print(convert_text_color(text="\n[Enter] Enter the URL of the 'episode' or 'series'", color='yellow'))
            url = input(convert_text_color(text='[Enter]: ', color='yellow'))
            
            episode_pattern = r"^https://tver\.jp/episodes/([a-z0-9]+)$"
            series_pattern = r"^https://tver\.jp/series/([a-z0-9]+)$"
            print(convert_text_color(text=f'\n[Check] System is checking the URL...', color='blue'))
            
            match_episode = re.match(pattern=episode_pattern, string=url)
            match_series = re.match(pattern=series_pattern, string=url)
            
            if match_episode:
                print(convert_text_color(text=f'[Check] OK...', color='blue'))
                episode_id = match_episode.group(1)
                return url, 'Episode', episode_id
            elif match_series:
                print(convert_text_color(text=f'[Check] OK...', color='blue'))
                series_id = match_series.group(1)
                return url, 'Series', series_id
            else:
                print(convert_text_color(text='[Error] Invalid URL, please try again.', color='red'))
            
    def access_Authentication(self):
        url = f'{self.tver_platform_api}/v2/api/platform_users/browser/create'
        
        data = f'device_type={
            self.device_type
        }'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self.http.request(method='POST', url=url, body=data, headers=headers).json()
        
        return response['result']

    def get_Episode_Info(self):
        accessTokens = self.access_Authentication()
        platform_uid = accessTokens['platform_uid']
        platform_token = accessTokens['platform_token']
        
        mode = self.mode
        if mode == 'Series':
            mode = 'SeriesEpisodes'
        
        data = {
            'platform_uid': platform_uid,
            'platform_token': platform_token,
            'require_data': 'mylist,later[epefy106ur],good[epefy106ur],resume[epefy106ur]'
        }
        query = urllib.parse.urlencode(data)
        url = f'{self.tver_platform_api}/service/api/v1/call{mode}/{self.content_id}?{query}'
        
        response = self.http.request(method='GET', url=url, headers=self.headers).json()
        
        if mode == 'Episode':
            return response['result']['episode']['content']
        elif mode == 'SeriesEpisodes':
            return response['result']['contents'][0]['contents'][0]['content']
    
    def check_content(self):
        print(convert_text_color(text=f"[Information] System is '{self.mode}' mode...", color='blue'))
        print(convert_text_color(text=f'[Load] System is Loading the content information...', color='blue'))
        print(self.sep_bar)
        print(convert_text_color(text=f'[{self.mode} Information]\n', color='green'))
        print(f'Broadcast: {self.content['broadcasterName']}')
        print(f'Series Title: {self.content['seriesTitle']}')
        if self.mode == 'Episode':
            print(f'Date: {self.content['broadcastDateLabel']}')
            print(f'Episode Title: {self.content['title']}')
        print(self.sep_bar)
        
        check = input(convert_text_color(text='[Check] Is it right? [Y/n] ', color='yellow'))
        
        if check.lower() != 'y':
            self.url, self.mode, self.content_id  = self.get_url()
            self.content_id = pathlib.PurePath(urllib.parse.urlparse(self.url).path).name
            self.content = self.get_Episode_Info()
            self.check_content()
    
    def get_Program_Path(self, cmd_name):
        try:
            if subprocess.getstatusoutput(f'type {cmd_name}')[0] == 0:
                return subprocess.check_output(f'which {cmd_name}', shell=True).strip().decode('utf8')
            else:
                print(f'{cmd_name} not found, install {cmd_name}')
                sys.exit()
        except Exception as e:
            print(f"[Error] Getting program path for {cmd_name}: {e}")
        return ''

    def get_yt_dlp_Command(self):
        try:
            ydl_option = {
                '--quiet': True,
                '--write-sub': True,
                '--embed-subs': True,
            }
            
            command = "yt-dlp"
            for key, value in ydl_option.items():
                if isinstance(value, list):
                    for val in value:
                        command += f" {key} {val}"
                elif value is True:
                    command += f" {key}"
                else:
                    command += f" {key} {value}"
            return command
        except Exception as e:
            print(f"[Error] Generating FFmpeg command: {e}")
            
        return ''

    def get_FFmpeg_Command(self, save_dir) -> str:
        try:
            program_path = self.get_Program_Path('ffmpeg')
            ffmpeg_option = {
                '--ffmpeg-location': f'"{program_path}"',
                '-n': True,
                '-i': True,
                'url': f'"{self.url}"',
                '--concurrent-fragments': 8,
                '--reject-title': '解説放送版|ダイジェスト|予告|ナビ|イベント|配信限定',
                '--output': f'{save_dir}/%(episode)s/%(episode)s.%(ext)s'
            }
            
            command = ""
            for key, value in ffmpeg_option.items():
                if isinstance(value, list):
                    for val in value:
                        command += f' {key} {val}'
                elif value is True:
                    command += f' {key}'
                elif key == 'url':
                    command += f' {value}'
                else:
                    command += f' {key} {value}'
            return command
        except Exception as e:
            print(f"[Error] Generating FFmpeg command: {e}")
        return ''
            
    def get_Command(self):
        self.save_dir = f'./data/{self.content['broadcasterName']}/{self.content['seriesTitle']}'
        os.makedirs(self.save_dir, exist_ok=True)
        
        yt_dlp_cmd = self.get_yt_dlp_Command()
        ffmpeg_cmd = self.get_FFmpeg_Command(save_dir=self.save_dir)
        command = f'{yt_dlp_cmd} {ffmpeg_cmd}'
        
        return command

    def save_mp4_file(self, command):
        command_split = shlex.split(command)
        
        print(self.sep_bar)
        try:
            print(convert_text_color(text=f'[Download] System is downloading the video...', color='blue'))
            # process = subprocess.Popen(command_split)
            # process.communicate()
            print(convert_text_color(text=f"[Download] System successfully downloaded to '{self.save_dir}'", color='green'))
        except Exception as e:
            print(convert_text_color(text=f"[Error] {e}", color='red'))
        print(self.sep_bar)

    def run_process(self):
        command = self.get_Command()
        self.save_mp4_file(command)

    