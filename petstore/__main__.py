from petstore.generator import PetstoreGenerator
from petstore.parser import PetstoreParser

if __name__ == '__main__':
    g = PetstoreGenerator(PetstoreParser('petstore.json'), 'templates', '.')
    g.generate()

