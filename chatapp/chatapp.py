"""Welcome to Reflex!."""

from chatapp import styles
from chatapp.templates import template
# Import all the pages.
from chatapp.pages import *
from chatapp.state import State

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
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=styles.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=styles.button_style,
        ),
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
