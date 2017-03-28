def do_admin(self, args, arguments):
        """
        ::
          Usage:
                admin [db|rest] start
                admin [db|rest] stop
                admin db backup
                admin db reset
                admin status
          Description:
                db start
                    starts the database service
                db stop
                    stops the database service
                db backup
                    creates abackup of the database
                db reset
                    resets the database
          Arguments:
              FILE   a file name
          Options:
              -f      specify the file
        """
        print(arguments)
        if arguments["db"] and arguments["stop"]:

            print("PLEASE stop db")
            m = Mongo()
            m.stop()
        elif arguments["db"] and arguments["start"]:

            print("PLEASE start db")
            m = Mongo()
            m.start()

        elif arguments["rest"] and arguments["start"]:

            print("PLEASE start rest")
            # m = Eve()
            # m.start()

        elif arguments["rest"] and arguments["stop"]:

            print("PLEASE stop rest")
            # m = Eve()
            # m.stop()


        elif arguments["start"]:
            m = Mongo()
            r = m.start()
            print(r)

            # start mong, start eve
            pass
        elif arguments["stop"]:
            m = Mongo()
            r = m.stop()
            print(r)

            # stop eve
            pass

        elif arguments["status"]:
            m = Mongo()
            r = m.status()
            print(r)
