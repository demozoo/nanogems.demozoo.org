import argparse
import config

from add_entry import add_entry, __update
from generate import freezer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="nanopage")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser(
        "add_entry", help="Add / Update entry data to page from demozoo id"
    )
    parser_add.add_argument(
        "category",
        type=str,
        help="Category",
        choices=[c["id"] for c in config.CATEGORIES],
    )
    parser_add.add_argument(
        "flavor", type=str, help="Flavor", choices=[c["id"] for c in config.FLAVORS]
    )
    parser_add.add_argument("demozoo_id", type=str, help="demozoo_id")

    parser_add = subparsers.add_parser("generate", help="Generate HTML")

    parser_update = subparsers.add_parser("update", help="Regenerate json from demozoo")
    args = parser.parse_args()
    if args.command == "add_entry":
        add_entry(args.category, args.flavor, args.demozoo_id)
    if args.command == "update":
        __update()
    elif args.command == "generate":
        freezer.freeze()
