# Prompty do obrazków

[← Spis podręcznika](README.md)

Ten plik zawiera gotowe opisy (prompty) do wygenerowania obrazków dla podręcznika. Są dwa rodzaje:

- **Część A — Ilustracje klimatyczne** na początek rozdziałów (`obrazki/ilustracje/`). Już są wygenerowane — możesz je zrobić od nowa według tych promptów.
- **Część B — Schematy zasad** (`obrazki/`). Proste wersje już są w folderze. Prompty pozwalają zrobić ładniejsze — pod tą samą nazwą pliku.

Prompty są po angielsku, bo większość modeli rozumie angielski najlepiej.

---

## Zanim zaczniesz — ważne uwagi

1. **Bez nazw i znaków Warhammera.** Prompty celowo nie używają słów takich jak „Warhammer”, „Space Marine”, „Necron”, „Ork” czy „Tyranid”. Takie nazwy to znaki towarowe Games Workshop. Model może odmówić albo wygenerować podróbkę figurek GW, a takiego obrazka nie warto potem udostępniać. Opisujemy więc ogólny klimat: mroczna, gotycka fantastyka naukowa.
2. **Bez tekstu na obrazku.** Modele graficzne często źle piszą litery, a polskie znaki (ą, ę, ł, ż) prawie zawsze psują. Napisy — jeśli są potrzebne — lepiej dodać później w programie graficznym. Każdy prompt ma na końcu prośbę o brak tekstu.
3. **Bez przemocy.** Odbiorcą jest 11-latek. Prompty proszą o akcję i napięcie, ale bez krwi i drastycznych scen.
4. **Schematy muszą być dokładne.** Modele graficzne często mylą proporcje i odległości. Po wygenerowaniu schematu sprawdź go z opisem w polu „Co musi się zgadzać”. Jeśli się nie zgadza, zostaw prostą wersję, która już jest w folderze — jest narysowana dokładnie według zasad.
5. **Jeden styl dla całego podręcznika.** Do każdego promptu dodaj na początku odpowiedni **blok stylu** (niżej). Dzięki temu obrazki będą do siebie pasować.

---

## Bloki stylu

### STYL A — ilustracje

```
Painterly digital illustration for a children's tabletop game rulebook, gritty gothic science-fiction setting, small squads of armoured future soldiers, dramatic but kid-friendly (ages 10+), no blood, no gore, warm orange light against cold blue-grey shadows, rich detail, cinematic composition, slightly stylised like a modern board game box art.
```

**Negatyw (jeśli model go obsługuje):**

```
text, letters, words, logos, watermarks, signatures, blood, gore, corpses, skulls in close-up, recognizable trademarked miniatures, photorealistic faces, extra limbs, distorted hands
```

### STYL B — schematy

```
Clean flat vector infographic, top-down or side view as specified, light warm beige background, simple geometric shapes, thick clear outlines, colour code: blue circle = friendly operative, red circle = enemy operative, dark grey blocks = heavy terrain, ochre/brown blocks = light terrain, gold circle = objective marker, dotted black line = line of sight, dashed circle = 1 inch range. Minimal, educational, high contrast, no shadows, no perspective distortion, no text.
```

**Negatyw:**

```
text, letters, numbers, labels, words, logos, watermark, 3D render, perspective, clutter, photorealism, gradients, characters
```

