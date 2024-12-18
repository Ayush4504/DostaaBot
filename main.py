from g4f.client import Client
import gradio as gr

client = Client()

def chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

Interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your query here, Dostaa will resolve it..!"),
    outputs="text",
    title="DostaaBot",
    description="Dostaa is here for you..!"
)

if __name__ == "__main__":
    Interface.launch()