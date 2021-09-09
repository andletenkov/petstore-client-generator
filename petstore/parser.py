from petstore.model import PetstoreSchema


class PetstoreParser:

    def __init__(self, schema_file: str):
        self.schema_file = schema_file

    def parse(self) -> PetstoreSchema:
        with open(self.schema_file, 'r') as f:
            return PetstoreSchema.parse_raw(f.read())