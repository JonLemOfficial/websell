################################################################################
#   Copyright (C) 2022 - present | WebSell Corporation. All rights reserved.
#   Author: Jonathan Lemos (dev@jonlem.com)
################################################################################

from sys import argv
from typing import List

from scripts import cli

def main(argv: List[]): -> None:
  # cli.execute(argv)

if __name__ == '__main__':
  try:
    main(argv)
  except KeyboardInterrupt:
    pass
  finally:
    # cli.show_thank_you_meesage()
    pass
