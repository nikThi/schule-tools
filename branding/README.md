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

Die Schriften (Inter, Space Grotesk; SIL Open Font License, siehe `fonts/OFL-*.txt`) liegen selbst gehostet in `fonts/` – es werden keine Google-Server angefragt.

## Auf den Server

| Repo | Server | Domain |
|---|---|---|
| `index.html` | `/var/www/schule-tools.de/html/index.html` | schule-tools.de |
| `tools/index.html` | `/var/www/tools.schule-tools.de/html/index.html` | tools.schule-tools.de |
| `Fehlzeiten-Rechner.html` | `/var/www/tools.schule-tools.de/html/fehlzeiten.html` | tools.schule-tools.de |
| `klassenbuch.html` | `/var/www/tools.schule-tools.de/html/klassenbuch.html` | tools.schule-tools.de |
| `branding/` | in **beide** Web-Roots als `branding/` | beide |

`branding/` muss auf beiden Domains liegen, weil die Seiten per Content-Security-Policy nur Bilder und Schriften von der eigenen Domain laden.

```bash
S=USER@schule-tools.de
scp index.html $S:/var/www/schule-tools.de/html/
scp -r branding $S:/var/www/schule-tools.de/html/
scp tools/index.html klassenbuch.html $S:/var/www/tools.schule-tools.de/html/
scp Fehlzeiten-Rechner.html $S:/var/www/tools.schule-tools.de/html/fehlzeiten.html
scp -r branding $S:/var/www/tools.schule-tools.de/html/
```
