"""Base state for the app."""

import reflex as rx
import asyncio


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        answer="I don't know"
        self.chat_history.append((self.question, answer))
        self.question = ""
        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[:i+1],
            )
            yield

    pass
