import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = osp.dirname(__file__)

# Add lib to PYTHONPATH
faster_rcnn_path = osp.join(this_dir, '..', '..')
# add_path(faster_rcnn_path)

tools_path = osp.join(faster_rcnn_path, 'tools')
add_path(tools_path)

lib_path = osp.join(faster_rcnn_path, 'lib')
add_path(lib_path)

vqa_path = osp.join(faster_rcnn_path, 'vqa')
add_path(vqa_path)