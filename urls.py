from views import ReadHandler, ResetHandler, TestHandler, WriteHandler


router = [
    (r"/read", ReadHandler),
    (r'/write', WriteHandler),
    (r'/reset', ResetHandler),

    (r"/test", TestHandler),

]
