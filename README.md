# ffce-fiscal-security-guoard
Economic antifraud system (MVP): risk rules, immutable audit log (hash-chain), account suspension and judicial review flow.
# FFCE – Fiscal Security Guard

**Economic antifraud system (MVP)**  
Risk detection · Immutable audit log · Preventive alerts · Legal escalation flow

---

## 📌 Scopul proiectului

FFCE (Fiscal & Financial Compliance Engine) este un sistem de **prevenție și detecție a neregulilor economice**, conceput pentru:

- identificarea **riscurilor financiare și contabile**
- semnalarea **neconformităților legale**
- prevenirea **fraudelor intenționate sau accidentale**
- oferirea unui **mecanism transparent de avertizare și corecție**
- protejarea organizației și a persoanelor implicate

⚠️ **Sistemul NU este o instanță de judecată.**  
Nu emite verdicte juridice și nu aplică sancțiuni legale.

---

## ⚖️ Principiul de funcționare

FFCE funcționează ca un **sistem de avertizare și control preventiv**, nu ca un organ de pedepsire.

Scopul său este:
- să **informeze**
- să **prevină**
- să **documenteze**

Nu să judece sau să condamne.

---

## 🔍 Ce verifică sistemul

FFCE analizează, în mod controlat:

- inconsecvențe contabile  
- modificări neautorizate ale datelor  
- încălcări ale regulilor interne  
- pattern-uri suspecte (fraudă, abuz, manipulare)  
- modificări care pot genera risc fiscal sau juridic  

---

## 🚦 Niveluri de reacție (graduale)

### 🟢 Nivel 1 – Avertizare informativă
- utilizatorul este notificat
- se indică exact **ce regulă nu este respectată**
- se oferă timp pentru corectare

### 🟡 Nivel 2 – Avertizare oficială
- se înregistrează incidentul
- este notificată conducerea (ex: director financiar)
- accesul poate fi limitat temporar

### 🔴 Nivel 3 – Blocare + notificare autorități
- activată **doar dacă există risc major**
- datele sunt sigilate în jurnalul de audit
- autoritățile competente pot fi notificate
- accesul este suspendat până la clarificare

---

## 🧠 Principiul de prevenție

Sistemul este construit pentru a:
- preveni erorile umane
- avertiza înainte de consecințe legale
- oferi explicații clare despre **ce este greșit și de ce**
- permite corectarea voluntară

---

## 🔐 Integritatea datelor

- Toate evenimentele sunt înregistrate într-un **audit log imutabil (hash-chain)**  
- Orice tentativă de modificare este detectată automat  
- Jurnalul poate fi auditat independent  

---

## 🧭 Conformitate legală

FFCE operează în conformitate cu:
- legislația fiscală națională aplicabilă
- principiile europene de conformitate și audit
- bune practici internaționale de guvernanță

⚠️ FFCE nu substituie autoritățile legale.

---

## 🧩 Arhitectură (simplificat)

- `integrity.py` – verificare integritate & audit log  
- `middleware.py` – control acces și blocare preventivă  
- `state.py` – stare globală și mecanism de blocare  
- `main.py` – interfață API (FastAPI)  

---

## 🛡️ Scop etic

Acest sistem este creat pentru:
- protecția organizațiilor corecte  
- responsabilitate economică  
- transparență decizională  

Nu este destinat abuzului, supravegherii excesive sau sancționării arbitrare.

---

## 📄 Licență

Vezi fișierul `LICENSE`.

---

## 🧭 Notă finală

Utilizarea acestui sistem implică acceptarea principiilor de:
**transparență – responsabilitate – legalitate – bună credință**.
