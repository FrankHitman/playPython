import contextlib


class Resource(object):
    def open(self):
        print('Open Resource')

    # this function must define
    def close(self):
        print('Close Resource')


with contextlib.closing(Resource()) as r:
    r.open()
    # pass

# ------output------
# Open Resource
# Close Resource

# the contextlib.closing code, it implement context too
# class closing(object):
#     """Context to automatically close something at the end of a block.
#
#     Code like this:
#
#         with closing(<module>.open(<arguments>)) as f:
#             <block>
#
#     is equivalent to this:
#
#         f = <module>.open(<arguments>)
#         try:
#             <block>
#         finally:
#             f.close()
#
#     """
#     def __init__(self, thing):
#         self.thing = thing
#     def __enter__(self):
#         return self.thing
#     def __exit__(self, *exc_info):
#         self.thing.close()
