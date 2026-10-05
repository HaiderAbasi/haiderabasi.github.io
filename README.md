# Haider Najeeb — Engineering Portfolio

A static portfolio with six case studies, six supporting projects, actual project visuals, and on-demand demo viewing. No framework, server, package installation, or build service is required.

## Preview

Extract the ZIP. Open `index.html` in Chrome, Edge, Safari, or Firefox. Local navigation, project filters, and case-study pages work directly from the extracted folder. Internet access is needed only for external demos and profile links.

## Publish on GitHub Pages — easiest method

1. Sign in to [GitHub](https://github.com).
2. Create a **public** repository named **YOUR-USERNAME.github.io**. Use your actual GitHub username, not your display name. If your account is still `HaiderAbasi`, the repository should be `HaiderAbasi.github.io`.
3. In that repository, choose **Add file → Upload files**. Drag in the **contents** of the extracted portfolio folder: `index.html`, `assets`, `projects`, and the other supplied files. Do not upload the ZIP or put the whole portfolio folder inside another folder. `index.html` must be at the repository root.
4. Click **Commit changes** on the `main` branch.
5. Open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**.
6. Choose **main**, then **/(root)**, and click **Save**.
7. Wait for the Pages deployment to finish. The same settings page will show the live link. For `HaiderAbasi`, it will be `https://haiderabasi.github.io/`.
8. Open the site in a private/incognito browser window. Test a case study, a demo, LinkedIn, and the mobile layout.

GitHub Free supports Pages from public repositories. Official references:

- https://docs.github.com/en/pages/quickstart
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

If the username repository already exists, upload these files into that repository rather than trying to create a second one. Another repository name also works, producing a URL such as `https://YOUR-USERNAME.github.io/portfolio/`; all asset paths are relative so both forms are supported.

## Publish using Git instead

Create the empty public repository on GitHub first. In a terminal inside this extracted folder, replace `YOUR-USERNAME` below:

```bash
git init
git add .
git commit -m "Add engineering portfolio"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io.git
git push -u origin main
```

Then configure Pages using steps 5–7 above. These commands assume a new empty repository. Do not use force-push to replace an existing site.

## Editing

- `content.json`: case-study text, demo URLs, supporting projects, and profile URLs.
- `build.py`: page generation and homepage text/layout. Uses Python 3 standard library only.
- `assets/style.css`: typography, color, spacing, and mobile styles.
- `assets/app.js`: project filters, the video dialog, and mobile menu behavior.
- `assets`: locally hosted fonts and actual project images.

After editing `content.json` or `build.py`, run:

```bash
python build.py
```

Commit/upload the regenerated HTML pages and changed assets. Visitors need neither Python nor Node.js.

## Evidence and scope

The content was checked against the current Master Career Evidence workbook, the supplied project demos, and public project references. Client POCs, public teaching projects, delivered research work, and ongoing client systems are labeled separately.

- PPWE's ~2.7× result belongs to the measured CUDA/OpenCV workflow processing ~2.5 hours of footage. The separate orientation-inference reduction is not a whole-pipeline claim.
- Image-to-KG's 76/76 result is a targeted macOS compatibility regression checkpoint.
- Retail Analytics is presented as a client POC.
- OpenDroneMap's public release note supports the feature/timeline, not sole authorship of ODM's multispectral support.
- Secure Access is a public teaching application, not certified access-control hardware.
- Diagrams are marked as schematics; image labels identify actual project outputs.

No invented testimonials, client names, deployment counts, model accuracy, production cloud experience, or contact details are included.

## Demo behavior

Demo players load only when a visitor clicks a demo. Each player has an **Open original demo** link in case an embedded player is blocked or requires access. Closing the dialog unloads the player. No trackers, cookies, contact forms, or backend services are included in the site itself.

## Fonts

Manrope is hosted locally. Its SIL Open Font License is included in `assets/FONT_LICENSE.txt`.

## Verification

Before packaging: HTML and local asset/anchor links, JavaScript syntax, filter interactions, modal open/close behavior, and project content were checked. Automated visual browser rendering was unavailable in the build environment. Check the extracted site in your browser at desktop and mobile widths before publishing.
