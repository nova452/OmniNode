# ComfyUI Omni Node

# 10/08 Latest Update: Prompt-based Omni Node in ComfyUI
* Omni Node family extended
<img width="2321" height="1102" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/cea89d2f-12d1-4a66-81b2-70075102fb0f" />


# 29/07 OmniNode
A sole ComfyUI node that lets you paste in the body of a
node class, rebuilding its own inputs/outputs to mirror the source.
<img width="2889" height="1521" alt="627795071-43d362c4-cfa6-42b7-b2a6-3c29ad8a769a" src="https://github.com/user-attachments/assets/2158258c-6b47-491e-b859-886615afb048" />

## Nodes
* **Omni Node Manual** (`OmniNode`) - paste a node class; the node mirrors its inputs/outputs and runs it.
* **Omni Node Guide** (`OmniNodeGuide`) - holds the OpenRouter API key and settings for the prompt-based node.
* **Omni Node** (`OmniNodeAPI`) - describe a node in plain words; it's generated through OpenRouter and built in place.

These nodes compile and run Python code you paste or generate, which is why they're in their own
pack, separate from Rebalance-Pack. Only run code you trust.
