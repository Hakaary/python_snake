from sshkeyboard import listen_keyboard


class UserInput:

    def __init__(self):
        self.last_key: str | None = None

    def start_retrieving_input(self):
        self._keyboard = listen_keyboard(
            on_press=self.get_key,
        )

    def get_key(self, key: str):
        self.last_key = key
