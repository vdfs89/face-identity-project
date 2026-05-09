import torch
from diffusers import FluxPipeline
import os

# =================================================================
# PROTOCOLO DE INFERÊNCIA - FACE IDENTITY PROJECT (V5)
# =================================================================

# Caminho absoluto para armazenamento de modelos (fora do Git)
# No Windows, o '~' expande para o perfil do usuário (C:\Users\...)
model_id = os.path.expanduser("~/ai_storage/models/flux2") 

if not os.path.exists(model_id):
    print(f"[!] Aviso: Pasta de modelo não encontrada em {model_id}")
    print("[*] Certifique-se de baixar os pesos do Flux.1 e colocá-los nesta pasta.")

def run_inference():
    print("[*] Inicializando Pipeline Flux.1 (bfloat16)...")
    try:
        pipe = FluxPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.bfloat16
        ).to("cuda")

        # Aplicação do Protocolo de Invariância Física V5
        prompt = (
            "Extreme high-resolution close-up portrait of a 25-year-old professional woman, "
            "maintaining the absolute and identical facial geometry of REFERENCE_IDENTITY. "
            "The skin must show sophisticated micro-topography, including invisible pores, "
            "natural skin translucency with subtle subsurface scattering, and a fresh, youthful glow. "
            "Sharp, focused brown eyes with realistic iris patterns and a crystal-clear catchlight "
            "reflecting a modern lab environment. Silky light brown hair (warm honey tones) with "
            "realistic individual hair strands and natural sheen. She is standing with a composed, "
            "confident posture, holding a professional business folder with both hands. "
            "Pristine white laboratory coat made of heavy, high-quality fabric. "
            "Shot on Sony A7R V, 85mm G-Master lens, f/1.8. Cinematic depth of field."
        )

        print("[*] Gerando imagem de alta fidelidade...")
        image = pipe(
            prompt=prompt,
            num_inference_steps=50,
            guidance_scale=3.5,
            height=1024,
            width=1024
        ).images[0]

        output_path = "outputs/resultado_final_v5.png"
        image.save(output_path)
        print(f"[-] Sucesso! Imagem salva em: {output_path}")

    except Exception as e:
        print(f"[!] Erro na inferência: {e}")

if __name__ == "__main__":
    run_inference()
