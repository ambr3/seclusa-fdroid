# Seclusa F-Droid

Personal [F-Droid](https://f-droid.org/) binary repo for Seclusa apps by [ambr3](https://github.com/ambr3). Hosted on GitHub Pages; APKs come from upstream GitHub Releases.

## Add this repository

```
https://ambr3.github.io/seclusa-fdroid/fdroid/repo
```

Fingerprint (SHA-256):

```
2462df4f9948237cb60596149114523606eda87c9bb72db14cf3852ed4b4d33b
```

**F-Droid:** Settings → Repositories → + → paste URL → confirm fingerprint.

**Obtainium:** Add app → source **F-Droid** → same URL + fingerprint → pick package (e.g. `com.ambr3.seclusasolitaire`).

## Apps

| App | Package | Releases |
|-----|---------|----------|
| Seclusa Solitaire | `com.ambr3.seclusasolitaire` | [ambr3/Seclusa-Solitaire](https://github.com/ambr3/Seclusa-Solitaire/releases) |

## Privacy

This repo hosts signed index metadata and APKs already on GitHub Releases. Seclusa Solitaire has **zero permissions**, **no network**, no ads or tracking. F-Droid update checks are separate from the apps’ offline behaviour.

Landing: https://ambr3.github.io/seclusa-fdroid/

## Build

On deploy (GitHub Actions): pull latest release APKs → `fdroid update` → publish `fdroid/repo` + landing page. Keystore / `config.yml` stay in secrets — not in git.

## License

See each app’s license (Solitaire is GPL-3.0-or-later).
