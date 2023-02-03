#this is arribute of __doc__
"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]

Example:
    snek --type=nor,spec,cute  if you need use spec or cute，please install snek_types module
"""

from one import one
from two import two

import docopt
import pkg_resources

normal_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""


def getsnek():
    print("load snake.....")
    snek_type = {'nor':normal_snek}
    #load pkg entry_points == 'snek_types'
    for entry_point in pkg_resources.iter_entry_points('snek_types'):
        snek_type[entry_point.name] = entry_point.load()
    return snek_type

def main():
    args = docopt.docopt(__doc__)
    snek_type = args['--type'] or 'nor'
    one.promt()
    print(getsnek()[snek_type], end='\n')
    two.promt()


if __name__ == "__main__":
    main()
else:
    print(__name__)

# setup 生成的工具exe 运行结尾末尾会自动调用 main函数
