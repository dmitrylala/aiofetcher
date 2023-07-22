import argparse
import json
import logging
import time
from pathlib import Path

from .fetcher import fetch


def aiofetcher(
    urls_file: Path,
    save_to: Path,
    verbose: bool = False,
) -> None:
    logger = logging.getLogger()
    if verbose:
        logger.setLevel(logging.INFO)
        logging.basicConfig(level=logging.INFO)

    with open(urls_file) as f:
        urls = list(map(str.strip, f.readlines()))
    logger.info(f"Read {len(urls)} urls")

    start = time.perf_counter()
    answers = fetch(urls)
    end = time.perf_counter()
    logger.info(f"Fetched, elapsed={end-start:.2f}s")

    with open(save_to, "w") as f:
        json.dump(answers, f)
    logger.info(f"Saved to {save_to!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetcher using aiohttp")
    parser.add_argument("urls_file", type=Path)
    parser.add_argument("save_to", type=Path)
    parser.add_argument("--verbose", "-v", action="store_true", default=False)
    args = parser.parse_args()
    aiofetcher(**vars(args))


if __name__ == "__main__":
    main()