Napisy i liczby (np. „1"”, „A”, „B”) dodaj później ręcznie, jeśli są potrzebne.

---

## Część A — Ilustracje klimatyczne

Zalecany format: **16:9** (np. 1600 × 900 px), chyba że podano inaczej.

### il_00_okladka.png — okładka podręcznika

- **Gdzie:** `README.md`, na górze.
- **Format:** 3:4 (pionowo), np. 1200 × 1600 px.

```
[STYL A] Book cover illustration: a small elite squad of five armoured future soldiers advancing through the ruins of a gothic industrial city at dusk, seen from a low heroic angle. One soldier crouches behind a broken wall aiming a rifle, another points forward giving orders, one carries a glowing data device. Smoke, sparks and distant searchlights. Leave the top third of the image calmer (sky and smoke) so a title can be added later. No text.
```

### il_01_zasady.png — zasady podstawowe

- **Gdzie:** `01_zasady_podstawowe.md`, pod tytułem.

```
[STYL A] An armoured future soldier crouching in cover behind a low ruined wall, peeking over it with a rifle, while a second soldier sprints across an open street behind him. Rubble, broken gothic arches, dust in the air, a ruined building with an upper floor in the background. The scene clearly shows the idea of cover and moving between cover. No text.
```

### il_02_misje.png — misje

- **Gdzie:** `02_misje.md`, pod tytułem.

```
[STYL A] Two rival squads of future soldiers — one in blue-grey armour, one in rust-red armour — racing towards a glowing circular objective beacon in the middle of a ruined plaza. Each side takes cover behind crates and broken pillars on opposite sides of the beacon. Tension before the clash, golden light from the beacon. No text.
```

### il_03_sprzet.png — sprzęt

- **Gdzie:** `03_sprzet.md`, pod tytułem.

```
[STYL A] A future soldier throwing a smoke grenade that bursts into a thick grey cloud, while a teammate climbs a metal ladder leaning against a two-storey ruin. In the foreground: a portable armoured shield on legs, coils of razor wire and an ammunition crate. Clear, readable equipment, gritty sci-fi style. No text.
```

### il_04_strefy_walki.png — strefy walki (ogólna)

- **Gdzie:** `04_strefy_walki.md`, pod tytułem.

```
[STYL A] Wide panoramic illustration split into four vertical panels showing four different battlefields: 1) ruined gothic city streets with a small fortified stronghold, 2) metal gantries above a glowing hazardous mining pit, 3) dark narrow corridors of an abandoned spaceship with heavy bulkhead doors, 4) an ancient tomb with green glowing portals and stone sarcophagi. Consistent lighting, no characters needed, no text.
```

### il_04_volkus.png — Volkus

- **Gdzie:** `04_strefy_walki.md`, rozdział 2.

```
[STYL A] A war-torn gothic industrial city: two small two-storey fortified strongholds with firing steps and heavy doors, roofless ruins with broken upper floors and barred windows, piles of heavy and light rubble across cracked streets. Elevated three-quarter view showing the layout like a game board. Small squads of soldiers taking positions. No text.
```

### il_04_bheta_decima.png — Bheta-Decima

- **Gdzie:** `04_strefy_walki.md`, rozdział 4.

```
[STYL A] An industrial mining facility: rusty metal gantries and walkways on pillars over a dangerous glowing pit floor, with a large cylindrical machine (a condenser) in the centre surrounded by battlements. Soldiers running along the gantries, steam and sparks, orange glow from below. Elevated three-quarter view. No text.
```

### il_04_tomb_world.png — Tomb World

- **Gdzie:** `04_strefy_walki.md`, rozdział 6.

```
[STYL A] Ancient alien tomb deep underground: dark stone and black metal corridors, glowing green portals in the walls, a breakable wall section cracking open from an explosion, two glowing teleport pads on the floor, a large sarcophagus in a central chamber. A squad of soldiers with flashlights advancing carefully. Mysterious, eerie but not scary for kids. No text.
```

### il_05_tryby_gry.png — inne tryby gry

- **Gdzie:** `05_inne_tryby_gry.md`, pod tytułem.

```
[STYL A] Two allied future soldiers standing back to back in a ruined courtyard, defending against a wave of shadowy, faceless alien creatures approaching from the fog. Teamwork and courage, dramatic rim lighting, no blood. No text.
```

### il_05_joint_ops.png — gra kooperacyjna

- **Gdzie:** `05_inne_tryby_gry.md`, rozdział 3.
- **Format:** 4:3.

```
Warm, friendly illustration (not grim): a parent and an 11-year-old child sitting side by side at a table covered with a miniature ruined-city battlefield, playing together on the same team, rolling dice and smiling, a rulebook and dice tray on the table. Cosy living-room lighting, semi-realistic painted style. No text, no logos.
```

---

## Część B — Schematy zasad

Zalecany format: **16:9** albo jak podano. Do każdego dodaj **STYL B**. W polu „Co musi się zgadzać” jest lista rzeczy, które sprawdzasz po wygenerowaniu.

### 01_control_range.png — zasięg kontroli

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 6.
- **Co musi się zgadzać:** po lewej niebieski i czerwony stoją tuż obok siebie, wokół niebieskiego przerywany okrąg (zasięg 1"), czerwony jest w środku okręgu. Po prawej czerwony i niebieski są tak samo blisko, ale między nimi stoi ciemnoszara ściana.

```
[STYL B] Top-down diagram in two halves. Left half: a blue circle and a red circle almost touching; a dashed ring around the blue circle with radius slightly larger than the distance to the red circle, the red circle inside the ring; a green check-mark symbol below. Right half: a red circle and a blue circle the same short distance apart but separated by a thick dark grey wall segment between them; a red cross symbol below. No text.
```

### 02_cover.png — osłona (4 przypadki)

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 11.
- **Format:** 16:10, siatka 2 × 2.
- **Co musi się zgadzać:** w każdym polu czerwony (strzelec) po lewej, niebieski (cel) po prawej, kropkowana linia między nimi. 1) brązowy blok tuż przed celem, na linii — ✔. 2) brązowy blok na linii, ale daleko od celu — ✘. 3) brązowy blok tuż przy celu, ale obok linii — ✘. 4) strzelec bardzo blisko celu, blok między nimi — ✘.

