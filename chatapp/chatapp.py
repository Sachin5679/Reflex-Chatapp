"""Welcome to Reflex!."""

from chatapp import styles
from chatapp.templates import template
# Import all the pages.
from chatapp.pages import *

import reflex as rx

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=styles.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",         
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer) for question, answer in qa_pairs
        ]
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            style=styles.input_style,
        ),
        rx.button("Ask", style=styles.button_style),
    )
@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.add_page(index)
app.compile()
