# ComfyUI Logic Toolkit
<img width="800" alt="Screenshot 2026-07-15 204501" src="https://github.com/user-attachments/assets/4c2fad82-0666-437f-affc-e77a4916345d" />

A collection of utility nodes for building dynamic and configurable ComfyUI workflows.

## Features

### Conditional Nodes

- **If True**
- **If True 3**
- **If True 4**

These nodes compare the **Trigger** input with the **Expected** value.

If both strings match, the node outputs the **If True** input(s). Otherwise it outputs the optional **Fallback** input(s), if connected.

This makes it easy to switch between models, prompts, LoRAs or any other data based on a simple string value.

Example:

```
trigger == expected
        │
      Yes ──► If True Output(s)
      No  ──► Fallback Output(s) (optional)
```
<img width="600" alt="image" src="https://github.com/user-attachments/assets/22715167-4bb0-4907-a197-05b6ff3f5803" />

---

### Merge Nodes

#### Merge First

Returns the first connected input that contains a valid value.

Useful when several conditional branches can produce an output and you only want to continue with the first available one.

Example:

```
Branch A ─┐
Branch B ─┼──► Merge First ─► Output
Branch C ─┘
```

---

### Constant Nodes

#### Const String

Outputs a fixed string value.

Useful for trigger values, model names or reusable workflow parameters.

#### Const Int

Outputs a fixed integer value.

Useful for seeds, steps or any integer input.

#### Const Float

Outputs a fixed float value.

Useful for CFG, strengths or other floating-point values.

---

### Dynamic Loaders

#### Load Diffusion From String

Loads a diffusion model using its filename.

Example:

```
flux1-dev.safetensors
```

The string must exactly match the filename inside your `models/diffusion_models` folder.

---

#### Load Checkpoint From String

Loads a checkpoint using its filename.

Outputs:

- MODEL
- CLIP
- VAE

Example:

```
juggernautXL_v9.safetensors
```

The string must match a checkpoint inside your `models/checkpoints` folder.

---

#### Load LoRA From String

Loads a LoRA by filename and applies it to a MODEL and CLIP.

If the LoRA name is empty, the original MODEL and CLIP are returned unchanged.

Example:

```
DetailTweaker.safetensors
```

The filename must exist inside your `models/loras` folder.

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

Search for:

> **Conditional Nodes by Mikudes**

and install.

---

### Manual Installation

Clone this repository into your `custom_nodes` folder.

Example locations:

```
C:\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes
```

or

```
C:\Users\<username>\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes
```

Restart ComfyUI after installation.

---

## Example Use Cases

- Dynamic checkpoint selection
- Dynamic diffusion model selection
- Dynamic LoRA loading
- Shared workflows with multiple configurations
- Conditional workflow branches
- Cleaner workflows using Merge First

---

## License

MIT License
