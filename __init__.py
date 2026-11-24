"""
ComfyUI Omni Node - paste the body of a node class (or describe one) and the node
rebuilds its own inputs/outputs to mirror it.

    omni_nodes.py -> OmniNode, OmniNodeGuide, OmniNodeAPI

Split out of Rebalance-Pack: these nodes compile and run user-supplied Python, so they
live in their own pack and the rest of Rebalance-Pack isn't flagged with them.
"""

from .omni_nodes import OmniNode, OmniNodeGuide, OmniNodeAPI

NODE_CLASS_MAPPINGS = {
    "OmniNode": OmniNode,
    "OmniNodeGuide": OmniNodeGuide,
    "OmniNodeAPI": OmniNodeAPI,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "OmniNode": "Omni Node Manual",
    "OmniNodeGuide": "Omni Node Guide",
    "OmniNodeAPI": "Omni Node",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
