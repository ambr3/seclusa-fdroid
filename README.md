# Seclusa F-Droid

Personal [F-Droid](https://f-droid.org/) binary repository for **Seclusa** apps by [ambr3](https://github.com/ambr3).

Hosted on GitHub Pages. APKs are taken from upstream GitHub Releases (not rebuilt here).

## Add this repository

**Repository URL**

```
https://ambr3.github.io/seclusa-fdroid/fdroid/repo
```

**Fingerprint** (SHA-256)

```
2462df4f9948237cb60596149114523606eda87c9bb72db14cf3852ed4b4d33b
```

### F-Droid client

1. Install [F-Droid](https://f-droid.org/).
2. Open **Settings → Repositories → +**.
3. Paste the repository URL above.
4. Confirm the fingerprint matches.
5. Search for Seclusa apps and install.

### Obtainium

1. Install [Obtainium](https://obtainium.imranr.dev/).
2. Add app → source type **F-Droid**.
3. Use the repository URL and fingerprint above, then pick the app package (e.g. `com.ambr3.seclusasolitaire`).

You can also add apps directly from their GitHub release pages in Obtainium; this repo is convenient if you prefer the F-Droid client UI.

## Apps included

| App | Package | Upstream releases |
|-----|---------|-------------------|
| Seclusa Solitaire | `com.ambr3.seclusasolitaire` | [ambr3/Seclusa-Solitaire](https://github.com/ambr3/Seclusa-Solitaire/releases) |

## Privacy

This repository only hosts signed index metadata and APKs already published on GitHub Releases. Seclusa Solitaire requests **zero permissions**, makes **no network requests**, and has no ads or tracking. Adding this repo in F-Droid lets the client check for updates; that is separate from the apps’ own offline behaviour.

## Landing page

https://ambr3.github.io/seclusa-fdroid/

## How this repo is built

On each deploy (GitHub Actions):

1. Download the latest non-prerelease APK(s) from upstream releases.
2. Run `fdroid update` to build and sign the repo index.
3. Publish `fdroid/repo` plus a small landing page to GitHub Pages.

Signing keystore and `config.yml` are **not** in git; they live in Actions secrets / local keystores only.

## License

Repository tooling and metadata: same spirit as the apps — see each app’s license (Solitaire is GPL-3.0-or-later).
