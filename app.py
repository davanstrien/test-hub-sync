import gradio as gr

gr.Interface(
    fn=lambda x: f"Hello {x}! This Space was synced from GitHub using huggingface/hub-sync.",
    inputs="text",
    outputs="text",
    title="Hub Sync Test",
).launch()
