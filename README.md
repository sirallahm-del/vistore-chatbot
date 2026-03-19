# 🤖 VISTORÉ Chatbot

Ce projet est né d'une question simple : **est-ce qu'on peut remplacer les appels téléphoniques répétitifs d'un restaurant par une IA ?

La réponse est oui. Et c'est ce que fait ce chatbot.

---

## C'est quoi exactement ?

Un assistant virtuel pour restaurant marocain. Il répond aux clients qui posent des questions sur le menu, les horaires et les réservations — comme un vrai serveur, mais disponible 24h/24.

C'est le premier projet IA que j'ai construit from scratch, en Python, en partant de zéro.

---

## Ce qu'il sait faire

- Présenter le menu avec les prix en Dirhams
- Donner les horaires d'ouverture
- Orienter vers les réservations
- Garder le fil de la conversation (il se souvient de ce que tu as dit avant)

---

## Comment le lancer

```bash
git clone https://github.com/sirallahm-del/vistore-chatbot.git
cd vistore-chatbot
pip install -r requirements.txt
```

Crée un fichier `.env` avec ta clé Groq :
```
GROQ_API_KEY=ta_cle_ici
```

Puis :
```bash
python chatbot.py


## Exemple

```
Vous : C'est quoi le menu ?
Assistant : Bonsoir ! Voici nos spécialités du soir :
  • Tajine poulet — 85 DH
  • Couscous royal — 120 DH
  • Pastilla — 95 DH
  • Thé à la menthe — 15 DH
  Quelque chose vous tente ?
```

---

## Ce projet fait partie de VISTORÉ

[VISTORÉ](https://sirallahm-del.github.io/VISTORE_S/) 
