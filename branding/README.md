# schule-tools.de – Logo & Favicons

| Datei | Wofür |
|---|---|
| `logo-light.svg` / `logo-light@2x.png` | Logo auf hellem Hintergrund |
| `logo-dark.svg` / `logo-dark@2x.png` | Logo auf dunklem Hintergrund (Navy `#17233B`) |
| `favicon.svg`, `favicon.ico`, `icon-32.png` | Browser-Tab |
| `apple-touch-icon.png` | iPhone/iPad-Homescreen |
| `icon-192.png`, `icon-512.png`, `site.webmanifest` | Android/PWA |
| `build_logo.py` | erzeugt die SVGs neu (Schrift: Space Grotesk Bold, Text in Pfade umgewandelt) |

Farben: Navy `#17233B`, Amber `#F2A93B`, Teal `#2F8F83`, Hellblau `#DCE6F2`.

## Einbinden (im `<head>` jeder Seite)

```html
<link rel="icon" href="/branding/favicon.ico" sizes="any">
<link rel="icon" href="/branding/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/branding/apple-touch-icon.png">
<link rel="manifest" href="/branding/site.webmanifest">
<meta name="theme-color" content="#17233B">
```

## Logo auf der Landingpage

```html
<a href="/" class="site-logo">
  <img src="/branding/logo-light.svg" alt="schule-tools.de" width="320">
</a>
```

## Auf den Server

Den Ordner `branding/` nach `/var/www/schule-tools.de/html/branding/` kopieren, z. B.:

```bash
scp -r branding/ USER@schule-tools.de:/var/www/schule-tools.de/html/
```
