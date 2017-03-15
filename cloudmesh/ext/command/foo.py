from __future__ import print_function
from cloudmesh_client.shell.command import command
from cloudmesh_client.shell.command import PluginCommand


class FooCommand(PluginCommand):

    @command
    def do_foo(self, args, arguments):
        """
        ::

          Usage:
                command -f FILE
                command FILE
                command list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)
