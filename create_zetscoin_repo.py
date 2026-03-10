import os
from zipfile import ZipFile

# 1️⃣ Define folder structure and files
structure = {
    "zetscoin": {
        "contracts": {
            "Zetscoin.sol": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Zetscoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("Zetscoin", "ZET") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }
}
"""
        },
        "docs": {
            "whitepaper.md": """# Zetscoin Whitepaper

## Introduction
Zetscoin is a decentralized cryptocurrency token designed for fast and secure transactions.

## Vision
Empowering the crypto community with a reliable, scalable, and community-driven token.

## Technology
Built on Ethereum blockchain using ERC20 standard.
""",
            "tokenomics.md": """# Tokenomics

- Total Supply: 1,000,000 ZET
- Token Symbol: ZET
- Decimals: 18
- Initial Distribution:
  - 50% Public Sale
  - 30% Team & Advisors
  - 20% Reserve & Marketing
"""
        },
        "images": {
            "zetscoin_logo.png": None  # Placeholder, you can replace with actual logo later
        },
        "README.md": """# Zetscoin

Zetscoin is a decentralized ERC20 token on the Ethereum blockchain.

## Features
- Fast and secure transactions
- Community-driven token
- Transparent supply

## Folder Structure
- `contracts/` → Smart contract files
- `docs/` → Whitepaper and tokenomics
- `images/` → Logos and graphics

## Contract
- `Zetscoin.sol` → ERC20 smart contract
"""
    }
}

# 2️⃣ Function to create files recursively
def add_files(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            add_files(path, content)
        else:
            with open(path, "w" if content else "wb") as f:
                if content:
                    f.write(content.encode("utf-8"))
                else:
                    # Placeholder for binary files like PNG
                    f.write(b"")

# 3️⃣ Create the folder structure
root_folder = "zetscoin"
add_files(".", structure)

# 4️⃣ Create zip file
zip_name = f"{root_folder}.zip"
with ZipFile(zip_name, "w") as zipf:
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zipf.write(filepath)

print(f"✅ Zetscoin repository zip ready: {zip_name}")
print("Upload this zip to GitHub and your folders will be created automatically.")
