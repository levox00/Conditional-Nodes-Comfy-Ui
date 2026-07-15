import comfy
import folder_paths
from comfy_execution.graph import ExecutionBlocker


class IfTrue:

    """
    If trigger == expected: output if_true.
    Else: output fallback or None.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("STRING", {"forceInput": True}),
                "expected": ("STRING", {"default": "text", "multiline": False}),
                "if_true": ("*",),
            },
            "optional": {
                "fallback": ("*",),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    CATEGORY = "conditional"

    def is_empty(self, value):
        if value is None:
            return True
        if isinstance(value, str) and value.strip() == "":
            return True
        return False

    def execute(self, trigger, expected, if_true, fallback=None):

        if trigger == expected:
            if self.is_empty(if_true):
                return (None,)
            return (if_true,)

        if fallback is not None:
            if self.is_empty(fallback):
                return (None,)
            return (fallback,)

        return (None,)


class IfTrue3:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("STRING", {"forceInput": True}),
                "expected": ("STRING", {"default": "text", "multiline": False}),
                "if_true_1": ("*",),
                "if_true_2": ("*",),
                "if_true_3": ("*",),
            },
            "optional": {
                "fallback_1": ("*",),
                "fallback_2": ("*",),
                "fallback_3": ("*",),
            }
        }
    RETURN_TYPES = ("*", "*", "*")
    RETURN_NAMES = ("out_1", "out_2", "out_3")
    FUNCTION = "execute"
    CATEGORY = "conditional"

    def is_empty(self, value):
        if value is None:
            return True
        if isinstance(value, str) and value.strip() == "":
            return True
        return False

    def execute(self, trigger, expected, if_true_1, if_true_2, if_true_3,
                fallback_1=None, fallback_2=None, fallback_3=None):
        
        def pick(if_true, fallback, name):
            if trigger == expected:
                if self.is_empty(if_true):
                    return ExecutionBlocker(None)
                return if_true

            if fallback is not None:
                if self.is_empty(fallback):
                    return ExecutionBlocker(None)
                return fallback

            return ExecutionBlocker(None)

        return (pick(if_true_1, fallback_1, "1"),
                pick(if_true_2, fallback_2, "2"),
                pick(if_true_3, fallback_3, "3"))


class IfTrue4:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("STRING", {"forceInput": True}),
                "expected": ("STRING", {"default": "text", "multiline": False}),
                "if_true_1": ("*",),
                "if_true_2": ("*",),
                "if_true_3": ("*",),
                "if_true_4": ("*",),
            },
            "optional": {
                "fallback_1": ("*",),
                "fallback_2": ("*",),
                "fallback_3": ("*",),
                "fallback_4": ("*",),
            }
        }
    RETURN_TYPES = ("*", "*", "*", "*")
    RETURN_NAMES = ("out_1", "out_2", "out_3", "out_4")
    FUNCTION = "execute"
    CATEGORY = "conditional"

    def is_empty(self, value):
        if value is None:
            return True
        if isinstance(value, str) and value.strip() == "":
            return True
        return False

    def execute(self, trigger, expected, if_true_1, if_true_2, if_true_3, if_true_4,
                fallback_1=None, fallback_2=None, fallback_3=None, fallback_4=None):
        
        def pick(if_true, fallback, name):
            if trigger == expected:
                if self.is_empty(if_true):
                    return ExecutionBlocker(None)
                return if_true

            if fallback is not None:
                if self.is_empty(fallback):
                    return ExecutionBlocker(None)
                return fallback

            return ExecutionBlocker(None)

        return (pick(if_true_1, fallback_1, "1"),
                pick(if_true_2, fallback_2, "2"),
                pick(if_true_3, fallback_3, "3"),
                pick(if_true_4, fallback_4, "4"))


class StringConst:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("STRING", {"default": "", "multiline": False})}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "execute"
    CATEGORY = "conditional"
    def execute(self, value): return (value,)


class IntConst:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("INT", {"default": 20, "min": 1, "max": 10000})}}
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int",)
    FUNCTION = "execute"
    CATEGORY = "conditional"
    def execute(self, value): return (value,)


class FloatConst:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 100.0, "step": 0.1})}}
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)
    FUNCTION = "execute"
    CATEGORY = "conditional"
    def execute(self, value): return (value,)


class MergeFirst:
    """
    Nimmt bis zu 16 Inputs. Gibt den ersten gültigen Wert zurück.
    ExecutionBlocker wird als ungültig behandelt (übersprungen).
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {
                "in_1": ("*", {"forceInput": True}),
                "in_2": ("*", {"forceInput": True}),
                "in_3": ("*", {"forceInput": True}),
                "in_4": ("*", {"forceInput": True}),
                "in_5": ("*", {"forceInput": True}),
                "in_6": ("*", {"forceInput": True}),
                "in_7": ("*", {"forceInput": True}),
                "in_8": ("*", {"forceInput": True}),
                "in_9": ("*", {"forceInput": True}),
                "in_10": ("*", {"forceInput": True}),
                "in_11": ("*", {"forceInput": True}),
                "in_12": ("*", {"forceInput": True}),
                "in_13": ("*", {"forceInput": True}),
                "in_14": ("*", {"forceInput": True}),
                "in_15": ("*", {"forceInput": True}),
                "in_16": ("*", {"forceInput": True}),
            }
        }
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("out",)
    FUNCTION = "execute"
    CATEGORY = "conditional"

    def is_valid(self, value):
        if value is None:
            return False
        if isinstance(value, ExecutionBlocker):
            return False
        if isinstance(value, str) and value.strip() == "":
            return False
        return True

    def execute(self, in_1=None, in_2=None, in_3=None, in_4=None, in_5=None, in_6=None,
                in_7=None, in_8=None, in_9=None, in_10=None, in_11=None, in_12=None,
                in_13=None, in_14=None, in_15=None, in_16=None):
        inputs = [in_1, in_2, in_3, in_4, in_5, in_6, in_7, in_8,
                  in_9, in_10, in_11, in_12, in_13, in_14, in_15, in_16]
        for inp in inputs:
            if self.is_valid(inp):
                return (inp,)
        return (ExecutionBlocker("MergeFirst: no valid input"),)


