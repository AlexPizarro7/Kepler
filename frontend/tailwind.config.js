/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "index.html",
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero': 'url("/src/img/hero.jpg")',
        'solar': 'url("/src/img/solar-eclipse.webp")',
      }
    },
  },
  plugins: [],
}

