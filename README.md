# Ancoragem de Identidade e Consistência Facial em Modelos Generativos 🧬

Este projeto apresenta uma metodologia técnica para mitigar a **Deriva de Identidade (Identity Drift)** em modelos de IA generativa, com foco nos motores **Flux.1** e ferramentas do **Freepik Pikaso**.

## 🚀 Visão Geral
Como Engenheiro de Machine Learning, desenvolvi este framework para garantir que a IA mantenha a fidelidade aos traços anatômicos originais de uma referência, permitindo alterações de cenário, iluminação e estilo sem a perda da identidade visual.

## 🛠️ Pilares Técnicos

### 1. Engenharia de Prompts de Ancoragem
Utilização de tokens de fotografia técnica e pesos negativos para "travar" a estrutura facial. 
- **Foco:** Evitar que o modelo prioritize o realismo do cenário em detrimento dos traços da face.

### 2. Calibração de Referência (Face & Structure)
Metodologia para encontrar o ponto de equilíbrio entre a influência da imagem de origem e a flexibilidade do modelo generativo.

### 3. Refinamento Cirúrgico (Inpainting)
Uso de máscaras de alta precisão para restauração de detalhes faciais que sofreram distorções durante o processo de geração.

## 📁 Estrutura do Projeto
- `/prompts`: Modelos de prompts avançados configurados para preservação de traços.
- `/workflows`: Guia passo a passo para utilização no Freepik/Pikaso.
- `/exemplos`: Casos reais de "Antes e Depois" demonstrando a consistência.

---
**Desenvolvido por:** Vitor Silva | ML Engineer & Pesquisador em IA.
