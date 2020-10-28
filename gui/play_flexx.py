from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text='hello')
        flx.Button(text='world')

ex = Example()
ex.