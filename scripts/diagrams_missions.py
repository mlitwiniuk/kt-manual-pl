import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import os, sys

OUT = sys.argv[1]
plt.rcParams["font.family"] = "DejaVu Sans"
BLUE, RED, HEAVY, LIGHT = "#2f6fb3", "#c0392b", "#555555", "#b08a4a"
OBJ = "#e0a800"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=130, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def board(ax, title=None):
    ax.set_xlim(-1, 31)
    ax.set_ylim(-1.5, 23.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 30, 22, fc="#f4f1ea", ec="#333", lw=2))
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold")


def obj(ax, x, y, label):
    ax.add_patch(Circle((x, y), 0.79, fc=OBJ, ec="#333", lw=1.2, zorder=5))
    ax.text(x, y, label, ha="center", va="center", fontsize=10,
            fontweight="bold", zorder=6)


# 09 MAPA MISJI ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 7))
board(ax, "Przykładowa mapa misji (widok z góry)")
ax.add_patch(Rectangle((0, 0), 30, 11, fc=BLUE, alpha=0.07))
ax.add_patch(Rectangle((0, 11), 30, 11, fc=RED, alpha=0.07))
ax.add_patch(Rectangle((0, 0), 30, 3, fc=BLUE, alpha=0.25))
ax.add_patch(Rectangle((0, 19), 30, 3, fc=RED, alpha=0.25))
ax.plot([0, 30], [11, 11], ls="--", color="#333", lw=1.5)
ax.text(30.3, 11, "linia\nśrodkowa", va="center", fontsize=9)
ax.text(15, 1.5, "TWOJA STREFA ROZSTAWIENIA (drop zone)", ha="center",
        va="center", fontsize=10, color=BLUE, fontweight="bold")
ax.text(15, 20.5, "STREFA ROZSTAWIENIA PRZECIWNIKA", ha="center",
        va="center", fontsize=10, color=RED, fontweight="bold")
ax.text(1, 4.3, "TWOJE TERYTORIUM\n(territory)", fontsize=10, color=BLUE)
ax.text(1, 17.0, "TERYTORIUM\nPRZECIWNIKA", fontsize=10, color=RED)
obj(ax, 15, 11, "C")
obj(ax, 8, 7.5, "T")
obj(ax, 22, 14.5, "P")
# teren
for (x, y, w, h, c) in [(4, 12.5, 4, 3, HEAVY), (22, 5, 4, 3, HEAVY),
                        (12, 15, 1, 3, LIGHT), (17, 4, 1, 3, LIGHT),
                        (11, 8, 2.5, 1, LIGHT), (16.5, 13, 2.5, 1, LIGHT),
                        (26, 11.5, 2, 2, HEAVY), (2, 8.5, 2, 2, HEAVY)]:
    ax.add_patch(Rectangle((x, y), w, h, fc=c, ec="#222"))
ax.text(15, -1.1, "C = cel centralny,  T = twój cel,  P = cel przeciwnika;"
        "  szare = teren ciężki, brązowe = lekki", ha="center", fontsize=9)
ax.annotate("", xy=(30, 22.9), xytext=(0, 22.9),
            arrowprops=dict(arrowstyle="<->"))
ax.text(15, 23.2, "30\"", ha="center", fontsize=9)
ax.annotate("", xy=(-0.6, 22), xytext=(-0.6, 0),
            arrowprops=dict(arrowstyle="<->"))
ax.text(-0.9, 11, "22\"", ha="right", va="center", fontsize=9, rotation=90)
save(fig, "09_mapa_misji.png")


