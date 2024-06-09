from .latent_misc import EmptyLatentImageAR, EmptyLatentImageARAdvanced, LatentToWidthHeight, LatentToMaskBB
from .random_gen import RandomPromptGenerator
from .cascade_utils import StableCascade_AutoCompLatent
from .clip_misc import CLIPTextEncodeBREAK, CLIPMicroConditioning, CLIPTokenCounter
from .clip_negpip import CLIPNegPip
from .attention_couple_ppm import AttentionCouplePPM

WEB_DIRECTORY = "./js"

NODE_CLASS_MAPPINGS = {
    "EmptyLatentImageAR": EmptyLatentImageAR,
    "EmptyLatentImageARAdvanced": EmptyLatentImageARAdvanced,
    "LatentToWidthHeight": LatentToWidthHeight,
    "LatentToMaskBB": LatentToMaskBB,
    "RandomPromptGenerator": RandomPromptGenerator,
    "StableCascade_AutoCompLatent": StableCascade_AutoCompLatent,
    "CLIPTextEncodeBREAK": CLIPTextEncodeBREAK,
    "CLIPMicroConditioning": CLIPMicroConditioning,
    "CLIPTokenCounter": CLIPTokenCounter,
    "CLIPNegPip": CLIPNegPip,
    "AttentionCouplePPM": AttentionCouplePPM,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmptyLatentImageAR": "Empty Latent Image (Aspect Ratio)",
    "EmptyLatentImageARAdvanced": "Empty Latent Image (Aspect Ratio+)",
    "LatentToWidthHeight": "LatentToWidthHeight",
    "LatentToMaskBB": "LatentToMaskBB",
    "TokenCounter": "Token Counter",
    "RandomPromptGenerator": "Random Prompt Generator",
    "StableCascade_AutoCompLatent": "StableCascade_AutoCompLatent",
    "CLIPTextEncodeBREAK": "CLIPTextEncodeBREAK",
    "CLIPMicroConditioning": "CLIPMicroConditioning",
    "CLIPTokenCounter": "CLIPTokenCounter",
    "CLIPNegPip": "CLIPNegPip",
    "AttentionCouplePPM": "AttentionCouplePPM",
}
