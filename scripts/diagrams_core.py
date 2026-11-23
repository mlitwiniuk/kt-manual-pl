import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Polygon
import os, sys

OUT = sys.argv[1]
plt.rcParams["font.family"] = "DejaVu Sans"

BLUE = "#2f6fb3"     # nasi
RED = "#c0392b"      # wrogowie
HEAVY = "#555555"
LIGHT = "#b08a4a"
OK = "#2e8b57"
BAD = "#c0392b"
GRID = "#eeeeee"


def base(ax, x, y, label, color, r=0.5):
    ax.add_patch(Circle((x, y), r, color=color, zorder=5))
    ax.text(x, y, label, color="white", ha="center", va="center",
            fontsize=13, fontweight="bold", zorder=6)


def setup(ax, w, h, title=None):
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#cccccc")
    ax.set_facecolor("#fafafa")
    if title:
        ax.set_title(title, fontsize=12, fontweight="bold", pad=8)


def verdict(ax, x, y, text, good):
    ax.text(x, y, ("✔ " if good else "✘ ") + text, ha="center", va="center",
            fontsize=11, fontweight="bold", color=OK if good else BAD,
            bbox=dict(boxstyle="round,pad=0.3", fc="white",
                      ec=OK if good else BAD))


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=130, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# 1. CONTROL RANGE --------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.2))
setup(ax, 12, 6.3)
base(ax, 2.5, 3, "A", BLUE)
ax.add_patch(Circle((2.5, 3), 1.5, fill=False, ls="--", ec=BLUE, lw=1.5))
ax.text(2.5, 4.85, "zasięg 1\"", ha="center", color=BLUE, fontsize=10)
base(ax, 3.9, 3, "B", RED)
verdict(ax, 3.2, 0.9, "A i B: w Control Range", True)

ax.add_patch(Rectangle((8.3, 1.6), 0.35, 3.0, color=HEAVY))
ax.text(8.47, 4.9, "ściana", ha="center", fontsize=10, color=HEAVY)
base(ax, 7.6, 3, "B", RED)
base(ax, 9.35, 3, "C", BLUE)
ax.annotate("", xy=(8.85, 3), xytext=(8.1, 3),
            arrowprops=dict(arrowstyle="<->", color="#333"))
ax.text(8.47, 2.45, "< 1\"", ha="center", fontsize=9, color="white", fontweight="bold")
verdict(ax, 8.5, 0.9, "B i C: NIE (nie widzą się)", False)
save(fig, "01_control_range.png")


# 2. COVER - 4 przypadki ----------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(10, 6.2))
cases = [
    ("1. Teren blisko celu i na linii strzału", 8.35, 2.2, True,
     "W osłonie (Cover)"),
    ("2. Teren na linii strzału, ale daleko od celu", 4.5, 2.2, False,
     "Brak osłony"),
    ("3. Teren blisko celu, ale z boku", 8.6, 0.25, False, "Brak osłony"),
    ("4. Strzelec bliżej niż 2\"", 2.85, 2.2, False,
     "Brak osłony (za blisko)"),
]
for ax, (title, tx, ty, good, txt) in zip(axs.flat, cases):
    setup(ax, 12, 4.4, title)
    sx = 1.2 if "Strzelec" not in title else 1.3
    tgt = 9.5 if "Strzelec" not in title else 4.6
    if "Strzelec" in title:
        tx, ty = 3.55, 2.2
    base(ax, sx, 2.2, "S", RED)
    base(ax, tgt, 2.2, "A", BLUE)
    ax.plot([sx + 0.5, tgt - 0.5], [2.2, 2.2], ls=":", color="#444", lw=1.5)
    if "z boku" in title:
        ax.add_patch(Rectangle((tx, 2.9), 0.9, 0.3, color=LIGHT))
    else:
        ax.add_patch(Rectangle((tx if "Strzelec" not in title else tx,
                                ty - 0.9), 0.3, 1.8, color=LIGHT))
    if "Strzelec" not in title:
        ax.add_patch(Circle((tgt, 2.2), 1.5, fill=False, ls="--", ec=BLUE,
                            lw=1))
    else:
        ax.annotate("", xy=(tgt - 0.5, 0.9), xytext=(sx + 0.5, 0.9),
                    arrowprops=dict(arrowstyle="<->", color="#333"))
        ax.text((sx + tgt) / 2, 0.45, "≤ 2\"", ha="center", fontsize=9)
    verdict(ax, 7.5 if "Strzelec" in title else 6, 3.95 if "z boku" not in
            title else 3.95, txt, good)
