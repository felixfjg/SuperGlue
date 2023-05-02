import numpy as np
path = 'dump_match_pairs/scene0711_00_frame-001680_scene0711_00_frame-001995_matches.npz'
npz = np.load(path)
npz.files
# ['keypoints0', 'keypoints1', 'matches', 'match_confidence']
npz['keypoints0'].shape
# (382, 2)
npz['keypoints1'].shape
# (391, 2)
npz['matches'].shape
# (382,)
np.sum(npz['matches']>-1)
# 115
npz['match_confidence'].shape
# (382,)