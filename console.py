import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
    def do_help(self, line):
        """Get help on commands
        
        Usage: help <command>
        """
        if line:
            try:
                doc = getattr(self, 'do_' + line).__doc__
                if doc:
                    self.stdout.write("%s\n" % str(doc))
                    return
            except AttributeError:
                pass
            self.stdout.write("%s\n" % str("Command not found."))
        else:
            cmd.Cmd.do_help(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
