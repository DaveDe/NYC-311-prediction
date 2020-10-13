from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

# Instantiate the PGM.
pgm = daft.PGM([5.3, 2.05], origin=[0.3, 0.3])

pgm.add_node(daft.Node("y1", r"$y_1$", 1.5, 2))
pgm.add_node(daft.Node("y2", r"$y_2$", 2.5, 2))
pgm.add_node(daft.Node("dotsy", r'\texttt{...}', 3.5, 2, plot_params={"ec": "none"}))
pgm.add_node(daft.Node("ym", r"$y_7$", 4.5, 2))

pgm.add_node(daft.Node("x1", r"$x_1$", 1, 1))
pgm.add_node(daft.Node("d1", r"$d_1$", 1.7, 1))
pgm.add_node(daft.Node("x2", r"$x_2$", 2.4, 1))
pgm.add_node(daft.Node("d2", r"$d_2$", 3.1, 1))
pgm.add_node(daft.Node("dotsx", r'\texttt{...}', 3.7, 1, plot_params={"ec": "none"}))
pgm.add_node(daft.Node("xn", r"$x_{14}$", 4.2, 1))
pgm.add_node(daft.Node("dn", r"$d_{14}$", 4.9, 1))

# Add in the edges.
pgm.add_edge("x1", "y1", directed=False)
pgm.add_edge("x2", "y1", directed=False)
pgm.add_edge("xn", "y1", directed=False)
pgm.add_edge("d1", "y1", directed=False)
pgm.add_edge("d2", "y1", directed=False)


pgm.add_edge("x1", "y2", directed=False)
pgm.add_edge("x2", "y2", directed=False)
pgm.add_edge("d2", "y2", directed=False)
pgm.add_edge("xn", "y2", directed=False)

pgm.add_edge("x2", "ym", directed=False)
pgm.add_edge("d2", "ym", directed=False)
pgm.add_edge("xn", "ym", directed=False)
pgm.add_edge("dn", "ym", directed=False)

pgm.add_edge("y1", "y2", directed=False)
pgm.add_edge("y2", "ym", directed=False)


# Render and save.
pgm.render()
pgm.figure.savefig("basic_crf.png", dpi=150)
pgm.figure.savefig("basic_crf.eps", dpi=150)