class LoadDiffusionFromString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_name": ("STRING", {"forceInput": True}),
            }
        }
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "conditional"

    def load_model(self, model_name):
        if isinstance(model_name, ExecutionBlocker):
            return (ExecutionBlocker("blocked"),)
        if not model_name:
            return (ExecutionBlocker("empty model_name"),)
        model_path = folder_paths.get_full_path("diffusion_models", model_name)
        if model_path is None:
            raise FileNotFoundError(f"Diffusion Model nicht gefunden: {model_name}")
        model = comfy.sd.load_diffusion_model(model_path)
        return (model,)


class LoadCheckpointFromString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"ckpt_name": ("STRING", {"forceInput": True})}}
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    RETURN_NAMES = ("model", "clip", "vae")
    FUNCTION = "load_checkpoint"
    CATEGORY = "conditional"

    def load_checkpoint(self, ckpt_name):
        if isinstance(ckpt_name, ExecutionBlocker):
            return (ExecutionBlocker("blocked"), ExecutionBlocker("blocked"), ExecutionBlocker("blocked"))
        if not ckpt_name:
            return (ExecutionBlocker("empty ckpt_name"), ExecutionBlocker("empty ckpt_name"), ExecutionBlocker("empty ckpt_name"))
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        if ckpt_path is None:
            raise FileNotFoundError(f"Checkpoint nicht gefunden: {ckpt_name}")
        out = comfy.sd.load_checkpoint_guess_config(
            ckpt_path, output_vae=True, output_clip=True,
            embedding_directory=folder_paths.get_folder_paths("embeddings")
        )
        return out[:3]


class LoadLoraFromString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "lora_name": ("STRING", {"forceInput": True}),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                "strength_clip": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
            }
        }
    RETURN_TYPES = ("MODEL", "CLIP")
    RETURN_NAMES = ("model", "clip")
    FUNCTION = "load_lora"
    CATEGORY = "conditional"

    def load_lora(self, model, clip, lora_name, strength_model, strength_clip):
        if isinstance(lora_name, ExecutionBlocker):
            return (ExecutionBlocker("blocked"), ExecutionBlocker("blocked"))
        if not lora_name:
            return (model, clip)
        if strength_model == 0 and strength_clip == 0:
            return (model, clip)
        lora_path = folder_paths.get_full_path("loras", lora_name)
        if lora_path is None:
            raise FileNotFoundError(f"LoRA nicht gefunden: {lora_name}")
        lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
        model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora, strength_model, strength_clip)
        return (model_lora, clip_lora)


NODE_CLASS_MAPPINGS = {
    "LoadDiffusionFromString": LoadDiffusionFromString,
    "IfTrue": IfTrue,
    "IfTrue3": IfTrue3,
    "IfTrue4": IfTrue4,
    "StringConst": StringConst,
    "IntConst": IntConst,
    "FloatConst": FloatConst,
    "MergeFirst": MergeFirst,
    "LoadCheckpointFromString": LoadCheckpointFromString,
    "LoadLoraFromString": LoadLoraFromString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadDiffusionFromString": "Load Diffusion From String",
    "IfTrue": "If True",
    "IfTrue3": "If True 3",
    "IfTrue4": "If True 4",
    "StringConst": "Const String",
    "IntConst": "Const Int",
    "FloatConst": "Const Float",
    "MergeFirst": "Merge First",
    "LoadCheckpointFromString": "Load Checkpoint From String",
    "LoadLoraFromString": "Load LoRA From String",
}