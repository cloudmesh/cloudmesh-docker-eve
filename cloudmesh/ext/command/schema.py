"""
The admin command for the REST services
"""
from __future__ import print_function

from pprint import pprint

from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.rest.elements import Elements

from cloudmesh.rest.schema import ConvertSpec
from cloudmesh.common.error import Error
import glob

import os.path


class SchemaCommand(PluginCommand):
    """
    The admin command to manage the REST service
    """

    @command
    def do_schema(self, args, arguments):
        """
        ::

          Usage:
            schema cat DIRECTORY FILENAME  
            schema convert INFILE [OUTFILE]
                
          Arguments:
              FILENAME   a filename
              DIRECTORY  the derectory where the schma 
                         objects are defined

          Options:
              -h     help

          Description:
             schema eve [json|yml] DIRECTORY FILENAME
                concatenates all files with ending yml 
                or json in the directory and combines 
                them. Using evegenie on the combined 
                file a eve settings file is generated 
                and written into FILENAME
                
             schema cat [json|yml] DIRECTORY FILENAME
                Concatinates all files with the given 
                ending (either json, or yml) into the
                file called FILENAME
            
   
                
        """
        # pprint(arguments)

        if arguments.cat:
            directory = arguments.DIRECTORY
            filename = arguments.FILENAME
            elements = Elements(directory, filename)

        elif arguments.convert:
            try:
                filename = arguments.INFILE
                outfile = arguments.OUTFILE or "settings.py"
                if arguments.OUTFILE is None:


                    if ".py" in outfile:
                        pass
                    elif ".json" in filename:
                        outfile = filename.replace(".json", ".yml")
                    elif ".yml" in filename:
                        outfile = filename.replace(".yml", ".json")


                ConvertSpec(filename, outfile)
            except Exception as e:
                print (e)
                Error.traceback(error=e, debug=True, trace=True)