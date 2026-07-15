# ComfyUI Logic Toolkit

A collection of utility nodes for building dynamic and configurable ComfyUI workflows.

## Features

### Conditional Nodes

- **If True**
- **If True 3**
- **If True 4**

Route data depending on a string comparison.

Example:

```
trigger == expected
        │
      Yes ──► Output
      No  ──► Fallback (optional)
```

---

### Merge Nodes

**Merge First**

Returns the first valid input from up to 16 inputs.

Useful for combining multiple conditional branches.

---

### Constant Nodes

- Const String
- Const Int
- Const Float

Useful for reusable workflows.

---

### Dynamic Loaders

#### Load Diffusion From String

Loads a diffusion model using its filename.

#### Load Checkpoint From String

Loads a checkpoint from a string.

Outputs:

- MODEL
- CLIP
- VAE

#### Load LoRA From String

Loads a LoRA by filename.

---

## Included Nodes

- If True
- If True 3
- If True 4
- Merge First
- Const String
- Const Int
- Const Float
- Load Diffusion From String
- Load Checkpoint From String
- Load LoRA From String

---

## Installation

### Using ComfyUI Manager

Search for

> Logic Toolkit

and install.

---

### Manual Installation

Clone into your `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes

git clone https://github.com/YOUR_USERNAME/ComfyUI-Logic-Toolkit
```

Restart ComfyUI.

---

## Example Use Cases

- Dynamic checkpoint selection
- Dynamic LoRA loading
- Conditional workflow branches
- Shared workflows with multiple configurations
- Cleaner workflows using Merge First

---

## License

MIT License
