#! python3.9.2
# Start
# TODO : Explaining the pourpse
# TODO : Modules 

class Usage(object):
    """ Showing the usage of the kwargs 
    when we pasd a parameter """

    def __init__(self, phone:str='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

    def __str__(self):
        return self.phone
lil = Usage('0343-3425-5612')
print(lil)

class Aux(object):
    def __init__(se


# End