#!/usr/bin/env python
"""
Plot interactions to and from glyphs.
"""

import parasbolv as psv
import matplotlib.pyplot as plt

part_list = []
part_list.append( ['CDS', 
                   None,
                   {'cds': {'facecolor': (1,1,1), 'edgecolor': (0.75,0,0), 'linewidth': 2}}
                  ] )
part_list.append( ['Promoter', 
                   None,
                   None
                  ] )
part_list.append( ['CDS', 
                   None,
                   {'cds': {'facecolor': (1,1,1), 'edgecolor': (0,0.75,0), 'linewidth': 2}}
                  ] )
part_list.append( ['Promoter', 
                   None,
                   None
                  ] )
part_list.append( ['CDS', 
                   None,
                   {'cds': {'facecolor': (1,1,1), 'edgecolor': (0,0,0.75), 'linewidth': 2}}
                  ] )

# Create list of interactions to pass to render_part_list
interaction_list = []
interaction_list.append([0, 1, 'inhibition', {'color': (0.75, 0, 0),
                                              'heightskew': 0,
                                              'headheight': 2,
                                              'headwidth': 10,
                                              'zorder': 0,
                                              'linewidth': 2,
                                              'sending_xy_skew': (0,0),
                                              'receiving_xy_skew': (0,0)}])
interaction_list.append([0, 3, 'inhibition', {'color': (0.75, 0, 0),
                                              'heightskew': 3,
                                              'headheight': 2,
                                              'headwidth': 10,
                                              'zorder': 0,
                                              'linewidth': 2,
                                              'sending_xy_skew': (0,0),
                                              'receiving_xy_skew': (0,9)}])
interaction_list.append([2, 3, 'inhibition', {'color': (0, 0.75, 0),
                                              'heightskew': 0,
                                              'headheight': 2,
                                              'headwidth': 10,
                                              'zorder': 0,
                                              'linewidth': 2,
                                              'sending_xy_skew': (0,0),
                                              'receiving_xy_skew': (0,0)}])
interaction_list.append([4, 0, 'inhibition', {'color': (0, 0, 0.75),
                                              'heightskew': 13,
                                              'headheight': 2,
                                              'headwidth': 20,
                                              'zorder': 0,
                                              'linewidth': 2,
                                              'sending_xy_skew': (0,0),
                                              'receiving_xy_skew': (0,25)}])

fig, ax, baseline_start, baseline_end = psv.render_part_list(part_list, glyph_path='../glyphs/', padding=0.2, interaction_list=interaction_list)

# Can also manually plot interactions:
# interaction_bounds = psv.draw_interaction(ax, ((50, 15), (55, 15)), ((60, 15), (65, 15)), 'process', None)

ax.plot([baseline_start[0], baseline_end[0]], [baseline_start[1], baseline_end[1]], color=(0,0,0), linewidth=1.5, zorder=0)
fig.savefig('06_draw_interactions.pdf', transparent=True, dpi=300)
plt.show()