# Project Brief & Product Requirements Document (PRD)

## 1. Project Overview
**Project Name:** Carlos Bernardo Institutional Ecosystem  
**Client:** Carlos Bernardo (Business Leader, Educator, and Visionary)  
**Objective:** Develop a high-fidelity, premium institutional website that establishes Carlos Bernardo's authority in high-level leadership and education, showcasing his professional trajectory, strategic projects (Grupo Monarca), and educational legacy (Universidad Interamericana).

## 2. Visual Identity & Design System
**Design System Name:** Cinematic Editorial (`{{DATA:DESIGN_SYSTEM:DESIGN_SYSTEM_1}}`)  
**Core Aesthetic:** A "Cinematic Editorial" style characterized by luxury typography, high-contrast imagery, and purposeful negative space. It balances the authority of a business leader with the accessibility of an educator.

### Design Tokens:
*   **Color Palette:**
    *   **Surface:** Dark/Ink (#131312) providing a premium, nocturnal foundation.
    *   **Accent:** Copper/Gold (#c17f59) used for highlights, icons, and CTA elements.
    *   **Text:** Cream/Muted Gray for legibility and sophistication.
*   **Typography:** *Playfair Display* (Headlines) and *Inter/Lora* (Body), utilizing serif styles for an editorial look.
*   **Interactions:** Smooth `cubic-bezier` entry animations, mouse-tracking hover effects, and horizontal looping "Instagram-style" story feeds.

## 3. Technical Architecture (i18n)
The project utilizes a custom reactive Internationalization (i18n) engine.
*   **Supported Languages:** Portuguese (pt-BR), Spanish (es-419), English (en), and Mandarin (zh-CN).
*   **State Management:** Instant DOM-level updates without full page reloads.
*   **Fallback Policy:** `pt-BR` is the root locale. Any missing translation key in other dictionaries automatically falls back to the Portuguese string.
*   **Data Structure:** 100% of strings are mapped to semantic JSON dictionaries; no hardcoded text in components.

## 4. Site Map & Screen Inventory
The ecosystem consists of 5 core desktop screens:

1.  **Home (Hero Cinematográfica):**
    *   **Feature:** Cinematic portrait of Carlos Bernardo with integrated dynamic highlights.
    *   **Feature:** "Instagram Highlights" style feed for Technology, Agribusiness, Education, Health, and Infrastructure.
2.  **Trajetória (Trajectory):**
    *   **Feature:** Chronological narrative of his roots (Carajá) to his binational legacy.
    *   **Focus:** Humanization, Integration, and Innovation.
3.  **Projetos (Projects):**
    *   **Feature:** Strategic portfolio highlighting Grupo Monarca and Global Ventures.
    *   **Focus:** Impact metrics (484 families, 12k+ hectares, 15 tech ventures).
4.  **Universidad:**
    *   **Feature:** Dedicated space for Universidad Interamericana.
    *   **Focus:** Mission, infrastructure (Labs, Library, Plaza), and a bilingual manifesto.
5.  **Contato (Contact):**
    *   **Feature:** Minimalist lead capture form for institutional relations.
    *   **Focus:** Location mapping and direct communication channels.

## 5. Component Specifications
*   **TopNavBar:** Fixed position with a quadrimodal language switcher (PT | ES | EN | ZH).
*   **Dynamic Feed:** Horizontal auto-scrolling ticker/feed for "Impact Metrics" and "Latest News".
*   **Editorial Grid:** Responsive layouts that adapt typography alignment based on the negative space of photographic assets.
*   **Footer:** Minimalist structure with legal links, social icons, and professional credits.

## 6. Constraints & Compliance
*   **Imagery:** Use high-resolution, premium editorial photography only.
*   **Exclusions:** No references to political parties or elective offices.
*   **Language:** Strict adherence to localized terminology (e.g., specific terms for Paraguayan/South American educational contexts).
