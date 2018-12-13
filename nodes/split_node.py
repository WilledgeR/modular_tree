from bpy.types import Node
from bpy.props import IntProperty, FloatProperty, EnumProperty, BoolProperty, StringProperty
from .base_node import BaseNode
from ..tree import MTree

class MtreeSplit(Node, BaseNode):
    bl_label = "Split Node"
    
    amount = IntProperty(min=0, default=20) # number of splits
    split_angle = FloatProperty(min=0, max=1, default=.3) # angle of a fork
    max_split_number = IntProperty(min=0, default=2) # number of forks per split
    radius = FloatProperty(min=0, max=1, default=.6) # radius of split
    min_height = FloatProperty(min=0, default=3) # min height at which a split occurs

    def init(self, context):
        self.outputs.new('TreeSocketType', "Tree")
        self.inputs.new('TreeSocketType', "Tree")
        self.name = MtreeSplit.bl_label

    def draw_buttons(self, context, layout):        
        properties = ["amount", "split_angle", "max_split_number", "radius", "min_height"]
        col = layout.column()
        for i in properties:
            col.prop(self, i)
    
    def execute(self, tree):
        tree.split(self.amount, self.split_angle, self.max_split_number, self.radius, self.min_height, 0)
        print("split has been executed")
        links = self.outputs["Tree"].links
        if len(links) > 0:
            links[0].to_node.execute(tree)
            