#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:40
# describe：
import gradio as gr

from gradio_ui.tabs.video_demo import u_handler_video_demo
from utils.video.enums import AudioFormatEnum


def create_layout():
    """ build layout """
    with gr.Row().style(equal_height=True):
        with gr.Column(scale=1):
            input_path_single = gr.Textbox(show_label=True, label="InputPath", placeholder="[SINGLE] Please enter the video path to be compressed", lines=1, max_lines=1)
            input_dir = gr.Textbox(show_label=True, label="InputDir", placeholder="[BATCH] Please enter the video dir to be compressed", lines=1, max_lines=1)
            output_path = gr.Textbox(show_label=True, label="OutputDir", placeholder="[OPTIONAL] Please enter the video output dir", lines=1, max_lines=1)
            with gr.Row().style(equal_height=True):
                target_bitrate = gr.components.Dropdown(
                    choices=[f"{i}M" for i in range(1, 11)],
                    label="target_bitrate",
                    value="1M"
                )
                audio_separation_format = gr.components.Dropdown(
                    choices=[member.value for member in AudioFormatEnum],
                    label="audio_separation_format",
                    value=""
                )
                without_audio = gr.inputs.Checkbox(label="without_audio", default=False)
            with gr.Row().style(equal_height=True):
                button_load = gr.Button("LoadCache")
                button = gr.Button("Submit")
        with gr.Column(scale=1):
            result = gr.Textbox(
                label="ResultInfo",
                placeholder="Show the result info here",
                lines=20,
                max_lines=20
            )
    button.click(u_handler_video_demo.handler, inputs=[input_path_single, input_dir, output_path, target_bitrate, audio_separation_format, without_audio], outputs=[result])
    button_load.click(u_handler_video_demo.load, inputs=[], outputs=[input_path_single, input_dir, output_path, target_bitrate, audio_separation_format, without_audio])
