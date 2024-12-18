from g4f.client import Client
import gradio as gr

client = Client()

def generate_writing_prompt(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

interface = gr.Interface(
    fn=generate_writing_prompt,
    inputs=gr.Textbox(lines=3, placeholder="Enter your desired genre or tone..."),
    outputs="text",
    title="DostaaBot but a writer",
    description="Get inspired by DostaaBot, here to help you with your writing skills in any genre of your liking.",
    theme="hugging_face",
    examples=[
        ["A story where Spider-man gets exposed to gamma radiations and turns to Spider-Hulk?"],
        ["What if Bruce Wayne was The Joker?"],
        ["What if Tony Stark came to us before making JARVIS?"],

    ]
)
if __name__ == "__main__":
    interface.launch()