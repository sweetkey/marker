from marker.schema import BlockTypes
from marker.schema.blocks import Block


class Caption(Block):
    block_type: BlockTypes = BlockTypes.Caption

    def assemble_html(self, child_blocks, parent_structure):
        template = super().assemble_html(child_blocks, parent_structure)
        template = template.replace("\n", " ")
        return f"<p>{template}</p>"