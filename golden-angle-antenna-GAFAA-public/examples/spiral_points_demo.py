import matplotlib.pyplot as plt
from src.gafaa_public.phyllotaxis_utils import golden_like_spiral_points

def main():
    x, y = golden_like_spiral_points(n_points=200, radius_scale=0.1, angle_deg=137.0)

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=10)
    ax.set_aspect("equal", "box")
    ax.set_title("Generic golden-like spiral demo")
    plt.show()

if __name__ == "__main__":
    main()
