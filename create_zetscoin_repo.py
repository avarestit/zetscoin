import os
from zipfile import ZipFile

# -----------------------------
# Define folder structure with type
# -----------------------------
structure = {
    "zetscoin": {
        "contracts": {
            "Zetscoin.sol": ("text", """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Zetscoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("Zetscoin", "ZET") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }
}
""")
        },
        "docs": {
            "whitepaper.md": ("text", """# Zetscoin Whitepaper

## Introduction
Zetscoin is a decentralized cryptocurrency token designed for fast and secure transactions.

## Vision
Empowering the crypto community with a reliable, scalable, and community-driven token.

## Technology
Built on Ethereum blockchain using ERC20 standard.
"""),
            "tokenomics.md": ("text", """# Tokenomics

- Total Supply: 1,000,000 ZET
- Token Symbol: ZET
- Decimals: 18
- Initial Distribution:
  - 50% Public Sale
  - 30% Team & Advisors
  - 20% Reserve & Marketing
""")
        },
        "images": {
            "zetscoin_logo.png": ("binary", b"")  # empty placeholder
        },
        "README.md": ("text", """# Zetscoin

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
""")
    }
}

# -----------------------------
# Function to create files/folders recursively
# -----------------------------
def create_files(base_path, struct):
    for name, (ftype, content) in struct.items():
        path = os.path.join(base_path, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if ftype == "text":
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        elif ftype == "binary":
            with open(path, "wb") as f:
                f.write(content)
        elif ftype == "folder":
            os.makedirs(path, exist_ok=True)
            create_files(path, content)

# -----------------------------
# Convert top-level folder to type "folder"
# -----------------------------
typed_structure = {"zetscoin": ("folder", structure["zetscoin"])}

# -----------------------------
# Create folder structure
# -----------------------------
create_files(".", typed_structure)

# -----------------------------
# Create zip file
# -----------------------------
zip_name = "zetscoin.zip"
with ZipFile(zip_name, "w") as zipf:
    for foldername, subfolders, filenames in os.walk("zetscoin"):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zipf.write(filepath, os.path.relpath(filepath, "."))

print(f"✅ Zetscoin repository zip ready: {zip_name}")