```
[STYL B] A 2 by 2 grid of four small top-down panels, each with a red circle on the left and a blue circle on the right connected by a dotted line. Panel 1: a small ochre block placed right next to the blue circle, crossing the dotted line; green check symbol. Panel 2: the ochre block crossing the dotted line but far from the blue circle, near the middle; red cross symbol. Panel 3: the ochre block right next to the blue circle but off to the side, not touching the dotted line; red cross symbol. Panel 4: the red and blue circles very close together with the ochre block between them; red cross symbol. A faint dashed ring around each blue circle. No text.
```

### 03_obscured.png — zasłonięcie

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 11.
- **Co musi się zgadzać:** lewa strona — duży ciemnoszary blok dokładnie w środku między figurkami (✔ zasłonięty). Prawa strona — taki sam blok tuż przy strzelcu (✘).

```
[STYL B] Two side-by-side top-down panels. Left: red circle far left, blue circle far right, a large dark grey wall block exactly in the middle crossing the dotted line between them; green check symbol. Right: the same, but the dark grey block is placed immediately next to the red circle, touching it; red cross symbol. No text.
```

### 04_rozkazy.png — rozkazy Engage i Conceal

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 8.
- **Co musi się zgadzać:** trzy panele. 1) cel z symbolem oka przekreślonego (ukryty) za brązowym blokiem — ✔. 2) cel z symbolem przekreślonego oka bez bloku — ✘. 3) cel z symbolem celownika (gotowy do walki) za brązowym blokiem — ✘.

```
[STYL B] Three side-by-side top-down panels, each with a red circle on the left and a blue circle on the right joined by a dotted line. Above the blue circle a small icon badge: panels 1 and 2 show a closed-eye icon (hidden), panel 3 shows a crosshair icon (ready to fight). Panel 1: an ochre block directly in front of the blue circle; green check. Panel 2: no block, open ground; red cross. Panel 3: an ochre block directly in front of the blue circle; red cross. No text.
```

### 05_vantage.png — strzelanie z punktu obserwacyjnego

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 16.
- **Format:** 2:1, **widok z boku**.
- **Co musi się zgadzać:** czerwona figurka na dachu budynku po lewej, niebieska na ziemi po prawej, za nią niska brązowa skrzynka. Kropkowana linia z góry na dół, nad skrzynką. Strzałka pionowa pokazuje różnicę wysokości.

```
[STYL B] Side-view cross-section diagram. On the left, a tall dark grey building with a flat roof; a small red standing figure silhouette on the roof. On the right on the ground, a small blue standing figure silhouette with a low ochre crate just in front of it, facing the building. A dotted line goes diagonally from the red figure down over the crate to the blue figure. A vertical double-headed arrow at the far right shows the height difference between roof level and ground. Flat ground line across the bottom. No text.
```

### 06_ruch_pionowy.png — wspinanie, zeskok, skok

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 10.
- **Format:** 3:1, trzy panele, **widok z boku**.
- **Co musi się zgadzać:** 1) figurka przy ścianie, strzałka w górę, potem w bok na dach. 2) figurka na dachu, strzałka w bok i pionowo w dół na ziemię. 3) dwa budynki z przerwą, figurka skacze łukiem z wyższego na niższy.

```
[STYL B] Three side-view panels in a row. Panel 1 (climb): a small blue figure on the ground next to a grey block, a blue arrow going straight up the wall then turning onto the roof, a faded copy of the figure on the roof. Panel 2 (drop): a faded blue figure on top of a grey block, an arrow going sideways off the edge then straight down to the ground, a solid blue figure on the ground. Panel 3 (jump): two grey blocks with a gap between them, the left one taller; a curved blue arc arrow from the faded figure on the taller block to the solid figure on the lower block. No text.
```

### 07_linie_celowania.png — linie celowania

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 11.
- **Co musi się zgadzać:** z jednego punktu na krawędzi czerwonego koła wychodzi wachlarz cienkich linii do całej bliższej krawędzi niebieskiego koła. Lewo: brązowy blok przecina część linii (✔). Prawo: blok jest obok wachlarza i go nie dotyka (✘).

```
[STYL B] Two top-down panels. In each: a red circle on the left and a blue circle on the right; from a single point on the red circle's edge, a fan of 7 thin grey straight lines spreads to points all along the facing half of the blue circle's edge. Left panel: a small ochre block placed so that it crosses some of the lines; green check. Right panel: the ochre block placed above the fan, not touching any line; red cross. No text.
```

### 08_runda.png — przebieg rundy

- **Gdzie:** `01_zasady_podstawowe.md`, rozdział 7.
- **Uwaga:** ten schemat jest głównie tekstowy, więc model graficzny słabo się sprawdzi. Lepiej zostawić obecną wersję albo wygenerować samo tło z ikonami i dopisać tekst ręcznie.