fig.text(0.5, 0.01, "S = strzelec,  A = cel,  przerywany okrąg = 1\" wokół "
         "celu,  kropki = linia strzału", ha="center", fontsize=9,
         color="#555")
fig.tight_layout(rect=(0, 0.03, 1, 1))
save(fig, "02_cover.png")


# 3. OBSCURED ----------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(10, 3.4))
setup(axs[0], 12, 4.4, "Ciężki teren daleko od obu figurek")
base(axs[0], 1.2, 2.2, "S", RED)
base(axs[0], 10.8, 2.2, "A", BLUE)
axs[0].add_patch(Rectangle((5.6, 0.8), 0.8, 2.8, color=HEAVY))
axs[0].plot([1.7, 10.3], [2.2, 2.2], ls=":", color="#444", lw=1.5)
axs[0].text(6.0, 3.85, "okno w ścianie (Heavy)", ha="center", fontsize=9)
verdict(axs[0], 6, 0.35, "Zasłonięty (Obscured)", True)

setup(axs[1], 12, 4.4, "Ciężki teren tuż przy strzelcu")
base(axs[1], 1.2, 2.2, "S", RED)
base(axs[1], 10.8, 2.2, "A", BLUE)
axs[1].add_patch(Rectangle((2.0, 0.8), 0.6, 2.8, color=HEAVY))
axs[1].plot([1.7, 10.3], [2.2, 2.2], ls=":", color="#444", lw=1.5)
axs[1].text(2.3, 3.85, "róg budynku", ha="center", fontsize=9)
verdict(axs[1], 6.5, 0.35, "Nie zasłonięty (wychyla się)", False)
fig.tight_layout()
save(fig, "03_obscured.png")


# 4. ROZKAZY: ENGAGE / CONCEAL --------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(12, 3.6))
data = [
    ("Conceal + osłona", "C", True, False,
     "Nie można\ndo niego strzelać"),
    ("Conceal na otwartym terenie", "C", False, True,
     "Można strzelać\n(bez darmowej obrony)"),
    ("Engage + osłona", "E", True, True,
     "Można strzelać,\nale ma 1 darmowy obronny rzut"),
]
for ax, (title, order, cover, shootable, txt) in zip(axs, data):
    setup(ax, 8, 5, title)
    base(ax, 1.0, 2.6, "S", RED)
    base(ax, 6.5, 2.6, "A", BLUE)
    ax.text(6.5, 3.5, "Conceal" if order == "C" else "Engage", ha="center",
            fontsize=9, color="white",
            bbox=dict(boxstyle="round", fc="#333" if order == "C" else
                      "#d35400"))
    if cover:
        ax.add_patch(Rectangle((5.4, 1.7), 0.3, 1.8, color=LIGHT))
    ax.plot([1.5, 6.0], [2.6, 2.6], ls=":", color="#444", lw=1.5)
    verdict(ax, 4, 0.75, txt, not shootable)
fig.text(0.5, 0.01, "✔ = dobrze dla celu A,  ✘ = cel A może oberwać",
         ha="center", fontsize=9, color="#555")
fig.tight_layout(rect=(0, 0.04, 1, 1))
save(fig, "04_rozkazy.png")


# 5. VANTAGE (widok z boku) ---------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.4))
ax.set_xlim(0, 14)
ax.set_ylim(-0.3, 7)
ax.set_aspect("equal")
ax.axis("off")
ax.plot([0, 14], [0, 0], color="#333", lw=2)
ax.text(13.9, -0.25, "podłoga stołu", ha="right", fontsize=9, va="top")
ax.add_patch(Rectangle((0.5, 0), 3.5, 4.0, color=HEAVY, alpha=0.85))
ax.text(2.25, 2.0, "budynek\n(Heavy)", color="white", ha="center",
        va="center", fontsize=10)
