from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class StoryAI(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="STORY AI",
            font_size=32,
            size_hint_y=None,
            height=70
        )

        story = TextInput(
            hint_text="Enter your story here...",
            multiline=True
        )

        video_button = Button(
            text="🎬  CREATE VIDEO",
            size_hint_y=None,
            height=60
        )

        image_button = Button(
            text="🖼️  CREATE IMAGE",
            size_hint_y=None,
            height=60
        )

        layout.add_widget(title)
        layout.add_widget(story)
        layout.add_widget(video_button)
        layout.add_widget(image_button)

        return layout


if __name__ == "__main__":
    StoryAI().run()
