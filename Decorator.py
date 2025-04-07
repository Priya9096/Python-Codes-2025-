def decor(function):
    def inner(name):
        if name == 'Ayush':
            print(name,'likes Biryani')
        else:
            return function(name)
    return inner

@decor
def process(name):
    print(name,'likes pulao')

process('Ankit')
process('Akash')
process('Ayush')
process('Punith')