ax.add_patch(Rectangle((0.5, 4.0), 3.5, 0.15, color="#2d2d2d"))
ax.text(0.5, 3.6, "piętro = Vantage", ha="left", fontsize=9, color="white")
ax.add_patch(Rectangle((1.9, 4.15), 0.7, 1.2, color=RED))
ax.text(2.25, 4.75, "S", color="white", ha="center", va="center",
        fontsize=12, fontweight="bold")
ax.add_patch(Rectangle((9.0, 0), 0.4, 1.0, color=LIGHT))
ax.text(8.8, 0.5, "skrzynka\n(Light)", ha="right", fontsize=9, va="center")
ax.add_patch(Rectangle((10.0, 0), 0.7, 1.2, color=BLUE))
ax.text(10.35, 0.6, "A", color="white", ha="center", va="center",
        fontsize=12, fontweight="bold")
ax.plot([2.6, 10.0], [5.2, 1.1], ls=":", color="#444", lw=1.5)
ax.annotate("", xy=(12.0, 0.05), xytext=(12.0, 4.1),
            arrowprops=dict(arrowstyle="<->", color="#333"))
ax.plot([4.0, 12.2], [4.1, 4.1], ls="--", color="#999", lw=0.8)
ax.text(12.2, 2.1, "4\" niżej", fontsize=10, va="center")
ax.text(7, 6.6, "Strzelec na Vantage, cel co najmniej 2\" niżej", ha="center",
        fontsize=12, fontweight="bold")
ax.text(4.6, 5.85, "• cel z Conceal za lekkim terenem MOŻNA wybrać na cel\n"
        "   (ale dostaje lepszą darmową obronę)\n"
        "• na cel z Engage broń dostaje Accurate 1 (≥2\" niżej)\n"
        "   lub Accurate 2 (≥4\" niżej)", ha="left", fontsize=9.5, va="top")
save(fig, "05_vantage.png")


# 6. RUCH PIONOWY (widok z boku) -------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.8))
titles = ["Climb (wspinanie)", "Drop (zeskok)", "Jump (skok z Vantage)"]
for ax, t in zip(axs, titles):
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.4, 6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(t, fontsize=12, fontweight="bold")
    ax.plot([0, 10], [0, 0], color="#333", lw=2)

