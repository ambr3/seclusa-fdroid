#!/usr/bin/env python3
"""Write fdroid/config.yml from environment (CI / local). Never commit the output."""
import os
import pathlib
import sys

alias = os.environ.get("FDROID_KEY_ALIAS") or "seclusafdroid"
store_pass = os.environ.get("FDROID_KEYSTORE_PASS")
key_pass = os.environ.get("FDROID_KEY_PASS")
keystore = os.environ.get(
    "FDROID_KEYSTORE",
    str(pathlib.Path.home() / "fdroid-secrets" / "seclusa-fdroid.jks"),
)

if not store_pass or not key_pass:
    sys.exit("FDROID_KEYSTORE_PASS and FDROID_KEY_PASS are required")

out = pathlib.Path(os.environ.get("FDROID_CONFIG_OUT", "fdroid/config.yml"))
out.parent.mkdir(parents=True, exist_ok=True)

# YAML-safe single-quoted strings (escape embedded single quotes)
def sq(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"

text = f"""---
repo_url: https://ambr3.github.io/seclusa-fdroid/fdroid/repo
repo_name: Seclusa F-Droid
repo_description: |-
  Personal F-Droid repository for Seclusa apps by ambr3.
  Privacy-first, offline-friendly Android apps.
archive_older: 0
repo_icon: icon.png
repo_keyalias: {alias}
keystore: {keystore}
keystorepass: {sq(store_pass)}
keypass: {sq(key_pass)}
keydname: CN=Seclusa F-Droid, OU=Seclusa, O=Seclusa, C=GB
"""
out.write_text(text)
out.chmod(0o600)
print(f"Wrote {out}")
