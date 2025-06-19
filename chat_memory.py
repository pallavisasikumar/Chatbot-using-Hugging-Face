class ChatMemory:
    def _init_(self, max_turns=3):
        self.history = []
        self.max_turns = max_turns

    def add(self, user_input, bot_reply):
        self.history.append((user_input, bot_reply))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return "\n".join([f"{u}\n{b}" for u, b in self.history])