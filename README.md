# Gàidhlig: Hit the Button

A single-file, no-dependency Scottish Gaelic drill app.

- **Prepositional pronouns**: choose which prepositions to include, and drill Gaelic → English, English → Gaelic, or mixed.
- **Irregular verbs**: bi, rach, thig, dèan, thoir, faic, faigh, cluinn, abair, ruig (verbal noun, imperative, present, past, future, conditional, plus dependent forms).
- Optional per-question timer, streaks, best scores (saved in the browser), "practise missed" and reference tables.

## Adding audio

The app shows a 🔊 button (and the **P** key replays) for any Gaelic form that has a recording; forms without one simply show no button.

1. `audio/words.csv` lists every form in the app with the filename it expects, e.g. `agam` → `audio/agam.mp3`. Accents are dropped in filenames (`chì` → `chi.mp3`, `às` → `as.mp3`).
2. Drop `.mp3` files into `audio/`.
3. Run `python3 tools/make_manifest.py`. It rebuilds `audio/manifest.json` (the list the app reads) and tells you which words are still missing.
4. Commit and push.

Only use recordings you have made yourself or have permission to publish. Most online Gaelic audio (LearnGaelic, Forvo) is not free to redistribute.

## Publish on GitHub Pages

1. Create a repo and push `index.html` (and this README) to the `main` branch.
2. Repo **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)`.
3. Your site appears at `https://<username>.github.io/<repo>/`.

To run locally, just open `index.html` in a browser.
