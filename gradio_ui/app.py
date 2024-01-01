#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-24 17:50
# describe：
import gradio as gr

from gradio_ui.tabs.video_demo import u_layout_video_demo

"""
Gradio interface
Reference：https://blog.csdn.net/LuohenYJ/article/details/127489768
Official Documents：https://github.com/gradio-app/gradio
"""


with gr.Blocks() as app:
    gr.Markdown("## VideoTools")
    with gr.Tab("VideoCompress"):
        u_layout_video_demo.create_layout()


app.launch(share=False, inbrowser=False, debug=True, server_name="0.0.0.0", server_port=7860)
