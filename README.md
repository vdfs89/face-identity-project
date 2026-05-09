# Ancoragem de Identidade e Consistência Facial em Modelos Generativos 🧬

Este projeto apresenta uma metodologia técnica avançada para mitigar a **Deriva de Identidade (Identity Drift)** em modelos de IA generativa (Flux.1 + Freepik Pikaso).

## 📸 Caso de Estudo: Consistência em Ambiente Laboratorial
O objetivo deste exemplo foi mover a modelo de um retrato de estúdio para um ambiente de laboratório científico de alta tecnologia, mantendo a identidade exata de 25 anos e eliminando o envelhecimento artificial causado pelo cenário clínico.

| Referência Original (Input) | Resultado Ancorado (Output) |
|:---:|:---:|
| ![Referência](exemplos/caso-estudo-executiva/referencia.jpg) | ![Resultado](exemplos/caso-estudo-executiva/resultado_ancorado.jpg) |
| **Identidade Base** | **95% de Fidelidade Preservada** |

> **Highlight:** Note a manutenção da distância interocular, estrutura do jawline e o rejuvenescimento controlado para 25 anos, corrigindo a interpretação equivocada do modelo sobre texturas clínicas.

## 🚀 Visão Geral
Como Engenheiro de Machine Learning, desenvolvi este framework para garantir que a IA mantenha a fidelidade aos traços anatômicos originais, permitindo alterações radicais de cenário e iluminação sem a perda da identidade visual.

## 🛠️ Pilares Técnicos
1. **Engenharia de Ancoragem**: Tokens técnicos para "travar" a geometria óssea.
2. **Calibração de Pesos**: Ajuste fino entre *Face Reference* (0.9) e *Structure* (0.4).
3. **Mitigação de Age-Drift**: Protocolo de denoise cirúrgico para evitar envelhecimento por artefatos de cenário.

## 📁 Estrutura do Projeto
- [`/prompts`](prompts/README.md): Instruções para gestão de prompts privados (IP Protegido).
- [`/workflows`](workflows/freepik_pikaso.md): Guia de configuração técnica.
- [`/exemplos`](exemplos/README.md): Showcase de resultados e casos de estudo.

---
**Desenvolvido por:** [Vitor Silva](https://github.com/vdfs89) | ML Engineer & AI Researcher.
