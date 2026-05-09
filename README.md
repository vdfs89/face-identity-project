# Identity Anchoring & Facial Consistency 🧬

Metodologia técnica avançada para preservação de identidade em modelos generativos de alta fidelidade (**Flux.1** + **Freepik Pikaso**).

---

## 📸 Caso de Estudo: Executiva em Ambiente Clínico

Neste benchmark, demonstramos a transição de um retrato corporativo para um cenário de laboratório científico, mantendo a geometria facial intacta e corrigindo distorções de idade.

<div align="center">

| 🖼️ Referência Original | 🚀 Resultado Ancorado |
| :---: | :---: |
| <img src="exemplos/caso-estudo-executiva/referencia.jpg" height="400"> | <img src="exemplos/caso-estudo-executiva/resultado_ancorado.jpg" height="400"> |
| **Identidade Base** | **95% Fidelity @ 25 Years** |

</div>

> [!TIP]
> **Key Optimization:** A ancoragem de 0.9 permitiu a mudança radical de pose e cenário (segurando a pasta) sem sacrificar os traços anatômicos da modelo original.

---

## 🚀 Visão Geral
Framework desenvolvido para garantir que a IA mantenha a fidelidade aos traços anatômicos originais, permitindo alterações radicais de cenário, pose e iluminação sem a perda da identidade visual (*Identity Drift*).

## 🛠️ Pilares do Framework
*   **Ancoragem Geométrica**: Utilização de tokens de estrutura óssea para "travar" a face.
*   **Calibração Dinâmica**: Ajuste de pesos entre *Face Reference* e *Structure*.
*   **Rejuvenescimento Técnico**: Protocolo para evitar envelhecimento por ruído de cenário.

## 📁 Estrutura do Projeto
*   📂 [**Prompts**](prompts/README.md) - Gestão de IP e instruções de segurança.
*   📂 [**Workflows**](workflows/freepik_pikaso.md) - Parâmetros técnicos de calibração.
*   📂 [**Exemplos**](exemplos/caso-estudo-executiva/README.md) - Detalhamento do caso de estudo.

---
**Desenvolvido por:** [Vitor Silva](https://github.com/vdfs89) | ML Engineer & AI Researcher.
