# Publish Florida State Roleplay Website

The website is ready in `c:\Users\rmd60\florida-rp-site`.

## Option 1: GitHub Pages
1. Create a new GitHub repository.
2. Copy the contents of `florida-rp-site` into the repository.
3. Add and commit the files:
   ```powershell
   git init
   git add .
   git commit -m "Initial website publish"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
4. Enable GitHub Pages in repository settings:
   - Source: `main` branch
   - Folder: `/ (root)`

Your site will be available at `https://<your-username>.github.io/<repo-name>/`.

## Option 2: Netlify
1. Create a Netlify account.
2. Drag and drop the `florida-rp-site` folder into Netlify deploy.
3. Use the generated site URL or connect a custom domain.

## Option 3: Vercel
1. Create a Vercel account.
2. Import a GitHub repository or use the CLI.
3. Deploy the `florida-rp-site` folder.

## Notes
- `index.html` is the main entry point.
- `.nojekyll` ensures GitHub Pages serves the folder correctly.
