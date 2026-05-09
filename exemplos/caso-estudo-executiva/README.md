# Caso de Estudo: Manutenção de Identidade (Executiva) 💼

## 🎯 Objetivo
Demonstrar a manutenção da consistência facial da modelo em um cenário de iluminação e ambiente 100% distintos do original, evitando a **"deriva de identidade" (Identity Drift)**.

## ⚙️ Configurações de Engenharia de Machine Learning
- **Modelo de Referência Original**: `referencia.jpg` (Businesswoman Portrait).
- **Algoritmo de Ancoragem**: Calibração personalizada de pesos entre Face Reference e Structure (Freepik Pikaso).
- **Parâmetro de Fidelidade**: **0.85** (Foco em geometria óssea e distância interocular).
- **Controle de Difusão**: Ajustado para preservar a textura de pele original sem suavização excessiva por IA.

## 🧪 Metodologia Aplicada (Blindada)
A geração utilizou uma estrutura de tokens de fotografia técnica e pesos negativos para impedir que a IA "alucinasse" traços de rostos genéricos do dataset do Flux.1. 

> [!IMPORTANT]
> O prompt exato e a lógica de tokens são parte da propriedade intelectual entregue na mentoria técnica e estão protegidos localmente.

<div align="center">
 
| 🖼️ Referência Original | 🚀 Resultado Ancorado |
| :---: | :---: |
| <img src="referencia.jpg" height="400"> | <img src="resultado_ancorado.jpg" height="400"> |

</div>
