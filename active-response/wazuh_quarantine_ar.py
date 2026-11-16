import json
import sys
import shutil
import logging
from pathlib import Path

BASE_DIR = Path(r"C:\SOC-Test").resolve()
QUARANTINE_DIR = Path(r"C:\SOC-Quarantine").resolve()

LOG_FILE = Path(
    r"C:\Program Files (x86)\ossec-agent\active-response\quarantine.log"
)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def main():
    try:
        data = json.loads(sys.stdin.readline())

        command = data.get("command")
        if command == "delete":
            logging.info("Delete command ignored")
            return

        if command != "add":
            raise ValueError(f"Invalid command: {command}")

        parameters = data.get("parameters", {})
        arguments = parameters.get("extra_args", [])

        # Require explicit malicious confirmation from n8n
        if len(arguments) < 2:
            raise ValueError("Missing confirmation token or file path")

        confirmation = arguments[0]
        raw_path = arguments[1]

        if confirmation != "MALICIOUS_CONFIRMED":
            raise ValueError("Malicious confirmation missing")

        if not isinstance(raw_path, str) or not raw_path.strip():
            raise ValueError("Invalid file path")

        target = Path(raw_path).resolve(strict=True)

        if not target.is_relative_to(BASE_DIR):
            raise ValueError("File outside allowed folder")

        if not target.is_file():
            raise ValueError("Not a regular file")

        QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)

        destination = QUARANTINE_DIR / target.name
        counter = 1

        while destination.exists():
            destination = QUARANTINE_DIR / (
                f"{target.stem}_{counter}{target.suffix}"
            )
            counter += 1

        shutil.move(str(target), str(destination))

        logging.info(
            "QUARANTINED: %s -> %s",
            target,
            destination
        )

        print(json.dumps({
            "status": "QUARANTINED",
            "original_path": str(target),
            "quarantine_path": str(destination)
        }))

    except Exception as exc:
        logging.exception("Quarantine failed: %s", exc)

        print(json.dumps({
            "status": "FAILED",
            "reason": str(exc)
        }))

        sys.exit(1)


if __name__ == "__main__":
    main()