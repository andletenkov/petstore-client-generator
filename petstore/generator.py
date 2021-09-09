import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from petstore.parser import PetstoreParser


class PetstoreGenerator:

    def __init__(self, parser: PetstoreParser, templates_dir: str, out_path: str):
        self.parser = parser
        self.templates_dir = templates_dir
        self.out_path = out_path
        self.env = Environment(
            loader=FileSystemLoader(self.templates_dir),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self) -> None:
        os.makedirs(self.out_path, exist_ok=True)

        for file in os.listdir(self.templates_dir):
            template = self.env.get_template(file)
            content = template.render(schema=self.parser.parse())

            filename, _ = file.rsplit('.', 1)
            with open(os.path.join(self.out_path, filename), 'w') as f:
                f.write(content)



