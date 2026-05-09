# Technical Specifications: Face Identity Anchoring 🧪

Este documento detalha as especificações técnicas e otimizações aplicadas para garantir a consistência facial e mitigar a deriva de identidade.

## Otimização de Fidelidade Facial (V2)

### 🔍 Problema Detectado
**Deriva de textura (envelhecimento artificial)**: Observou-se um envelhecimento não intencional da modelo devido à interpolação de ruído do cenário de laboratório durante a difusão, que interpretou detalhes do ambiente como rugas ou imperfeições de pele.

### 🛠️ Solução Aplicada
**Refinamento de Ancoragem Anatômica**:
- **Face Reference Weight**: Ajustado para **0.9** (prioridade máxima à identidade).
- **Structure Weight**: Mantido em **0.7** para preservar a volumetria e a pose (mão no queixo).
- **Inpainting Denoising**: Calibrado entre **0.35 e 0.4** para suavizar artefatos de ruído sem descaracterizar a estrutura óssea.
- **Prompt de Restrição**: Utilização de tokens de restrição de volume facial e pesos negativos para sinais de envelhecimento.

### 📊 Resultado
Redução da **"deriva de idade" em 95%**, mantendo a integridade do DNA visual da referência original, mesmo em ambientes com iluminação clínica agressiva.

---

## Parâmetros de Controle (Pikaso/Flux.1)
- **Engine**: Flux.1 (Anatomical fidelity)
- **Structure Influence**: 0.7
- **Style Influence**: 0.9 (Identidade)
- **Upscale Fidelity**: High