# 10 INICJATYWA ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 3.6))
ax.set_xlim(0, 33)
ax.set_ylim(0, 10)
ax.axis("off")
steps = [
    ("1. Rzut", "Obaj gracze\nrzucają kością.\nRemisu nie\nprzerzucacie."),
    ("2. Karty", "Zaczyna ten, kto\nprzegrywa. Na zmianę:\nzagraj kartę\ninicjatywy albo pasuj."),
    ("3. Decyzja", "Kto wygrał rzut,\nwybiera, kto ma\ninicjatywę.\nRemis: wygrywa ten\nBEZ inicjatywy."),
    ("4. Nagroda", "Przegrany bierze\nkartę o wartości\nnumeru rundy\n(nie w rundzie 4)."),
]
for i, (t, b) in enumerate(steps):
    x = 0.4 + i * 8.2
    ax.add_patch(Rectangle((x, 0.6), 7.2, 8.4, fc="#eef3fa", ec="#333"))
    ax.text(x + 3.6, 8.3, t, ha="center", va="center", fontsize=12,
            fontweight="bold")
    ax.text(x + 3.6, 4.4, b, ha="center", va="center", fontsize=10,
            linespacing=1.4)
    if i < 3:
        ax.annotate("", xy=(x + 8.1, 4.8), xytext=(x + 7.3, 4.8),
                    arrowprops=dict(arrowstyle="-|>", lw=2))
save(fig, "10_inicjatywa.png")


# 11 FLANK -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 7))
board(ax, "Tac Op Flank: dwie flanki na połowie przeciwnika")
ax.add_patch(Rectangle((0, 11), 15, 11, fc="#8e44ad", alpha=0.15))
ax.add_patch(Rectangle((15, 11), 15, 11, fc="#16a085", alpha=0.15))
ax.plot([0, 30], [11, 11], ls="--", color="#333", lw=1.5)
ax.plot([15, 15], [0, 22], ls="-", color="#333", lw=2)
ax.text(7.5, 20, "LEWA FLANKA", ha="center", fontsize=12, fontweight="bold",
        color="#8e44ad")
ax.text(22.5, 20, "PRAWA FLANKA", ha="center", fontsize=12,
        fontweight="bold", color="#16a085")
ax.text(15, 5.5, "twoja połowa —\ntu flanki się nie liczą", ha="center",
        fontsize=10, color="#555",
        bbox=dict(fc="white", ec="#aaa"))
for (x, y) in [(5, 14), (8, 16)]:
    ax.add_patch(Circle((x, y), 0.6, color=BLUE))
ax.add_patch(Circle((11, 17), 0.6, color=RED))
ax.text(7.5, 12, "Twoje APL: 2+2=4, przeciwnika: 2\n→ kontrolujesz lewą flankę",
        ha="center", fontsize=9)
ax.add_patch(Circle((22, 15), 0.6, color=BLUE))
ax.add_patch(Circle((24, 16), 0.6, color=RED))
ax.add_patch(Circle((20, 17), 0.6, color=RED))
ax.text(22.5, 12, "Twoje APL: 2, przeciwnika: 4\n→ nie kontrolujesz",
        ha="center", fontsize=9)
save(fig, "11_flank.png")


# 12 GALLOWDARK ------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
for ax, (title, opened) in zip(axs, [("Właz zamknięty", False),
                                     ("Właz otwarty", True)]):
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.add_patch(Rectangle((0, 0), 12, 8, fc="#f4f1ea", ec="#999"))
    ax.add_patch(Rectangle((5.6, 0), 0.8, 3, fc="#333"))
    ax.add_patch(Rectangle((5.6, 5), 0.8, 3, fc="#333"))
    if not opened:
        ax.add_patch(Rectangle((5.6, 3), 0.8, 2, fc="#8b0000"))
        ax.text(6.0, 4.0, "właz", rotation=90, color="white", ha="center",
                va="center", fontsize=9)
        ax.text(6, -0.6, "ściana i zamknięty właz: Heavy + Wall\n"
                "nie widać, nie da się przejść", ha="center", va="top",
                fontsize=9)
    else:
        ax.add_patch(Rectangle((5.6, 3), 0.8, 2, fc="none", ec="#8b0000",
                               ls="--", lw=1.5))
        ax.text(6, -0.6, "otwarte przejście: Accessible\n"
                "przejście kosztuje +1\"", ha="center", va="top", fontsize=9)
        ax.plot([2.6, 9.4], [4, 4], ls=":", color="#333", lw=1.5)
    ax.add_patch(Circle((2, 4), 0.6, color=BLUE))
    ax.add_patch(Circle((10, 4), 0.6, color=RED))
save(fig, "12_gallowdark.png")
print("ok")
