import dictionary


class Command(object):
    def __init__(self):
        self.commands = {
            "jump": self.jump,
            "help": self.help,
            "dict": self.dict
        }

    def handle_command(self, user, message):
        response = "<@" + user + "> "
        tokens = message.split(' ')
        command = tokens[0]
        if len(tokens) > 1:
            support = tokens[1]
        else:
            support = None
        if command in self.commands:
            response += self.commands[command](support)
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        return response

    def jump(self, support=None):
        return "Kris Kross will make you jump jump"

    def help(self, support=None):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response

    def dict(self, word_id):
        if word_id != None:
            response = dictionary.getMeaning(word_id)
            return response
