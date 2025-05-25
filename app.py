import gradio as gr
import spaces
from transformers import pipeline

# Initialize Model
get_completion = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0)

@spaces.GPU(duration=120)
def summarize(input: str) -> str:
    """
    Summarize the given input text using the sshleifer/distilbart-cnn-12-6 model.

    Args:
        input (str): The text to be summarized.

    Returns:
        str: The summarized version of the input text.
    """
    output: List[Dict[str, str]] = get_completion(input)
    return output[0]['summary_text']

####### GRADIO APP #######
title = """<h1 id="title"> Text Summarization </h1>"""

description = """
- The model used for Summarizing Text [DISTILBART-12-6-CNN](https://huggingface.co/sshleifer/distilbart-cnn-12-6).
"""

css = '''
h1#title {
  text-align: center;
}
'''

theme = gr.themes.Soft()
demo = gr.Blocks(css=css, theme=theme)

with demo:
  gr.Markdown(title)
  gr.Markdown(description)
  interface = gr.Interface(fn=summarize, 
                    inputs=[gr.Textbox(label="Text to Summarize", lines=15)], 
                    outputs=[gr.Textbox(label="Result", lines=7)],
                    examples=["""Artificial Intelligence (AI) has been a rapidly growing field over the past decade, transforming various industries such as healthcare, finance, and transportation. 
                                 One of the key areas of AI research is machine learning, which focuses on developing algorithms that allow computers to learn from and make decisions based on data. 
                                 Recent advancements in deep learning, a subset of machine learning, have led to significant breakthroughs in image and speech recognition, natural language processing, and autonomous systems. 
                                 As AI continues to evolve, it is expected to play an increasingly important role in solving complex problems, enhancing productivity, and driving innovation across different sectors.""",
                               """The tower is 324 metres (1,063 ft) tall, about the same height
                                as an 81-storey building, and the tallest structure in Paris. 
                                Its base is square, measuring 125 metres (410 ft) on each side. 
                                During its construction, the Eiffel Tower surpassed the Washington 
                                Monument to become the tallest man-made structure in the world,
                                a title it held for 41 years until the Chrysler Building
                                in New York City was finished in 1930. It was the first structure 
                                to reach a height of 300 metres. Due to the addition of a broadcasting 
                                aerial at the top of the tower in 1957, it is now taller than the 
                                Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the 
                                Eiffel Tower is the second tallest free-standing structure in France 
                                after the Millau Viaduct."""
                             ],
                    cache_examples=True
                   )
demo.launch()