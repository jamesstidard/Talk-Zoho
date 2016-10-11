class Thing:

    @property
    def thang(self):
        print('the real thang')

    def __getattr__(self, name):
        print(name)

thing = Thing()
thing.thang
