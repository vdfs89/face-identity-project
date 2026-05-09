# Flux.1 Identity Anchoring Prompt Template 🧬

This template is designed to maximize facial consistency by using technical photography tokens and descriptive anatomical markers.

## Template structure

```text
[PHOTO_TYPE], [SUBJECT_DESCRIPTION], [ANATOMICAL_TOKENS], [TECHNICAL_ANCHORS], [ENVIRONMENT], [LIGHTING], [STYLE_TOKENS]
```

## Example Prompt

```text
Professional close-up portrait, a 30-year-old woman with high cheekbones and a slight dimple on the left side, sharp jawline, asymmetrical eyebrows, cinematic lighting, 8k resolution, shot on 85mm lens, f/1.8, extremely detailed skin texture, micro-details on iris, identity-lock:high.
```

## Key Anchoring Tokens

- **Anatomical Tokens:** "High cheekbones", "sharp jawline", "asymmetrical eyebrows", "slight dimple". These create "unique identifiers" for the AI to hold onto.
- **Technical Anchors:** "shot on 85mm lens", "micro-details on iris". These force the model to focus on high-fidelity facial rendering rather than background noise.
- **Negative Prompting (if supported):** "identity drift, morphing, facial distortion, generic features".
