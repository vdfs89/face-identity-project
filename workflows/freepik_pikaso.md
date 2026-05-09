# Freepik Pikaso Workflow for Identity Consistency 🎨

Guide to using Freepik Pikaso's tools to maintain facial identity.

## Step 1: Base Image Generation
- Use the **Flux.1** engine for high anatomical fidelity.
- Input your **Anchor Prompt** (see `/prompts/flux_anchor.md`).
- Generate 4 variations and select the one that best matches the target identity.

## Step 2: Reference Image Upload (Face Swap / Structure)
- Use the "Style Reference" or "Face Reference" feature.
- Set the **Influence Weight** to 0.7 - 0.8. 
    - *Tip:* Going higher than 0.8 often destroys the new prompt's style. 
    - *Tip:* Going lower than 0.6 allows for significant identity drift.

## Step 3: Inpainting for Refinement
- If the generated image has minor distortions (e.g., eyes not matching, jawline slightly off):
    - Use the **Pikaso Inpainting** tool.
    - Mask ONLY the affected area.
    - Use a prompt focusing purely on that feature (e.g., "extremely detailed realistic eye iris, sharp focus").
    - Keep the "Denoising Strength" low (around 0.4) to maintain the base structure.

## Step 4: Upscaling
- Use the **AI Upscaler** to finalize textures.
- This often "bakes in" the identity by adding micro-pores and skin details that were lost in the generation phase.