# climb
a = axs[0]
a.add_patch(Rectangle((4, 0), 3, 3, color=HEAVY, alpha=0.85))
a.add_patch(Rectangle((2.6, 0), 0.6, 1.0, color=BLUE))
a.add_patch(Rectangle((5.0, 3), 0.6, 1.0, color=BLUE, alpha=0.5))
a.annotate("", xy=(3.7, 3.2), xytext=(3.7, 0.2),
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
a.annotate("", xy=(4.9, 3.5), xytext=(3.7, 3.5),
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
a.text(3.5, 1.6, "3\"", ha="right", fontsize=11, fontweight="bold")
a.text(5, -0.35, "w poziomie ≤1\" od ściany, wysokość ≤3\"\n"
       "każda wspinaczka liczy się min. jako 2\"", ha="center", va="top",
       fontsize=8.5)

# drop
a = axs[1]
a.add_patch(Rectangle((1, 0), 3, 3, color=HEAVY, alpha=0.85))
a.add_patch(Rectangle((2.5, 3), 0.6, 1.0, color=BLUE, alpha=0.5))
a.add_patch(Rectangle((5.2, 0), 0.6, 1.0, color=BLUE))
a.annotate("", xy=(4.6, 3.3), xytext=(3.2, 3.3),
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
a.annotate("", xy=(4.6, 0.2), xytext=(4.6, 3.3),
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
a.text(4.8, 1.7, "3\" w dół\n= płacisz 1\"", fontsize=9, va="center")
a.text(5, -0.35, "pierwsze 2\" spadania w akcji są za darmo", ha="center",
       va="top", fontsize=8.5)

# jump
a = axs[2]
a.add_patch(Rectangle((0.3, 0), 3, 3.5, color=HEAVY, alpha=0.85))
a.add_patch(Rectangle((7.0, 0), 2.7, 2.6, color=HEAVY, alpha=0.85))
a.add_patch(Rectangle((1.8, 3.5), 0.6, 1.0, color=BLUE, alpha=0.5))
a.add_patch(Rectangle((7.4, 2.6), 0.6, 1.0, color=BLUE))
a.annotate("", xy=(7.4, 3.9), xytext=(2.4, 4.0),
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=2,
                           connectionstyle="arc3,rad=-0.25"))
a.text(5.0, 5.3, "do 4\" w poziomie", ha="center", fontsize=9.5)
a.text(5, -0.35, "tylko z Vantage wyższego niż 2\"\n"
       "jedna prosta linia, potem zeskok lub wspinaczka", ha="center",
       va="top", fontsize=8.5)
fig.tight_layout()
save(fig, "06_ruch_pionowy.png")


# 7. LINIE CELOWANIA ---------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
for ax, (title, yterrain, good, txt) in zip(axs, [
        ("Choć jedna linia przecina teren", 2.6, True,
         "Teren przesłania (intervening)"),
        ("Żadna linia nie przecina terenu", 4.3, False,
         "Teren NIE przesłania")]):
    setup(ax, 12, 5, title)
    base(ax, 1.2, 2.5, "S", RED, r=0.6)
    base(ax, 10.6, 2.5, "A", BLUE, r=0.6)
    import numpy as np
    for ang in np.linspace(-1.2, 1.2, 7):
        ex = 10.6 + 0.6 * np.cos(np.pi - ang)
        ey = 2.5 + 0.6 * np.sin(np.pi - ang)
        ax.plot([1.2, ex], [3.0, ey], color="#777", lw=0.8)
    ax.add_patch(Rectangle((6.5, yterrain), 0.5, 1.4 if yterrain > 3 else
                           1.2, color=LIGHT))
    verdict(ax, 6, 0.5, txt, good)
fig.text(0.5, 0.01, "Linie rysujesz z jednego punktu podstawki strzelca do "
         "każdego punktu podstawki celu (widok z góry)", ha="center",
         fontsize=9, color="#555")
fig.tight_layout(rect=(0, 0.04, 1, 1))
save(fig, "07_linie_celowania.png")


# 8. PRZEBIEG RUNDY -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 4.8))
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
ax.axis("off")


def box(x, y, w, h, title, body, color):
    ax.add_patch(Rectangle((x, y), w, h, fc=color, ec="#333", lw=1.2,
                           alpha=0.95))
    ax.text(x + w / 2, y + h - 0.55, title, ha="center", va="top",
            fontsize=12, fontweight="bold")
    ax.text(x + 0.35, y + h - 1.45, body, ha="left", va="top", fontsize=9.5,
            linespacing=1.45)


box(0.3, 2.6, 9, 6.4, "STRATEGY PHASE (Faza Strategii)",
    "1. Initiative – rzut kośćmi, kto zaczyna\n"
    "2. Ready – dostajesz CP, wszystkie\n"
    "    figurki znów są gotowe (Ready)\n"
    "3. Gambit – na zmianę zagrywacie\n"
    "    zagrywki strategiczne (Strategy Ploys)\n"
    "    albo pasujecie", "#e8f0fa")
box(10.7, 2.6, 9, 6.4, "FIREFIGHT PHASE (Faza Walki)",
    "Na zmianę, po JEDNEJ figurce:\n"
    "  a) wybierz rozkaz: Engage / Conceal\n"
    "  b) wykonaj akcje (max = APL)\n"
    "  c) figurka jest zużyta (Expended)\n\n"
    "Kiedy jeden gracz skończy figurki,\n"
    "drugi aktywuje resztę, a pierwszy\n"
    "może robić Counteract.", "#fbeee6")
ax.annotate("", xy=(10.6, 5.8), xytext=(9.4, 5.8),
            arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#333"))
ax.text(10, 9.6, "Jedna runda (Turning Point) – gra ma ich zwykle 4",
        ha="center", fontsize=13, fontweight="bold")
save(fig, "08_runda.png")

print("ok")
