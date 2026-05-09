from PIL import Image
import os

def gerar_comparativo_tecnico(path_ref, path_res, output_name="comparativo_final_padronizado.jpg", size=(1024, 1024)):
    """
    Padroniza imagens de referência e resultado para validação de identidade visual.
    Utiliza amostragem Lanczos para preservar detalhes da pele e geometria facial.
    """
    try:
        # Carregamento das imagens
        print(f"[*] Carregando Referência: {path_ref}")
        img_ref = Image.open(path_ref).convert('RGB')
        
        print(f"[*] Carregando Resultado: {path_res}")
        img_res = Image.open(path_res).convert('RGB')

        # Redimensionamento padronizado (1:1) para análise métrica
        print("[*] Redimensionando com amostragem Lanczos...")
        img_ref_resized = img_ref.resize(size, Image.LANCZOS)
        img_res_resized = img_res.resize(size, Image.LANCZOS)

        # Criação do canvas lado a lado (Side-by-Side)
        print("[*] Compondo canvas técnico...")
        canvas = Image.new('RGB', (size[0] * 2, size[1]))
        canvas.paste(img_ref_resized, (0, 0))
        canvas.paste(img_res_resized, (size[0], 0))

        # Exportação em alta qualidade
        canvas.save(output_name, quality=95, subsampling=0)
        print(f"[-] Arquivo gerado com sucesso: {output_name}")
        
    except FileNotFoundError as e:
        print(f"[!] Erro: Arquivo não encontrado - {e.filename}")
    except Exception as e:
        print(f"[!] Erro inesperado: {e}")

if __name__ == "__main__":
    # Caminhos atualizados para a estrutura do projeto
    PATH_REFERENCIA = "exemplos/caso-estudo-executiva/referencia.jpg"
    PATH_RESULTADO = "exemplos/caso-estudo-executiva/resultado_ancorado.jpg"
    OUTPUT_FINAL = "exemplos/caso-estudo-executiva/comparativo_final_padronizado.jpg"
    
    gerar_comparativo_tecnico(PATH_REFERENCIA, PATH_RESULTADO, output_name=OUTPUT_FINAL)