```
[STYL B] A flow diagram with two large rounded rectangles side by side connected by a thick arrow from left to right. Left rectangle (pale blue) contains three stacked icons: two dice, a stack of tokens, a playing card. Right rectangle (pale orange) contains three stacked icons: a toggle switch with two states, a lightning bolt, a check mark. A circular return arrow from the right rectangle back to the left, with four small dots on it. No text.
```

### 09_mapa_misji.png — mapa misji

- **Gdzie:** `02_misje.md`, rozdział 2.
- **Format:** 30:22 (np. 1500 × 1100 px), **widok z góry**.
- **Co musi się zgadzać:** prostokątny stół; pas na dole (niebieski) i na górze (czerwony) — strefy rozstawienia; przerywana linia przez środek; trzy złote koła: jedno na linii środkowej, jedno na dolnej połowie, jedno na górnej; kilka szarych i brązowych bloków.

```
[STYL B] Top-down game board map, a rectangle with a 30 to 22 width-to-height ratio. A pale blue band along the bottom edge and a pale red band along the top edge (deployment zones). A dashed horizontal line across the exact middle. Three gold circles: one on the middle line at the centre, one in the lower half towards the left, one in the upper half towards the right. Several dark grey rectangles and ochre bars scattered evenly as terrain, roughly mirrored between the halves. No text.
```

### 10_inicjatywa.png — rzut o inicjatywę

- **Gdzie:** `02_misje.md`, rozdział 4.
- **Format:** 3:1.
- **Uwaga:** ten schemat jest tekstowy — model graficzny może zrobić ładne tło z ikonami, a tekst dopisz ręcznie.

```
[STYL B] Four rounded boxes in a row connected by arrows. Box 1: two dice. Box 2: two hands each holding a small playing card. Box 3: a crown or a flag icon. Box 4: a single card with a small plus-minus symbol. No text.
```

### 11_flank.png — Tac Op Flank

- **Gdzie:** `02_misje.md`, rozdział 8.
- **Format:** 30:22, **widok z góry**.
- **Co musi się zgadzać:** stół podzielony przerywaną linią poziomo (połowy graczy) i ciągłą linią pionowo (flanki). Górna-lewa ćwiartka fioletowa, górna-prawa zielona, dolna połowa neutralna. W lewej ćwiartce 2 niebieskie i 1 czerwony, w prawej 1 niebieski i 2 czerwone.

```
[STYL B] Top-down game board rectangle, 30 to 22 ratio. A dashed horizontal line across the middle and a solid vertical line down the middle, making four quarters. The top-left quarter is tinted pale purple, the top-right quarter pale teal, the bottom half plain beige. In the top-left quarter: two blue circles and one red circle. In the top-right quarter: one blue circle and two red circles. No text.
```

### 12_gallowdark.png — właz zamknięty i otwarty

- **Gdzie:** `04_strefy_walki.md`, rozdział 5.
- **Co musi się zgadzać:** dwa panele z góry. W obu pionowa gruba ściana przez środek, niebieski po lewej, czerwony po prawej. Lewo: w środku ściany ciemnoczerwona klapa (zamknięty). Prawo: w środku ściany przerwa z przerywanym obrysem, kropkowana linia między figurkami przechodzi przez przerwę.

```
[STYL B] Two top-down panels side by side. In each, a thick vertical charcoal wall runs through the middle with a blue circle on the left and a red circle on the right. Left panel: in the centre of the wall a dark red door segment fills the gap completely. Right panel: the centre of the wall has an open gap outlined with a dashed dark red rectangle, and a dotted line passes through the gap from the blue circle to the red circle. Sci-fi spaceship corridor feel through subtle floor plating texture. No text.
```

---

## Lista kontrolna

| Plik | Typ | Jest w folderze? |
|---|---|---|
| `obrazki/ilustracje/il_00_okladka.png` | ilustracja | tak |
| `obrazki/ilustracje/il_01_zasady.png` | ilustracja | tak |
| `obrazki/ilustracje/il_02_misje.png` | ilustracja | tak |
| `obrazki/ilustracje/il_03_sprzet.png` | ilustracja | tak |
| `obrazki/ilustracje/il_04_strefy_walki.png` | ilustracja | tak |
| `obrazki/ilustracje/il_04_volkus.png` | ilustracja | tak |
| `obrazki/ilustracje/il_04_bheta_decima.png` | ilustracja | tak |
| `obrazki/ilustracje/il_04_tomb_world.png` | ilustracja | tak |
| `obrazki/ilustracje/il_05_tryby_gry.png` | ilustracja | tak |
| `obrazki/ilustracje/il_05_joint_ops.png` | ilustracja | tak |
| `obrazki/01_control_range.png` … `obrazki/12_gallowdark.png` | schemat | tak (prosta wersja) |

[← Spis podręcznika](README.md)
